import src.pieces.aoe2_piece as scenario_piece
from src.helper.retriever import Retriever
from src.helper.datatype import DataType


class FileHeaderPiece(scenario_piece.ScenarioPiece):

    def __init__(self, parser_obj):
        retrievers = [
            Retriever("Version", DataType("c4")),
            Retriever("Header length", DataType("u32")),
            Retriever("Savable", DataType("s32")),
            Retriever("Timestamp of Last Save", DataType("u32")),
            Retriever("Scenario Instructions", DataType("str32")),
            Retriever("Individual Victories Used", DataType("u32")),
            Retriever("Player Count", DataType("u32")),
            Retriever("Unknown Data", DataType("36"), log_value=True),
            Retriever("Steam name", DataType("str32"), log_value=True),
            Retriever("Unknown Data", DataType("4"), log_value=True),
        ]

        super().__init__(parser_obj, "File Header", retrievers)
