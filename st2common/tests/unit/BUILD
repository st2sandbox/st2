python_tests(
    name="tests",
    dependencies=["st2common/tests/unit/base.py"],
    uses=["mongo"],
    skip_pylint=True,
    tags=["unit"],
    stevedore_namespaces=[
        "orquesta.expressions.functions",
        "st2common.runners.runner",
        "st2common.rbac.backend",
        "st2common.metrics.driver",
    ],
)

python_library(skip_pylint=True)
