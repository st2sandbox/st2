python_sources(skip_pylint=True)

stevedore_extension(
    name="runner",
    namespace="st2common.runners.runner",
    entry_points={
        "remote-shell-cmd": "remote_runner.remote_command_runner",
        "remote-shell-script": "remote_runner.remote_script_runner",
    },
)
