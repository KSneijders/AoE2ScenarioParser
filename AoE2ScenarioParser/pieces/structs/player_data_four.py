from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.structs.aoe2_struct import AoE2Struct


class PlayerDataFourStruct(AoE2Struct):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("Food, duplicate", DataType("f32")),
            Retriever("Wood, duplicate", DataType("f32")),
            Retriever("Gold, duplicate", DataType("f32")),
            Retriever("Stone, duplicate", DataType("f32")),
            Retriever("'Ore X', duplicate", DataType("f32")),
            Retriever("Trade Goods, duplicate", DataType("f32")),
            Retriever("Population limit", DataType("f32")),
        ]

        super().__init__("Player Data #4", retrievers, parser_obj, data)
