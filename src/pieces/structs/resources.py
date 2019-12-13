from src.helper.datatype import DataType
from src.helper.retriever import Retriever
import src.pieces.structs.struct as structs


class ResourcesStruct(structs.Struct):
    def __init__(self, parser, data=None):
        retrievers = [
            Retriever("Gold", DataType("u32")),
            Retriever("Wood", DataType("u32")),
            Retriever("Food", DataType("u32")),
            Retriever("Stone", DataType("u32")),
            Retriever("Ore X (unused)", DataType("u32")),
            Retriever("Trade Goods", DataType("u32")),
            Retriever("Unknown", DataType("4"))
        ]

        super().__init__(parser, "Resources", retrievers, data)