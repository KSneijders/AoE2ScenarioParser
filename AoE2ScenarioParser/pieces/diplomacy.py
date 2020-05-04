from AoE2ScenarioParser.pieces import aoe2_piece
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.pieces.structs.player_diplomacy import PlayerDiplomacyStruct


class DiplomacyPiece(aoe2_piece.AoE2Piece):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("Per-player diplomacy", DataType(PlayerDiplomacyStruct, repeat=16)),
            Retriever("Individual Victories", DataType("60", repeat=16*12)),  # 12 Conditions per (16) Player(s).
            Retriever("Separator", DataType("u32")),
            Retriever("Per-player allied victory", DataType("u32", repeat=16)),  # Ignored -> PlayerDataThree
            Retriever("Unknown", DataType("4")),
        ]

        super().__init__("Diplomacy", retrievers, parser_obj, data=data)
