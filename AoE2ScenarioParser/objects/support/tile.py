from __future__ import annotations

import math
from typing import NamedTuple, TYPE_CHECKING

from AoE2ScenarioParser.helper.coordinates import i_to_xy, xy_to_i
from AoE2ScenarioParser.helper.helper import bound

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.support import TileT


class Tile(NamedTuple):
    """NamedTuple for tiles. use tile.x or tile.y for coord access"""
    x: int
    y: int

    @classmethod
    def from_value(cls, val: TileT | list | dict) -> Tile:
        """
        Create a Tile object based on a given value

        Args:
            val: The value used to create a tile with

        Returns:
            A new Tile instance if a tuple is given. If a tile is given it's directly returned.

        Raises:
            ValueError: When a value is given that cannot be turned into a Tile()
        """
        if isinstance(val, Tile):
            return val
        elif isinstance(val, tuple) or isinstance(val, list):
            return Tile(*val)
        elif isinstance(val, dict):
            return Tile(**val)
        raise ValueError(f"Unable to create instance of tile from the given value: {val}")

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

    def bound(self, map_size: int) -> Tile:
        """
        Create a new tile object with the same coords as this tile but bounded between 0 and map_size

        Args:
            map_size: the map size

        Returns:
            A new tile object with the bounded coordinates
        """
        return Tile(
            bound(self.x, (0, map_size)),
            bound(self.y, (0, map_size)),
        )

    def resolve_negative_coords(self, map_size: int = None) -> Tile:
        """
        Converts negative coordinates to the non-negative value. Like: ``-1 == 119`` when ``map_size = 120``

        Args:
            map_size: the map size

        Returns:
            A new Tile object with the mapped coordinates

        Raises:
            ValueError: When negative coordinates are provided without a map_size
        """
        if map_size is None and (self.x < 0 or self.y < 0):
            raise ValueError("Cannot use negative coordinates to make an area selection when map_size is not set")

        return Tile(
            (self.x + map_size) if self.x < 0 else self.x,
            (self.y + map_size) if self.y < 0 else self.y,
        )

    def mid_tile(self, other: Tile, de_behaviour: bool = True) -> Tile:
        """
        Returns the tile that is in the middle of the current and given tile.

        Args:
            other: The other tile to get the middle from compared to the current tile
            de_behaviour: If false, rounds the center tile down instead of up

        Returns:
            The middle as Tile (rounded down coordinates)
        """
        x, y = self.mid_point(other)
        if not de_behaviour:
            return Tile(math.floor(x), math.floor(y))
        return Tile(math.ceil(x), math.ceil(y))

    def mid_point(self, other: Tile) -> tuple[float, float]:
        """
        Returns the mid-point between the two tiles as 2 floats

        Args:
            other: The other tile to get the middle from compared to the current tile

        Returns:
            The middle as floats in a tuple
        """
        return (self.x + other.x) / 2, (self.y + other.y) / 2

    def dist(self, other: Tile) -> float:
        """
        Get the euclidean distance between two tiles

        Args:
            other: The tile to find the distance to

        Returns:
            The distance between the current and given tile
        """
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

    def dist_taxicab(self, other: Tile) -> int:
        """
        Get the taxicab/manhattan distance between two tiles

        Args:
            other: The tile to find the distance to

        Returns:
            The taxi cab/manhattan distance between the current and given tile
        """
        return abs(other.x - self.x) + abs(other.y - self.y)

    def __repr__(self):
        return f"Tile({self.x}, {self.y})"
