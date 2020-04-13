from __future__ import annotations

from typing import List

from AoE2ScenarioParser.helper import parser
from AoE2ScenarioParser.helper.retriever import find_retriever
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.unit_obj import UnitObject
from AoE2ScenarioParser.pieces.structs.player_units import PlayerUnitsStruct


class UnitsObject(AoE2Object):
    def __init__(self,
                 units: List[List[UnitObject]]
                 ):

        self.units = units

        super().__init__()

    def add_unit(self, player: int, unit_id: int, x: int, y: int, z: int = 0, rotation: int = 0,
                 garrisoned_in_id: int = -1, animation_frame: int = 0, status: int = 2,
                 reference_id: int = None, ) -> UnitObject:
        """
        Adds a unit to the scenario.

        Args:
            player: The player the unit belongs to.
            unit_id: Defines what unit you're placing. The IDs used in the unit/buildings dataset.
            x: The x location in the scenario.
            y: The y location in the scenario.
            z: The z (height) location in the scenario.
            rotation: The rotation of the unit.
            garrisoned_in_id: The reference_id of another unit this unit is garrisoned in.
            animation_frame: The animation frame of the unit.
            status: Unknown (ALWAYS: 2) -> Please let me know if you know what this does
            reference_id: The reference ID of this unit. Normally added automatically. Used for garrisoning or reference
                in triggers
        Returns:
            The UnitObject created
        """
        if reference_id is None:
            reference_id = self.get_new_reference_id()

        unit = UnitObject(
            x=x,
            y=y,
            z=z,
            reference_id=reference_id,
            unit_id=unit_id,
            status=status,
            rotation=rotation,
            animation_frame=animation_frame,
            garrisoned_in_id=garrisoned_in_id,
        )

        self.units[player].append(unit)
        return unit

    def remove_eye_candy(self):
        eye_candy_ids = [1351, 1352, 1353, 1354, 1355, 1358, 1359, 1360, 1361, 1362, 1363, 1364, 1365, 1366]
        self.units[0] = [gaia_unit for gaia_unit in self.units[0] if gaia_unit.unit_id not in eye_candy_ids]

    def change_ownership(self, unit: UnitObject, to_player: int, from_player: int = None, skip_gaia: int = False):
        """
        Changes a unit's ownership to the given player.

        Args:
            unit: The unit object which ownership will be changed
            to_player: The player that'll get ownership over the unit (0: Gaia, 1: P1, ... 8: P8)
            from_player: (Optional) [Performance Increasement] The player that currently has ownership over the unit.
                Cannot be used together with skip_gaia.
            skip_gaia: (Optional) [Performance Increasement] Skip player gaia when searching for the unit. Cannot be
                used together with from_player.
        """
        if from_player is not None and skip_gaia:
            raise ValueError("Can't use from_player and skip_gaia. Use one or the other.")

        start = 0
        end = 9
        if from_player is not None:
            start = from_player
            end = from_player + 1
        elif skip_gaia:
            start = 1

        for player in range(start, end):
            for i, player_unit in enumerate(self.units[player]):
                if player_unit == unit:
                    del self.units[player][i]
                    self.units[to_player].append(unit)
                    break

    def get_new_reference_id(self) -> int:
        highest_id = 0  # If no units, default to 0
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

        return UnitsObject(
            units=player_units
        )

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
