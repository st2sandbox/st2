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
from pants.backend.python.target_types import PythonSourceField
from pants.core.target_types import FileSourceField
from pants.core.util_rules.source_files import SourceFilesRequest
from pants.core.util_rules.stripped_source_files import StrippedSourceFiles
from pants.engine.fs import (
    CreateDigest,
    Digest,
    DigestContents,
    FileContent,
    Snapshot,
)
from pants.engine.rules import Get, MultiGet, collect_rules, rule
from pants.engine.target import (
    GeneratedSources,
    GenerateSourcesRequest,
    SourcesField,
    TransitiveTargets,
    TransitiveTargetsRequest,
)
from pants.engine.unions import UnionRule

from sample_conf.target_types import (
    #GenerateSampleConfSourceField,
    SampleConfSourceField,
    SampleConf,
)


class GenerateSampleConfRequest(GenerateSourcesRequest):
    input = SampleConfSourceField
    output = SampleConfSourceField
    #output = FileSourceField


@rule
async def generate_sample_conf(
    request: GenerateSampleConfRequest,
) -> GeneratedSources:
    target = request.protocol_target

    # Find all the dependencies of our target
    transitive_targets = await Get(TransitiveTargets, TransitiveTargetsRequest([target.address]))

    # Get the source files without the source-root prefix.
    #stripped_sources = await Get(StrippedSourceFiles, SourceFilesRequest(
    #    (tgt.get(SourcesField) for tgt in transitive_targets.closure)
    #))

    #contents = await Get(DigestContents, Digest, stripped_sources)

    # actually generate it with an external script.
    # Generation cannot be inlined here because it needs to import the st2 code.
    sample_conf = "asdf\n"

    output_path = f"{target.address.spec_path}/{target[SampleConfSourceField].value}"
    content = FileContent(output_path, sample_conf.encode("utf-8"))

    output_digest = await Get(Digest, CreateDigest([content]))
    output_snapshot = await Get(Snapshot, Digest, output_digest)
    return GeneratedSources(output_snapshot)


def rules():
    return [
        *collect_rules(),
        UnionRule(
            GenerateSourcesRequest,
            GenerateSampleConfRequest,
        ),
    ]
