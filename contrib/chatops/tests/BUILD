files(
    name="fixtures",
    sources=["fixtures/*.json"],
)

python_tests(
    name="tests0",
    dependencies=[":fixtures"],
    skip_pylint=True,
)

python_library(skip_pylint=True)
