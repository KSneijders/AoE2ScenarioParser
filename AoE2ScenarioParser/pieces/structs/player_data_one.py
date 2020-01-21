from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
import AoE2ScenarioParser.pieces.structs.aoe2_struct as structs


class PlayerDataOneStruct(structs.Struct):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("Active", DataType("u32")),
            Retriever("Human", DataType("u32")),
            Retriever("Civilization", DataType("u32")),
            Retriever("CTY mode", DataType("u32"))
        ]

        super().__init__("Player Data #1", retrievers, parser_obj, data)
