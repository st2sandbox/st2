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

unmatched_globs(
    name="git_submodule",
    dependencies=[":test_content_version", ":metadata"],
    message_on_error="You need git submodules! Please init ... instructions",
)

python_library(
    dependencies=[":git_submodule", ":test_content_version"],
)
