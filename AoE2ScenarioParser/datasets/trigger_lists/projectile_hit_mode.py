from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class ProjectileHitMode(_DataSetIntEnums):
    """
    This enum class provides the integer values used to references the different projectile hit mode settings that can
    be used in the 'Modify Attribute' effect with the 'Projectile Hit Mode' attribute.

    **Examples**

    >>> ProjectileHitMode.ANY_OBSTACLE
    <ProjectileHitMode.ANY_OBSTACLE: 2>
    """
    TARGET_ONLY = 0
    """
    Collide only with the targeted unit"
    """
    ANY_PLAYER_UNIT = 1
    """
    Collide with any damage-able units in the path to the targeted unit"
    """
    ANY_OBSTACLE = 2
    """
    Collide with any unit in the path to the targeted unit
    """
