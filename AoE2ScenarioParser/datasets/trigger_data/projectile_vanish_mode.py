from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class ProjectileVanishMode(_DataSetIntEnums):
    """
    This enum class provides the integer values used to references the different projectile vanish mode settings that
    can be used in the 'Modify Attribute' effect with the 'Projectile Vanish Mode' attribute.

    **Examples**

    >>> ProjectileVanishMode.DISAPPEAR_ON_IMPACT
    <ProjectileVanishMode.DISAPPEAR_ON_IMPACT: 0>
    """
    DISAPPEAR_ON_IMPACT = 0
    PASS_THROUGH = 1
