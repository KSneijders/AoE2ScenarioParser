from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.structs.aoe2_struct import AoE2Struct


class AIStruct(AoE2Struct):
    def __init__(self, data=None, pieces=None):
        retrievers = [
            Retriever("unknown", DataType("u32")),
            Retriever("unknown_2", DataType("u32")),
            Retriever("ai_per_file_text", DataType("str32")),
        ]

        super().__init__("AI", retrievers, data, pieces=pieces)

    @staticmethod
    def defaults(pieces):
        defaults = {
            'unknown': 0,
            'unknown_2': 0,
            'ai_per_file_text': ''
        }
        return defaults
