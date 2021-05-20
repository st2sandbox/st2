# coding: utf-8
from collections import defaultdict

from pants.backend.python.goals.pytest_runner import (
    PytestPluginSetupRequest,
    PytestPluginSetup,
)
from pants.backend.python.target_types import PythonTestsDependencies
from pants.engine.fs import CreateDigest, Digest, FileContent, PathGlobs, Paths
from pants.engine.rules import Get, MultiGet, collect_rules, rule
from pants.engine.target import DependenciesRequest, Target, Targets
from pants.engine.unions import UnionRule
from pants.util.logging import LogLevel

from stevedore_extensions.target_types import (
    ResolvedStevedoreEntryPoints,
    ResolveStevedoreEntryPointsRequest,
    StevedoreEntryPoints,
    StevedoreEntryPointsField,
    StevedoreExtension,
    StevedoreNamespaceField,
    StevedoreNamespacesField,
)


class GenerateEntryPointsTxtFromStevedoreExtensionRequest(PytestPluginSetupRequest):
    @classmethod
    def is_applicable(cls, target: Target) -> bool:
        # select python_tests targets with stevedore_namespaces field
        return target.has_field(StevedoreNamespacesField) and target.get(StevedoreNamespacesField).value is not None


@rule(desc="Generate entry_points.txt from stevedore_extension target metadata", level=LogLevel.DEBUG)
async def generate_entry_points_txt_from_stevedore_extension(
    request: GenerateEntryPointsTxtFromStevedoreExtensionRequest,
) -> PytestPluginSetup:
    # similar to relocate_files, this isn't standard codegen.
    # It uses the metadata on targets as source instead of source files.

    # get all injected dependencies that are StevedoreExtension targets
    dependencies = await Get(
        Targets,
        DependenciesRequest(request.target.get(PythonTestsDependencies))
    )
    stevedore_targets = [
        tgt for tgt in dependencies
        if tgt.has_field(StevedoreEntryPointsField)
        and tgt.get(StevedoreEntryPointsField).value is not None
    ]

    resolved_entry_points = await MultiGet(
        Get(
            ResolvedStevedoreEntryPoints,
            ResolveStevedoreEntryPointsRequest(tgt[StevedoreEntryPointsField])
        )
        for tgt in stevedore_targets
    )

    possible_paths = [
        {
            f"{stevedore_extension.address.spec_path}/{entry_point.value.module.split('.')[0]}"
            for entry_point in resolved_ep.val
        } for stevedore_extension, resolved_ep in zip(stevedore_targets, resolved_entry_points)
    ]
    resolved_paths = []
    # MultiGet can only do up to 10 at a time
    batchsize = 10
    for i in range(0, len(possible_paths), batchsize):
        resolved_paths.extend(
            await MultiGet(
                Get(
                    Paths,
                    PathGlobs(module_candidate_paths)
                ) for module_candidate_paths in possible_paths[i:i+batchsize]
            )
        )

    # arrange in sibling groups
    stevedore_extensions_by_path = defaultdict(list)
    for stevedore_extension, resolved_ep, paths in zip(stevedore_targets, resolved_entry_points, resolved_paths):
        path = paths.dirs[0]  # just take the first match
        stevedore_extensions_by_path[path].append(
            (stevedore_extension, resolved_ep)
        )

    entry_points_txt_files = []
    for module_path, stevedore_extensions in stevedore_extensions_by_path.items():
        entry_points_txt_path = f"{module_path}.egg-info/entry_points.txt"
        entry_points_txt_contents = ""

        stevedore_extension: StevedoreExtension
        for stevedore_extension, resolved_ep in stevedore_extensions:
            namespace: StevedoreNamespaceField = stevedore_extension[StevedoreNamespaceField]
            entry_points: StevedoreEntryPoints = resolved_ep.val
            if not entry_points:
                continue

            entry_points_txt_contents += f"[{namespace.value}]\n"
            for entry_point in entry_points:
                entry_points_txt_contents += f"{entry_point.name} = {entry_point.value.spec}\n"
            entry_points_txt_contents += "\n"

        entry_points_txt_contents = entry_points_txt_contents.encode("utf-8")
        entry_points_txt_files.append(
            FileContent(entry_points_txt_path, entry_points_txt_contents)
        )

    digest = await Get(Digest, CreateDigest(entry_points_txt_files))
    return PytestPluginSetup(digest)


def rules():
    return [
        *collect_rules(),
        UnionRule(PytestPluginSetupRequest, GenerateEntryPointsTxtFromStevedoreExtensionRequest),
    ]
