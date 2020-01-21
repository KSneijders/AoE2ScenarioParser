from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
import AoE2ScenarioParser.pieces.structs.aoe2_struct as structs


class ResourcesStruct(structs.Struct):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("Gold", DataType("u32")),
            Retriever("Wood", DataType("u32")),
            Retriever("Food", DataType("u32")),
            Retriever("Stone", DataType("u32")),
            Retriever("Ore X (unused)", DataType("u32")),
            Retriever("Trade Goods", DataType("u32")),
            Retriever("Player color", DataType("u32"))
        ]

        super().__init__("Resources", retrievers, parser_obj, data)
