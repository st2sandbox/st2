# python_sources(skip_pylint=True)  # setup.py

stevedore_extension(
    name="runner",
    namespace="st2common.runners.runner",
    entry_points={
        "remote-shell-cmd": "remote_runner.remote_command_runner",
        "remote-shell-script": "remote_runner.remote_script_runner",
    },
)

st2_runner_python_distribution(
    runner_name="remote",
    description=(
        "Remote SSH shell command and script action runner for StackStorm event-driven "
        "automation platform"
    ),
)
