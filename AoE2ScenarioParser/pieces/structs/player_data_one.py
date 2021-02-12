from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.aoe2_file_section import AoE2FileSection


class PlayerDataOneStruct(AoE2FileSection):
    def __init__(self):
        retrievers = [
            Retriever("active", DataType("u32")),
            Retriever("human", DataType("u32")),
            Retriever("civilization", DataType("u32")),
            Retriever("architecture_set", DataType("u32")),
            Retriever("cty_mode", DataType("u32")),
        ]

        super().__init__("Player Data #1", retrievers)

    @staticmethod
    def defaults(pieces):
        # This default is adjusted in DataHeaderPiece:
        # - P1 (Active: 1, Human: 1)
        # - P2 (Active: 1)
        defaults = {
            'active': 0,
            'human': 0,
            'civilization': 36,
            'architecture_set': 36,
            'cty_mode': 4,
        }
        return defaults
