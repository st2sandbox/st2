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

import sys

from pants.backend.python.target_types import EntryPoint
from pants.backend.python.util_rules.pex import (
    InterpreterConstraints,
    Pex,
    PexProcess,
    PexRequest,
    PexRequirements,
)
from pants.engine.environment import CompleteEnvironment
from pants.engine.fs import AddPrefix, Digest, EMPTY_DIGEST, Workspace
from pants.engine.goal import Goal, GoalSubsystem
from pants.engine.process import InteractiveRunner, InteractiveProcess, Process
from pants.engine.rules import collect_rules, Get, goal_rule, MultiGet
from pants.option.custom_types import shell_str


class DoInvokeSubsystem(GoalSubsystem):
    name = "do"  # maybe invoke or inv?
    # options_scope = "invoke"
    help = "Run python tasks from the 'tasks' directory (via pyinvoke)"
    # TODO: dynamic help pulled from invoke

    @classmethod
    def register_options(cls, register):
        super().register_options(register)
        # register(
        #    "--args",
        #    type=list,
        #    member_type=shell_str,
        #    passthrough=True,
        #    help="Args to pass to invoke",
        # )

        # TODO: deal with erroring out if invoke is not specified in pants.toml [GLOBAL].plugins
        # late import so that this is only used when pants needs the options
        import invoke
        from invoke.main import program

        # this initialization logic comes from the beginning of program.run()
        program.create_config()
        program.parse_core(argv=[])
        program.parse_collection()

        # In invoke, this "Parser" parses CLI and config options. The context holds available options.
        context: invoke.ParserContext
        for context in [program.initial_context, *program.collection.to_contexts()]:
            flag: str
            arg: invoke.Argument
            for flag, arg in context.flags.items():
                # skip problematic or unneeded
                if arg.name in (
                    "complete",
                    "debug",
                    "help",
                    "print-completion-script",
                    "version",
                ):
                    continue
                if flag.startswith("--no-"):
                    # pants doesn't like args that start with --no
                    flag = f"--{flag[5:]}"
                    default = not arg.default
                else:
                    default = arg.default
                names = [flag]
                for name in arg.nicknames:
                    if len(name) == 1:
                        # skip problematic short forms
                        if name in ("d", "l"):  # --log-dir, --level
                            continue
                        names.append(f"-{name}")
                    else:
                        names.append(f"--{name}")
                register(
                    *names,
                    # dest is the name of field containing option value, key in config file, computing env var name
                    dest=arg.attr_name,
                    default=default,
                    type=arg.kind,
                    # metavar=,  # name for the var that shows up in help
                    help=arg.help,
                    # advanced=True,  # when should this be triggered?
                    # member_type=,  # ie members of a list (see pants.option.parser.Parser._allowed_member_types)
                    # choices=,  # enum
                    # mutually_exclusive_group=,  # ???
                )


class DoInvoke(Goal):
    subsystem_cls = DoInvokeSubsystem


# using `invoke` or `inv`, you would put your tasks in:
#    - tasks.py
#    - or in a "tasks" module (organized into collections/namespaces of tasks)


@goal_rule
async def do_invoke(
    invoke_subsystem: DoInvokeSubsystem,
    interactive_runner: InteractiveRunner,
    workspace: Workspace,
    complete_env: CompleteEnvironment,
) -> DoInvoke:
    invoke_argv = [sys.executable, "-m", "invoke"]

    # invoke is available somewhere on sys.path already because it is included in pants.toml [GLOBAL].plugins
    env = {**complete_env, "PYTHONPATH": ":".join(sys.path)}

    result = interactive_runner.run(
        InteractiveProcess(
            argv=invoke_argv,
            #argv=(*invoke_argv, *invoke_subsystem.args),
            env=env,
            input_digest=EMPTY_DIGEST,  # run_in_workspace requires EMPTY_DIGEST
            run_in_workspace=True,
            forward_signals_to_process=True,
        )
    )
    return DoInvoke(exit_code=result.exit_code)


def rules():
    return collect_rules()
