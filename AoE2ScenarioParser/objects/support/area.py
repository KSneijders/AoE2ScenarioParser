from __future__ import annotations

import math
from typing import Iterable, overload, TYPE_CHECKING

from AoE2ScenarioParser.objects.support.enums.direction import Direction
from AoE2ScenarioParser.objects.support.tile import Tile
from AoE2ScenarioParser.objects.support.tile_sequence import TileSequence

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.support.typedefs import AreaT, TileT


# Todo: Add immutability to class
class Area(TileSequence):
    """
    Represents an area selection on a map. An area is defined by two opposite corners of a rectangle.

    - Supports iteration ``for corner in area: ...``
    - Supports index access (``area[0]`` => corner1, ``area[1]`` => corner2)
    - Supports comparison to tuples or other ``Area`` instances
    """

    @overload
    def __init__(self, corner1: TileT):
        ...

    @overload
    def __init__(self, corner1: TileT, corner2: TileT):
        ...

    def __init__(self, corner1: TileT, corner2: TileT = None):
        if corner2 is None:
            corner2 = corner1

        x1, x2 = sorted((corner1[0], corner2[0]))
        y1, y2 = sorted((corner1[1], corner2[1]))

        self.corner1 = Tile(x1, y1)
        self.corner2 = Tile(x2, y2)

        self._apply_bounding = True
        """If the area should automatically bound the EAST corner so the corner cannot go below (0, 0)"""

    @classmethod
    def from_value(cls, val: AreaT | TileT | tuple[int, int, int, int] | list | dict) -> Area:
        """
        Create an Area object based on a given value

        Args:
            val: The value used to create an area with

        Returns:
            A new Area instance if a tuple is given. If an area is given it's directly returned.

        Raises:
            ValueError: When a value is given that cannot be turned into an Area()
        """

        def from_iterable(iterable: list | tuple) -> Area | None:
            """Check content of iterable and return proper Area object"""
            if len(iterable) == 1:
                return cls(*iterable)
            if len(iterable) == 2:
                if isinstance(iterable[0], (list, tuple, Tile)):
                    return cls(*iterable)
                else:
                    return cls(Tile.from_value(iterable))
            elif len(iterable) == 4:
                return cls(iterable[:2], iterable[2:])
            return None

        if isinstance(val, cls):
            return val
        elif isinstance(val, Tile):
            return cls(val)
        elif isinstance(val, tuple) or isinstance(val, list):
            if area := from_iterable(val):
                return area
        elif isinstance(val, dict):
            vals = tuple(val.values())
            if area := from_iterable(vals):
                return area
            return cls(**val)
        raise ValueError(f"Unable to create instance of area from the given value: {val}")

    def to_tiles(self) -> set[Tile]:
        """Turn this area into a set of tiles"""
        return {Tile(x, y) for y in self.height_range for x in self.width_range}

    @property
    def center_tile(self) -> Tile:
        """
        The tile in the center of the area.
        When the height or width is even, the coordinates are rounded up as that matches DE behaviour
        """
        return self.corner1.mid_tile(self.corner2)

    # Todo: Use Position object here once it is implemented
    @property
    def center_point(self) -> tuple[float, float]:
        """the point in the center of this area as coordinates"""
        return self.corner1.mid_point(self.corner2)

    @property
    def width(self) -> int:
        """The width (along x-axis) of the area (inclusive)"""
        return self.x2 - self.x1 + 1

    @property
    def height(self) -> int:
        """The height (along y-axis) of the area (inclusive)"""
        return self.y2 - self.y1 + 1

    @property
    def width_range(self) -> range:
        """A range object looping over the x coordinates along the entire width"""
        return range(self.x1, self.x2 + 1)

    @property
    def height_range(self) -> range:
        """A range object looping over the y coordinates along the entire height"""
        return range(self.y1, self.y2 + 1)

    @property
    def x1(self) -> int:
        """The x coordinate of the west-most (lowest x & y) corner"""
        return self.corner1.x

    @property
    def y1(self) -> int:
        """The y coordinate of the west-most (lowest x & y) corner"""
        return self.corner1.y

    @property
    def x2(self) -> int:
        """The x coordinate of the east-most (highest x & y) corner"""
        return self.corner2.x

    @property
    def y2(self) -> int:
        """The y coordinate of the east-most (highest x & y) corner"""
        return self.corner2.y

    @property
    def dimensions(self) -> tuple[int, int]:
        """The dimensions of this area (inclusive)"""
        return self.width, self.height

    @property
    def surface_area(self) -> int:
        """The total surface area in number of tiles of this area"""
        return self.width * self.height

    @property
    def corners(self) -> tuple[TileT, TileT]:
        """The dimensions of this area (inclusive)"""
        return self.corner1, self.corner2

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

    def move(self, x_offset: int = 0, y_offset: int = 0) -> Area:
        """
        Moves the selection by the given offsets

        Args:
            x_offset: The amount to move the selection on the x-axis (West to East)
            y_offset: The amount to move the selection on the y-axis (North to South)

        Returns:
            A copy of the area object but offset by the given values
        """
        corner1 = Tile(self.corner1.x + x_offset, self.corner1.y + y_offset)
        corner2 = Tile(self.corner2.x + x_offset, self.corner2.y + y_offset)

        return Area(corner1, corner2)

    def move_to(self, tile: TileT, corner: Direction):
        """
        Moves the selection to the given coordinate by placing the given corner of this area on the coordinate.

        For center placement, use ``.center(...)``

        Args:
            corner: The corner used to align the selection onto the given tile
            tile: The coordinate to place the selection onto

        Returns:
            A copy of the area object but moved to the given tile aligned using the given corner.
        """
        x, y = Tile.from_value(tile)

        if x < 0 or y < 0:
            raise ValueError("Invalid tile: No negative coordinates allowed")

        width = self.width - 1
        height = self.height - 1

        if corner == Direction.WEST:
            return Area((x, y), (x + width, y + height))
        elif corner == Direction.NORTH:
            return Area((x - width, y), (x, y + height))
        elif corner == Direction.EAST:
            return Area((x - width, y - height), (x, y))
        elif corner == Direction.SOUTH:
            return Area((x, y - height), (x + width, y))
        else:
            raise ValueError(f"Invalid direction: '{corner}'")

    def shrink(self, n: int) -> Area:
        """
        Shrinks the selection by the given amount of tiles from all sides

        Args:
            n: The amount of tiles to shrink

        Returns:
            A copy of the area object but shrunken
        """
        width, height = self.dimensions

        width = max(1, width - n * 2)
        height = max(1, height - n * 2)

        return self.size(width = width, height = height)

    def shrink_corner1_by(self, *, dx: int = 0, dy: int = 0) -> Area:
        """
        Shrinks the selection from the west-corner by moving the west-corner by the given offset

        Args:
            dx: The amount of offset on the corner1 x-axis to be applied
            dy: The amount of offset on the corner1 y-axis to be applied

        Returns:
            A copy of the area object but shrunken from corner1
        """
        corner1, corner2 = self.corners
        corner1 = Tile(
            min(corner1.x + dx, corner2.x),
            min(corner1.y + dy, corner2.y),
        )
        return Area(corner1, corner2)

    def shrink_corner2_by(self, *, dx: int = 0, dy: int = 0) -> Area:
        """
        Shrinks the selection from the east-corner by moving the east-corner by the given offset

        Args:
            dx: The amount of offset on the corner2 x-axis to be applied
            dy: The amount of offset on the corner2 y-axis to be applied

        Returns:
            A copy of the area object but shrunken from corner2
        """
        corner1, corner2 = self.corners
        corner2 = Tile(
            max(corner1.x, corner2.x - dx),
            max(corner1.y, corner2.y - dy),
        )
        return Area(corner1, corner2)

    def expand(self, n: int) -> Area:
        """
        Expands the selection by the given amount of tiles from all sides

        Args:
            n: The amount of tiles to expand

        Returns:
            A copy of the area object but expanded
        """
        width, height = self.dimensions

        return self.size(width = width + n * 2, height = height + n * 2)

    def expand_corner1_by(self, *, dx: int = 0, dy: int = 0) -> Area:
        """
        Expands the selection from the west-corner by moving the west-corner by the given offset

        Args:
            dx: The amount of offset on the corner1 x-axis to be applied
            dy: The amount of offset on the corner1 y-axis to be applied

        Returns:
            A copy of the area object but expanded from corner1
        """
        corner1, corner2 = self.corners
        corner1 = Tile(corner1.x - dx, corner1.y - dy)

        return Area(corner1, corner2)

    def expand_corner2_by(self, *, dx: int = 0, dy: int = 0) -> Area:
        """
        Expands the selection from the east-corner by moving the east-corner by the given offset

        Args:
            dx: The amount of offset on the corner2 x-axis to be applied
            dy: The amount of offset on the corner2 y-axis to be applied

        Returns:
            A copy of the area object but expanded from corner2
        """
        corner1, corner2 = self.corners
        corner2 = Tile(corner2.x + dx, corner2.y + dy)

        return Area(corner1, corner2)

    def size(self, size: int = None, *, width: int = None, height: int = None) -> Area:
        """
        Sets the selection to a size around the center. Using the same logic as the game for rounding when even numbers
         are used.

        Examples:
            - If the center is ``(4,4)`` and ``size=3`` is given, the selection will become ``((3,3),(5,5))``
            - If the center is ``(4,4)`` and ``width=3`` is given, the selection will become ``((3,4),(5,4))``
            - If the center is ``(4,4)`` and ``width=3,height=5`` is given, the selection will become ``((3,2),(5,6))``

        Args:
            size: The new width and height of the area
            width: The new width (x-axis) of the area, overwrites the size parameter if used
            height: The new height (y-axis) of the area, overwrites the size parameter if used

        Returns:
            A copy of the area object with the new sizes
        """
        center = self.center_tile

        # Ignore the center tile
        new_width = (width or size or self.width) - 1
        new_height = (height or size or self.height) - 1

        corner1 = Tile(center.x - math.ceil(new_width / 2), center.y - math.ceil(new_height / 2))
        corner2 = Tile(center.x + math.floor(new_width / 2), center.y + math.floor(new_height / 2))

        return Area(corner1, corner2)

    def center(self, tile: TileT) -> Area:
        """
        Move the center of the area to the given tile

        Args:
            tile: The tile to center the area on

        Returns:
            A copy of the area object but centered on the given tile
        """
        x, y = tile
        center = self.center_tile
        dx, dy = x - center.x, y - center.y
        (x1, y1), (x2, y2) = self.corners

        return Area((x1 + dx, y1 + dy), (x2 + dx, y2 + dy))

    def bound(self, limit: int) -> Area:
        """
        Update the corners to be bounded between 0 and the given limit

        Args:
            limit: The limit used for bound checks

        Returns:
            A copy of the area object but with bounded corners
        """
        if not self.covers_tiles_within_bounds(limit):
            raise ValueError("Unable to bound area when area does not cover any tiles within given bounds")

        return Area(
            self.corner1.bound(limit),
            self.corner2.bound(limit)
        )

    def covers_tiles_within_bounds(self, limit: int) -> bool:
        """
        If this Area covers tiles that are within bounds. Even if both corners are out of bounds, if those bounds are
        opposite sides, tiles within bounds are still covered.

        Args:
            limit: The limit used for bound checks

        Returns:
            True if the area covers any tiles that are within bounds
        """
        both_below_zero = (self.x1 < 0 or self.y1 < 0) and (self.x2 < 0 or self.y2 < 0)
        both_above_limit = (self.x1 > limit or self.y1 > limit) and (self.x2 > limit or self.y2 > limit)

        return not (both_below_zero or both_above_limit)

    def is_within_bounds(self, bound: int, resolve_negative_coords: bool = False) -> bool:
        """
        If this area is within the bounds of the given limit (allowing negative coordinates)

        Args:
            bound: The limit used for bound checks
            resolve_negative_coords: If negative coordinates should be resolved to wrap to the other side of the map

        Returns:
            True if this tile is within the bounds of the given map_size
        """
        return self.corner1.is_within_bounds(bound, resolve_negative_coords) \
            and self.corner2.is_within_bounds(bound, resolve_negative_coords)

    def contains(self, tile: TileT) -> bool:
        """
        Checks if a tile is within this area

        Args:
            tile: The tile to check

        Returns:
            True if the tile is within this area, False otherwise
        """
        x, y = tile
        return self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2

    def __hash__(self):
        return hash((self.corner1, self.corner2))

    def __iter__(self) -> Iterable[Tile]:
        return iter((self.corner1, self.corner2))

    def __getitem__(self, item: int) -> Tile:
        return (self.corner1, self.corner2)[item]

    def __str__(self) -> str:
        bound_text = '' if self._apply_bounding else ', [No bounding]'

        return f"Area({self.corner1}, {self.corner2}{bound_text})"

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
