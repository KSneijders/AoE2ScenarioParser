from __future__ import annotations

import math
from typing import NamedTuple, Tuple

from AoE2ScenarioParser.helper.coordinates import i_to_xy
from AoE2ScenarioParser.helper.helper import bound

TileT = Tuple[int, int]


class Tile(NamedTuple):
    """NamedTuple for tiles. use tile.x or tile.y for coord access"""
    x: int
    y: int

    # Todo: Add tests
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

    def resolve_negative_coords(self, map_size: int | None = None) -> Tile:
        """
        Converts negative coordinates to the non-negative value. Like: ``-1 == 119`` when ``map_size = 120``

        Args:
            map_size: the map size

        Returns:
            A new Tile object with the mapped coordinates

        Raises:
            ValueError: When negative coordinates are provided without a map_size
        """
        if map_size is None:
            if self.x < 0 or self.y < 0:
                raise ValueError("Cannot use negative coordinates to make an area selection when map_size is not set")
            return self
        return Tile(
            (self.x + map_size) if self.x < 0 else self.x,
            (self.y + map_size) if self.y < 0 else self.y,
        )

    # Todo: Add tests
    def middle_tile(self, other: Tile) -> Tile:
        """
        Returns the tile that is in the middle of the current and given tile.

        Args:
            other: The other tile to get the middle from compared to the current tile

        Returns:
            The middle as Tile (rounded down coordinates)
        """
        x, y = self.middle_location(other)
        return Tile(math.floor(x), math.floor(y))

    # Todo: Add tests
    def middle_location(self, other: Tile) -> tuple[float, float]:
        """
        Returns the middle location in between the two tiles as 2 floats

        Args:
            other: The other tile to get the middle from compared to the current tile

        Returns:
            The middle as floats in a tuple
        """
        return (self.x + other.x) / 2, (self.y + other.y) / 2

    # Todo: Add tests
    def distance_to(self, other: Tile) -> float:
        """
        Get the distance between two tiles

        Args:
            other: The tile to compare to

        Returns:
            The distance between the current and given tile
        """
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
