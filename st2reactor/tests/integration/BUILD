__defaults__({python_tests: dict(tags=["integration"])})

python_tests(
    name="tests",
    skip_pylint=True,
    dependencies=[
        "conf/st2.tests.conf:st2_tests_conf",
        "conf/st2.tests2.conf:st2_tests_conf",
    ],
)
