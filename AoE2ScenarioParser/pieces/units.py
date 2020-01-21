import AoE2ScenarioParser.pieces.aoe2_piece as scenario_piece
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.pieces.structs.player_data_four import PlayerDataFourStruct
from AoE2ScenarioParser.pieces.structs.player_data_three_struct import PlayerDataThreeStruct
from AoE2ScenarioParser.pieces.structs.player_units import PlayerUnitsStruct


class UnitsPiece(scenario_piece.ScenarioPiece):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("Number of unit sections", DataType("u32"), save_as="unit_sections"),
            Retriever("Player data #4", DataType(PlayerDataFourStruct, repeat=8)),
            # Retriever("Unknown", DataType("4")),
            Retriever("Number of players?", DataType("u32")),
            # Retriever("Unknown (2)", DataType("115", repeat=8)),
            Retriever("Player data #3", DataType(PlayerDataThreeStruct, repeat=8)),
            Retriever("Player Units", DataType(PlayerUnitsStruct), set_repeat="{unit_sections}"),
        ]

        super().__init__("Units", retrievers, parser_obj)
