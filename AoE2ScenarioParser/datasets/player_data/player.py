from __future__ import annotations

from enum import IntEnum
from typing import Iterable, List


class Player(IntEnum):
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

    @staticmethod
    def all(exclude_gaia: bool = False) -> List[Player]:
        """
        Return a list of all players

        Args:
            exclude_gaia: if the GAIA player should be excluded from the list or not

        Returns:
            The list of playerIds
        """
        return ([] if exclude_gaia else [Player.GAIA]) + [
            Player.ONE, Player.TWO, Player.THREE, Player.FOUR,
            Player.FIVE, Player.SIX, Player.SEVEN, Player.EIGHT
        ]

    @staticmethod
    def all_except(players: Iterable[Player]) -> List[Player]:
        """
        Return a list of all players without the given players

        Args:
            players: The list of players to exclude

        Returns:
            The list of playerIds without the given players
        """
        return [player for player in Player.all() if player not in players]
