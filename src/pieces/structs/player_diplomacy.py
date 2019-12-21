from src.helper.datatype import DataType
from src.helper.retriever import Retriever
import src.pieces.structs.struct as structs


class PlayerDiplomacyStruct(structs.Struct):
    def __init__(self, parser_obj, data=None):
        retrievers = [
            Retriever("Stance with each player", DataType("u32", repeat=16)),
        ]

        super().__init__(parser_obj, "Player Diplomacy", retrievers, data)
