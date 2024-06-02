from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class Age(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the different ages in the game. These values are
    used by the 'Current Age' player resource

    **Examples**

    >>> Age.IMPERIAL_AGE
    <Age.IMPERIAL_AGE: 3>
    """
    DARK_AGE = 0
    FEUDAL_AGE = 1
    CASTLE_AGE = 2
    IMPERIAL_AGE = 3
