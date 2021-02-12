from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.aoe2_file_section import AoE2FileSection
from AoE2ScenarioParser.pieces.structs.player_diplomacy import PlayerDiplomacyStruct


class DiplomacyPiece(AoE2FileSection):
    def __init__(self):
        retrievers = [
            Retriever("per_player_diplomacy", DataType(PlayerDiplomacyStruct, repeat=16)),
            Retriever("individual_victories", DataType("60", repeat=16 * 12)),  # 12 Conditions per (16) Player(s).
            Retriever("separator", DataType("u32")),
            Retriever("per_player_allied_victory", DataType("u32", repeat=16)),  # Ignored -> PlayerDataThree
            Retriever("unknown", DataType("4")),
        ]

        super().__init__("DiplomacyPiece", retrievers)

    @staticmethod
    def defaults(pieces):
        defaults = {
            # 'per_player_diplomacy': [
            #     PlayerDiplomacyStruct(data=list(PlayerDiplomacyStruct.defaults(pieces).values()), pieces=pieces) for _
            #     in range(16)
            # ],
            'individual_victories': [b'\x00' * 60] * 192,
            'separator': 4294967197,
            'per_player_allied_victory': [0] * 16,
            'unknown': b'\x00\x01\x00\x04',
        }
        return defaults
