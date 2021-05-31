# coding: utf-8

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
