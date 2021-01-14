from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.aoe2_file_part import AoE2FilePart


class PlayerDataFourStruct(AoE2FilePart):
    def __init__(self):
        retrievers = [
            Retriever("food_duplicate", DataType("f32")),
            Retriever("wood_duplicate", DataType("f32")),
            Retriever("gold_duplicate", DataType("f32")),
            Retriever("stone_duplicate", DataType("f32")),
            Retriever("ore_x_duplicate", DataType("f32")),
            Retriever("trade_goods_duplicate", DataType("f32")),
            Retriever("population_limit", DataType("f32")),
        ]

        super().__init__("Player Data #4", retrievers)

    @staticmethod
    def defaults(pieces):
        defaults = {
            'food_duplicate': 0.0,
            'wood_duplicate': 0.0,
            'gold_duplicate': 0.0,
            'stone_duplicate': 0.0,
            'ore_x_duplicate': 0.0,
            'trade_goods_duplicate': 0.0,
            'population_limit': 200.0,
        }
        return defaults
