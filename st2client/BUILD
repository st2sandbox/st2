st2_component_python_distribution(
    component_name="st2client",
    dependencies=[
        # required for SOCKS proxy support (HTTP_PROXY, HTTPS_PROXY, NO_PROXY)
        ":pysocks",
    ],
)

python_requirement(
    name="pysocks",
    requirements=["pysocks"],
)
