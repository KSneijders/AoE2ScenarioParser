from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class ChargeType(_DataSetIntEnums):
    """
    This enum provides the integer values used to reference the type of charge that a unit holds

    **Examples**

    >>> ChargeType.AREA_ATTACK_CHARGE
    <ChargeType.AREA_ATTACK_CHARGE: 3>
    """
    SPAWN_BUILDING_ON_TOP_ABILITY = -5
    CONVERSION_ABILITY = -4
    AURA_ABILITY = -3
    TRANSFORM_ABILITY = -2
    TEMPORARY_TRANSFORM_ABILITY = -1
    ATTACK_CHARGE = 1
    UNKNOWN_CHARGE = 2
    AREA_ATTACK_CHARGE = 3
    AGILITY_CHARGE = 4
    IGNORE_MELEE_ATTACK = 5
    FIRE_ONLY_CHARGE_PROJECTILES = 6
    FIRE_ONE_CHARGE_AND_ADDITIONAL_SECONDARY_PROJECTILES = 7
