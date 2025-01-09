from __future__ import annotations

from enum import IntEnum
from typing import List


class PlayerId(IntEnum):
    """
    This enum class provides the integer values used to reference each player in the game. Use these over specifying
    player number directly to improve code readability
    """

    @staticmethod
    def all(exclude_gaia: bool = False) -> List[PlayerId]:
        """
        Return a list of all players

        Args:
            exclude_gaia: if the GAIA player should be excluded from the list or not

        Returns:
            The list of playerIds
        """
        return ([] if exclude_gaia else [PlayerId.GAIA]) + [
            PlayerId.ONE, PlayerId.TWO, PlayerId.THREE, PlayerId.FOUR,
            PlayerId.FIVE, PlayerId.SIX, PlayerId.SEVEN, PlayerId.EIGHT
        ]

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
    This enum class provides the integer values used to reference the colors in-game.
    These are used in the 'Change Object Color', etc. effects
    """
    BLUE = 1
    RED = 2
    GREEN = 3
    YELLOW = 4
    AQUA = 5
    PURPLE = 6
    GRAY = 7
    ORANGE = 8


class ColorId(IntEnum):
    """
    This enum represents the actual colors in the dropdown menu for players.
    Do not confuse with the PlayerColorId which is used to reference a player number by it's color.
    """
    BLUE = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    AQUA = 4
    PURPLE = 5
    GRAY = 6
    ORANGE = 7
    INVALID_8 = 8
    INVALID_9 = 9
    INVALID_10 = 10
    INVALID_11 = 11
    INVALID_12 = 12
    INVALID_13 = 13
    INVALID_14 = 14
    INVALID_15 = 15

    @staticmethod
    def from_player_id(player_id: PlayerId | int):
        if not 0 <= player_id <= 8:
            raise ValueError(f"Invalid player ID. Should be between 0 and 8 (both incl), but got: {player_id}")
        if player_id == 0:
            return ColorId.GRAY
        return ColorId(player_id - 1)
