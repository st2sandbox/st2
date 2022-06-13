python_sources(
    resolve="pylint_plugins",
)

python_requirement(
    name="pylint",
    requirements=[
        # This must be the same as [pylint].version in pants.toml
        "pylint~=2.8.2",
        # other requirements in [pylint].extra_requirements in pants.toml
        "setuptools",
    ],
    resolve="pylint_plugins",
)

python_requirement(
    name="astroid",
    # The version of astroid is constrained by the pylint version above
    requirements=["astroid"],
    resolve="pylint_plugins",
)

python_tests(
    name="tests",
    resolve="pylint_plugins",
    dependencies=[
        "!//conftest.py:root",
    ],
)
