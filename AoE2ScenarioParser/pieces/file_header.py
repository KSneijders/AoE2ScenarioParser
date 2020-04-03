from AoE2ScenarioParser.pieces import aoe2_piece
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.datatype import DataType


class FileHeaderPiece(aoe2_piece.AoE2Piece):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("Version", DataType("c4"), save_as="scenario_version"),
            Retriever("Header length", DataType("u32")),
            Retriever("Savable", DataType("s32")),
            Retriever("Timestamp of last save", DataType("u32")),
            Retriever("Scenario instructions", DataType("str32")),
            Retriever("Individual victories used", DataType("u32")),
            Retriever("Player count", DataType("u32")),
            Retriever("Data", DataType("36")),
            Retriever("Creator name", DataType("str32")),
            Retriever("Data (2)", DataType("4")),
        ]

        super().__init__("File Header", retrievers, parser_obj)
