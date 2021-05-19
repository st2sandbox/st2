python_library(skip_pylint=True)

stevedore_extension(
    name="metrics_drivers",
    namespace = "st2common.metrics.driver",
    entry_points = {
        "statsd": "st2common.metrics.drivers.statsd_driver:StatsdDriver",
        "noop": "st2common.metrics.drivers.noop_driver:NoopDriver",
        "echo": "st2common.metrics.drivers.echo_driver:EchoDriver",
    }
)

stevedore_extension(
    name="rbac_backend",
    namespace = "st2common.rbac.backend",
    entry_points = {
        "noop": "st2common.rbac.backends.noop:NoOpRBACBackend",
    }
)
