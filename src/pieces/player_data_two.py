from src.helper.datatype import DataType
from src.helper.retriever import Retriever
import src.pieces.aoe2_piece as scenario_piece
from src.pieces.structs.ai import AIStruct
from src.pieces.structs.resources import ResourcesStruct


class PlayerDataTwoPiece(scenario_piece.ScenarioPiece):
    def __init__(self, parser_obj, data=None):
        retrievers = [
            Retriever("Strings", DataType("str16", repeat=32)),
            Retriever("AI names", DataType("str16", repeat=16)),
            Retriever("AI files", DataType(AIStruct, repeat=16)),
            Retriever("AI type", DataType("u8", repeat=16)),
            Retriever("Separator", DataType("u32")),
            Retriever("Resources", DataType(ResourcesStruct, repeat=16))
        ]

        super().__init__(parser_obj, "Player Data #2", retrievers, data)
