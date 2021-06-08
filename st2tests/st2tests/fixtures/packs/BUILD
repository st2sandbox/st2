python_library()

# The files in test_content_version* targets are in ./test_content_version
# which is a git submodule. pack_metadata_in_git_submodule will error with
# instructions on how to checkout the submodules if they are not checked out.
# The test_content_version* targets are dependencies of ./test_content_version_fixture

pack_metadata_in_git_submodule(
    name="test_content_version_metadata",
    sources=[
        "test_content_version/pack.yaml",
        "test_content_version/**/*.yaml",
        "test_content_version/icon.png",
    ],
)

python_library(
    name="test_content_version",
    dependencies=[":test_content_version_metadata"],
    sources=[
        "test_content_version/**/*.py",
    ],
)
