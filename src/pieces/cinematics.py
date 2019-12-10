from src.pieces.scenario_piece import *
from src.helper.retriever import Retriever
from src.helper.datatype import DataType


class CinematicsPiece(ScenarioPiece):

    def __init__(self, parser):
        retrievers = [
            Retriever("ASCII, Pregame cinematic filename", DataType("str16")),
            Retriever("ASCII, Victory cinematic filename", DataType("str16")),
            Retriever("ASCII, Loss cinematic filename", DataType("str16")),
            # Retriever("Separator (! in some version)", DataType("1")),
        ]

        super().__init__(parser, "Cinematics", retrievers)
