import src.pieces.scenario_piece as scenario_piece
from src.helper.retriever import Retriever
from src.helper.datatype import DataType
from src.pieces.structs.player_data_four import PlayerDataFourStruct


class UnitsPiece(scenario_piece.ScenarioPiece):
    def __init__(self, parser):
        retrievers = [
            Retriever("Number of unit sections", DataType("u32")),
            Retriever("Player Data 4", DataType(PlayerDataFourStruct, repeat=8)),
        ]

        super().__init__(parser, "Units", retrievers)
