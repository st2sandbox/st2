resources(
    name="execution_fixtures",
    sources=["execution*.json", "execution*.txt"],
)

resources(
    name="st2client-ini",
    sources=["*.ini"],
)

python_library(
    skip_pylint=True,
    dependencies=[":execution_fixtures"],
)
