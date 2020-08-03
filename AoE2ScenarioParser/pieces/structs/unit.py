import math

from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.helper import Tile
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.structs.aoe2_struct import AoE2Struct
from AoE2ScenarioParser.datasets import units, buildings
from AoE2ScenarioParser.datasets.players import Player

class UnitStruct(AoE2Struct):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("x", DataType("f32")),
            Retriever("y", DataType("f32")),
            Retriever("z", DataType("f32")),
            Retriever("reference_id", DataType("s32")),
            Retriever("unit_const", DataType("u16")),
            Retriever("status", DataType("u8")),
            # Status, Always 2. 0-6 no difference (?) | 7-255 makes it disappear. (Except from the mini-map)
            Retriever("rotation_radians", DataType("f32")),
            Retriever("initial_animation_frame", DataType("u16")),
            Retriever("garrisoned_in_id", DataType("s32")),
        ]

        self._player = -1 # Unset by default, will be set by the UnitsObject

        super().__init__("Unit", retrievers, parser_obj, data)

    @property
    def player(self) -> Player:
        """
        PLEASE NOTE: This is an internal (read-only) value for ease of access. It DOES accurately represent the actual
        player controlling the unit BUT IT IS NOT directly connected to it. Changing this value will have no impact to
        your scenario.
        To change which player controls this unit, use:
            unit_manager.change_ownership(UnitObject, to_player)
        """
        return self._player

    @property
    def rotation(self) -> float:
        return self.rotation_radians

    @rotation.setter
    def rotation(self, rotation: float) -> None:
        """Rotation in radians"""
        if not 0.0 <= rotation <= math.tau:
            raise ValueError(f'The Rotation value must be between 0 and tau (excl).')
        self.rotation_radians = rotation

    @property
    def tile(self) -> Tile:
        return Tile(math.floor(self.x), math.floor(self.y))
        # Floor x and y as location (0.9, 0.9) is still Tile[x=0, y=0]

    @tile.setter
    def tile(self, tile: Tile) -> None:
        self.x = tile.x
        self.y = tile.y

    @property
    def name(self) -> str:
        try:
            return helper.pretty_print_name(units.unit_names[self.unit_const])
        except KeyError:  # Object wasn't a unit, maybe a building?
            return helper.pretty_print_name(buildings.building_names[self.unit_const])
