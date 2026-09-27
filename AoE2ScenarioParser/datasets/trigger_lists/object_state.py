from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class ObjectState(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the object state values used in the game. Used in the
    'Object in Area' condition, 'Remove Object' effect, and unit creation.

    **Examples**

    >>> ObjectState.FOUNDATION
    <ObjectState.FOUNDATION: 0>
    """
    FOUNDATION = 0
    ALMOST_ALIVE = 1
    ALIVE = 2
    DEAD = 3
    ALMOST_DEAD = 4
    REALLY_DEAD = 5
    UNDEAD = 6
    REMOVE = 7
    GOING = 8
