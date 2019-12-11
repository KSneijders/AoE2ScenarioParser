from src.pieces.scenario_piece import ScenarioPiece
from src.helper.datatype import DataType
from src.helper.retriever import Retriever


class GlobalVictoryPiece(ScenarioPiece):
    def __init__(self, parser):
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

        super().__init__(parser, "Global Victory", retrievers)
