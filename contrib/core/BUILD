python_requirements(
    source="requirements-tests.txt",
    module_mapping={"mail-parser": ["mailparser"]},
)

pack_metadata(
    name="metadata",
)

python_sources(
    dependencies=[":metadata"],
)
