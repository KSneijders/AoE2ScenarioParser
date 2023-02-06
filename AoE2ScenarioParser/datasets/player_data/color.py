from __future__ import annotations

from enum import IntEnum

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from AoE2ScenarioParser.datasets.player_data import Player


class Color(IntEnum):
    """This enum represents the actual colors in the dropdown menu for players."""
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
    def from_player_id(player_id: 'Player' | int):
        if not 0 <= player_id < 8:
            raise ValueError(f"Invalid player ID. Should be between 0 and 8 (excl), but got: {player_id}")
        if player_id == 0:
            return Color.GRAY
        return Color(player_id - 1)
