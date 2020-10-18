from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.structs.aoe2_struct import AoE2Struct


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
            Retriever("rotation", DataType("f32")),
            Retriever("initial_animation_frame", DataType("u16")),
            Retriever("garrisoned_in_id", DataType("s32")),
        ]

        super().__init__("Unit", retrievers, parser_obj, data)

    @staticmethod
    def defaults():
        defaults = {
            'x': 0.5,
            'y': 0.5,
            'z': 0,
            'reference_id': 0,
            'unit_const': 4,  # Archer
            'status': 2,
            'rotation': 0,
            'initial_animation_frame': 0,
            'garrisoned_in_id': -1,
        }
        return defaults
