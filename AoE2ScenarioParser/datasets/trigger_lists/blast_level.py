from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class BlastLevel(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the blast level values used in the game. Used in the
    'Modify Attribute' effect with the 'Blast Attack/Defense Level' attributes

    **Examples**

    >>> BlastLevel.TREES
    <BlastLevel.TREES: 1>
    """
    RESOURCES = 0
    """
    damage resources, nearby allied units and tress
    """
    TREES = 1
    """
    damage trees, nearby allied units
    """
    NEARBY_UNITS = 2
    """
    damage nearby allied units
    """
    TARGET_ONLY = 3
    """
    damage targeted unit only
    """
    FIXED_FIVE = 4
    """
    Deal a fixed 5 HP of damage to nearby units
    """
    DISTANCE_ATTENUATION = 64
    """
    Attenuate damage as distance from the centre of attack increases (infantry only)
    """
    DIRECTIONAL = 128
    """
    Blast damage is dealt along the direction the unit is facing only. This area is a very narrow cone    
    """
