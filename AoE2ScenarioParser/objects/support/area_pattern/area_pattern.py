from __future__ import annotations

import copy
import math
import sys
from typing import TYPE_CHECKING, Iterable, Literal, NoReturn, List, Dict
from uuid import UUID

from ordered_set import OrderedSet

from AoE2ScenarioParser.exceptions.asp_exceptions import UnlinkedScenarioError, UnchunkableConfigurationError
from AoE2ScenarioParser.exceptions.asp_warnings import UuidForcedUnlinkWarning
from AoE2ScenarioParser.helper.coordinates import xy_to_i
from AoE2ScenarioParser.helper.printers import warn
from AoE2ScenarioParser.objects.support.area_pattern import AreaState, AreaAttr
from AoE2ScenarioParser.objects.support.area import Area
from AoE2ScenarioParser.objects.support.tile import Tile, TileT
from AoE2ScenarioParser.scenarios.scenario_store import getters

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.data_objects.terrain_tile import TerrainTile
    from AoE2ScenarioParser.scenarios.aoe2_scenario import AoE2Scenario


class AreaPattern:
    _recursion_steps = [Tile(0, -1), Tile(1, 0), Tile(0, 1), Tile(-1, 0)]
    """Values used for recursion steps"""

    def __init__(
            self,
            area: Area | tuple[TileT, TileT] | tuple[TileT] = None,
            corner1: TileT = None,
            corner2: TileT = None,
            map_size: int = None,
            uuid: UUID = None,
    ) -> None:
        """
        Object to easily select and create area_pattern patterns on the map. Uses method chaining for ease of use.

        **Please note**: Setting a ``uuid`` will always overwrite the ``map_size`` attribute, even if it's not ``None``.

        Args:
            area: The area_pattern to make the selection with
            corner1: The location of the left corner
            corner2: The location of the right corner
            map_size: The size of the map this area_pattern object will handle
            uuid: The UUID of the scenario this area_pattern belongs to

        Raises
            ValueError: If insufficient information is provided to create a tile pattern selection
        """
        if all((map_size is None, uuid is None, area is None, corner1 is None)):
            raise ValueError("Cannot create AreaPattern. At least one of map_size, uuid, area or corner1 is required.")

        if isinstance(area, tuple):
            area = Area(*area)

        self.uuid: UUID = uuid
        self._map_size = None
        if uuid:
            self._map_size = getters.get_map_size(uuid)
        if map_size:
            self.map_size = map_size

        if area is None:
            if corner1 is None:
                x = y = self._map_size // 2  # select the centre tile
                corner1 = Tile(x, y)
            if corner2 is None:
                corner2 = corner1
            area = Area(corner1, corner2)

        self.area = area.resolve_negative_coords(self._map_size)
        self.state: AreaState = AreaState.RECT
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
    def from_uuid(cls, uuid: UUID) -> AreaPattern:
        return cls(uuid=uuid)

    @classmethod
    def from_tiles(cls, corner1: TileT, corner2: TileT = None, map_size: int = None) -> AreaPattern:
        return cls(corner1=corner1, corner2=corner2, map_size=map_size)

    # ============================ Properties ============================

    @property
    def map_size(self) -> int:
        if self.uuid is not None:
            return getters.get_map_size(self.uuid) - 1
        if self._map_size is not None:
            return self._map_size
        raise ValueError(
            "No UUID or map_size was set. "
            "Set a map_size or associate with a scenario to use map size related functionality"
        )

    @map_size.setter
    def map_size(self, value: int):
        if self.uuid is not None and value != getters.get_map_size(self.uuid):
            warn(
                "Overriding the map size of a AreaPattern with linked scenario. AreaPattern.uuid was set to None.",
                category=UuidForcedUnlinkWarning
            )
            self.uuid = None
        self._map_size = value

    @property
    def area_bounded(self) -> Area:
        """Get the four values of the selection as: ((x1, y1), (x2, y2))"""
        return self.area.bound(self.map_size)

    # ============================ Conversion functions ============================

    def to_coords(self, as_terrain: bool = False) -> OrderedSet[Tile | TerrainTile]:
        """
        Converts the selection to an OrderedSet of (x, y) coordinates

        Args:
            as_terrain: If the returning coordinates should be Tile objects or Terrain Tiles. If True the coordinates
                are returned as TerrainTiles.

        Returns:
            An OrderedSet of Tiles ((x, y) named tuple) of the selection.

        Raises:
            UnlinkedScenarioError: When as_terrain is set to True, but no scenario is linked with this TerrainTile
                object

        Examples:
            The selection: ``((3,3), (5,5))`` would result in an OrderedSet with a length of 9::

                [
                    (3,3), (4,3)  ...,
                    ...,   ...,   ...,
                    ...,   (4,5), (5,5)
                ]
        """
        if as_terrain and self.uuid is None:
            self._raise_unlinked_scenario_error()

        (x1, y1), (x2, y2) = self.area
        tiles = OrderedSet(
            Tile(x, y)
            for y in range(y1, y2 + 1)
            for x in range(x1, x2 + 1)
            if self.is_within_selection((x, y))
        )
        return self._tiles_to_terrain_tiles(tiles) if as_terrain else tiles

    def to_chunks(
            self,
            as_terrain: bool = False
    ) -> List[OrderedSet[Tile | TerrainTile]]:
        """
        Converts the selection to a list of OrderedSets with Tile NamedTuples with (x, y) coordinates.
        The separation between chunks is based on if they're connected to each other.
        So the tiles must share an edge (i.e. they should be non-diagonal).

        Args:
            as_terrain: If the returning coordinates should be Tile objects or Terrain Tiles. If True the coordinates
                are returned as TerrainTiles.

        Returns:
            A list of OrderedSets of Tiles ((x, y) named tuple) of the selection.

        Raises:
            UnlinkedScenarioError: When as_terrain is set to True, but no scenario is linked with this
                TerrainTile object
            UnchunkableConfigurationError: When a pattern configuration makes the chunk segregation indeterminate
        """
        if as_terrain and self.uuid is None:
            self._raise_unlinked_scenario_error()

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

        map_size = self._map_size
        chunks_ordered: List[OrderedSet[Tile | TerrainTile]] = []
        for chunk_id, chunk_tiles in chunks.items():
            tiles = self._tiles_to_terrain_tiles(chunk_tiles) if as_terrain else chunk_tiles
            chunks_ordered.append(
                OrderedSet(sorted(tiles, key=lambda t: t.y * map_size + t.x))
            )

        return chunks_ordered

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
        self.attrs(line_width=line_width, line_width_x=line_width_x, line_width_y=line_width_y)
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
        self.attrs(corner_size=corner_size, corner_size_x=corner_size_x, corner_size_y=corner_size_y)
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
            block_size=block_size, gap_size=gap_size,
            block_size_x=block_size_x, gap_size_x=gap_size_x,
            block_size_y=block_size_y, gap_size_y=gap_size_y
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
        self.attrs(axis=axis, gap_size=gap_size, line_width=line_width)
        self.state = AreaState.LINES
        return self

    # ============================ Adjustment functions ============================

    def invert(self) -> AreaPattern:
        """
        Inverts the inverted boolean. Causes the `to_coords` to return the inverted selection. (Especially useful for
        the grid state). Not as useful for the edge which would be the same as shrinking the selection. When used with
        the fill state an empty set is returned.

        **Please note:** This inverts the INTERNAL selection. Tiles OUTSIDE the selection will NOT be returned.
        """
        self.inverted = not self.inverted
        return self

    def along_axis(self, axis: Literal["x", "y", "X", "Y"]) -> AreaPattern:
        """Sets the axis. Can be either "x" or "y"."""
        if (lcase_axis := axis.lower()) not in {"x", "y"}:
            raise ValueError(f"The allowed values for axis are 'x' or 'y', given: {axis}")
        self.axis = lcase_axis
        return self

    def attr(self, key: str | AreaAttr, value: int) -> AreaPattern:
        """Sets the attribute to the given value. AreaAttr or str can be used as key"""
        if isinstance(key, AreaAttr):
            key = key.value

        keys: List[str] = [key]
        if key in ['line_width', 'gap_size', 'corner_size', 'block_size']:
            keys = [key + '_x', key + '_y']

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
            This area_pattern object
        """
        for key, value in locals().items():
            if value is None or key == 'self':
                continue
            self.attr(key, value)
        return self

    def size(self, n: int) -> AreaPattern:
        """
        Sets the selection to a size around the center. If center is (4,4) with a size of 3 the selection will become
        ``((3,3), (5,5))``
        """
        center = self.area.center_tile
        n -= 1  # Ignore center tile

        self.area = Area(
            (center.x - math.ceil(n / 2), center.y - math.ceil(n / 2)),
            (center.x + math.floor(n / 2), center.y + math.floor(n / 2)),
        )
        return self

    def height(self, n: int) -> AreaPattern:
        """
        Sets the height (y-axis) of the selection. Shrinks/Expands both sides equally.
        If the expansion hits the edge of the map, it'll expand on the other side.
        """
        corner1, corner2 = self.area
        center = self.area.center_tile
        n -= 1  # Ignore center tile
        self.area = Area(
            (corner1.x, center.y - math.ceil(n / 2)),
            (corner2.x, center.y + math.floor(n / 2)),
        )
        return self

    def width(self, n: int) -> AreaPattern:
        """
        Sets the width (x-axis) of the selection. Shrinks/Expands both sides equally.
        If the expansion hits the edge of the map, it'll expand on the other side.
        """
        corner1, corner2 = self.area
        center = self.area.center_tile
        n -= 1  # Ignore center tile

        self.area = Area(
            (center.x - math.ceil(n / 2), corner1.y),
            (center.x + math.floor(n / 2), corner2.y),
        )
        return self

    def cut_overflow(self) -> AreaPattern:
        """
        If the area_pattern selection is off the map, shrink the area_pattern to fit inside the map
        """
        self.area = self.area.bound(self.map_size)
        return self

    def shift_overflow(self) -> AreaPattern:
        """
        If the area_pattern selection is off the map, shift the excess area_pattern inside the map without shrinkage
        """
        # first get a new area_pattern object with the excess tiles cut out, then check
        # how many extra tiles need to be re-added.
        # Re-add that many tiles to both sides of the new area_pattern and then
        # just cut the excess off again to get the shifted version of the old area_pattern

        new_area = self.area.bound(self.map_size)
        diff_width = self.area.width - new_area.width
        diff_height = self.area.height - new_area.height
        self.area = Area(
            (new_area.corner1.x - diff_width, new_area.corner1.y - diff_height),
            (new_area.corner2.x + diff_width, new_area.corner2.y + diff_height),
        ).bound(self._map_size)
        return self

    def center(self, tile: TileT) -> AreaPattern:
        """
        Moves the selection center to a given position while retaining the old width/height
        """
        x, y = tile
        center = self.area.center_tile
        dx, dy = x - center.x, y - center.y
        (x1, y1), (x2, y2) = self.area
        self.area = Area(
            (x1+dx, y1+dy),
            (x2+dx, y2+dy),
        )
        return self

    def select_entire_map(self) -> AreaPattern:
        """Sets the selection to the entire map"""
        self.area = Area(
            (0, 0),
            (self.map_size, self.map_size),
        )
        return self

    def select(self, corner1: TileT, corner2: TileT = None) -> AreaPattern:
        """Sets the selection to the given coordinates"""
        if corner2 is None:
            corner2 = corner1
        corner1 = Tile(*corner1)
        corner2 = Tile(*corner2)
        self.area = Area(
            corner1.resolve_negative_coords(self._map_size),
            corner2.resolve_negative_coords(self._map_size),
        )
        return self

    def select_centered(self, tile: TileT, *, dx: int = 1, dy: int = 1) -> AreaPattern:
        """Sets the selection to the given coordinates"""
        self.center(tile).width(dx).height(dy)
        return self

    def shrink(self, n: int) -> AreaPattern:
        """Shrinks the selection from all sides"""
        self.shrink_bottom_corner_by(dx=n, dy=n)
        self.shrink_top_corner_by(dx=n, dy=n)
        return self

    def shrink_bottom_corner_by(self, *, dx: int = 0, dy: int = 0) -> AreaPattern:
        """Shrinks the selection from the bottom corner by shifting the bottom corner up by (dx, dy)"""
        corner1, corner2 = self.area
        self.area.corner1 = Tile(
            min(corner1.x + dx, corner2.x),
            min(corner1.y + dy, corner2.y),
        )
        return self

    def shrink_top_corner_by(self, *, dx: int = 0, dy: int = 0) -> AreaPattern:
        """Shrinks the selection from the top corner by shifting the bottom corner down by (dx, dy)"""
        corner1, corner2 = self.area
        self.area.corner2 = Tile(
            max(corner1.x, corner2.x - dx),
            max(corner1.y, corner2.y - dy),
        )
        return self

    def expand(self, n: int) -> AreaPattern:
        """Expands the selection from all sides"""
        self.expand_bottom_corner_by(dx=n, dy=n)
        self.expand_top_corner_by(dx=n, dy=n)
        return self

    def expand_bottom_corner_by(self, *, dx: int = 0, dy: int = 0) -> AreaPattern:
        """Expands the selection from the bottom corner by shifting the bottom corner down by (dx, dy)"""
        corner1 = self.area.corner1
        self.area.corner1 = Tile(
            max(0, corner1.x - dx),
            max(0, corner1.y - dy),
        )
        return self

    def expand_top_corner_by(self, *, dx: int = 0, dy: int = 0) -> AreaPattern:
        """Expands the selection from the top corner by shifting the bottom corner up by (dx, dy)"""
        corner2 = self.area.corner2
        self.area.corner2 = Tile(
            min(corner2.x + dx, self._map_size or sys.maxsize),
            min(corner2.y + dy, self._map_size or sys.maxsize),
        )
        return self

    # ============================ Test against ... functions ============================

    def is_within_selection(self, tile: TileT) -> bool:
        """
        If a given (x, y) location is within the selection.

        Args:
            tile: The location to check

        Returns:
            True if (x, y) is within the selection, False otherwise
        """
        if not self.area.contains(tile):
            return False

        return any((
            self.state == AreaState.RECT,
            self.state == AreaState.EDGE and self._is_on_edge(tile),
            self.state == AreaState.GRID and self._is_in_grid(tile),
            self.state == AreaState.LINES and self._is_on_line(tile),
            self.state == AreaState.CORNERS and self._is_in_corner(tile),
        )) ^ self.inverted

    # ============================ Miscellaneous functions ============================

    def copy(self) -> AreaPattern:
        """
        Copy this instance of an Area. Useful for when you want to do multiple extractions (to_...) from the same source
        with small tweaks.

        Examples:

            Get a grid and the surrounding edge::

                area_pattern = Area.select(10,10,20,20)
                edge = area_pattern.copy().expand(1).use_only_edge().to_coords()
                # Without copy you'd have to undo all changes above. In this case that'd be: `.shrink(1)`
                grid = area_pattern.use_pattern_grid().to_coords()

        Returns:
            A copy of this Area object
        """
        return copy.copy(self)

    def link_scenario(self, scenario: AoE2Scenario) -> AreaPattern:
        """
        Link pattern with scenario. Saves scenario UUID in this tile object and update the map size

        Args:
            scenario: The scenario to link with
        """
        self.uuid = scenario.uuid
        self.map_size = getters.get_map_size(self.uuid)
        return self

    # ============================ Support functions ============================

    def _raise_unlinked_scenario_error(self) -> NoReturn:
        """Raises the UnlinkedScenarioError exception"""
        raise UnlinkedScenarioError(
            "No scenario is associated with this AreaPattern object, cannot get coordinates as terrain"
        )

    def _is_on_edge(self, tile: TileT) -> bool:
        """Returns if a given tile (x, y) is an edge tile of the set selection given a certain edge width."""
        x, y = tile
        corner1, corner2 = self.area
        return any((
            0 <= x - corner1.x < self.line_width_x,
            0 <= corner2.x - x < self.line_width_x,
            0 <= y - corner1.y < self.line_width_y,
            0 <= corner2.y - y < self.line_width_y,
        ))

    def _is_in_corner(self, tile: TileT) -> bool:
        """If a given (x, y) location is a corner tile."""
        x, y = tile
        corner1, corner2 = self.area
        return all((
            any((
                0 <= x - corner1.x < self.corner_size_x,
                0 <= corner2.x - x < self.corner_size_x,
            )),
            any((
                0 <= y - corner1.y < self.corner_size_y,
                0 <= corner2.y - y < self.corner_size_y,
            ))
        ))

    def _is_in_grid(self, tile: TileT) -> bool:
        """If a given (x, y) location is within the grid selection."""
        x, y = tile
        corner1, _ = self.area
        return all((
            (x - corner1.x) % (self.block_size_x + self.gap_size_x) < self.block_size_x,
            (y - corner1.y) % (self.block_size_y + self.gap_size_y) < self.block_size_y,
        ))

    def _is_on_line(self, tile: TileT) -> bool:
        """If a given (x, y) location is within the grid selection."""
        x, y = tile
        corner1, _ = self.area
        if self.axis == "x":
            return (y - corner1.y) % (self.gap_size_y + self.line_width_y) < self.line_width_y
        return (x - corner1.x) % (self.gap_size_x + self.line_width_x) < self.line_width_x

    def _tiles_to_terrain_tiles(self, tiles: Iterable[Tile]) -> OrderedSet[TerrainTile]:
        """
        Converts the selection to an OrderedSet of terrain tile objects from the map manager.
        Can only be used if the area_pattern has been associated with a scenario.

        Returns:
            An OrderedSet of terrain tiles from the map manager based on the selection.
        """
        map_size = self.map_size
        terrain = getters.get_terrain(self.uuid)
        return OrderedSet(terrain[xy_to_i(x, y, map_size + 1)] for (x, y) in tiles)

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

    def __repr__(self) -> str:
        return f"AreaPattern(area_pattern={self.area}, state={self.state.name})"

    def __iter__(self):
        return self.to_coords()