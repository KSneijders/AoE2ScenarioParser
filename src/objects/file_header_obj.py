class FileHeaderObj:
    data = {
        "version": None,
        "savable": None,
        "timestamp": None,
        "scenario_instr": None,
        "player_count": None,
        "steam_name": None
    }

    def __init__(self):
        pass


attribute_mapping = {
    "Version": "version",
    "Savable": "savable",
    "Timestamp of Last Save": "timestamp",
    "Scenario Instructions": "scenario_instr",
    "Player Count": "player_count",
    "Steam name": "steam_name"
}

