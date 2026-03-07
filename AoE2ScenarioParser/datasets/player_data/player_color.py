from __future__ import annotations

from enum import IntEnum

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from AoE2ScenarioParser.datasets.player_data import Player


class PlayerColor(IntEnum):
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

    @staticmethod
    def from_player_id(player_id: 'Player | int'):
        if not 0 <= player_id < 8:
            raise ValueError(f"Invalid player ID. Should be between 0 and 8 (excl), but got: {player_id}")
        if player_id == 0:
            return PlayerColor.GRAY
        return PlayerColor(player_id)
