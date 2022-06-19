# python_sources(skip_pylint=True)  # setup.py

stevedore_extension(
    name="runner",
    namespace="st2common.runners.runner",
    entry_points={
        "noop": "noop_runner.noop_runner",
    },
)

st2_runner_python_distribution(
    runner_name="noop",
    description="No-Op action runner for StackStorm event-driven automation platform",
)
