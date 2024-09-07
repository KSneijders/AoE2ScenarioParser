from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntFlags


class GarrisonType(_DataSetIntFlags):
    """
    This enum class provides the integer values for the different garrison type flags that can be used in the 'Modify
    Attribute' effect with the 'Garrison Type' attribute. This is a combinable bit field

    **Examples**

    >>> GarrisonType.VILLAGERS
    <GarrisonType.VILLAGERS: 1>
    """
    NONE = 0
    VILLAGERS = 1
    INFANTRY = 2
    CAVALRY = 4
    MONKS = 8
    HERDABLES = 16
    SIEGE = 32
    SHIPS = 64
