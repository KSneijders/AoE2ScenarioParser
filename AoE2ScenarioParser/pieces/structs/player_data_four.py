from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.structs.aoe2_struct import AoE2Struct


class PlayerDataFourStruct(AoE2Struct):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("food_duplicate", DataType("f32")),
            Retriever("wood_duplicate", DataType("f32")),
            Retriever("gold_duplicate", DataType("f32")),
            Retriever("stone_duplicate", DataType("f32")),
            Retriever("ore_x_duplicate", DataType("f32")),
            Retriever("trade_goods_duplicate", DataType("f32")),
            Retriever("population_limit", DataType("f32")),
        ]

        super().__init__("Player Data #4", retrievers, parser_obj, data)
