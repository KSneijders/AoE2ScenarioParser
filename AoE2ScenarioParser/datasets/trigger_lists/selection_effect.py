from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class SelectionEffect(_DataSetIntEnums):
    """
    This enum class provides the integer values for the different selection effects that can be used in the 'Modify
    Attribute' effect with the 'SelectionEffect' attribute.

    **Examples**:

    >>> SelectionEffect.HP_BAR_OUTLINE
    <SelectionEffect.HP_BAR_OUTLINE: 1>
    """
    HP_BAR = 0
    """Has hit point bar"""
    HP_BAR_OUTLINE = 1
    """Has hit point bar, and outline"""
    NONE = 2
    """No hit point bar, or outline"""
    OUTLINE = 3
    """No hit point bar, but has outline"""
