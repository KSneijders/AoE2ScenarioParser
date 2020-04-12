from __future__ import annotations

from AoE2ScenarioParser.helper import parser
from AoE2ScenarioParser.helper.retriever import find_retriever
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.unit_obj import UnitObject
from AoE2ScenarioParser.pieces.structs.player_units import PlayerUnitsStruct


class UnitsObject(AoE2Object):
    def __init__(self,
                 units
                 ):

        self.units = units

        super().__init__()

    def get_new_reference_id(self) -> int:
        highest_id = -1
        for player in range(0, 9):
            for unit in self.units[player]:
                if highest_id < unit.reference_id:
                    highest_id = unit.reference_id
        return highest_id

    @staticmethod
    def _parse_object(parsed_data, **kwargs) -> UnitsObject:
        object_piece = parsed_data['UnitsPiece']
        units_per_player = find_retriever(object_piece.retrievers, "Player Units").data

        player_units = []
        for player_id in range(0, 9):  # 0 Gaia & 1-8 Players:
            player_units.append([])
            units = parser.listify(find_retriever(units_per_player[player_id].retrievers, "Units").data)

            for unit in units:
                player_units[player_id].append(
                    UnitObject._parse_object(parsed_data, unit=unit)
                )

        units_object = UnitsObject(
            units=player_units
        )

        return units_object

    @staticmethod
    def _reconstruct_object(parsed_data, objects, **kwargs) -> None:  # Expected {}
        player_units_retriever = find_retriever(parsed_data['UnitsPiece'].retrievers, "Player Units")

        player_units_retriever.data = []
        for player_units in objects['UnitsObject'].units:

            units_list = []
            for unit in player_units:
                UnitObject._reconstruct_object(parsed_data, objects, unit=unit, units=units_list)

            player_units_retriever.data.append(
                PlayerUnitsStruct(data=[len(units_list), units_list])
            )
