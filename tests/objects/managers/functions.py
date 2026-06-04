from __future__ import annotations

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.sections import Trigger, Unit


def create_unit(player: Player | int):
    return Unit(
        player = player,
        object_id = 4,
        location = (.5, .5)
    )


def create_trigger(name: str = "Trigger"):
    return Trigger(name=name)
