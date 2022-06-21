# Copyright 2022 The StackStorm Authors.
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


def st2_runner_python_distribution(**kwargs):
    runner_name = kwargs.pop("runner_name")
    description = kwargs.pop("description")

    kwargs["provides"] = python_artifact(
        name=f"stackstorm-runner-{runner_name.replace('_', '-')}",
        description=description,
        # version=__version__, # TODO: from action_chain_runner import __version__
        # test_suite="tests",
        # zip_safe=False,
    )

    dependencies = kwargs.pop("dependencies", [])
    for dep in [":runner", f"./{runner_name}_runner"]:
        if dep not in dependencies:
            dependencies.append(dep)
    kwargs["dependencies"] = dependencies

    python_distribution(**kwargs)


def st2_component_python_distribution(**kwargs):
    st2_component = kwargs.pop("component_name")
    description = (
        f"{st2_component} StackStorm event-driven automation platform component"
    )

    scripts = kwargs.pop("scripts", [])

    kwargs["provides"] = python_artifact(
        name=st2_component,
        description=description,
        scripts=[
            script[:-6] if script.endswith(":shell") else script
            for script in scripts
        ],
        # version=get_version_string(INIT_FILE)  # TODO
        # test_suite=st2_component,
        # zip_safe=False,
    )

    dependencies = kwargs.pop("dependencies", [])
    for dep in [st2_component] + scripts:
        if dep not in dependencies:
            dependencies.append(f"./{dep}")
    kwargs["dependencies"] = dependencies

    python_distribution(**kwargs)
