python_library(skip_pylint=True)

stevedore_extension(
    name="runner",
    namespace="st2common.runners.runner",
    entry_points={
        "local-shell-cmd": "local_runner.local_shell_command_runner",
        "local-shell-script": "local_runner.local_shell_script_runner",
    },
)
