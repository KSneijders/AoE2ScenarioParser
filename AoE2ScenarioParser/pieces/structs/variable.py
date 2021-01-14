from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.aoe2_file_part import AoE2FilePart


class VariableStruct(AoE2FilePart):
    def __init__(self):
        retrievers = [
            Retriever("variable_id", DataType("u32")),
            Retriever("name", DataType("str32")),
        ]

        super().__init__("Variable", retrievers)

    @staticmethod
    def defaults(pieces):
        defaults = {
            'variable_id': 0,
            'name': '_Variable0',
        }
        return defaults
