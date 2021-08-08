from __future__ import annotations

from enum import IntEnum
from typing import List


class PlayerId(IntEnum):
    @staticmethod
    def all(exclude_gaia: bool = False) -> List[PlayerId]:
        """
        Return a list of all players

        Args:
            exclude_gaia (bool): if the GAIA player should be excluded from the list or not

        Returns:
            The list of playerIds
        """
        return ([] if exclude_gaia else [PlayerId.GAIA]) + [
            PlayerId.ONE, PlayerId.TWO, PlayerId.THREE, PlayerId.FOUR,
            PlayerId.FIVE, PlayerId.SIX, PlayerId.SEVEN, PlayerId.EIGHT
        ]

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
