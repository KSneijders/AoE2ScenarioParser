from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.aoe2_file_part import AoE2FilePart


class AI2Struct(AoE2FilePart):
    def __init__(self):
        retrievers = [
            Retriever("ai_file_name", DataType("str32")),
            Retriever("ai_file", DataType("str32")),
        ]

        super().__init__("AI2", retrievers)

    @staticmethod
    def defaults(pieces):
        defaults = {
            'ai_file_name': '',
            'ai_file': '',
        }
        return defaults
