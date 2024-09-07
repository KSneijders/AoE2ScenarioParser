from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class VictoryTimerType(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the different types of victory timer types.

    **Examples**

    >>> VictoryTimerType.WONDER_TIMER
    <VictoryTimerType.WONDER_TIMER: 0>
    """
    WONDER_TIMER = 0
    RELIC_TIMER = 1
    KING_OF_THE_HILL_TIMER = 2
