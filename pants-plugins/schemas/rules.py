# Copyright 2021 The StackStorm Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from dataclasses import dataclass

from pants.backend.python.target_types import ConsoleScript, EntryPoint
from pants.backend.python.util_rules.pex import (
    PexRequest,
    VenvPex,
    VenvPexProcess,
)
from pants.backend.python.util_rules.pex_from_targets import PexFromTargetsRequest
from pants.backend.python.util_rules.python_sources import (
    PythonSourceFiles,
    PythonSourceFilesRequest,
)
from pants.core.goals.fmt import FmtResult, FmtRequest
from pants.core.util_rules.source_files import SourceFiles, SourceFilesRequest
from pants.engine.addresses import Address
from pants.engine.fs import (
    CreateDigest,
    Digest,
    FileContent,
    Snapshot,
)
from pants.engine.process import FallibleProcessResult
from pants.engine.rules import Get, MultiGet, collect_rules, rule
from pants.engine.target import (
    FieldSet,
    SourcesField,
    TransitiveTargets,
    TransitiveTargetsRequest,
)
from pants.engine.unions import UnionRule
from pants.util.logging import LogLevel

from schemas.target_types import (
    SchemasSourcesField,
    Schemas,
)


CMD = "generate_schemas"


@dataclass(frozen=True)
class GenerateSchemasFieldSet(FieldSet):
    required_fields = (SchemasSourcesField,)

    sources: SchemasSourcesField


class GenerateSchemasViaFmtRequest(FmtRequest):
    field_set_type = GenerateSchemasFieldSet
    name = CMD


@rule(
    desc=f"Update contrib/schemas/*.json with st2-generate-schemas",
    level=LogLevel.DEBUG,
)
async def generate_schemas_via_fmt(
    request: GenerateSchemasViaFmtRequest,
) -> FmtResult:
    # There will only be one target+field_set, but we iterate
    # to satisfy how fmt expects that there could be more than one.

    # Find all the dependencies of our target
    transitive_targets = await Get(
        TransitiveTargets,
        TransitiveTargetsRequest(
            [field_set.address for field_set in request.field_sets]
        ),
    )

    # actually generate it with an external script.
    # Generation cannot be inlined here because it needs to import the st2 code.
    pex = await Get(
        VenvPex,
        PexFromTargetsRequest(
            [
                Address(
                    "st2common/st2common/cmd",
                    target_name="cmd",
                    relative_file_path=f"{CMD}.py",
                )
            ],
            output_filename=f"{CMD}.pex",
            internal_only=True,
            main=EntryPoint.parse("st2common.cmd.{CMD}:main"),
        ),
    )

    output_directory = "contrib/schemas"

    result = await Get(
        FallibleProcessResult,
        VenvPexProcess(
            pex,
            input_digest=request.snapshot.digest,
            output_directories=[output_directory],
            description=f"Regenerating st2 metadata schemas in contrib/schemas",
            level=LogLevel.DEBUG,
            argv=(output_directory,),
        ),
    )

    output_snapshot = await Get(Snapshot, Digest, result.output_digest)
    return FmtResult.create(request, result, output_snapshot, strip_chroot_path=True)


def rules():
    return [
        *collect_rules(),
        UnionRule(FmtRequest, GenerateSchemasViaFmtRequest),
    ]
