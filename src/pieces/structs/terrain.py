from src.helper.datatype import DataType
from src.helper.retriever import Retriever
from src.pieces.structs.struct import Struct


class TerrainStruct(Struct):
    def __init__(self, parser, data=None):
        retrievers = [
            Retriever("Terrain ID", DataType("u8")),
            Retriever("Elevation", DataType("u8")),
            Retriever("Unused", DataType("u8")),
            Retriever("Separator?", DataType("4"))
        ]

        super().__init__(parser, "Terrain", retrievers, data)
