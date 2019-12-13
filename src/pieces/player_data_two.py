from src.helper.datatype import DataType
from src.helper.retriever import Retriever
from src.pieces.scenario_piece import ScenarioPiece
from src.pieces.structs.ai import AIStruct
from src.pieces.structs.resources import ResourcesStruct


class PlayerDataTwoPiece(ScenarioPiece):
    def __init__(self, parser, data=None):
        retrievers = [
            Retriever("Unknown strings", DataType("str16", repeat=32)),
            Retriever("AI names", DataType("str16", repeat=16)),
            Retriever("AI files", DataType(AIStruct, repeat=16)),
            Retriever("AI type", DataType("u8", repeat=16)),
            Retriever("Separator", DataType("u32")),
            Retriever("Resources", DataType(ResourcesStruct, repeat=16))
        ]

        super().__init__(parser, "Player Data #2", retrievers, data)
