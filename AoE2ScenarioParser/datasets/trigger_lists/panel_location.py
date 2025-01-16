from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class PanelLocation(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the panel positons in the game. Used in the 'Display
    Information' effect.

    **Examples**

    >>> PanelLocation.TOP
    <PanelLocation.TOP: 0>
    """
    TOP = 0
    """Panel at the top of the screen. ~13% from the top"""
    MIDDLE = 1
    """Panel between the top and the center of the screen. ~33% from the top"""
    BOTTOM = 2
    """Panel close to the center of the screen. ~45% from the top"""
