__defaults__({python_tests: dict(tags=["unit"])})

python_tests(
    name="tests",
    dependencies=["contrib/runners/orquesta_runner/tests/unit/base.py"],
    skip_pylint=True,
)

python_test_utils(
    sources=["*.py", "!test_*.py"],
    skip_pylint=True,
)
