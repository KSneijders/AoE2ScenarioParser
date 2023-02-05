from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class Comparison(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the comparisons in the game. Used in a lot of
    conditions like 'Accumulate Attribute' to perform logical operations on the attribute values

    **Examples**

    >>> Comparison.EQUAL
    <Comparison.EQUAL: 0>
    """
    EQUAL = 0
    LESS = 1
    LARGER = 2
    LESS_OR_EQUAL = 3
    LARGER_OR_EQUAL = 4
