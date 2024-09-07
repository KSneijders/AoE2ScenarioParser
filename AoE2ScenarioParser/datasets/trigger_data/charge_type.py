from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class ChargeType(_DataSetIntEnums):
    """
    This enum provides the integer values used to reference the type of charge that a unit holds

    **Examples**

    >>> ChargeType.AREA_ATTACK_CHARGE
    <ChargeType.AREA_ATTACK_CHARGE: 3>
    """
    ATTACK_CHARGE = 1
    UNKNOWN_CHARGE = 2
    AREA_ATTACK_CHARGE = 3
    AGILITY_CHARGE = 4
