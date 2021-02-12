from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.aoe2_file_section import AoE2FileSection


class AIStruct(AoE2FileSection):
    def __init__(self):
        retrievers = [
            Retriever("unknown", DataType("u32")),
            Retriever("unknown_2", DataType("u32")),
            Retriever("ai_per_file_text", DataType("str32")),
        ]

        super().__init__("AI", retrievers)

    @staticmethod
    def defaults(pieces):
        defaults = {
            'unknown': 0,
            'unknown_2': 0,
            'ai_per_file_text': ''
        }
        return defaults
