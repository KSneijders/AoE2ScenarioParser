from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class ObjectType(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the object types in the game. Used in a lot of effects
    and conditions, like 'Kill Object', 'Objects in Area'.

    **Examples**

    >>> ObjectType.OTHER
    <ObjectType.OTHER: 1>
    """
    OTHER = 1
    BUILDING = 2
    CIVILIAN = 3
    MILITARY = 4
