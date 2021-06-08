# The files here are in ../test_content_version which is a git submodule
# *_in_git_submodule will error with instructions on how to checkout the
# submodule if the submodules are not checked out.

pack_metadata_in_git_submodule(
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
    dependencies=[":git_submodule", ":test_content_version"],
)
