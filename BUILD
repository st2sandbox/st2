python_requirements(
    requirements_relpath="requirements-pants.txt",
    module_mapping={
        "gitpython": ["git"],
        "python-dateutil": ["dateutil"],
        "python-editor": ["editor"],
        "python-statsd": ["statsd"],
        "sseclient-py": ["sseclient"],
        "oslo.config": ["oslo_config"],
    },
)

python_requirement_library(
    name="flex",
    requirements=["flex"],
    dependencies=[
        # flex uses pkg_resources w/o declaring the dep
        "//:setuptools",
    ],
)

python_requirement_library(
    name="pydevd-pycharm",
    requirements=["pydevd-pycharm==211.7142.13"],
)

python_tests(
    name="tests",
    skip_pylint=True,
)
