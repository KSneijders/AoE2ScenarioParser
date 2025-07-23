from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class VisibilityState(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the visibility state of a player for another player
    in the game. Used in the 'Set Visibility State' and 'Change Object Visibility' effects.

    **Examples**

    >>> VisibilityState.EXPLORED
    <VisibilityState.EXPLORED: 1>
    """
    VISIBLE = 0
    EXPLORED = 1
    INVISIBLE = 2
