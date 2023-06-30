from enum import IntEnum


class ScenarioVariant(IntEnum):
    """
    This enum class provides the integer values used to reference the different variants of scenarios (and the game).
    """
    LEGACY = 0
    AOE2 = 1
    ROR = 2

    def to_display_name(self) -> str:
        return {
            ScenarioVariant.LEGACY: 'Legacy',
            ScenarioVariant.AOE2: 'Age of Empires 2',
            ScenarioVariant.ROR:  'Return of Rome',
        }[self]

    def applicants(self):
        return {
            ScenarioVariant.LEGACY: 'AoC & Bare HD',
            ScenarioVariant.AOE2: 'HD with expansions & DE',
            ScenarioVariant.ROR:  'Return of Rome',
        }[self]
