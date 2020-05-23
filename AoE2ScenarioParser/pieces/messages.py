from AoE2ScenarioParser.pieces import aoe2_piece
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.datatype import DataType


class MessagesPiece(aoe2_piece.AoE2Piece):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("Instructions", DataType("u32")),
            Retriever("Hints", DataType("u32")),
            Retriever("Victory", DataType("u32")),
            Retriever("Loss", DataType("u32")),
            Retriever("History", DataType("u32")),
            Retriever("Scouts", DataType("u32")),
            Retriever("ASCII Instructions", DataType("str16")),
            Retriever("ASCII Hints", DataType("str16")),
            Retriever("ASCII Victory", DataType("str16")),
            Retriever("ASCII Loss", DataType("str16")),
            Retriever("ASCII History", DataType("str16")),
            Retriever("ASCII Scouts", DataType("str16")),
        ]

        super().__init__("Messages", retrievers, parser_obj, data=data)
