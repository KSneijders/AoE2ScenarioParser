from src.helper.datatype import DataType
from src.helper.generator import create_generator
from src.helper.retriever import Retriever
from src.pieces.structs.struct import Struct


class PlayerDataOne(Struct):
    def __init__(self, parser, data=None):
        retrievers = [
            Retriever("Active", DataType("u32"), on_success=lambda x: x == 1),
            Retriever("Human", DataType("u32"), on_success=lambda x: x == 1),
            Retriever("Civilization", DataType("u32")),
            Retriever("CTY Mode", DataType("u32"), on_success=lambda x: x == 1)
        ]

        super().__init__(parser, "Player Data #1", retrievers, data)
