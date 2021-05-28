from AoE2ScenarioParser.datasets.units_base import UnitsBase


class OtherInfo(UnitsBase):
    FLARE1_SIGHT_SHOOTED = 112, -1, -1, False  # Generated when being attacked by ranged units.(2 tiles of sight)
    FLARE = 274, -1, -1, False  # Generated when having sent a signal on map by allies.(or name it FLARE2_ALLY_SIGNAL)
    FLARE3 = 332, -1, -1, False  # Unknown.(6 tiles of sight)
    FLARE4 = 697, -1, -1, False  # Unknown.(2 tiles of sight)
    FLARE5_PERMANENT = 1689, -1, -1, False  # Permanently exists on map once created.
