from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.structs.aoe2_struct import AoE2Struct


class VariableStruct(AoE2Struct):
    def __init__(self, data=None, pieces=None):
        retrievers = [
            Retriever("variable_id", DataType("u32")),
            Retriever("name", DataType("str32")),
        ]

        super().__init__("Variable", retrievers, data, pieces=pieces)

    @staticmethod
    def defaults(pieces):
        defaults = {
            'variable_id': 0,
            'name': '_Variable0',
        }
        return defaults
