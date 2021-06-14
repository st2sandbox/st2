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

from pants.backend.codegen import export_codegen_goal

from stevedore_extensions import (
    target_types_rules,
    rules as stevedore_rules,
    pytest_dependency_injection,
    setup_py_kwargs,
)
from stevedore_extensions.target_types import StevedoreExtension


# TODO: to support poetry + pyproject.toml, add a macro that extracts
#       details from pyproject.toml and adds the relevent stevedore_extension.
# TODO: add stevedore_namespaces field to python_library?


def rules():
    return [
        *target_types_rules.rules(),
        *stevedore_rules.rules(),
        *pytest_dependency_injection.rules(),
        *export_codegen_goal.rules(),
        *setup_py_kwargs.rules(),
    ]


def target_types():
    return [StevedoreExtension]
