from AoE2ScenarioParser.pieces import aoe2_piece
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.datatype import DataType


class BackgroundImagePiece(aoe2_piece.AoE2Piece):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("ascii_filename", DataType("str16")),
            Retriever("picture_version", DataType("u32")),
            Retriever("bitmap_width", DataType("u32")),
            Retriever("bitmap_height", DataType("s32")),
            Retriever("picture_orientation", DataType("s16")),
            # Retriever("BITMAPINFOHEADER", DataType("u32")),
        ]

        super().__init__("Background Image", retrievers, parser_obj, data=data)

    @staticmethod
    def defaults():
        defaults = {
            'ascii_filename': '',
            'picture_version': 3,
            'bitmap_width': 0,
            'bitmap_height': 0,
            'picture_orientation': 1,
        }
        return defaults
