__defaults__({python_tests: dict(tags=["unit"])})

python_tests(
    name="tests",
    dependencies=["st2common/tests/unit/base.py"],
    uses=["mongo"],
    skip_pylint=True,
    stevedore_namespaces=[
        "orquesta.expressions.functions",
        "st2common.runners.runner",
        "st2common.rbac.backend",
        "st2common.metrics.driver",
    ],
)

python_test_utils(
    sources=["*.py", "!test_*.py"],
    skip_pylint=True,
)
