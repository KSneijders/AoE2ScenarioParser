from src.pieces.scenario_piece import *
from src.helper.retriever import Retriever
from src.helper.datatype import DataType
from src.pieces.structs.player_diplomacy import PlayerDiplomacyStruct


class DiplomacyPiece(ScenarioPiece):

    def __init__(self, parser):
        retrievers = [
            Retriever("Per-player diplomacy", DataType("64", repeat=16), on_success=lambda x: PlayerDiplomacyStruct(parser, x)),
            Retriever("Individual Victories", DataType("60", repeat=16*12)),  # 12 Conditions per (16) Player(s).
            Retriever("Separator", DataType("u32")),
            Retriever("Per-player allied victory", DataType("u32", repeat=16)),  # Ignored -> PlayerDataThree
            Retriever("Unknown", DataType("4")),
        ]

        super().__init__(parser, "Diplomacy", retrievers)
