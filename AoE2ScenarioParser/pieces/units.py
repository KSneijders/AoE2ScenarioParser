from typing import Dict

from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.retriever_dependency import RetrieverDependency, DependencyAction, DependencyTarget, \
    DependencyEval
from AoE2ScenarioParser.pieces import aoe2_piece
from AoE2ScenarioParser.pieces.structs.player_data_four import PlayerDataFourStruct
from AoE2ScenarioParser.pieces.structs.player_data_three import PlayerDataThreeStruct
from AoE2ScenarioParser.pieces.structs.player_units import PlayerUnitsStruct


class UnitsPiece(aoe2_piece.AoE2Piece):
    dependencies: Dict[str, Dict[str, RetrieverDependency]] = {
        "number_of_unit_sections": {

            "on_refresh": RetrieverDependency(
                DependencyAction.SET_VALUE, DependencyTarget("self", "players_units"),
                DependencyEval('len(x)')
            )
        },
        "players_units": {
            "on_refresh": RetrieverDependency(
                DependencyAction.SET_REPEAT, DependencyTarget("self", "number_of_unit_sections")
            ),
            "on_construct": RetrieverDependency(DependencyAction.REFRESH_SELF),
            "on_commit": RetrieverDependency(
                DependencyAction.REFRESH,
                DependencyTarget("self", "number_of_unit_sections")
            )
        }
    }

    def __init__(self, parser_obj=None, data=None, pieces=None):
        retrievers = [
            Retriever("number_of_unit_sections", DataType("u32")),
            Retriever("player_data_4", DataType(PlayerDataFourStruct, repeat=8)),
            Retriever("number_of_players", DataType("u32")),  # Also always 9 (Gaia + 8Plyrs)
            Retriever("player_data_3", DataType(PlayerDataThreeStruct, repeat=8)),
            Retriever("players_units", DataType(PlayerUnitsStruct)),
        ]

        super().__init__("Units", retrievers, parser_obj, data=data, pieces=pieces)

    @staticmethod
    def defaults(pieces):
        defaults = {
            'number_of_unit_sections': 9,
            'player_data_4': [PlayerDataFourStruct(data=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 200.0], pieces=pieces) for _ in range(8)],
            'number_of_players': 9,
            'player_data_3': [PlayerDataThreeStruct(data=list(PlayerDataThreeStruct.defaults(pieces).values()), pieces=pieces) for _ in range(8)],
            'players_units': [PlayerUnitsStruct(data=[0, []], pieces=pieces) for _ in range(9)],
        }
        return defaults

