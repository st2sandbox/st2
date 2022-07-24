python_sources(
    overrides={
        "__init__.py": {
            "dependencies": [
                # keep this list up-to-date with MODEL_MODULE_NAMES
                "./auth.py",
                "./action.py",
                "./actionalias.py",
                "./keyvalue.py",
                "./execution.py",
                "./executionstate.py",
                "./execution_queue.py",
                "./liveaction.py",
                "./notification.py",
                "./pack.py",
                "./policy.py",
                "./rbac.py",
                "./rule.py",
                "./rule_enforcement.py",
                "./runner.py",
                "./sensor.py",
                "./trace.py",
                "./trigger.py",
                "./webhook.py",
                "./workflow.py",
                # these are not included on purpose
                # "./reactor.py",  # convenience imports (no models)
                # "./timer.py",  # meta model that is not persisted in db
            ],
        },
    },
)
