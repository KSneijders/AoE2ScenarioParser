from __future__ import annotations

from typing import Iterable, TYPE_CHECKING

from AoE2ScenarioParser.objects.support.tile import Tile

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.support.typedefs import TileT


class Area:
    """
    Represents an area selection on a map. An area is defined by two opposite corners of a rectangle.

    - Supports iteration ``for corner in area: ...``
    - Supports index access (``area[0]`` => corner1, ``area[1]`` => corner2)
    - Supports comparison to tuples or other ``Area`` instances
    """
    def __init__(self, corner1: TileT, corner2: TileT = None):
        if corner2 is None:
            self.corner1 = self.corner2 = Tile(corner1[0], corner1[1])
            return

        x1, x2 = sorted((corner1[0], corner2[0]))
        y1, y2 = sorted((corner1[1], corner2[1]))
        self._corner1 = Tile(x1, y1)
        self._corner2 = Tile(x2, y2)

    @property
    def corner1(self) -> Tile:
        return self._corner1

    @corner1.setter
    def corner1(self, value: TileT):
        self._corner1 = Tile(*value)

    @property
    def corner2(self) -> Tile:
        return self._corner2

    @corner2.setter
    def corner2(self, value: TileT):
        self._corner2 = Tile(*value)

    @property
    def center_tile(self) -> Tile:
        """
        The tile in the center of the area.
        When the height or width is even, the coordinates are rounded up as that matches DE behaviour
        """
        return self.corner1.mid_tile(self.corner2)

    @property
    def center_point(self) -> tuple[float, float]:
        """the point in the center of this area as coordinates"""
        return self.corner1.mid_point(self.corner2)

    @property
    def width(self) -> int:
        """The width (along x-axis) of the area (inclusive)"""
        return self.corner2.x - self.corner1.x + 1

    @property
    def height(self) -> int:
        """The height (along y-axis) of the area (inclusive)"""
        return self.corner2.y - self.corner1.y + 1

    @property
    def dimensions(self) -> tuple[int, int]:
        """The dimensions of this area (inclusive)"""
        return self.width, self.height

    def resolve_negative_coords(self, map_size: int = None) -> Area:
        """
        Converts negative coordinates to the non-negative value. Like: ``-1 == 119`` when ``map_size = 120``

        Args:
            map_size: the map size

        Returns:
            A copy of the area object but with the corners converted if necessary
        """
        return Area(
            self.corner1.resolve_negative_coords(map_size),
            self.corner2.resolve_negative_coords(map_size)
        )

    def bound(self, map_size: int) -> Area:
        """
        Update the corners to be bounded between 0 and map_size

        Args:
            map_size: the map size

        Returns:
            A copy of the area object but with bounded corners
        """
        return Area(
            self.corner1.bound(map_size),
            self.corner2.bound(map_size)
        )

    def contains(self, tile: tuple) -> bool:
        """
        Checks if a tile is within this area

        Args:
            tile: The tile to check

        Returns:
            True if the tile is within this area, False otherwise
        """
        x, y = tile
        return (
            self.corner1.x <= x <= self.corner2.x
            and self.corner1.y <= y <= self.corner2.y
        )

    def __iter__(self) -> Iterable[Tile]:
        return iter((self.corner1, self.corner2))

    def __getitem__(self, item: int) -> Tile:
        return (self.corner1, self.corner2)[item]

    def __repr__(self) -> str:
        return f"Area({self.corner1}, {self.corner2})"

    def __eq__(self, other) -> bool:
        if isinstance(other, Area):
            return self.corner1 == other.corner1 and self.corner2 == other.corner2
        if not isinstance(other, tuple):
            return False
        if len(other) == 1:
            tile, = other
            return self.corner1 == tile == self.corner2
        if len(other) == 2:
            tile1, tile2 = other
            return self.corner1 == tile1 and self.corner2 == tile2
        return False
