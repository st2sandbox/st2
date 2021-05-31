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
        "./packs:packs_metadata",
        "./packs_1:packs_metadata",
        "./packs_invalid:packs_metadata",
        "./traces:metadata",
    ],
)

python_library()
