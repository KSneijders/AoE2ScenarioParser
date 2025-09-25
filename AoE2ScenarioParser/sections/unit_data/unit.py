from __future__ import annotations

from math import floor
from typing import TYPE_CHECKING

from bfp_rs import BaseStruct, Context, Retriever, Version
from bfp_rs.types.le import f32, i32, str32, u16, u8

from AoE2ScenarioParser.concerns import CanBeLinked, CanHoldUnits
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.helper.string_manipulations import add_tabs
from AoE2ScenarioParser.objects.support import Point, Tile
from AoE2ScenarioParser.objects.support.location import Location
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST

if TYPE_CHECKING:
    # noinspection PyUnusedImports
    from sections import ScenarioSections
    from typing import Iterable


class Unit(BaseStruct, CanHoldUnits, CanBeLinked):
    __default_ver__ = DE_LATEST
    _struct: 'ScenarioSections | None' = None

    # @formatter:off
    x: float                = Retriever(f32,                             default = 0.5)
    y: float                = Retriever(f32,                             default = 0.5)
    z: float                = Retriever(f32,                             default = 0)
    reference_id: int       = Retriever(i32,                             default = -1)
    type: int               = Retriever(u16,                             default = 4)
    state: int              = Retriever(u8,                              default = 2)
    rotation: float         = Retriever(f32,                             default = 0)
    """In radians"""
    frame: int              = Retriever(u16,   min_ver = Version(1, 15), default = 0)
    _garrisoned_in_ref: int = Retriever(i32,   min_ver = Version(1, 13), default = -1)
    """Another object's reference_id. -1 (and 0 for v1.13 to 1.20) means None"""
    caption_string_id: int  = Retriever(i32,   min_ver = Version(1, 54), default = -1)
    caption_string: str     = Retriever(str32, min_ver = Version(1, 55), default = "")
    # @formatter:on

    def __init__(
        self,
        player: int | Player,
        type: int,
        location: Location | tuple,
        z: float = 0,
        state: int = 2,
        rotation: float = 0,
        frame: int = 0,
        caption_string_id: int = -1,
        caption_string: str = '',
        reference_id: int = -1,

        garrisoned_in: Unit = None,
        garrisoned_units: Iterable[Unit] = None,
    ):
        """
        Args:
            type: Unit type (UnitInfo / BuildingInfo).
            location: Location of the object (Point / Tile).
            z: Z-coordinate of the object. Defaults to 0.
            state: State identifier of the object. Defaults to 2.
            rotation: Rotation angle of the object. Defaults to 0.
            frame: Frame identifier for animation or state. Defaults to 0.
            caption_string_id: Identifier for the caption string. Defaults to -1.
            caption_string: Caption string associated with the object. Defaults to an empty string.
            reference_id: General reference ID associated with the object. Defaults to -1.

            garrisoned_in: Reference ID for the object it is garrisoned in, if applicable. Defaults to -1.
            garrisoned_units: Iterable of units that are garrisoned inside this unit.
        """
        super().__init__()

        self._garrisoned_units = tuple()

        self._player: Player = player
        self.type: int = type
        self.location = location
        self.z = z
        self.state = state
        self.rotation = rotation
        self.frame = frame
        self.caption_string_id = caption_string_id
        self.caption_string = caption_string
        self.reference_id = reference_id

        self.garrisoned_in = garrisoned_in
        self.garrisoned_units: tuple[Unit, ...] = garrisoned_units or tuple()

    # [BFP overwrite] - Adds "*args" to allow __init__ to be called without kwargs
    def __new__(cls, *args, ver = Version(-1), ctx = Context(), init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, ctx, init_defaults, **retriever_inits)

    _player: int | None = None

    @classmethod
    def garrisoned(
        cls,
        player: int | Player,
        type: int,
        caption_string_id: int = -1,
        caption_string: str = '',
        reference_id: int = -1,
    ):
        return cls(
            player,
            type,
            Point(0, 0),
            caption_string_id = caption_string_id,
            caption_string = caption_string,
            reference_id = reference_id,
        )

    @property
    def location(self) -> Point:
        return self.point

    @location.setter
    def location(self, location: Location | tuple) -> None:
        if isinstance(location, Location):
            self.point = (location.center_x, location.center_y)
        else:
            self.point = Point.from_value(location)

    @property
    def tile(self) -> Tile:
        return Tile(floor(self.x), floor(self.y))

    @tile.setter
    def tile(self, tile: Tile) -> None:
        self.x = tile.x + .5
        self.y = tile.y + .5

    @property
    def point(self) -> Point:
        return Point(self.x, self.y)

    @point.setter
    def point(self, point: Point) -> None:
        self.x, self.y = point

    @property
    def has_reference_id(self):
        return self.reference_id != -1

    @property
    def player(self) -> Player:
        return self._player

    @player.setter
    def player(self, value: int | Player):
        # Todo: CALL: UnitManager.change_ownership
        #   UnitManager(self._struct).change_ownership(value, self)
        self._player = value

    #  -------------------------- Garrisoning Units -------------------------- #

    def _get_unit_references(self, key: str = '') -> tuple[Unit, ...]:
        return self.garrisoned_units

    def _remove_unit_reference(self, unit: 'Unit', _: str = '') -> None:
        self._garrisoned_units = tuple(unit for unit in self.garrisoned_units if unit != unit)

    def _add_unit_reference(self, unit: 'Unit', _: str = '') -> None:
        if id(unit) in (id(u) for u in self.garrisoned_units):
            return

        self._garrisoned_units = (
            *self.garrisoned_units,
            unit,
        )

    def add_garrisoned_units(self, *units: Unit) -> None:
        self.garrisoned_units = (
            *self.garrisoned_units,
            *(unit for unit in units if unit not in self.garrisoned_units),
        )

    def remove_garrisoned_units(self, *units: Unit) -> None:
        self.garrisoned_units = tuple(unit for unit in self.garrisoned_units if unit not in units)

    @property
    def is_garrisoned(self):
        return self._garrisoned_in_ref != -1

    @property
    def is_not_garrisoned(self):
        return not self.is_garrisoned

    @property
    def garrisoned_in(self) -> Unit | None:
        return self._garrisoned_in

    @garrisoned_in.setter
    def garrisoned_in(self, unit: Unit | None):
        # garrisoned_in can never be None when is_garrisoned is True
        # except when setting it during initial scenario initialization
        if self.is_garrisoned and self.garrisoned_in is not None:
            self.garrisoned_in._remove_unit_reference(self)

        if unit is None:
            self._garrisoned_in = None
            self._garrisoned_in_ref = -1

            return

        self._garrisoned_in = unit
        self._garrisoned_in_ref = unit.reference_id

        unit._add_unit_reference(self)

    @property
    def garrisoned_units(self) -> tuple[Unit, ...]:
        return self._garrisoned_units

    @garrisoned_units.setter
    def garrisoned_units(self, units: Iterable[Unit]):
        new_unit_ids = list(id(u) for u in units)

        for unit in self.garrisoned_units:
            if id(unit) not in new_unit_ids:
                unit.garrisoned_in = None

        for unit in units:
            if unit.is_garrisoned and unit.garrisoned_in is not self:
                raise ValueError(f"Unit {unit} is already garrisoned in another unit")

            if self._is_linked() and not unit._is_linked():
                from AoE2ScenarioParser.managers import UnitManager

                UnitManager(self._struct).add_unit(unit)

            unit.garrisoned_in = self

    # ----- STRING FUNCTIONS -----

    def __repr__(self):
        datasets = (UnitInfo, BuildingInfo, OtherInfo, HeroInfo)

        for ds in datasets:
            try:
                type_ = ds.from_id(self.type).name
                break
            except KeyError:
                pass
        else:
            type_ = f"Unknown ({self.type})"

        attributes = {
            "type":              type_,
            "location":          self.location,
            "z":                 self.z,
            "state":             self.state,
            "rotation":          self.rotation,
            "frame":             self.frame,
            "caption_string_id": self.caption_string_id,
            "caption_string":    self.caption_string,
            "reference_id":      self.reference_id,
            "garrisoned_units":  add_tabs(str(self.garrisoned_units), 1) if self.garrisoned_units else None,
        }

        attributes = {key: value for key, value in attributes.items() if value and value != -1}

        longest_key = max(len(key) for key in attributes.keys()) + 2

        formatted = '\n'.join(f"\t{(key + ':').ljust(longest_key)}  {value}" for key, value in attributes.items())

        return f"Unit(\n{formatted}\n)"
