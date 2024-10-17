from __future__ import annotations

import math

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.helper.helper import raise_if_not_int_subclass
from AoE2ScenarioParser.helper.pretty_format import pretty_format_name
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.support.tile import Tile
from AoE2ScenarioParser.scenarios.scenario_store import actions
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.sections.retrievers.retriever_object_link_group import RetrieverObjectLinkGroup
from AoE2ScenarioParser.sections.retrievers.support import Support


class Unit(AoE2Object):
    """
    A class representing a single unit on the map.
    This can be an archer, a gold mine, a house or even a tree.
    """
    _link_list = [
        RetrieverObjectLink("player", retrieve_history_number=0),
        RetrieverObjectLinkGroup("Units", "players_units[__index__].units[__index__]", group=[
            RetrieverObjectLink("x"),
            RetrieverObjectLink("y"),
            RetrieverObjectLink("z"),
            RetrieverObjectLink("id"),
            RetrieverObjectLink("type"),
            RetrieverObjectLink("status"),
            RetrieverObjectLink("rotation"),
            RetrieverObjectLink("initial_animation_frame"),
            RetrieverObjectLink("garrisoned_in_id"),
            RetrieverObjectLink("caption_string_id", support=Support(since=1.54)),
        ])
    ]

    def __init__(
            self,
            player: int | Player,
            x: float,
            y: float,
            z: float,
            id: int,
            type: int,
            status: int,
            rotation: float,
            initial_animation_frame: int,
            garrisoned_in_id: int,
            caption_string_id: int,
            **kwargs
    ):
        raise_if_not_int_subclass({'type': type})

        super().__init__(**kwargs)

        self._player: Player = Player(player)
        self.x: float = x
        self.y: float = y
        self.z: float = z
        self.id: int = id
        self.type: int = type
        self.status: int = status
        self.rotation: float = rotation
        self.initial_animation_frame: int = initial_animation_frame
        self.garrisoned_in_id: int = garrisoned_in_id
        self.caption_string_id: int = caption_string_id

    @property
    def player(self) -> Player:
        """The player that owns this unit"""
        return self._player

    @player.setter
    def player(self, player: int | Player):
        actions.unit_change_ownership(self._uuid, player, self)
        self._player = player

    @property
    def tile(self) -> Tile:
        """The tile where the unit is located"""
        return Tile(math.floor(self.x), math.floor(self.y))
        # Floor x and y as location (0.9, 0.9) is still Tile[x=0, y=0]

    @tile.setter
    def tile(self, tile: Tile) -> None:
        self.x = tile.x
        self.y = tile.y

    @property
    def name(self) -> str:
        """The name of the unit, nicely formatted"""
        unit_enum = helper.get_enum_from_unit_type(self.type)
        if unit_enum:
            return pretty_format_name(unit_enum.name)
        else:
            return f"Unknown{self.type}"  # e.g."Unknown411"
