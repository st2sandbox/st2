# python_sources(skip_pylint=True)  # setup.py

stevedore_extension(
    name="runner",
    namespace="st2common.runners.runner",
    entry_points={
        "action-chain": "action_chain_runner.action_chain_runner",
    },
)

st2_runner_python_distribution(
    runner_name="action_chain",
    description=(
        "Action-Chain workflow action runner for StackStorm event-driven "
        "automation platform"
    ),
)
