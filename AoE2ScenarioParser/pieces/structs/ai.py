from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.structs.aoe2_struct import AoE2Struct


class AIStruct(AoE2Struct):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("Unknown, always 0", DataType("u32")),
            Retriever("Unknown, always 0 (2)", DataType("u32")),
            Retriever("AI .per file text", DataType("str32")),
        ]

        super().__init__("AI", retrievers, parser_obj, data)

    @staticmethod
    def defaults():
        defaults = {
            'Unknown, always 0': 0,
            'Unknown, always 0(2)': 0,
            'AI.per file text': ''
        }
        return defaults
