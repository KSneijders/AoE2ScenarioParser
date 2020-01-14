import src.pieces.aoe2_piece as scenario_piece
from src.helper.retriever import Retriever
from src.helper.datatype import DataType


class BackgroundImagePiece(scenario_piece.ScenarioPiece):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("ASCII, Background filename", DataType("str16")),
            Retriever("Picture Version", DataType("u32")),
            Retriever("Bitmap width", DataType("u32")),
            Retriever("Bitmap height", DataType("s32")),
            Retriever("Picture Orientation", DataType("s16")),
            # Retriever("	BITMAPINFOHEADER", DataType("u32")),
        ]

        super().__init__("Background Image", retrievers, parser_obj)
