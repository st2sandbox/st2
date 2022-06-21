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


def st2_license(**kwargs):
    """copy the LICENSE file into each wheel.

    As long as the file is in the src root when building the sdist/wheel,
    setuptools automatically includes the LICENSE file in the dist-info.
    """
    if "dest" not in kwargs:
        raise ValueError("'dest' path is required for st2_license macro")
    relocated_files(  # noqa: F821
        name="license",
        files_targets=["//:license"],
        src="",
        **kwargs,
    )


def st2_runner_python_distribution(**kwargs):
    runner_name = kwargs.pop("runner_name")
    description = kwargs.pop("description")

    st2_license(dest=f"contrib/runners/{runner_name}_runner")

    kwargs["provides"] = python_artifact(  # noqa: F821
        name=f"stackstorm-runner-{runner_name.replace('_', '-')}",
        description=description,
        # version=__version__, # TODO: from action_chain_runner import __version__
        # test_suite="tests",
        # zip_safe=False,
    )

    dependencies = kwargs.pop("dependencies", [])
    for dep in [":runner", f"./{runner_name}_runner", ":license"]:
        if dep not in dependencies:
            dependencies.append(dep)
    kwargs["dependencies"] = dependencies

    python_distribution(**kwargs)  # noqa: F821


def st2_component_python_distribution(**kwargs):
    st2_component = kwargs.pop("component_name")

    st2_license(dest=st2_component)

    description = (
        f"{st2_component} StackStorm event-driven automation platform component"
    )

    scripts = kwargs.pop("scripts", [])

    kwargs["provides"] = python_artifact(  # noqa: F821
        name=st2_component,
        description=description,
        scripts=[
            script[:-6] if script.endswith(":shell") else script for script in scripts
        ],
        # version=get_version_string(INIT_FILE)  # TODO
        # test_suite=st2_component,
        # zip_safe=False,
    )

    dependencies = kwargs.pop("dependencies", [])

    for dep in [st2_component, ":license"] + scripts:
        dep = f"./{dep}" if dep[0] != ":" else dep
        if dep not in dependencies:
            dependencies.append(dep)

        # see st2_shell_sources_and_resources below
        if dep.endswith(":shell"):
            dep_res = f"{dep}_resources"
            if dep_res not in dependencies:
                dependencies.append(dep_res)

    kwargs["dependencies"] = dependencies

    python_distribution(**kwargs)  # noqa: F821


def st2_shell_sources_and_resources(**kwargs):
    """This creates a shell_sources and a resources target.

    This is needed because python_sources dependencies on shell_sources
    are silently ignored. So, we also need the resources target
    to allow depending on them.
    """
    shell_sources(**kwargs)  # noqa: F821

    kwargs.pop("skip_shellcheck")

    kwargs["name"] += "_resources"
    resources(**kwargs)  # noqa: F821
