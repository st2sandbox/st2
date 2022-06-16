python_tests(
    name="tests",
    timeout=120,
    dependencies=[
        "st2client/tests/fixtures:st2client-ini",
    ],
    skip_pylint=True,
    tags=["unit"],
    overrides={
        (
            "test_execution_tail_command.py",
            "test_commands.py",
        ): {
            "dependencies": [
                "st2client/tests/base.py",
            ],
        },
    },
)

python_sources(skip_pylint=True)
