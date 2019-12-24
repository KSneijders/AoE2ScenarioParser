from src.helper.datatype import DataType
from src.helper.retriever import Retriever
import src.pieces.structs.aoe2_struct as structs


class TerrainStruct(structs.Struct):
    def __init__(self, parser_obj, data=None):
        retrievers = [
            Retriever("Terrain ID", DataType("u8")),
            Retriever("Elevation", DataType("u8")),
            Retriever("Unused", DataType("u8")),
            Retriever("Separator?", DataType("4"))
        ]

        super().__init__(parser_obj, "Terrain", retrievers, data)
