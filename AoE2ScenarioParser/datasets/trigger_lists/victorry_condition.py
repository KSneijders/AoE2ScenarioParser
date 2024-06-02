from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class VictoryCondition(_DataSetIntEnums):
    """
    This enum class provides the integer values used to references the different victory conditions that can be set
    using the Global Victory tab in the in-game editor.

    **Examples**

    >>> VictoryCondition.TIME_LIMIT
    <VictoryCondition.TIME_LIMIT: 3>
    """
    STANDARD = 0
    CONQUEST = 1
    SCORE = 2
    TIME_LIMIT = 3
    CUSTOM = 4
    SECONDARY_GAME_MODE = 6
