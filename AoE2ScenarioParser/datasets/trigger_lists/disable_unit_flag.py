from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class DisableUnitFlag(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the disable unit flag values used in the game. Used in the
    'Modify Attribute' effect with the 'Disable Unit Flag' attributes

    **Examples**

    >>> DisableUnitFlag.DISABLED
    <DisableUnitFlag.DISABLED: 0>
    """
    DISABLED = 0
    LIMITED_TRAINING_CAN_NOT_BE_RETRAINED = 1
    LIMITED_TRAINING_CAN_BE_RETRAINED = 2
