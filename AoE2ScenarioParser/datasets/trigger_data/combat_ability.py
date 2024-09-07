from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntFlags


class CombatAbility(_DataSetIntFlags):
    """
    This enum class provides the integer values for the break off combat flags that can be used
    in the 'Modify Attribute' effect with the 'Combat Ability' attribute. This is a combinable bit field.

    **Examples**

    >>> CombatAbility.RESIST_ARMOR_IGNORING_ATTACKS
    <CombatAbility.RESIST_ARMOR_IGNORING_ATTACKS: 2>
    """
    NORMAL = 0
    IGNORE_MELEE_PIERCE_ARMOR = 1
    RESIST_ARMOR_IGNORING_ATTACKS = 2
    DAMAGE_TARGET_ARMOR = 4
    ATTACK_GROUND = 8
    BULK_VOLLEY_RELEASE = 16
