from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class ChargeEvent(_DataSetIntEnums):
    """
    This enum provides the integer values used to reference the action which depletes a unit's charge
    The meaning of this value depends on `Charge Type`

    **Examples**

    >>> ChargeEvent.CHARGE_DEPLETED_ON_ATTACK
    <ChargeEvent.CHARGE_DEPLETED_ON_ATTACK: 1>
    """
    PERFORM_ATTACK_GROUND_ON_OWN_LOCATION = -1
    NO_CHARGE_DEPLETED = 0
    TRANSFORM_AFTER_ATTACK = 0
    CHARGE_DEPLETED_ON_ATTACK = 1
