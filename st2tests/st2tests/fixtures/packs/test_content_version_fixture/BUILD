pack_metadata(
    name="metadata",
    sources=[
        "st2tests/st2tests/fixtures/packs/test_content_version/pack.yaml",
        "st2tests/st2tests/fixtures/packs/test_content_version/**/*.yaml",
        "st2tests/st2tests/fixtures/packs/test_content_version/icon.png",
    ],
)

python_library(
    name="test_content_version",
    dependencies=[":metadata"],
    sources=[
        "st2tests/st2tests/fixtures/packs/test_content_version/**/*.py",
    ],
)

python_library(
    dependencies=[":test_content_version"],
)
