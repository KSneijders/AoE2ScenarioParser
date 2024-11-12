from __future__ import annotations

import copy
import math
from typing import Callable, Dict, List, Literal, TYPE_CHECKING

from ordered_set import OrderedSet

from AoE2ScenarioParser.exceptions.asp_exceptions import UnchunkableConfigurationError
from AoE2ScenarioParser.helper.coordinates import xy_to_i
from AoE2ScenarioParser.objects.support.area import Area
from AoE2ScenarioParser.objects.support.area_pattern import AreaAttr, AreaState
from AoE2ScenarioParser.objects.support.enums.direction import Direction
from AoE2ScenarioParser.objects.support.tile import Tile
from AoE2ScenarioParser.objects.support.tile_sequence import TileSequence
from AoE2ScenarioParser.objects.support.typedefs import AreaT, T, TileT

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.data_objects.terrain_tile import TerrainTile


class AreaPattern(TileSequence):
    _recursion_steps = [Tile(0, -1), Tile(1, 0), Tile(0, 1), Tile(-1, 0)]
    """Values used for recursion steps"""

    def __init__(
        self,
        area: AreaT = None,
        corner1: TileT = None,
        corner2: TileT = None,
        map_size: int = None,
    ) -> None:
        """
        Object to easily select and create area_pattern patterns on the map. Uses method chaining for ease of use.

        Args:
            area: The area_pattern to make the selection with
            corner1: The location of the west corner
            corner2: The location of the east corner
            map_size: The size of the map this AreaPattern object will handle

        Raises:
            ValueError: If insufficient information is provided to create a AreaPattern selection
        """
        if all((map_size is None, area is None, corner1 is None)):
            raise ValueError("Cannot create AreaPattern. At least one of [map_size], [area] or [corner1] is required.")
        if area is not None and (corner1 is not None or corner2 is not None):
            raise ValueError("Cannot create AreaPattern with both [area] and [corner<x>]")

        if area is None:
            if corner1 is None:
                x = y = map_size // 2  # select the centre tile
                corner1 = Tile(x, y)
            if corner2 is None:
                corner2 = corner1
            area = Area(corner1, corner2)
        else:
            area = Area.from_value(area)

        # Configs
        self.shift_bounds_on_set: bool = False

        self.map_size = map_size

        self.area: Area = area.resolve_negative_coords(map_size)
        self.state: AreaState = AreaState.RECT

        # Attributes
        self.inverted: bool = False

        self.gap_size_x: int = 1
        self.gap_size_y: int = 1
        self.line_width_x: int = 1
        self.line_width_y: int = 1
        self.block_size_x: int = 1
        self.block_size_y: int = 1

        self.axis: str = "x"

        self.corner_size_x: int = 1
        self.corner_size_y: int = 1

    # ============================ Class methods ============================

    @classmethod
    def from_tiles(cls, corner1: TileT, corner2: TileT = None, map_size: int = None) -> AreaPattern:
        return cls(corner1 = corner1, corner2 = corner2, map_size = map_size)

    # ============================ Properties ============================

    @property
    def map_size(self) -> int:
        if self._map_size is None:
            raise ValueError(
                "No map size was configured for this AreaPattern. "
                "Unable to use this functionality without setting a map_size"
            )
        return self._map_size

    @map_size.setter
    def map_size(self, value: int | None) -> None:
        self._map_size = max(1, value) if value is not None else None

    @property
    def area(self) -> Area:
        return self._area

    @area.setter
    def area(self, area: Area):
        if self._map_size:
            if self.shift_bounds_on_set:
                area = self._shift_area_bounds(area)
            else:
                area = area.bound(self.maximum_coordinate)

        # Set the area object to not manage bounding
        area._apply_bounding = False
        self._area = area

    @property
    def maximum_coordinate(self) -> int:
        """Get the highest possible coordinate for the current map (based on the size)"""
        return self.map_size - 1

    @property
    def area_bounded(self) -> Area:
        """Get the four values of the selection as: ((x1, y1), (x2, y2))"""
        return self.area.bound(self.maximum_coordinate)

    # ============================ Conversion functions ============================

    def to_coords(self) -> OrderedSet[Tile]:
        """Alias for ``to_tiles()``"""
        return self.to_tiles()

    def to_tiles(self) -> OrderedSet[Tile]:
        """
        Converts the chosen pattern to an OrderedSet of Tile objects

        Returns:
            An OrderedSet of Tile objects of the chosen pattern

        Examples:
            The selection: ``((3,3), (5,5))`` would result in an OrderedSet with a length of 9::

                [
                    (3,3), (4,3)  ...,
                    ...,   ...,   ...,
                    ...,   (4,5), (5,5)
                ]
        """
        return OrderedSet(
            Tile(x, y)
                for y in self.area.height_range
                for x in self.area.width_range
                if self.is_within_selection((x, y))
        )

    def to_chunks(self) -> List[OrderedSet[Tile]]:
        """
        Converts the selection to a list of OrderedSets with Tile NamedTuples with (x, y) coordinates.
        The separation between chunks is based on if they're connected to each other.
        So the tiles must share an edge (i.e. they should be non-diagonal).

        Returns:
            A list of OrderedSets of Tile objects of the selection.

        Raises:
            UnchunkableConfigurationError: When a pattern configuration makes the chunk segregation indeterminate
        """
        tiles = self.to_coords()

        # Shortcut for states that CANNOT be more than one chunk
        if not self.state.is_chunkable():
            return [tiles]

        chunks: Dict[int, List[Tile]] = {}
        for tile in tiles:
            chunk_id = self._get_chunk_id(tile)
            if chunk_id == -1:
                raise UnchunkableConfigurationError(
                    f"Invalid pattern configuration for getting the Chunk ID. If you believe this is an error, "
                    f"please raise an issue on github or in the Discord server"
                )
            chunks.setdefault(chunk_id, []).append(tile)

        map_size = self.map_size
        chunks_ordered: List[OrderedSet[Tile | TerrainTile]] = []
        for chunk_id, chunk_tiles in chunks.items():
            chunks_ordered.append(
                OrderedSet(sorted(chunk_tiles, key = lambda t: xy_to_i(t.x, t.y, map_size)))
            )

        return chunks_ordered

    def map(self, callback: Callable[[Tile], T]) -> dict[Tile, T]:
        """
        Map every tile inside this area pattern. Applies the given callable to every tile in this pattern.
        Returns as a dict where the tile used in the callback is the key

        Args:
            callback: The callable to be applied to every tile

        Returns:
            A dict containing `{key: <return of callable>}` for each tile in this pattern
        """
        return {
            tile: callback(tile) for tile in self.to_coords()
        }

    # ============================ Use functions ============================

    def use_full(self) -> AreaPattern:
        """Sets the area_pattern object to use the entire selection"""
        self.state = AreaState.RECT
        return self

    def use_only_edge(self, line_width: int = None, line_width_x: int = None, line_width_y: int = None) -> AreaPattern:
        """
        Sets the area_pattern object to only use the edge of the selection

        Args:
            line_width: The width of the x & y edge line
            line_width_x: The width of the x edge line
            line_width_y: The width of the y edge line

        Returns:
            This area_pattern object
        """
        self.attrs(line_width = line_width, line_width_x = line_width_x, line_width_y = line_width_y)
        self.state = AreaState.EDGE
        return self

    def use_only_corners(
        self,
        corner_size: int = None,
        corner_size_x: int = None,
        corner_size_y: int = None
    ) -> AreaPattern:
        """
        Sets the area_pattern object to only use the corners pattern within the selection.

        Args:
            corner_size: The size along both the x and y-axis of the corner areas
            corner_size_x: The size along the x-axis of the corner areas
            corner_size_y: The size along the y-axis of the corner areas

        Returns:
            This area_pattern object
        """
        self.attrs(corner_size = corner_size, corner_size_x = corner_size_x, corner_size_y = corner_size_y)
        self.state = AreaState.CORNERS
        return self

    def use_pattern_grid(
        self,
        block_size: int = None,
        gap_size: int = None,
        block_size_x: int = None,
        block_size_y: int = None,
        gap_size_x: int = None,
        gap_size_y: int = None
    ) -> AreaPattern:
        """
        Sets the area_pattern object to use a grid pattern within the selection.

        Args:
            block_size: The size of the gaps between lines
            gap_size: The width of the grid lines
            block_size_x: The size of the x gaps between lines
            block_size_y: The size of the y gaps between lines
            gap_size_x: The width of the x grid lines
            gap_size_y: The width of the y grid lines

        Returns:
            This area_pattern object
        """
        self.attrs(
            block_size = block_size, gap_size = gap_size,
            block_size_x = block_size_x, gap_size_x = gap_size_x,
            block_size_y = block_size_y, gap_size_y = gap_size_y
        )
        self.state = AreaState.GRID
        return self

    def use_pattern_lines(self, axis: str = None, gap_size: int = None, line_width: int = None) -> AreaPattern:
        """
        Sets the area_pattern object to use a lines pattern within the selection.

        Args:
            axis: The axis the lines should follow. Can either be "x" or "y"
            gap_size: The size of the gaps between lines
            line_width: The width of the x & y lines

        Returns:
            This area_pattern object
        """
        if axis is not None:
            axis = axis.lower()
        self.attrs(axis = axis, gap_size = gap_size, line_width = line_width)
        self.state = AreaState.LINES
        return self

    # ============================ Adjustment functions ============================

    def invert(self) -> AreaPattern:
        """
        Inverts the inverted boolean. Causes the `to_coords` to return the inverted selection. (Especially useful for
        the grid state). Not as useful for the edge which would be the same as shrinking the selection using full state.
        When used with the full state an empty set is returned.

        **Please note:** This inverts the INTERNAL selection. Tiles OUTSIDE the selection will NOT be returned.
        """
        self.inverted = not self.inverted
        return self

    def along_axis(self, axis: Literal["x", "y", "X", "Y"]) -> AreaPattern:
        """Sets the axis. Can be either "x" or "y"."""
        if (lcase_axis := axis.lower()) not in ["x", "y"]:
            raise ValueError(f"The allowed values for axis are 'x' or 'y', given: {axis}")
        self.axis = lcase_axis
        return self

    def attr(self, key: str | AreaAttr, value: int) -> AreaPattern:
        """Sets the attribute to the given value. AreaAttr or str can be used as key"""
        if isinstance(key, AreaAttr):
            key: str = key.value

        if key in ['line_width', 'gap_size', 'corner_size', 'block_size']:
            keys = [key + '_x', key + '_y']
        else:
            keys = [key]

        for key in keys:
            setattr(self, key, value)
        return self

    def attrs(
        self,
        x1: int = None,
        y1: int = None,
        x2: int = None,
        y2: int = None,
        gap_size: int = None,
        gap_size_x: int = None,
        gap_size_y: int = None,
        line_width: int = None,
        line_width_x: int = None,
        line_width_y: int = None,
        axis: str = None,
        corner_size: int = None,
        corner_size_x: int = None,
        corner_size_y: int = None,
        block_size: int = None,
        block_size_x: int = None,
        block_size_y: int = None,
    ) -> AreaPattern:
        """
        Sets multiple attributes to the corresponding values.

        Returns:
            This AreaPattern object
        """
        for key, value in locals().items():
            if value is None or key == 'self':
                continue
            self.attr(key, value)
        return self

    # ============================ Forwarded Area functions ============================

    def move(self, x_offset: int = 0, y_offset: int = 0):
        """
        Moves the selection by the given offsets

        Args:
            x_offset: The amount to move the selection on the x-axis (West to East)
            y_offset: The amount to move the selection on the y-axis (North to South)

        Returns:
            This AreaPattern object with the underlying area adjusted accordingly
        """
        self.area = self.area.move(x_offset, y_offset)

        return self

    def move_to(self, tile: TileT, corner: Direction):
        """
        Moves the selection to the given coordinate by placing the given corner of this area on the coordinate.

        For center placement, use ``.center(...)``

        Args:
            corner: The corner used to align the selection onto the given tile
            tile: The coordinate to place the selection onto

        Returns:
            This AreaPattern object with the underlying area adjusted accordingly
        """
        self.area = self.area.move_to(tile, corner)

        return self

    def shrink(self, n: int) -> AreaPattern:
        """
        Shrinks the selection by the given amount of tiles from all sides

        Args:
            n: The amount of tiles to shrink

        Returns:
            This AreaPattern object with the underlying area adjusted accordingly
        """
        self.area = self.area.shrink(n)

        return self

    def shrink_corner1_by(self, *, dx: int = 0, dy: int = 0) -> AreaPattern:
        """
        Shrinks the selection from the west-corner by moving the west-corner by the given offset

        Args:
            dx: The amount of offset on the corner1 x-axis to be applied
            dy: The amount of offset on the corner1 y-axis to be applied

        Returns:
            This AreaPattern object with the underlying area adjusted accordingly
        """
        self.area = self.area.shrink_corner1_by(dx = dx, dy = dy)

        return self

    def shrink_corner2_by(self, *, dx: int = 0, dy: int = 0) -> AreaPattern:
        """
        Shrinks the selection from the east-corner by moving the east-corner by the given offset

        Args:
            dx: The amount of offset on the corner2 x-axis to be applied
            dy: The amount of offset on the corner2 y-axis to be applied

        Returns:
            This AreaPattern object with the underlying area adjusted accordingly
        """
        self.area = self.area.shrink_corner2_by(dx = dx, dy = dy)

        return self

    def expand(self, n: int) -> AreaPattern:
        """
        Expands the selection by the given amount of tiles from all sides

        Args:
            n: The amount of tiles to expand

        Returns:
            This AreaPattern object with the underlying area adjusted accordingly
        """
        self.area = self.area.expand(n)

        return self

    def expand_corner1_by(self, *, dx: int = 0, dy: int = 0) -> AreaPattern:
        """
        Expands the selection from the west-corner by moving the west-corner by the given offset

        Args:
            dx: The amount of offset on the corner1 x-axis to be applied
            dy: The amount of offset on the corner1 y-axis to be applied

        Returns:
            This AreaPattern object with the underlying area adjusted accordingly
        """
        self.area = self.area.expand_corner1_by(dx = dx, dy = dy)

        return self

    def expand_corner2_by(self, *, dx: int = 0, dy: int = 0) -> AreaPattern:
        """
        Expands the selection from the east-corner by moving the east-corner by the given offset

        Args:
            dx: The amount of offset on the corner2 x-axis to be applied
            dy: The amount of offset on the corner2 y-axis to be applied

        Returns:
            This AreaPattern object with the underlying area adjusted accordingly
        """
        self.area = self.area.expand_corner2_by(dx = dx, dy = dy)

        return self

    def size(self, size: int = None, *, width: int = None, height: int = None) -> AreaPattern:
        """
        Sets the selection to a size around the center.
        If center is (4,4) and ``size=3`` is given, the selection will become ``((3,3), (5,5))``.
        If area is ((4,4), (4,4)) and ``width=3`` is given, the selection will become ``((3,4), (5,4))``

        Args:
            size: The new width and height of the area
            width: The new width (x-axis) of the area, overwrites the size parameter if used
            height: The new height (y-axis) of the area, overwrites the size parameter if used

        Returns:
            This AreaPattern object with the underlying area adjusted accordingly
        """
        self.area = self.area.size(size, width = width, height = height)

        return self

    # Todo: Move tests to area tests
    def center(self, tile: TileT) -> AreaPattern:
        """
        Move the center of the area to the given tile

        Args:
            tile: The tile to center the area on

        Returns:
            This AreaPattern object with the underlying area adjusted accordingly
        """
        self.area = self.area.center(tile)

        return self

    def select_entire_map(self) -> AreaPattern:
        """Sets the selection to the entire map"""
        self.area = Area(
            (0, 0),
            (self.maximum_coordinate, self.maximum_coordinate),
        )

        return self

    def select(self, corner1: TileT, corner2: TileT = None) -> AreaPattern:
        """Sets the selection to the given coordinates"""
        if corner2 is None:
            corner2 = corner1

        corner1 = Tile.from_value(corner1).resolve_negative_coords(self.map_size)
        corner2 = Tile.from_value(corner2).resolve_negative_coords(self.map_size)

        self.area = Area(corner1, corner2)

        return self

    def select_centered(self, tile: TileT, *, dx: int = 1, dy: int = 1) -> AreaPattern:
        """Sets the selection to the given coordinates"""
        self.area = self.area.center(tile).size(width = dx, height = dy)

        return self

    # ============================ Config functions ============================

    def cut_bounds(self) -> AreaPattern:
        """
        If the Area selection is (partially) outside the map, shrink the area to fit inside the map

        Returns:
            This AreaPattern object with the underlying area adjusted accordingly
        """
        self.shift_bounds_on_set = False

        return self

    def shift_bounds(self) -> AreaPattern:
        """
        If the Area selection is (partially) outside the map, shift the overflowing area to fit inside the map without
        changing the area dimensions.

        Returns:
            This AreaPattern object with the underlying area adjusted accordingly
        """
        self.shift_bounds_on_set = True

        return self

    # ============================ Test against ... functions ============================

    def is_within_selection(self, tile: TileT) -> bool:
        """
        If a given ``(x, y)`` location is within the selection.

        Args:
            tile: The location to check

        Returns:
            ``True`` if (x, y) is within the selection, ``False`` otherwise
        """
        if not self.area.contains(tile):
            return False

        return any(
            (
                self.state == AreaState.RECT,
                self.state == AreaState.EDGE and self._is_on_edge(tile),
                self.state == AreaState.GRID and self._is_in_grid(tile),
                self.state == AreaState.LINES and self._is_on_line(tile),
                self.state == AreaState.CORNERS and self._is_in_corner(tile),
            )
        ) ^ self.inverted

    # ============================ Miscellaneous functions ============================

    def copy(self) -> AreaPattern:
        """
        Copy this instance of an Area. Useful for when you want to do multiple extractions (to_...) from the same source
        with small tweaks.

        Examples:

            area_pattern = AreaPattern((10,10), (20,20))
            edge = area_pattern.copy().expand(1).use_only_edge().to_coords()

            # Without copy you'd have to undo the changes above.
            # Which, in this case would be: `.shrink(1)`
            grid = area_pattern.use_pattern_grid().to_coords()

        Returns:
            A copy of this AreaPattern object
        """
        return copy.copy(self)

    # ============================ Support functions ============================

    def _is_on_edge(self, tile: TileT) -> bool:
        """Returns if a given tile (x, y) is an edge tile of the set selection given a certain edge width."""
        x, y = tile
        corner1, corner2 = self.area
        return any(
            (
                0 <= x - corner1.x < self.line_width_x,
                0 <= corner2.x - x < self.line_width_x,
                0 <= y - corner1.y < self.line_width_y,
                0 <= corner2.y - y < self.line_width_y,
            )
        )

    def _is_in_corner(self, tile: TileT) -> bool:
        """If a given (x, y) location is a corner tile."""
        x, y = tile
        corner1, corner2 = self.area
        return all(
            (
                any(
                    (
                        0 <= x - corner1.x < self.corner_size_x,
                        0 <= corner2.x - x < self.corner_size_x,
                    )
                ),
                any(
                    (
                        0 <= y - corner1.y < self.corner_size_y,
                        0 <= corner2.y - y < self.corner_size_y,
                    )
                )
            )
        )

    def _is_in_grid(self, tile: TileT) -> bool:
        """If a given (x, y) location is within the grid selection."""
        x, y = tile
        corner1, _ = self.area
        return all(
            (
                (x - corner1.x) % (self.block_size_x + self.gap_size_x) < self.block_size_x,
                (y - corner1.y) % (self.block_size_y + self.gap_size_y) < self.block_size_y,
            )
        )

    def _is_on_line(self, tile: TileT) -> bool:
        """If a given (x, y) location is within the grid selection."""
        x, y = tile
        corner1, _ = self.area
        if self.axis == "x":
            return (y - corner1.y) % (self.gap_size_y + self.line_width_y) < self.line_width_y
        return (x - corner1.x) % (self.gap_size_x + self.line_width_x) < self.line_width_x

    def _calc_grid_chunk_id(self, tile: TileT):
        """
        Grid chunk ID is which "block of tiles" the given tile is in, starting from the top left (visually, the west
        corner on the minimap) and increasing moving down right (the east corner on the minimap)
        """
        if self.inverted:
            return 0

        corner1, _ = self.area
        (x, y) = tile

        per_row = math.ceil(self.area.height / (self.block_size_x + self.gap_size_x))
        return (
            (x - corner1.x) // (self.block_size_x + self.gap_size_x)
            + (y - corner1.y) // (self.block_size_y + self.gap_size_y) * per_row
        )

    def _calc_line_chunk_id(self, tile: TileT) -> int:
        """
        Line chunk ID is which "line of tiles" the given tile is on, starting from the top/left (visually, the west
        corner on the minimap) and increasing moving down/right (the east corner on the minimap)
        """
        corner1, _ = self.area
        (x, y) = tile

        if self.axis == "x":
            return (y - corner1.y) // (self.line_width_y + self.gap_size_y)
        return (x - corner1.x) // (self.line_width_x + self.gap_size_x)

    def _calc_corner_chunk_id(self, tile: TileT) -> int:
        """
        Corner chunk ID is which "corner of tiles" the given tile is on, starting from the top left (visually, the west
        corner on the minimap) and increasing clockwise
        """
        x, y = tile
        corner1, corner2 = self.area

        if 0 <= x - corner1.x < self.corner_size_x and 0 <= y - corner1.y < self.corner_size_y:
            return 0
        if 0 <= corner2.x - x < self.corner_size_x and 0 <= y - corner1.y < self.corner_size_y:
            return 1
        if 0 <= corner2.x - x < self.corner_size_x and 0 <= corner2.y - y < self.corner_size_y:
            return 2
        if 0 <= x - corner1.x < self.corner_size_x and 0 <= corner2.y - y < self.corner_size_y:
            return 3
        return -1

    def _get_chunk_id(self, tile: TileT) -> int:
        """
        This function gets the Chunk id of a tile based on the current state and configs. The chunk ID identifies which
        chunk the given tile is in. This is useful for separating chunks that are connected but shouldn't be in the same
        chunk (like when creating a checker or stripe pattern)

        Args:
            tile: The tile to check as Tile object

        Returns:
            The int ID of the chunk, or, -1 when it's not in a selection, or 0 when the selection cannot be split into
                chunks.
        """
        if not self.is_within_selection(tile):
            return -1
        if not self.state.is_chunkable():
            return 0
        if self.state == AreaState.GRID:
            return self._calc_grid_chunk_id(tile)
        if self.state == AreaState.LINES:
            return self._calc_line_chunk_id(tile)
        if self.state == AreaState.CORNERS:
            return self._calc_corner_chunk_id(tile)
        return -1

    def _shift_area_bounds(self, area: Area) -> Area:
        """
        If the Area selection is (partially) outside the map, shift the overflowing area to fit inside the map without
        changing the area dimensions.

        Returns:
            This AreaPattern object with the underlying area adjusted accordingly
        """
        new_area = area.bound(self.maximum_coordinate)

        diff_width = area.width - new_area.width
        diff_height = area.height - new_area.height

        corner1 = Tile(new_area.corner1.x - diff_width, new_area.corner1.y - diff_height)
        corner2 = Tile(new_area.corner2.x + diff_width, new_area.corner2.y + diff_height)

        return Area(corner1, corner2).bound(self.maximum_coordinate)

    def __repr__(self) -> str:
        return f"AreaPattern(area_pattern={self.area}, state={self.state.name})"

    def __iter__(self):
        return self.to_coords()
