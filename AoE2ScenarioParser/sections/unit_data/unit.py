from __future__ import annotations

from math import floor

from bfp_rs import BaseStruct, Retriever, Version
from bfp_rs.types.le import f32, i32, str32, u16, u8

from AoE2ScenarioParser.objects.support import Point, Tile
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
    """in radians"""
    frame: int              = Retriever(u16,   min_ver = Version(1, 15), default = 0)
    garrisoned_in_ref: int  = Retriever(i32,   min_ver = Version(1, 13), default = -1)
    """another object's reference_id. -1 (and 0 for v1.13 to 1.20) mean None"""
    caption_string_id: int  = Retriever(i32,   min_ver = Version(1, 54), default = -1)
    caption_string: str     = Retriever(str32, min_ver = Version(1, 55), default = "")
    # @formatter:on

    _player: int | None = None

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
