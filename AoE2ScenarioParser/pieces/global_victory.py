from AoE2ScenarioParser.pieces import aoe2_piece
from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever


class GlobalVictoryPiece(aoe2_piece.AoE2Piece):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("Separator", DataType("u32")),
            Retriever("Conquest required", DataType("u32")),
            Retriever("Ruins", DataType("u32")),
            Retriever("Artifacts", DataType("u32")),
            Retriever("Discovery", DataType("u32")),
            Retriever("Explored % of map required", DataType("u32")),
            Retriever("Gold", DataType("u32")),
            Retriever("All custom conditions required?", DataType("u32")),
            Retriever("Mode", DataType("u32")),
            Retriever("Required score for score victory", DataType("u32")),
            Retriever("Time for timed game, in 10ths of a year", DataType("u32")),
        ]

        super().__init__("Global Victory", retrievers, parser_obj, data=data)
