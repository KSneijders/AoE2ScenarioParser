from AoE2ScenarioParser.pieces import aoe2_piece
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.datatype import DataType


class CinematicsPiece(aoe2_piece.AoE2Piece):
    def __init__(self, parser_obj=None, data=None, pieces=None):
        retrievers = [
            Retriever("ascii_pregame", DataType("str16")),
            Retriever("ascii_victory", DataType("str16")),
            Retriever("ascii_loss", DataType("str16")),
            # Retriever("Separator (! in some version)", DataType("1")),
        ]

        super().__init__("Cinematics", retrievers, parser_obj, data=data, pieces=pieces)

    @staticmethod
    def defaults(pieces):
        defaults = {
            'ascii_pregame': '',
            'ascii_victory': '',
            'ascii_loss': '',
        }
        return defaults
