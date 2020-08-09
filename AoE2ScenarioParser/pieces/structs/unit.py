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

        self._player: Player  # Unset by default, will be set by the UnitsObject

        super().__init__("Unit", retrievers, parser_obj, data)
