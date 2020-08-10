from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.structs.aoe2_struct import AoE2Struct
from AoE2ScenarioParser.pieces.structs.unit import UnitStruct


class PlayerUnitsStruct(AoE2Struct):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("unit_count", DataType("u32"), save_as="unit_count"),
            Retriever("units", DataType(UnitStruct), set_repeat="{unit_count}")
        ]

        super().__init__("Player Units", retrievers, parser_obj, data)
