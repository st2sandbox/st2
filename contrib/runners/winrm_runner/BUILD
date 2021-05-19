python_library(skip_pylint=True)

python_requirement_library(
    name="winrm",
    requirements=["pywinrm"],
    module_mapping={
        "pywinrm": ["winrm"],
    }
)

stevedore_extension(
    name="runner",
    namespace = "st2common.runners.runner",
    entry_points = {
        "winrm-cmd": "winrm_runner.winrm_command_runner",
        "winrm-ps-cmd": "winrm_runner.winrm_ps_command_runner",
        "winrm-ps-script": "winrm_runner.winrm_ps_script_runner",
    }
)
