from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntFlags


class ProjectileSmartMode(_DataSetIntFlags):
    """
    This enum class provides the integer values used to reference the smart projectile flag values used in the game.
    Used in the 'Modify Attribute' effect with the 'Projectile Smart Mode' attribute. This is a combainable bit field

    **Examples**

    >>> ProjectileSmartMode.HAS_BALLISTICS
    <ProjectileSmartMode.HAS_BALLISTICS: 1>
    """
    TARGET_CURRENT_LOCATION = 0
    TARGET_FUTURE_LOCATION = 1
    FULL_DAMAGE_ON_MISSED_HIT = 2
