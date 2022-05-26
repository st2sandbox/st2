python_requirements(
    name="reqs",
    source="requirements-tests.txt",
    module_mapping={"mail-parser": ["mailparser"]},
)

pack_metadata(
    name="metadata",
)

python_sources(
    dependencies=[":metadata"],
)
