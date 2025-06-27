from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class AttackPriority(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the attack priority values used in the game. Used in the
    'Modify Attribute' effect with the 'Attack Priority' attributes

    **Examples**

    >>> AttackPriority.UNITS_BEFORE_BUILDINGS
    <AttackPriority.UNITS_BEFORE_BUILDINGS: 1>
    """
    UNITS_BEFORE_BUILDINGS = 1
    BUILDINGS_BEFORE_UNITS = 2
    BUILDINGS_ONLY = 3
