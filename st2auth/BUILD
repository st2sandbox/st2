# python_sources(skip_pylint=True)  # setup.py

st2_component_python_distribution(
    component_name="st2auth",
)

stevedore_extension(
    name="sso_backends",
    namespace="st2auth.sso.backends",
    entry_points={
        "noop": "st2auth.sso.noop:NoOpSingleSignOnBackend",
    },
)
