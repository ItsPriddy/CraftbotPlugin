CRAFTBOT_IDEX = dict(
    name="Craftbot IDEX",
    model="Craftbot IDEX",
    header_version=1,  # default is 1
)

CRAFTBOT_DISCOVER_MACHINES = [
    CRAFTBOT_IDEX,
]


def is_machine_discover_supported(machine_name: str) -> bool:
    return machine_name in [machine['name'] for machine in CRAFTBOT_DISCOVER_MACHINES]
