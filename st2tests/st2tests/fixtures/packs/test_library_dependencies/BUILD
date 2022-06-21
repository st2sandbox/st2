file(
    name="pack_requirements",
    source="requirements.txt",
)

pack_metadata(
    name="metadata",
    dependencies=[":pack_requirements"],
)

python_sources(
    dependencies=[
        ":metadata",
        "./actions",
    ],
)
