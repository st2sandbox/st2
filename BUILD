python_requirements(
    name="reqs",
    source="requirements-pants.txt",
    module_mapping={
        "gitpython": ["git"],
        "python-editor": ["editor"],
        "python-statsd": ["statsd"],
        "sseclient-py": ["sseclient"],
        "oslo.config": ["oslo_config"],
        "RandomWords": ["random_words"],
    },
    overrides={
        # flex uses pkg_resources w/o declaring the dep
        "flex": {
            "dependencies": [
                "//:reqs#setuptools",
            ]
        },
    },
)

python_requirement(
    name="pydevd-pycharm",
    requirements=["pydevd-pycharm==221.5080.212"],
)

python_test_utils(
    name="root",
)
