from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.structs.aoe2_struct import AoE2Struct


class UnitStruct(AoE2Struct):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("X position", DataType("f32")),
            Retriever("Y position", DataType("f32")),
            Retriever("Z position", DataType("f32")),
            Retriever("ID", DataType("u32")),
            Retriever("Unit 'constant'", DataType("u16")),
            Retriever("Status", DataType("u8")),
            # Status, Always 2. 0-6 no difference (?) | 7-255 makes it disappear. (Except from the mini-map)
            Retriever("Rotation, in radians", DataType("f32")),
            Retriever("Initial animation frame", DataType("u16")),
            Retriever("Garrisoned in: ID", DataType("s32")),
        ]

        super().__init__("Unit", retrievers, parser_obj, data)
