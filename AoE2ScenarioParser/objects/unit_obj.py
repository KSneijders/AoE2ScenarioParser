from __future__ import annotations

import math

from AoE2ScenarioParser.datasets import units, buildings
from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.helper.helper import Tile
from AoE2ScenarioParser.helper.retriever import find_retriever
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.pieces.structs.unit import UnitStruct


class UnitObject(AoE2Object):
    def __init__(self,
                 player,
                 x,
                 y,
                 z,
                 reference_id,
                 unit_id,
                 status,
                 rotation,
                 animation_frame,
                 garrisoned_in_id
                 ):

        self._player = player
        """
        PLEASE NOTE: This is an internal (read-only) value for ease of access. It accurately represent the actual 
        player controlling the unit but is not directly connected to it. Changing this value will have no impact to your
        scenario.
        To change which player controls this unit, use:
            unit_manager.change_ownership(UnitObject, to_player[, from_player, skip_gaia])
        """
        self.x = x
        self.y = y
        self.z = z
        self.reference_id = reference_id
        self.unit_id = unit_id
        self.status = status
        self.rotation = rotation % math.tau
        # Mods by tau because the scenario editor seems to place units at radian angles not strictly less than tau.
        self.animation_frame = animation_frame
        self.garrisoned_in_id = garrisoned_in_id

        super().__init__()

    @property
    def player(self):
        """
        PLEASE NOTE: This is an internal (read-only) value for ease of access. It DOES accurately represent the actual
        player controlling the unit BUT IT IS NOT directly connected to it. Changing this value will have no impact to
        your scenario.
        To change which player controls this unit, use:
            unit_manager.change_ownership(UnitObject, to_player[, from_player, skip_gaia])
        """
        return self._player

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, rotation: float) -> None:
        """Rotation in radians"""
        if not 0.0 <= rotation <= math.tau:
            raise ValueError(f'The Rotation value must be between 0 and tau (excl).')
        self._rotation = rotation

    @property
    def tile(self):
        return Tile(int(self.x), int(self.y))

    @tile.setter
    def tile(self, tile: Tile) -> None:
        self.x = tile.x + .5
        self.y = tile.y + .5

    @property
    def name(self):
        try:
            return helper.pretty_print_name(units.unit_names[self.unit_id])
        except KeyError:  # Object wasn't a unit
            return helper.pretty_print_name(buildings.building_names[self.unit_id])

    @staticmethod
    def _parse_object(parsed_data, **kwargs) -> UnitObject:  # Expected {unit=unitStruct, player=Player}
        unit = kwargs['unit']

        return UnitObject(
            player=kwargs['player'],
            x=find_retriever(unit.retrievers, "X position").data,
            y=find_retriever(unit.retrievers, "Y position").data,
            z=find_retriever(unit.retrievers, "Z position").data,
            reference_id=find_retriever(unit.retrievers, "ID").data,
            unit_id=find_retriever(unit.retrievers, "Unit 'constant'").data,
            status=find_retriever(unit.retrievers, "Status").data,
            rotation=find_retriever(unit.retrievers, "Rotation, in radians").data,
            animation_frame=find_retriever(unit.retrievers, "Initial animation frame").data,
            garrisoned_in_id=find_retriever(unit.retrievers, "Garrisoned in: ID").data,
        )

    @staticmethod
    def _reconstruct_object(parsed_data, objects, **kwargs) -> None:  # Expected {unit=unit_obj, units=units_list}
        unit_obj = kwargs['unit']
        units_list = kwargs['units']

        data_list = [value for key, value in vars(unit_obj).items()]
        del data_list[0]  # Remove player attribute

        units_list.append(UnitStruct(data=data_list))
