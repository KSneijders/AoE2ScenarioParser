from __future__ import annotations

from math import ceil
from typing import NamedTuple, Tuple

TileT = Tuple[int, int]

class Tile(NamedTuple):
    """NamedTuple for tiles. use tile.x or tile.y for coord access"""
    x: int
    y: int

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

    def mid_point(self, other: Tile) -> Tile:
        return Tile(
            ceil((self.x + other.x) / 2),
            ceil((self.y + other.y) / 2),
        )

def bound(value: int, bounds: TileT):
    low, high = bounds
    return max(low, min(high, value))
