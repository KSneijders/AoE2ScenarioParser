from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.structs.aoe2_struct import AoE2Struct


class PlayerDiplomacyStruct(AoE2Struct):
    def __init__(self, parser_obj=None, data=None, pieces=None):
        retrievers = [
            Retriever("stance_with_each_player", DataType("u32", repeat=16)),
        ]

        super().__init__("Player Diplomacy", retrievers, parser_obj, data, pieces=pieces)

    @staticmethod
    def defaults(pieces):
        defaults = {
            'stance_with_each_player': [3] * 16
        }
        return defaults
