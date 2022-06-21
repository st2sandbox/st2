# python_sources(skip_pylint=True)  # setup.py

st2_component_python_distribution(
    component_name="st2common",
    dependencies=[
        # public API (not imported directly by any st2common entry points)
        "./st2common/callback/base.py",
        "./st2common/constants/garbage_collection.py",
        "./st2common/constants/policy.py",
        "./st2common/constants/timer.py",
        "./st2common/models/api/auth.py",
        "./st2common/models/api/inquiry.py",
        "./st2common/models/api/rbac.py",
        "./st2common/models/api/rule_enforcement.py",
        "./st2common/models/api/webhook.py",
        "./st2common/models/db/timer.py",
        "./st2common/models/system/actionchain.py",
        "./st2common/models/system/paramiko_command_action.py",
        "./st2common/models/system/paramiko_script_action.py",
        "./st2common/persistence/execution_queue.py",
        "./st2common/persistence/marker.py",  # TODO: drop with st2exporter removal
        "./st2common/policies/concurrency.py",
        "./st2common/transport/consumers.py",
        "./st2common/validators/api/misc.py",
        "./st2common/services/datastore.py",
        "./st2common/services/inquiry.py",
        "./st2common/services/policies.py",
        "./st2common/services/rules.py",
        "./st2common/services/sensor_watcher.py",
        "./st2common/services/trigger_dispatcher.py",
        "./st2common/services/triggerwatcher.py",
        "./st2common/util/actionalias_helpstring.py",
        "./st2common/util/auth.py",
        "./st2common/util/keyvalue.py",
        "./st2common/util/sandboxing.py",
        "./st2common/util/service.py",
        "./st2common/util/wsgi.py",
        # public API: used by all of our logging conf files
        "./st2common/logging",
        # public API: used by runners and python actions
        "./st2common/runners",
        # API: used by st2auth, st2api, st2stream
        "./st2common/middleware",
        # API: used by st2stream
        "./st2common/stream",
        # TODO: missing st2common/bin/st2-purge-inquiries
        "./st2common/garbage_collection/inquiries.py",
        # these convenience imports can probably be removed
        # once persistence.reactor usages are replaced
        "./st2common/models/db/reactor.py",  # dead code / unused
        "./st2common/persistence/reactor.py",
        # dead code (nothing imports it)
        # "./st2common/constants/scheduler.py",
        # "./st2common/content/validators.py",
        # "./st2common/exceptions/api.py",  # InternalServerErrorException
        # "./st2common/exceptions/connection.py",  # UnknownHostException, ConnectionErrorException, AuthenticationException
        # "./st2common/exceptions/resultstracker.py",  # ReferenceNotFoundError
        # "./st2common/models/api/actionrunner.py",
        # "./st2common/util/argument_parser.py",
        # "./st2common/util/gunicorn_workers.py",
        # "./st2common/validators/workflow",
    ],
    scripts=[
        # some scripts in bin are only for development and should not be included.
        "bin/st2-bootstrap-rmq",
        "bin/st2-cleanup-db",
        "bin/st2-register-content",
        "bin/st2-purge-executions",
        "bin/st2-purge-workflows",
        "bin/st2-purge-task-executions",
        "bin/st2-purge-trigger-instances",
        "bin/st2-purge-traces",
        "bin/st2-purge-rule-enforcements",
        "bin/st2-generate-symmetric-crypto-key",
        "bin/st2-track-result",
        "bin/st2-validate-pack",
        "bin/st2-validate-pack-config",
        "bin/st2-pack-install",
        "bin/st2-pack-download",
        "bin/st2-pack-setup-virtualenv",
        "bin/migrations/v3.5/st2-migrate-db-dict-field-values",
        "bin/st2-run-pack-tests:shell",
        "bin/st2ctl:shell",
        "bin/st2-self-check:shell",
        # dev scripts we might want to include
        # "bin/st2-generate-schemas",
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
