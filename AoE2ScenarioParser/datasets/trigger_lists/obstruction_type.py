from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class ObstructionType(_DataSetIntEnums):
    """
    This enum class provides the integer values for the different obstruction types that can be used in the 'Modify
    Attribute' effect with the 'ObstructionType' attribute.

    **Examples**:

    >>> ObstructionType.SQUARE_OUTLINE_PASSABLE
    <ObstructionType.SQUARE_OUTLINE_PASSABLE: 0>
    """
    SQUARE_OUTLINE_PASSABLE = 0
    """Square outline and passable"""
    _SQUARE_OUTLINE_PASSABLE = 1
    """Use ``<ObstructionType.SQUARE_OUTLINE_PASSABLE: 0>`` instead"""
    SOLID_SQUARE_OUTLINE_COLLISION = 2
    """Solid square outline, and has collision box"""
    SQUARE_OUTLINE_COLLISION = 3
    """Square outline, and has collision box"""
    NO_OUTLINE_PASSABLE = 4
    """No outline, and passable"""
    ROUND_OUTLINE_COLLISION = 5
    """Round outline, and has collision box"""
    SOLID_SQUARE_OUTLINE_COLLISION_MOUNTAINS = 10
    """Same as ``<ObstructionType.SOLID_SQUARE_OUTLINE_COLLISION: 2>`` but designed for mountains"""
