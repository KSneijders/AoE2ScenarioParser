import AoE2ScenarioParser.pieces.aoe2_piece as scenario_piece
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.datatype import DataType


class CinematicsPiece(scenario_piece.ScenarioPiece):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("ASCII, Pregame cinematic filename", DataType("str16")),
            Retriever("ASCII, Victory cinematic filename", DataType("str16")),
            Retriever("ASCII, Loss cinematic filename", DataType("str16")),
            # Retriever("Separator (! in some version)", DataType("1")),
        ]

        super().__init__("Cinematics", retrievers, parser_obj)
