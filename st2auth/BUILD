st2_component_python_distribution(
    component_name="st2auth",
    dependencies=[
        # API classes not that cannot be inferred from bin/st2auth
        "./st2auth/backends/base.py",
    ],
    scripts=["bin/st2auth"],
)

stevedore_extension(
    name="sso_backends",
    namespace="st2auth.sso.backends",
    entry_points={
        "noop": "st2auth.sso.noop:NoOpSingleSignOnBackend",
    },
)
