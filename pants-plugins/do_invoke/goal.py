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

from pants.engine.goal import Goal, GoalSubsystem
from pants.engine.process import InteractiveRunner, InteractiveProcess
from pants.engine.rules import collect_rules, goal_rule


class DoInvokeSubsystem(GoalSubsystem):
    name = "do"
    help = "Run pyinvoke-based targets (locally; remote execution not supported)"


class DoInvoke(Goal):
    subsystem_cls = DoInvokeSubsystem


# using `invoke` or `inv`, you would put your tasks in:
#    - tasks.py
#    - or in a "tasks" module (organized into collections/namespaces of tasks)

@goal_rule
async def do_invoke(interactive_runner: InteractiveRunner) -> DoInvoke:
    # TODO: get/install invoke
    result = interactive_runner.run(
        InteractiveProcess(
            argv=["invoke"],
            env={},
            run_in_workspace=True,
            forward_signals_to_process=True,
        )
    )
    return DoInvoke(exit_code=result.exit_code)


def rules():
    return collect_rules()
