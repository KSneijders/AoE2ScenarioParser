from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.structs.aoe2_struct import AoE2Struct


class ResourcesStruct(AoE2Struct):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("gold", DataType("u32")),
            Retriever("wood", DataType("u32")),
            Retriever("food", DataType("u32")),
            Retriever("stone", DataType("u32")),
            Retriever("ore_x_unused", DataType("u32")),
            Retriever("trade_goods", DataType("u32")),
            Retriever("player_color", DataType("u32"))
        ]

        super().__init__("Resources", retrievers, parser_obj, data)
