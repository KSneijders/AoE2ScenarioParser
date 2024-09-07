from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class ObjectState(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the object state values used in the game. Used in the
    'Object in Area' condition

    **Examples**

    >>> ObjectState.FOUNDATION
    <ObjectState.FOUNDATION: 0>
    """
    FOUNDATION = 0
    ALMOST_ALIVE = 1
    ALIVE = 2
    RESOURCE = 3
    DYING = 4
    DEAD = 5
    UNDEAD = 6
    REMOVE = 7
