from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces import aoe2_piece
from AoE2ScenarioParser.pieces.structs.ai import AIStruct
from AoE2ScenarioParser.pieces.structs.resources import ResourcesStruct


class PlayerDataTwoPiece(aoe2_piece.AoE2Piece):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("Strings", DataType("str16", repeat=32)),
            Retriever("AI names", DataType("str16", repeat=16)),
            Retriever("AI files", DataType(AIStruct, repeat=16)),
            Retriever("AI type", DataType("u8", repeat=16)),
            Retriever("Separator", DataType("u32")),
            Retriever("Resources", DataType(ResourcesStruct, repeat=16))
        ]

        super().__init__("Player Data #2", retrievers, parser_obj, data=data)
