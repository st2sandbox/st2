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

"""
Please see https://www.pantsbuild.org/docs/plugins-setup-py
Based in part on Apache 2.0 licensed code from:
https://github.com/pantsbuild/pants/blob/master/pants-plugins/internal_plugins/releases/register.py
"""

from pants.backend.python.goals.setup_py import SetupKwargsRequest
from pants.engine.target import Target
from pants.backend.python.goals.setup_py import SetupKwargs
from pants.engine.rules import collect_rules, Get, rule, UnionRule

from stevedore_extensions.setup_py_kwargs import StevedoreSetupKwargs, StevedoreSetupKwargsRequest


class StackStormSetupKwargsRequest(SetupKwargsRequest):
    @classmethod
    def is_applicable(cls, _: Target) -> bool:
        return True
        # if we need to separate runner wheels vs component wheels,
        # we could have different Requests for each type:
        # return target.address.spec.startswith("contrib/runners/")
        # return target.address.spec.startswith("st2")


@rule
async def setup_kwargs_plugin(request: StackStormSetupKwargsRequest) -> SetupKwargs:
    kwargs = request.explicit_kwargs.copy()

    if "description" not in kwargs:
        raise ValueError(
            f"Missing a `description` kwarg in the `provides` field for {request.target.address}."
        )

    # Add classifiers. We preserve any that were already set.
    standard_classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        # TODO: maybe add these dynamically based on interpreter constraints
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
    ]
    kwargs["classifiers"] = [*standard_classifiers, *kwargs.get("classifiers", [])]

    # Hardcode certain kwargs and validate that they weren't already set.
    hardcoded_kwargs = dict(
        version="4.0.0dev0",  # TODO
        # long_description=long_description,
        # long_description_content_type="text/x-rst",
        author="StackStorm",
        author_email="info@stackstorm.com",
        url="https://stackstorm.com",
        project_urls={
            # TODO: use more standard slugs for these
            "Pack Exchange": "https://exchange.stackstorm.org",
            "Repository": "https://github.com/StackStorm/st2",
            "Documentation": "https://docs.stackstorm.com",
            "Community": "https://stackstorm.com/community-signup",
            "Questions": "https://github.com/StackStorm/st2/discussions",
            "Donate": "https://funding.communitybridge.org/projects/stackstorm",
            "News/Blog": "https://stackstorm.com/blog",
            "Security": "https://docs.stackstorm.com/latest/security.html",
            "Bug Reports": "https://github.com/StackStorm/st2/issues",
        },
        license="Apache License, Version 2.0",
        zip_safe=True,
    )
    conflicting_hardcoded_kwargs = set(kwargs.keys()).intersection(hardcoded_kwargs.keys())
    if conflicting_hardcoded_kwargs:
        raise ValueError(
            f"These kwargs should not be set in the `provides` field for {request.target.address} "
            "because Pants's internal plugin will automatically set them: "
            f"{sorted(conflicting_hardcoded_kwargs)}"
        )
    kwargs.update(hardcoded_kwargs)

    # stevedore extensions define most of our setup.py "entry_points"
    stevedore_kwargs = await Get(StevedoreSetupKwargs, StevedoreSetupKwargsRequest(request))
    kwargs["entry_points"] = {
        **stevedore_kwargs.kwargs["entry_points"],
        **kwargs.get("entry_points", {}),
    }

    return SetupKwargs(kwargs, address=request.target.address)


def rules():
    return [
        *collect_rules(),
        UnionRule(SetupKwargsRequest, StackStormSetupKwargsRequest),
    ]
