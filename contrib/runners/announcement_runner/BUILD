# python_sources(skip_pylint=True)  # setup.py

stevedore_extension(
    name="runner",
    namespace="st2common.runners.runner",
    entry_points={
        "announcement": "announcement_runner.announcement_runner",
    },
)

st2_runner_python_distribution(
    runner_name="announcement",
    description=(
        "Announcement action runner for StackStorm event-driven automation platform"
    ),
)
