from src.pieces.scenario_piece import *
from src.helper.retriever import Retriever
from src.helper.datatype import DataType


class FileHeaderPiece(ScenarioPiece):
    retrievers = [
        Retriever("Version (ASCII)", DataType("c4")),
        Retriever("Length of header", DataType("u32")),
        Retriever("Savable", DataType("s32")),
        Retriever("Timestamp of Last Save", DataType("u32")),
        Retriever("Scenario Instructions", DataType("str32")),
        Retriever("Individual Victories Used", DataType("u32")),
        Retriever("Player Count", DataType("u32")),
        Retriever("Unknown Data", DataType("52"))  # Todo: Explore 52 bytes of data (Steam name is in here)
    ]

    def __init__(self):
        super().__init__("File Header", self.retrievers)
