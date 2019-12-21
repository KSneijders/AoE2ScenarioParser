import src.pieces.scenario_piece as scenario_piece
from src.helper.retriever import Retriever
from src.helper.datatype import DataType
from src.pieces.structs.player_data_four import PlayerDataFourStruct
from src.pieces.structs.player_data_three_struct import PlayerDataThreeStruct
from src.pieces.structs.player_units import PlayerUnitsStruct


class UnitsPiece(scenario_piece.ScenarioPiece):
    def __init__(self, parser_obj):
        retrievers = [
            Retriever("Number of unit sections", DataType("u32"), save_as="unit_sections"),
            Retriever("Player Data 4", DataType(PlayerDataFourStruct, repeat=8)),
            # Retriever("Unknown", DataType("4")),
            Retriever("Number of players?", DataType("u32")),
            # Retriever("Unknown (2)", DataType("115", repeat=8)),
            Retriever("Player data #3?", DataType(PlayerDataThreeStruct, repeat=8)),
            Retriever("Player Units", DataType(PlayerUnitsStruct), set_repeat="{unit_sections}"),
        ]

        super().__init__(parser_obj, "Units", retrievers)
