python_sources(
    overrides={
        "process_container.py": {
            "dependencies": [
				# This is called in a subprocess using filesystem path
				# TODO: make sure that does not confuse pants+PEX
                "./sensor_wrapper.py",
            ],
        },
    },
)
