import math

from AoE2ScenarioParser.datasets import buildings, units
from AoE2ScenarioParser.datasets.players import Player
from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.helper.alias import Alias
from AoE2ScenarioParser.helper.helper import Tile
from AoE2ScenarioParser.pieces.structs.unit import UnitStruct


class UnitObject:
    x: float = Alias("self._unit_struct.x")
    y: float = Alias("self._unit_struct.y")
    z: float = Alias("self._unit_struct.z")
    reference_id: int = Alias("self._unit_struct.reference_id")
    unit_const: int = Alias("self._unit_struct.unit_const")
    _rotation: float = Alias("self._unit_struct.rotation_radians")
    initial_animation_frame: int = Alias("self._unit_struct.initial_animation_frame")
    garrisoned_in: int = Alias("self._unit_struct.garrisoned_in_id")

    def __init__(self, unit_struct: UnitStruct):
        self._unit_struct = unit_struct
        self._player: Player = None

    @property
    def player(self):
        """
        PLEASE NOTE: This is an internal (read-only) value for ease of access. It accurately represent the actual
        player controlling the unit but is not directly connected to it. Changing this value will have no impact to your
        scenario.
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
            return helper.pretty_print_name(units.unit_names[self.unit_const])
        except KeyError:  # Object wasn't a unit, maybe a building?
            return helper.pretty_print_name(buildings.building_names[self.unit_const])
