from src.helper.datatype import DataType
from src.helper.retriever import Retriever
import src.pieces.structs.struct as structs


class AIStruct(structs.Struct):
    def __init__(self, parser, data=None):
        retrievers = [
            Retriever("Unknown, always 0", DataType("u32")),
            Retriever("Unknown, always 0 (2)", DataType("u32")),
            Retriever("AI .per file text", DataType("str32")),
        ]

        super().__init__(parser, "AI", retrievers, data)
