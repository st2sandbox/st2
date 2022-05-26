python_requirements(
    source="requirements-pants.txt",
    module_mapping={
        "gitpython": ["git"],
        "python-editor": ["editor"],
        "python-statsd": ["statsd"],
        "sseclient-py": ["sseclient"],
        "oslo.config": ["oslo_config"],
        "RandomWords": ["random_words"],
    },
)

python_requirement(
    name="flex",
    requirements=["flex"],
    dependencies=[
        # flex uses pkg_resources w/o declaring the dep
        "//:setuptools",
    ],
)

python_requirement(
    name="pydevd-pycharm",
    requirements=["pydevd-pycharm==211.7142.13"],
)

python_test_utils(
    name="root",
)
