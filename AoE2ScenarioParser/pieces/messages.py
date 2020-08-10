from AoE2ScenarioParser.pieces import aoe2_piece
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.datatype import DataType


class MessagesPiece(aoe2_piece.AoE2Piece):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("instructions", DataType("u32")),
            Retriever("hints", DataType("u32")),
            Retriever("victory", DataType("u32")),
            Retriever("loss", DataType("u32")),
            Retriever("history", DataType("u32")),
            Retriever("scouts", DataType("u32")),
            Retriever("ascii_instructions", DataType("str16")),
            Retriever("ascii_hints", DataType("str16")),
            Retriever("ascii_victory", DataType("str16")),
            Retriever("ascii_loss", DataType("str16")),
            Retriever("ascii_history", DataType("str16")),
            Retriever("ascii_scouts", DataType("str16")),
        ]

        super().__init__("Messages", retrievers, parser_obj, data=data)
