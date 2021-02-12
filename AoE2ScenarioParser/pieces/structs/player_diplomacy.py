from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.aoe2_file_section import AoE2FileSection


class PlayerDiplomacyStruct(AoE2FileSection):
    def __init__(self):
        retrievers = [
            Retriever("stance_with_each_player", DataType("u32", repeat=16)),
        ]

        super().__init__("Player Diplomacy", retrievers)

    @staticmethod
    def defaults(pieces):
        defaults = {
            'stance_with_each_player': [3] * 16
        }
        return defaults
