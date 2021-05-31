files(
    name="registered_content",
    sources=[
        "./descendants/**/*.yaml",
        "./rbac/**/*.yaml",
        "./rbac_invalid/**/*.yaml",
        "./rule_enforcements/**/*.yaml",
        "./timers/**/*.yaml",
    ],
)

target(
    name="packs_metadata",
    dependencies=[
        "./aliases:metadata",
        "./backstop:metadata",
        "./generic:metadata",
        "./localrunner_pack:metadata",
        "./traces:metadata",
    ],
)

python_library()
