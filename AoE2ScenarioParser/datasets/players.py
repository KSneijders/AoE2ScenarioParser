from __future__ import annotations

from enum import IntEnum


class PlayerId(IntEnum):
    """

    This enum class provides the integer values used to reference each player in the game. Use these over specifying
    player number directly to improve code readability

    """

    GAIA = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8


class PlayerColorId(IntEnum):
    """

    This enum class provides the integer values used to reference the colours in-game. These are used in the 'Change Object
    Color', etc. effects

    """

    BLUE = 1
    RED = 2
    GREEN = 3
    YELLOW = 4
    AQUA = 5
    PURPLE = 6
    GREY = 7
    ORANGE = 8
