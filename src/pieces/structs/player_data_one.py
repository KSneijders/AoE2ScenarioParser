from src.helper.datatype import DataType
from src.helper.retriever import Retriever
import src.pieces.structs.aoe2_struct as structs


class PlayerDataOneStruct(structs.Struct):
    def __init__(self, parser_obj, data=None):
        retrievers = [
            Retriever("Active", DataType("u32")),
            Retriever("Human", DataType("u32")),
            Retriever("Civilization", DataType("u32")),
            Retriever("CTY Mode", DataType("u32"))
        ]

        super().__init__(parser_obj, "Player Data #1", retrievers, data)
