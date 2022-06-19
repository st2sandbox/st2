# python_sources(skip_pylint=True)  # setup.py

python_requirement(
    name="winrm",
    requirements=["pywinrm"],
    modules=["winrm"],
)

stevedore_extension(
    name="runner",
    namespace="st2common.runners.runner",
    entry_points={
        "winrm-cmd": "winrm_runner.winrm_command_runner",
        "winrm-ps-cmd": "winrm_runner.winrm_ps_command_runner",
        "winrm-ps-script": "winrm_runner.winrm_ps_script_runner",
    },
)

st2_runner_python_distribution(
    runner_name="winrm",
    description=(
        "WinRM shell command and PowerShell script action runner for"
        " the StackStorm event-driven automation platform"
    ),
)
