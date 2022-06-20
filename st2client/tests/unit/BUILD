python_tests(
    name="tests",
    timeout=120,
    dependencies=[
        "st2client/tests/fixtures:st2client-ini",
		# most of the files import tests.base which is ambiguous. Tell pants which one to use.
		"st2client/tests/base.py",
    ],
    skip_pylint=True,
    tags=["unit"],
)

python_sources(skip_pylint=True)
