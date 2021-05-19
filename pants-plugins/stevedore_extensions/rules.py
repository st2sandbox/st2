# coding: utf-8
from pants.backend.python.target_types import PythonSources
from pants.base.specs import AddressSpecs, SiblingAddresses
from pants.engine.fs import CreateDigest, Digest, FileContent
from pants.engine.rules import Get, MultiGet, collect_rules, rule
from pants.engine.target import (
    Address,
    GeneratedSources,
    GenerateSourcesRequest,
    Snapshot,
    Targets,
)
from pants.engine.unions import UnionRule
from pants.util.logging import LogLevel

from stevedore_extensions.target_types import (
    ResolvedStevedoreEntryPoints,
    ResolveStevedoreEntryPointsRequest,
    StevedoreEntryPoints,
    StevedoreEntryPointsField,
    StevedoreExtension,
    StevedoreNamespaceField,
    StevedoreSources,
)


class GenerateEntryPointsTxtFromStevedoreExtensionRequest(GenerateSourcesRequest):
    input = StevedoreSources
    output = PythonSources


@rule(desc="Generate entry_points.txt from stevedore_extension target metadata", level=LogLevel.DEBUG)
async def generate_entry_points_txt_from_stevedore_extension(
    request: GenerateEntryPointsTxtFromStevedoreExtensionRequest,
) -> GeneratedSources:
    # similar to relocate_files, this isn't standard codegen.
    # It uses the metadata on targets as source instead of source files.

    address: Address = request.protocol_target.address

    sibling_targets = await Get(
        Targets, AddressSpecs([SiblingAddresses(address.spec_path)]),
    )
    stevedore_targets = [
        tgt for tgt in sibling_targets if tgt.has_field(StevedoreEntryPointsField)
    ]
    resolved_entry_points = await MultiGet(
        Get(
            ResolvedStevedoreEntryPoints,
            ResolveStevedoreEntryPointsRequest(tgt[StevedoreEntryPointsField])
        )
        for tgt in stevedore_targets
    )

    entry_points_txt_path = f"{address.spec_path}.egg-info/entry_points.txt"
    entry_points_txt_contents = ""

    stevedore_extension: StevedoreExtension
    for i, stevedore_extension in enumerate(stevedore_targets):
        namespace: StevedoreNamespaceField = stevedore_extension[StevedoreNamespaceField]
        entry_points: StevedoreEntryPoints = resolved_entry_points[i].val
        if not entry_points:
            continue

        entry_points_txt_contents += f"[{namespace.value}]\n"
        for entry_point in entry_points:
            entry_points_txt_contents += f"{entry_point.name} = {entry_point.value.spec}\n"
        entry_points_txt_contents += "\n"

    entry_points_txt_contents = entry_points_txt_contents.encode("utf-8")

    digest = await Get(
        Digest,
        CreateDigest([FileContent(entry_points_txt_path, entry_points_txt_contents)])
    )
    snapshot = await Get(Snapshot, Digest, digest)
    return GeneratedSources(snapshot)


def rules():
    return [
        *collect_rules(),
        UnionRule(GenerateSourcesRequest, GenerateEntryPointsTxtFromStevedoreExtensionRequest),
    ]
