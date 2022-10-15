files(
    name="st2client_sample_config",
    sources=["st2rc.sample.ini"],
)

sample_conf(  # defined in pants-plugins/sample_conf
    name="st2.conf.sample",
    source="st2.conf.sample",
    dependencies=[
        "tools/config_gen.py",
    ],
)

files(
    name="logrotate",
    sources=["logrotate.conf"],
)

files(
    name="nginx_sample_config",
    sources=["nginx/st2.conf"],
)

files(
    name="st2_kvstore_demo_crypto_key",
    sources=["st2_kvstore_demo.crypto.key.json"],
)

files(
    name="st2_tests_conf",
    sources=[
        "st2.tests*.conf",
    ],
    dependencies=[
        "st2auth/conf:htpasswd",
        "st2actions/conf:logging",
        "st2reactor/conf:logging",
        "st2tests/conf:other-logging-conf",
    ],
)

files(
    name="st2_dev_conf",
    sources=[
        "st2.dev.conf",
    ],
    dependencies=[
        ":st2_kvstore_demo_crypto_key",
        "st2auth/conf:htpasswd",
        "st2actions/conf:logging",
        "st2api/conf:logging",
        "st2auth/conf:logging",
        "st2reactor/conf:logging",
        "st2stream/conf:logging",
    ],
)

files(
    name="st2_package_conf",
    sources=[
        "st2.package.conf",
    ],
)
