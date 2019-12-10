from src.pieces.scenario_piece import *
from src.helper.retriever import Retriever
from src.helper.datatype import DataType


class MessagesPiece(ScenarioPiece):

    def __init__(self, parser):
        retrievers = [
            Retriever("Instructions, String table", DataType("u32")),
            Retriever("Hints, String table", DataType("u32")),
            Retriever("Victory, String table", DataType("u32")),
            Retriever("Loss, String table", DataType("u32")),
            Retriever("History, String table", DataType("u32")),
            Retriever("Scouts, String table", DataType("u32")),
            Retriever("ASCII Instructions", DataType("str16")),
            Retriever("ASCII Hints", DataType("str16")),
            Retriever("ASCII Victory", DataType("str16")),
            Retriever("ASCII Loss", DataType("str16")),
            Retriever("ASCII History", DataType("str16")),
            Retriever("ASCII Scouts", DataType("str16")),
        ]

        super().__init__(parser, "Messages", retrievers)
