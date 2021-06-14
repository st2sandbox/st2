files(
    name="logging",
    sources=["logging*.conf"],
)

files(
    name="logging_syslog",
    sources=["syslog*.conf"],
)

files(
    name="st2.conf",
    sources=["st2exporter.dev.conf"],
    dependencies=[
        "st2actions/conf/logging.notifier.conf:logging",
    ],
)
