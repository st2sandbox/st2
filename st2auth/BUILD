python_sources(skip_pylint=True)

stevedore_extension(
    name="sso_backends",
    namespace="st2auth.sso.backends",
    entry_points={
        "noop": "st2auth.sso.noop:NoOpSingleSignOnBackend",
    },
)
