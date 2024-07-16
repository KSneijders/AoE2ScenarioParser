from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class ColorMood(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the color mood values used in the game. Used in the
    'Change Color Mood' effect

    **Examples**

    >>> ColorMood.AUTUMN
    <ColorMood.AUTUMN: 1>
    """
    DEFAULT = 0
    AUTUMN = 1
    WINTER = 2
    JUNGLE = 3
    DESERT = 4
    NIGHT = 5
