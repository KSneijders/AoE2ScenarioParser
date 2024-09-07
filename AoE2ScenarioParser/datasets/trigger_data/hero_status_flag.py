from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntFlags


class HeroStatusFlag(_DataSetIntFlags):
    """
    This enum class provides the integer values for the different hero status flags that can be used in the 'Modify
    Attribute' effect with the 'Hero Status' attribute. This is a combinable bit field

    **Methods**

    - ``HeroStatusFlag.combine()``
    - ``HeroStatusFlag.split_flags()``


    **Examples**

    >>> HeroStatusFlag.HERO_REGENERATION
    <HeroStatusFlag.HERO_REGENERATION: 4>
    >>> HeroStatusFlag.HERO_REGENERATION | HeroStatusFlag.HERO_GLOW
    <HeroStatusFlag.HERO_GLOW|HERO_REGENERATION: 68>
    """
    NO_HERO_STATUS = 0
    FULL_HERO_STATUS = 1
    CANNOT_BE_CONVERTED = 2
    HERO_REGENERATION = 4
    DEFENSIVE_STANCE_BY_DEFAULT = 8
    PROTECTED_FORMATION = 16
    DELETE_CONFIRMATION = 32
    HERO_GLOW = 64
    INVERT_FLAGS = 128
