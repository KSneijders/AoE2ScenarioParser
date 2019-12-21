import src.pieces.scenario_piece as scenario_piece
from src.helper.retriever import Retriever
from src.helper.datatype import DataType


class CinematicsPiece(scenario_piece.ScenarioPiece):

    def __init__(self, parser_obj):
        retrievers = [
            Retriever("ASCII, Pregame cinematic filename", DataType("str16")),
            Retriever("ASCII, Victory cinematic filename", DataType("str16")),
            Retriever("ASCII, Loss cinematic filename", DataType("str16")),
            # Retriever("Separator (! in some version)", DataType("1")),
        ]

        super().__init__(parser_obj, "Cinematics", retrievers)
