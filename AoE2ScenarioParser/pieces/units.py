from AoE2ScenarioParser.pieces import aoe2_piece
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.pieces.structs.player_data_four import PlayerDataFourStruct
from AoE2ScenarioParser.pieces.structs.player_data_three import PlayerDataThreeStruct
from AoE2ScenarioParser.pieces.structs.player_units import PlayerUnitsStruct


class UnitsPiece(aoe2_piece.AoE2Piece):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("Number of unit sections", DataType("u32"), save_as="unit_sections"),  # Always 9 (Gaia + 8Plyrs)
            Retriever("Player data #4", DataType(PlayerDataFourStruct, repeat=8)),
            Retriever("Number of players?", DataType("u32")),  # Also always 9 (Gaia + 8Plyrs)
            Retriever("Player data #3", DataType(PlayerDataThreeStruct, repeat=8)),
            Retriever("Player Units", DataType(PlayerUnitsStruct), set_repeat="{unit_sections}"),
        ]

        super().__init__("Units", retrievers, parser_obj, data=data)
