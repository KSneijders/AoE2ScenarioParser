from src.helper.datatype import DataType
from src.helper.retriever import Retriever
from src.pieces.structs.struct import Struct


class PlayerDiplomacyStruct(Struct):
    def __init__(self, parser, data=None):
        retrievers = [
            Retriever("Stance with each player", DataType("u32", repeat=16)),
        ]

        super().__init__(parser, "Player Diplomacy", retrievers, data)
