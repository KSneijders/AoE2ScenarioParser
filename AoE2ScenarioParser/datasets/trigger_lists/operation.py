from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class Operation(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the operations in the game. Used in a lot of effects
    like 'Modify Attribute' to control whether an attribute is set, added to, multiplied or divided by a value.

    **Examples**

    >>> Operation.MULTIPLY
    <Operation.MULTIPLY: 4>
    """
    SET = 1
    ADD = 2
    SUBTRACT = 3
    MULTIPLY = 4
    DIVIDE = 5
