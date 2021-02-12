from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.aoe2_file_section import AoE2FileSection


class ResourcesStruct(AoE2FileSection):
    def __init__(self):
        retrievers = [
            Retriever("gold", DataType("u32")),
            Retriever("wood", DataType("u32")),
            Retriever("food", DataType("u32")),
            Retriever("stone", DataType("u32")),
            Retriever("ore_x_unused", DataType("u32")),
            Retriever("trade_goods", DataType("u32")),
            Retriever("player_color", DataType("u32"))
        ]

        super().__init__("Resources", retrievers)

    @staticmethod
    def defaults(pieces):
        defaults = {
            'gold': 0,
            'wood': 0,
            'food': 0,
            'stone': 0,
            'ore_x_unused': 0,
            'trade_goods': 0,
            'player_color': 0,
        }
        return defaults
