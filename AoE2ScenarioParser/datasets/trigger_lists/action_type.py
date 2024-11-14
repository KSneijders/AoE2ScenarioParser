from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class ActionType(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the different action types in the game.
    These values are used in the Task Object effect

    **Examples**

    >>> ActionType.DROP_RELIC
    <ActionType.DROP_RELIC: 14>
    """
    DEFAULT = 0
    MOVE = 1
    PATROL = 2
    GUARD = 3
    FOLLOW = 4
    STOP = 5
    ATTACK_GROUND = 6
    GARRISON = 7
    KILL = 8
    UNLOAD = 9
    GATHER_POINT = 10
    LOCK_UNLOCK = 11
    WORK = 12
    UNGARRISON = 13
    DROP_RELIC = 14
    PACK = 15
    UNPACK = 16
    ATTACK_MOVE = 17
    LINE_FORMATION = 18
    BOX_FORMATION = 19
    STAGGERED_FORMATION = 20
    FLANK_FORMATION = 21
