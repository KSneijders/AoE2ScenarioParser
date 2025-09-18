from __future__ import annotations

import math
from typing import overload, TYPE_CHECKING

from AoE2ScenarioParser.helper.coordinates import i_to_xy, xy_to_i
from AoE2ScenarioParser.objects.support.location import Location

if TYPE_CHECKING:
    from typing import Self


# Todo: Add immutability to class
class Tile(Location):

    @overload
    def __init__(self, x: int, y: int):
        ...

    @overload
    def __init__(self, tile: tuple[int, int]):
        ...

    def __init__(self, x: int | tuple[int, int], y: int = None):
        super().__init__(x, y)

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int):
        self._x = math.floor(value)

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value: int):
        self._y = math.floor(value)

    @overload
    def move(self, x_offset: int = 0, y_offset: int = 0) -> Self:
        ...

    def move(self, *args, **kwargs):
        super().move(*args, **kwargs)

    @classmethod
    def from_i(cls, i: int, map_size: int) -> Tile:
        """
        Create a Tile object based on an index and a map_size

        Args:
            i: The index of the tile
            map_size: The map_size of the map

        Returns:
            A tile object representing the given tile
        """
        return cls(*i_to_xy(i, map_size))

    def to_i(self, map_size: int) -> int:
        """
        Get the index of a tile if it'd be on a map

        Args:
            map_size: The map_size of the map

        Returns:
            A number representing the index of this tile on a map
        """
        return xy_to_i(self.x, self.y, map_size)

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Tile({self.x}, {self.y})"

    def __lt__(self, other) -> bool:
        if isinstance(other, Tile) or isinstance(other, tuple):
            other_x, other_y = other

            return self.y < other_y \
                or self.y == other_y and self.x < other_x

        return super().__lt__(other)

    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.x == other.x and self.y == other.y
        if isinstance(other, tuple):
            return self.x == other[0] and self.y == other[1]
        return False
