GIT_SUBMODULES_INSTRUCTIONS = """
You need git submodules! Please init ... instructions
"""

pack_metadata_no_unmatched_globs(
    name="metadata",
    sources=[
        "st2tests/st2tests/fixtures/packs/test_content_version/pack.yaml",
        "st2tests/st2tests/fixtures/packs/test_content_version/**/*.yaml",
        "st2tests/st2tests/fixtures/packs/test_content_version/icon.png",
    ],
    message_on_unmatched_globs=GIT_SUBMODULES_INSTRUCTIONS,
)

python_library_no_unmatched_globs(
    name="test_content_version",
    dependencies=[":metadata"],
    sources=[
        "st2tests/st2tests/fixtures/packs/test_content_version/**/*.py",
    ],
    message_on_unmatched_globs=GIT_SUBMODULES_INSTRUCTIONS,
)

python_library(
    dependencies=[":git_submodule", ":test_content_version"],
)
