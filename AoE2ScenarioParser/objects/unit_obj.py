from __future__ import annotations

import math

from AoE2ScenarioParser.datasets import units, buildings
from AoE2ScenarioParser.datasets.players import Player
from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.helper.helper import Tile
from AoE2ScenarioParser.helper.retriever import get_retriever_by_name
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.pieces.structs.unit import UnitStruct


class UnitObject(AoE2Object):
    def __init__(self,
                 player: Player,
                 x: float,
                 y: float,
                 z: float,
                 reference_id: int,
                 unit_const: int,
                 status: int,
                 rotation: float,
                 animation_frame: int,
                 garrisoned_in_id: int
                 ):

        self._player: Player = player
        """
        PLEASE NOTE: This is an internal (read-only) value for ease of access. It accurately represent the actual 
        player controlling the unit but is not directly connected to it. Changing this value will have no impact to your
        scenario.
        To change which player controls this unit, use:
            unit_manager.change_ownership(UnitObject, to_player)
        """
        self.x: float = x
        self.y: float = y
        self.z: float = z
        self.reference_id: int = reference_id
        self.unit_id: int = unit_const
        self.status: int = status
        self.rotation: float = rotation % math.tau
        # Mods by tau because the scenario editor seems to place units at radian angles not strictly less than tau.
        self.animation_frame: int = animation_frame
        self.garrisoned_in_id: int = garrisoned_in_id

        super().__init__()

    @property
    def player(self) -> Player:
        """
        PLEASE NOTE: This is an internal (read-only) value for ease of access. It DOES accurately represent the actual
        player controlling the unit BUT IT IS NOT directly connected to it. Changing this value will have no impact to
        your scenario.
        To change which player controls this unit, use:
            unit_manager.change_ownership(UnitObject, to_player)
        """
        return self._player

    @property
    def rotation(self) -> float:
        return self._rotation

    @rotation.setter
    def rotation(self, rotation: float) -> None:
        """Rotation in radians"""
        if not 0.0 <= rotation <= math.tau:
            raise ValueError(f'The Rotation value must be between 0 and tau (excl).')
        self._rotation = rotation

    @property
    def tile(self) -> Tile:
        return Tile(math.floor(self.x), math.floor(self.y))
        # Floor x and y as location (0.9, 0.9) is still Tile[x=0, y=0]

    @tile.setter
    def tile(self, tile: Tile) -> None:
        self.x = tile.x
        self.y = tile.y

    @property
    def name(self) -> str:
        try:
            return helper.pretty_print_name(units.unit_names[self.unit_id])
        except KeyError:  # Object wasn't a unit, maybe a building?
            return helper.pretty_print_name(buildings.building_names[self.unit_id])

    @staticmethod
    def _parse_object(parsed_data, **kwargs) -> UnitObject:  # Expected {unit=unitStruct, player=Player}
        unit = kwargs['unit']

        return UnitObject(
            player=kwargs['player'],
            x=get_retriever_by_name(unit.retrievers, "x").data,
            y=get_retriever_by_name(unit.retrievers, "y").data,
            z=get_retriever_by_name(unit.retrievers, "z").data,
            reference_id=get_retriever_by_name(unit.retrievers, "reference_id").data,
            unit_const=get_retriever_by_name(unit.retrievers, "unit_const").data,
            status=get_retriever_by_name(unit.retrievers, "status").data,
            rotation=get_retriever_by_name(unit.retrievers, "rotation_radians").data,
            animation_frame=get_retriever_by_name(unit.retrievers, "initial_animation_frame").data,
            garrisoned_in_id=get_retriever_by_name(unit.retrievers, "garrisoned_in_id").data,
        )

    @staticmethod
    def _reconstruct_object(parsed_header, parsed_data, objects, **kwargs) -> None:  # Expected {unit=unit_obj, units=units_list}
        unit_obj = kwargs['unit']
        units_list = kwargs['units']

        data_list = [value for key, value in vars(unit_obj).items()]
        del data_list[0]  # Remove player attribute

        units_list.append(UnitStruct(data=data_list))
