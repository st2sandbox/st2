__defaults__({python_tests: dict(tags=["integration"])})

python_tests(
    name="tests",
    skip_pylint=True,
    stevedore_namespaces=[
        "orquesta.expressions.functions",
        "st2common.runners.runner",
        "st2common.rbac.backend",
        "st2common.metrics.driver",
    ],
    dependencies=[
        # used by test_register_content_script
        "conf/st2.tests.conf:st2_tests_conf",
        "conf/st2.tests1.conf:st2_tests_conf",
    ],
)

python_sources(skip_pylint=True)
