from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.structs.aoe2_struct import AoE2Struct


class AI2Struct(AoE2Struct):
    def __init__(self, data=None, pieces=None):
        retrievers = [
            Retriever("ai_file_name", DataType("str32")),
            Retriever("ai_file", DataType("str32")),
        ]

        super().__init__("AI2", retrievers, parser_obj, data, pieces=pieces)

    @staticmethod
    def defaults(pieces):
        defaults = {
            'ai_file_name': '',
            'ai_file': '',
        }
        return defaults
