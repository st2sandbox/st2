# python_sources(skip_pylint=True)  # setup.py

st2_component_python_distribution(
    component_name="st2common",
    dependencies=[
        ":metrics_drivers",
        ":rbac_backend",
        "./st2common",
        "./st2common/bootstrap",
        "./st2common/callback",
        "./st2common/cmd",
        "./st2common/constants",
        "./st2common/content",
        "./st2common/exceptions",
        #"./st2common/expressions",
        "./st2common/garbage_collection",
        "./st2common/logging",
        #"./st2common/metrics",
        #"./st2common/metrics/drivers",
        "./st2common/middleware",
        "./st2common/models",
        "./st2common/models/api",
        "./st2common/models/db",
        "./st2common/models/system",
        "./st2common/models/utils",
        "./st2common/persistence",
        "./st2common/policies",
        "./st2common/policies/meta",
        #"./st2common/rbac",
        "./st2common/runners",
        "./st2common/services",
        "./st2common/stream",
        "./st2common/transport",
        "./st2common/util",
        "./st2common/util/green",
        "./st2common/util/schema",
        "./st2common/validators",
        "./st2common/validators/api",
        "./st2common/validators/workflow",
    ],
)

stevedore_extension(
    name="metrics_drivers",
    namespace="st2common.metrics.driver",
    entry_points={
        "statsd": "st2common.metrics.drivers.statsd_driver:StatsdDriver",
        "noop": "st2common.metrics.drivers.noop_driver:NoopDriver",
        "echo": "st2common.metrics.drivers.echo_driver:EchoDriver",
    },
)

stevedore_extension(
    name="rbac_backend",
    namespace="st2common.rbac.backend",
    entry_points={
        "noop": "st2common.rbac.backends.noop:NoOpRBACBackend",
    },
)
