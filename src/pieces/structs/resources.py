from src.helper.datatype import DataType
from src.helper.retriever import Retriever
import src.pieces.structs.aoe2_struct as structs


class ResourcesStruct(structs.Struct):
    def __init__(self, parser_obj, data=None):
        retrievers = [
            Retriever("Gold", DataType("u32")),
            Retriever("Wood", DataType("u32")),
            Retriever("Food", DataType("u32")),
            Retriever("Stone", DataType("u32")),
            Retriever("Ore X (unused)", DataType("u32")),
            Retriever("Trade Goods", DataType("u32")),
            Retriever("Player number 0-7, 2nd 6 = gaia", DataType("u32"))
        ]

        super().__init__(parser_obj, "Resources", retrievers, data)
