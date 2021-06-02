files(
    name="artifacts",
    sources=[
        "**/*.cer",
        "**/*.cnf",
        "**/*.p12",
        "**/*.pem",
        "ca/index.txt*",
        "ca/serial*",
    ],
)

python_library(
    dependencies=[":artifacts"],
)
