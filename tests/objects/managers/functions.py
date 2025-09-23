from __future__ import annotations

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.sections import Unit


def create_unit(player: Player | int):
    return Unit(
        player = player,
        type = 4,
        location = (.5, .5)
    )
