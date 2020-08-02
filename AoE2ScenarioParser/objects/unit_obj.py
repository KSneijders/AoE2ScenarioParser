from __future__ import annotations

import math

from AoE2ScenarioParser.datasets import units, buildings
from AoE2ScenarioParser.datasets.players import Player
from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.helper.helper import Tile
from AoE2ScenarioParser.helper.retriever import find_retriever
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object


class UnitObject(AoE2Object):
    @classmethod
    def create_unit(self,
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

        from AoE2ScenarioParser.pieces.structs.unit import UnitStruct
        unit = UnitObject(UnitStruct())

        unit._player: Player = player
        """
        PLEASE NOTE: This is an internal (read-only) value for ease of access. It accurately represents the actual 
        player controlling the unit but is not directly connected to it. Changing this value will have no impact to your
        scenario.
        To change which player controls this unit, use:
            unit_manager.change_ownership(UnitObject, to_player)
        """
        unit.x: float = x
        unit.y: float = y
        unit.z: float = z
        unit.reference_id: int = reference_id
        unit.unit_const: int = unit_const
        unit.status: int = status
        unit.rotation_radians: float = rotation % math.tau
        # Mods by tau because the scenario editor seems to place units at radian angles not strictly less than tau.
        unit.initial_animation_frame: int = animation_frame
        unit.garrisoned_in_id: int = garrisoned_in_id

        return unit

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
        return self.rotation_radians

    @rotation.setter
    def rotation(self, rotation: float) -> None:
        """Rotation in radians"""
        if not 0.0 <= rotation <= math.tau:
            raise ValueError(f'The Rotation value must be between 0 and tau (excl).')
        self.rotation_radians = rotation

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
            return helper.pretty_print_name(units.unit_names[self.unit_const])
        except KeyError:  # Object wasn't a unit, maybe a building?
            return helper.pretty_print_name(buildings.building_names[self.unit_const])

