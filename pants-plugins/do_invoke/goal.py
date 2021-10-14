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

import hashlib
import re
import sys

from textwrap import dedent

# from pants.engine.environment import CompleteEnvironment
from pants.engine.fs import (
    CreateDigest,
    Digest,
    DigestContents,
    FileContent,
    PathGlobs,
    Workspace,
)
from pants.engine.goal import Goal, GoalSubsystem
from pants.engine.rules import collect_rules, Get, goal_rule


class InitializeInvokeSubsystem(GoalSubsystem):
    name = "initialize-invoke"
    help = "Setup the invoke wrapper script(s) using the pants environment."


class InitializeInvoke(Goal):
    subsystem_cls = InitializeInvokeSubsystem


@goal_rule
async def initialize_invoke(
    invoke_subsystem: InitializeInvokeSubsystem,
    workspace: Workspace,
    # complete_env: CompleteEnvironment,
) -> InitializeInvoke:
    # invoke_argv = [sys.executable, "-m", "invoke"]

    # invoke is available somewhere on sys.path already because it is included in pants.toml [GLOBAL].plugins
    # env = {**complete_env, "PYTHONPATH": ":".join(sys.path)}

    pants_toml_digest = await Get(Digest, PathGlobs(["pants.toml"]))
    pants_toml = await Get(DigestContents, Digest, pants_toml_digest)
    lines = pants_toml[0].content.decode().splitlines()

    # INVOKE_WRAPPER=./pants.d/invoke-$( grep -e invoke -e pants_version pants.toml | _checksum )
    pattern = re.compile(r"pants_version|invoke")
    lines = [line for line in lines if pattern.search(line)]
    grepped = "\n".join(lines).encode() + b"\n"

    # depending on tooling, we might need one or the other.
    shasum = hashlib.sha1(grepped).hexdigest()
    md5sum = hashlib.md5(grepped).hexdigest()
    invoke_wrapper_paths = [
        f".pants.d/invoke/sha1-{shasum}",
        f".pants.d/invoke/md5-{md5sum}",
    ]

    # This has the "magic" that simplifies setting up invoke. We just use pants' pythonpath + python.
    invoke_wrapper = dedent(
        f"""\
        #!/usr/bin/env bash
        export PYTHONPATH="{':'.join(sys.path)}"
        exec {sys.executable} -m invoke $@
        """
    )
    invoke_digest = await Get(
        Digest,
        CreateDigest(
            [
                FileContent(
                    path,
                    invoke_wrapper.encode(),
                    is_executable=True,
                )
                for path in invoke_wrapper_paths
            ]
        ),
    )
    workspace.write_digest(invoke_digest)

    # TODO: cleanup the .pants.d/invoke directory at some point

    return InitializeInvoke(exit_code=0)


def rules():
    return collect_rules()
