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
        # do not use the prance[flex] extra as that pulls in an old version of flex
        "prance": {
            "dependencies": [
                "//:reqs#flex",
            ]
        },
        # stevedore uses pkg_resources w/o declaring the dep
        "stevedore": {
            "dependencies": [
                "//:reqs#setuptools",
            ]
        },
        # make sure anything that uses st2-auth-ldap gets the st2auth constant
        "st2-auth-ldap": {
            "dependencies": [
                "st2auth/st2auth/backends/constants.py",
            ]
        },
    },
)

target(
    name="auth_backends",
    dependencies=[
        "//:reqs#st2-auth-backend-flat-file",
        "//:reqs#st2-auth-ldap",
    ],
)

python_requirement(
    name="pydevd-pycharm",
    requirements=["pydevd-pycharm==221.5080.212"],
)

python_test_utils(
    name="root",
    skip_pylint=True,
)

file(
    name="license",
    source="LICENSE",
)
