import src.pieces.aoe2_piece as scenario_piece
from src.helper.retriever import Retriever
from src.helper.datatype import DataType


class FileHeaderPiece(scenario_piece.ScenarioPiece):

    def __init__(self, parser_obj):
        retrievers = [
            Retriever("Version", DataType("c4")),
            Retriever("Header length", DataType("u32")),
            Retriever("Savable", DataType("s32")),
            Retriever("Timestamp of last save", DataType("u32")),
            Retriever("Scenario instructions", DataType("str32")),
            Retriever("Individual victories used", DataType("u32")),
            Retriever("Player count", DataType("u32")),
            Retriever("Data", DataType("36"), log_value=True),
            Retriever("Creator steam name", DataType("str32"), log_value=True),
            Retriever("Data", DataType("4"), log_value=True),
        ]

        super().__init__(parser_obj, "File Header", retrievers)
