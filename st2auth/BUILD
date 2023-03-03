st2_component_python_distribution(
    component_name="st2auth",
    dependencies=[
        # API classes not that cannot be inferred from bin/st2auth
        "./st2auth/backends/base.py",
    ],
    scripts=["bin/st2auth"],
    entry_points={
        stevedore_namespace("st2auth.sso.backends"): {
            "noop": "st2auth.sso.noop:NoOpSingleSignOnBackend",
        },
    },
)
