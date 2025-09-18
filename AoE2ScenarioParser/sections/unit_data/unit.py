from __future__ import annotations

from math import floor

from bfp_rs import BaseStruct, Context, Retriever, Version
from bfp_rs.types.le import f32, i32, str32, u16, u8

from AoE2ScenarioParser.objects.support import Point, Tile
from AoE2ScenarioParser.objects.support.location import Location
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class Unit(BaseStruct):
    __default_ver__ = DE_LATEST

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
    garrisoned_in_ref: int  = Retriever(i32,   min_ver = Version(1, 13), default = -1)
    """Another object's reference_id. -1 (and 0 for v1.13 to 1.20) means None"""
    caption_string_id: int  = Retriever(i32,   min_ver = Version(1, 54), default = -1)
    caption_string: str     = Retriever(str32, min_ver = Version(1, 55), default = "")
    # @formatter:on

    def __init__(
        self,
        type: int,
        location: Location | tuple,
        z: float = 0,
        state: int = 2,
        rotation: float = 0,
        frame: int = 0,
        garrisoned_in_ref: int = -1,
        caption_string_id: int = -1,
        caption_string: str = '',
        reference_id: int = -1,
    ):
        """
        Args:
            type: Unit type (UnitInfo / BuildingInfo).
            location: Location of the object (Point / Tile).
            z: Z-coordinate of the object. Defaults to 0.
            state: State identifier of the object. Defaults to 2.
            rotation: Rotation angle of the object. Defaults to 0.
            frame: Frame identifier for animation or state. Defaults to 0.
            garrisoned_in_ref: Reference ID for the object it is garrisoned in, if applicable. Defaults to -1.
            caption_string_id: Identifier for the caption string. Defaults to -1.
            caption_string: Caption string associated with the object. Defaults to an empty string.
            reference_id: General reference ID associated with the object. Defaults to -1.
        """
        super().__init__()

        self.type = type
        self.location = location
        self.z = z
        self.state = state
        self.rotation = rotation
        self.frame = frame
        self.garrisoned_in_ref = garrisoned_in_ref
        self.caption_string_id = caption_string_id
        self.caption_string = caption_string
        self.reference_id = reference_id

    # [BFP overwrite] - Adds "*args" to allow __init__ to be called without kwargs
    def __new__(cls, *args, ver = Version(-1), ctx = Context(), init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, ctx, init_defaults, **retriever_inits)

    _player: int | None = None

    @property
    def location(self) -> Point:
        return self.point

    @location.setter
    def location(self, location: Location | tuple) -> None:
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
    def player(self):
        """Read-only property for the owner player. Use the Unit Manager to change ownership"""
        return self._player
