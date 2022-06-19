# python_sources(skip_pylint=True)  # setup.py

stevedore_extension(
    name="runner",
    namespace="st2common.runners.runner",
    entry_points={
        "python-script": "python_runner.python_runner",
    },
)

st2_runner_python_distribution(
    runner_name="python",
    description=(
        "Python action runner for StackStorm event-driven automation platform"
    ),
)
