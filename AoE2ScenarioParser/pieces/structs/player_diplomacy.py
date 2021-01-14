from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.aoe2_file_part import AoE2FilePart


class PlayerDiplomacyStruct(AoE2FilePart):
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
