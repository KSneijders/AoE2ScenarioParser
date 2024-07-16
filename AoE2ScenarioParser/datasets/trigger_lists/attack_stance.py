from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class AttackStance(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the different unit stances in the game. Used in the
    'Change Object Stance' effect

    **Examples**

    >>> AttackStance.AGGRESSIVE_STANCE
    <AttackStance.AGGRESSIVE_STANCE: 0>
    """
    AGGRESSIVE_STANCE = 0
    DEFENSIVE_STANCE = 1
    STAND_GROUND = 2
    NO_ATTACK_STANCE = 3
