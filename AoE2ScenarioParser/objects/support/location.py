from __future__ import annotations

import math
from typing import TYPE_CHECKING

from AoE2ScenarioParser.helper.helper import bound

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.support import Point
    from AoE2ScenarioParser.objects.support import Tile
    from typing import Iterable, Self


class Location:

    def __init__(self, x: int | float | tuple[int | float, int | float], y: int | float = None):
        if isinstance(x, tuple):
            coords = x
            if len(coords) != 2:
                raise ValueError("tuple must have exactly two coordinates")
            x, y = coords

        self.x = x
        self.y = y

    def _new(self, *args) -> Self:
        return self.__class__(*args)

    @classmethod
    def from_value(cls, val: Self | tuple[int | float] | tuple[int | float, int | float] | list | dict) -> Self:
        """
        Create an object based on a given value

        Args:
            val: The value used to create the object with

        Returns:
            A new instance if a tuple is given. If the same class is given it's directly returned

        Raises:
            ValueError: When a value is given that cannot be used to create the object
        """
        if isinstance(val, cls):
            return val
        elif isinstance(val, tuple) or isinstance(val, list):
            return cls(*val)
        elif isinstance(val, dict):
            return cls(**val)
        raise ValueError(f"Unable to create instance from the given value: {val}")

    def bound(self, limit: int) -> Self:
        """
        Create a new object with the same coords as the current object but bounded between 0 and the given limit

        Args:
            limit: the maximum coordinate value

        Returns:
            A new object with the bounded coordinates
        """
        return self._new(
            bound(self.x, (0, limit)),
            bound(self.y, (0, limit)),
        )

    def resolve_negative_coords(self, map_size: int = None) -> Self:
        """
        Converts negative coordinates to the non-negative value. Like: ``-1 == 119`` when ``map_size = 120``

        Args:
            map_size: the map size

        Returns:
            A new object with the mapped coordinates

        Raises:
            ValueError: When negative coordinates are provided without a map_size
        """
        if map_size is None and (self.x < 0 or self.y < 0):
            raise ValueError("Cannot use negative coordinates when map_size is not set")

        return self._new(
            (self.x + map_size) if self.x < 0 else self.x,
            (self.y + map_size) if self.y < 0 else self.y,
        )

    def move(self, x_offset: int | float = 0, y_offset: int | float = 0) -> Self:
        """
        Moves this object by the given offsets

        Args:
            x_offset: The amount to move the tile on the x-axis (West to East)
            y_offset: The amount to move the tile on the y-axis (North to South)

        Returns:
            A copy of the object but offset by the given values
        """
        return self._new(self.x + x_offset, self.y + y_offset)

    def mid_point(self, other: 'Location') -> 'Point':
        """
        Returns the mid-point between the two locations

        Args:
            other: The other location to get the middle from compared to the current location

        Returns:
            The middle as Point
        """
        from AoE2ScenarioParser.objects.support import Point

        return Point((self.x + other.x) / 2, (self.y + other.y) / 2)

    def mid_tile(self, other: 'Location', de_behaviour: bool = True) -> 'Tile':
        """
        Returns the tile that is in the middle of the current location and given location.

        Args:
            other: The other location to get the middle from compared to the current location
            de_behaviour: If false, rounds the center tile down instead of up

        Returns:
            The middle as Tile
        """
        from AoE2ScenarioParser.objects.support import Tile

        x, y = self.mid_point(other)
        if not de_behaviour:
            return Tile(math.floor(x), math.floor(y))
        return Tile(math.ceil(x), math.ceil(y))

    def dist(self, other: 'Location') -> float:
        """
        Get the Euclidean distance between two locations

        Args:
            other: The location to find the distance to

        Returns:
            The distance between the current location and the given location
        """
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

    def dist_taxicab(self, other: 'Location') -> int:
        """
        Get the taxicab/manhattan distance between two locations

        Args:
            other: The location to find the distance to

        Returns:
            The taxi cab/manhattan distance between the current location and the given location
        """
        return abs(other.x - self.x) + abs(other.y - self.y)

    def is_within_bounds(self, bound: int, resolve_negative_coords: bool = False) -> bool:
        """
        If this location is within the bounds of the given map_size (allowing negative coordinates)

        Args:
            bound: The map_size of the map
            resolve_negative_coords: If negative coordinates should be resolved to wrap to the other side of the map

        Returns:
            True if this location is within the bounds of the given map_size
        """
        location = self.resolve_negative_coords(bound) if resolve_negative_coords else self

        return 0 <= location.x < bound and 0 <= location.y < bound

    def __iter__(self) -> Iterable[int]:
        return iter((self.x, self.y))

    def __getitem__(self, item: int) -> int:
        return (self.x, self.y)[item]

    def __lt__(self, other) -> bool:
        if isinstance(other, self.__class__) or isinstance(other, tuple):
            other_x, other_y = other

            return self.y < other_y \
                or self.y == other_y and self.x < other_x

        return super().__lt__(other)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        if isinstance(other, tuple):
            return self.x == other[0] and self.y == other[1]
        return False
