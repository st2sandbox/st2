__defaults__(
    {(python_test, python_tests): dict(tags=["unit"])},
    extend=True,
)

python_tests(
    name="tests",
    dependencies=[
        # several files import tests.unit.base which is ambiguous. Tell pants which one to use.
        "st2common/tests/unit/base.py",
    ],
    uses=["mongo", "rabbitmq"],
    stevedore_namespaces=[
        "orquesta.expressions.functions",
        "st2common.runners.runner",
        "st2common.rbac.backend",
        "st2common.metrics.driver",
    ],
)

python_test_utils(
    sources=["*.py", "!test_*.py"],
)
