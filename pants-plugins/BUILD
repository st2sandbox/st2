__defaults__(
    all=dict(
        resolve="pants-plugins",
        skip_pylint=True,
    )
)

# only one of these targets should be uncommented (pants_ or python_requirement)

pants_requirements(
    name="pants",
    testutil=False,
)

# this is a more restricted version of the above.
# python_requirement(
#    name="pants",
#    requirements=["pantsbuild.pants==2.11.0"],
# )

python_sources()
