from AoE2ScenarioParser.pieces import aoe2_piece
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.datatype import DataType


class CinematicsPiece(aoe2_piece.AoE2Piece):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("ASCII, Pregame cinematic filename", DataType("str16")),
            Retriever("ASCII, Victory cinematic filename", DataType("str16")),
            Retriever("ASCII, Loss cinematic filename", DataType("str16")),
            # Retriever("Separator (! in some version)", DataType("1")),
        ]

        super().__init__("Cinematics", retrievers, parser_obj, data=data)
