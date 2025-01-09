from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class UnitAIAction(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the unit AI actions in the game. Used in the 'Object
    Has Action' condition.

    **Examples**

    >>> UnitAIAction.ATTACK
    <UnitAIAction.ATTACK: 1>
    """
    ANY = 0
    """Fires if the unit has any action"""
    ATTACK = 1
    """Fires when the unit is attacking any unit"""
    BUILD = 3
    """Unknown"""
    CONVERT = 5
    """Fires when a monk or missionary is converting any unit"""
    DEFEND = 2
    """Unknown"""
    ENTER = 18
    """Unknown"""
    EVADE = 17
    """Unknown"""
    EXPLORE = 6
    """Unknown"""
    FOLLOW = 13
    """Fires when a unit is following any unit"""
    GATHER = 10
    """Fires when a villager or fishing ship is gathering resources"""
    HEAL = 4
    """Fires when a monk or missionary is healing another unit"""
    HUNT = 14
    """
    Fires when a hunter is gathering from a corpse of a hunted animal. Does **NOT** fire when the hunter is chasing the
    animal
    """
    IDLE = 24
    """Fires when a unit is standing still"""
    MOVE = 11
    """Fires when a unit is moving"""
    PATROL = 12
    """Fires when a unit is patrolling"""
    RELIC = 23
    """Unknown"""
    REPAIR = 19
    """Fires when a villager is repairing any other unit"""
    RESEARCH = 21
    """Unknown"""
    RETREAT = 9
    """Unknown"""
    RUNAWAY = 8
    """Unknown"""
    STOP = 7
    """Unknown"""
    TRADE = 16
    """Fires when a trade cart is returning to any of its own player's markets"""
    TRAIN = 20
    """Unknown"""
    TRANSPORT = 15
    """Unknown"""
    UNLOAD = 22
    """Fires when a transport ship is tasked to unload objects. Note that the transport gets stuck in this state!"""
