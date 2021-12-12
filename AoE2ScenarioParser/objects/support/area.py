from __future__ import annotations

import copy
import math
from enum import Enum
from typing import Dict, Union, NamedTuple, TYPE_CHECKING, Set, List, Tuple
from uuid import UUID

from AoE2ScenarioParser.external.ordered_set import OrderedSet
from AoE2ScenarioParser.helper.helper import xy_to_i
from AoE2ScenarioParser.scenarios.scenario_store import getters

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.data_objects.terrain_tile import TerrainTile
    from AoE2ScenarioParser.scenarios.aoe2_scenario import AoE2Scenario


class AreaState(Enum):
    """Enum to show the state of the Area object"""
    FULL = 0
    EDGE = 1
    GRID = 2
    LINES = 3
    CORNERS = 4


class AreaAttr(Enum):
    """Enum to show the supported attributes that can be edited using ``Area.attr(k, v)``"""
    X1 = "x1"
    Y1 = "y1"
    X2 = "x2"
    Y2 = "y2"
    LINE_GAP = "line_gap"
    LINE_WIDTH = "line_width"
    LINE_GAP_X = "line_gap_x"
    LINE_GAP_Y = "line_gap_y"
    LINE_WIDTH_X = "line_width_x"
    LINE_WIDTH_Y = "line_width_y"
    AXIS = "axis"
    CORNER_SIZE = "corner_size"
    CORNER_SIZE_X = "corner_size_x"
    CORNER_SIZE_Y = "corner_size_y"


class Tile(NamedTuple):
    """NamedTuple for tiles. use tile.x or tile.y for coord access"""
    x: int
    y: int


class Area:
    def __init__(self, map_size: int = None, uuid: UUID = None) -> None:
        """
        Object to easily select an area on the map. Uses method chaining for ease of use.

        **Please note**: Setting a ``uuid`` will always overwrite the ``map_size`` attribute, even if it's not ``None``.

        Args:
            map_size (int): The size of the map this area object will handle
            uuid (UUID): The UUID of the scenario this area belongs to
        """
        if map_size is None and uuid is None:
            raise ValueError("Cannot create area object without knowing the map size or a UUID from a scenario.")
        super().__init__()

        self.uuid: UUID = uuid
        if uuid is None:
            self._map_size_value = map_size - 1

        self.state: AreaState = AreaState.FULL
        self.inverted: bool = False

        center = math.floor(self._map_size / 2)
        self.x1: int = center
        self.y1: int = center
        self.x2: int = center
        self.y2: int = center

        self.line_gap_x: int = 1
        self.line_gap_y: int = 1
        self.line_width_x: int = 1
        self.line_width_y: int = 1

        self.axis: str = ""

        self.corner_size_x: int = 1
        self.corner_size_y: int = 1

    @classmethod
    def from_uuid(cls, uuid: UUID) -> Area:
        return cls(uuid=uuid)

    @property
    def _map_size(self) -> int:
        if self.uuid is not None:
            return getters.get_map_size(self.uuid) - 1
        else:
            return self._map_size_value

    def associate_scenario(self, scenario: AoE2Scenario) -> None:
        """
        Associate area with scenario. Saves scenario UUID in this area object.

        Args:
            scenario (AoE2Scenario): The scenario to associate with
        """
        self.uuid = scenario.uuid

    def _force_association(self):
        """Raise ValueError if UUID is not set"""
        if self.uuid is None:
            raise ValueError("Area object not associated with scenario. Cannot request terrain information")

    # ============================ Conversion functions ============================

    def to_coords(self) -> OrderedSet[Tile]:
        """
        Converts the selection to an OrderedSet of (x, y) coordinates

        Returns:
            An OrderedSet of (x, y) tuples of the selection.

        Examples:
            The selection: ``((3,3), (5,5))`` would result in an OrderedSet with a length of 9::

                [
                    (3,3), (4,3)  ...,
                    ...,   ...,   ...,
                    ...,   (4,5), (5,5)
                ]
        """
        return OrderedSet(
            Tile(x, y) for y in self.get_range_y() for x in self.get_range_x() if self.is_within_selection(x, y)
        )

    def to_terrain_tiles(self) -> OrderedSet['TerrainTile']:
        """
        Converts the selection to an OrderedSet of terrain tile objects from the map manager.
        Can only be used if the area has been associated with a scenario (created through map manager)

        Returns:
            An OrderedSet of terrain tiles from the map manager based on the selection.
        """
        self._force_association()
        terrain = getters.get_terrain(self.uuid)
        return OrderedSet(terrain[xy_to_i(x, y, self._map_size + 1)] for (x, y) in self.to_coords())

    def to_dict(self) -> Dict[str, int]:
        """
        Converts the 2 corners of the selection to area keys for use in effects etc.
        This can be used by adding double stars (**) before this function.

        Returns:
            A dict with area_x1, area_y1, area_x2, area_y2 as keys and their respective values.

        Examples:
            The selection: ``((3,3), (5,5))`` would result in a dict that looks like:
                ``{'area_x1': 3, 'area_y1': 3, 'area_x2': 5, 'area_y2': 5}``
            Usage: ``**area.to_dict()`` (i.e. in a ``new_effect.something`` function)
        """
        return {f"area_{key}": getattr(self, key) for key in ['x1', 'y1', 'x2', 'y2']}

    # ============================ Getters ============================

    def get_selection(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        """Get the four values of the selection as: ((x1, y1), (x2, y2))"""
        return (self.x1, self.y1), (self.x2, self.y2)

    def get_center(self) -> Tuple[float, float]:
        """Get center of current selection"""
        return (self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2

    def get_center_int(self) -> Tuple[int, int]:
        """Get center of current selection, coords can only be integers. If even length, the value is floored"""
        return math.floor((self.x1 + self.x2) / 2), math.floor((self.y1 + self.y2) / 2)

    def get_range_x(self) -> range:
        """Returns a range object for the x coordinates."""
        return range(self.x1, self.x2 + 1)

    def get_range_y(self) -> range:
        """Returns a range object for the y coordinates."""
        return range(self.y1, self.y2 + 1)

    def get_width(self) -> int:
        """Returns the length of the x side of the selection."""
        return self.x2 + 1 - self.x1

    def get_height(self) -> int:
        """Returns the length of the y side of the selection."""
        return self.y2 + 1 - self.y1

    # ============================ Use functions ============================

    def use_full(self) -> Area:
        """Sets the area object to use the entire selection"""
        self.state = AreaState.FULL
        return self

    def use_only_edge(self, line_width: int = None, line_width_x: int = None, line_width_y: int = None) -> Area:
        """
        Sets the area object to only use the edge of the selection

        Args:
            line_width (int): The width of the x & y edge line
            line_width_x (int): The width of the x edge line
            line_width_y (int): The width of the y edge line

        Returns:
            This area object
        """
        self.attrs(line_width=line_width, line_width_x=line_width_x, line_width_y=line_width_y)
        self.state = AreaState.EDGE
        return self

    def use_only_corners(self, corner_size: int = None, corner_size_x: int = None, corner_size_y: int = None) -> Area:
        """
        Sets the area object to only use the corners  pattern within the selection.

        Args:
            corner_size (int): The size along both the x and y axis of the corner areas
            corner_size_x (int): The size along the x axis of the corner areas
            corner_size_y (int): The size along the y axis of the corner areas

        Returns:
            This area object
        """
        self.attrs(corner_size=corner_size, corner_size_x=corner_size_x, corner_size_y=corner_size_y)
        self.state = AreaState.CORNERS
        return self

    def use_pattern_grid(self, line_gap: int = None, line_width: int = None, line_gap_x: int = None,
                         line_gap_y: int = None, line_width_x: int = None, line_width_y: int = None) -> Area:
        """
        Sets the area object to use a grid pattern within the selection.

        Args:
            line_gap (int): The size of the gaps between lines
            line_width (int): The width of the x & y grid lines
            line_gap_x (int): The size of the x gaps between lines
            line_gap_y (int): The size of the y gaps between lines
            line_width_x (int): The width of the x grid lines
            line_width_y (int): The width of the y grid lines

        Returns:
            This area object
        """
        self.attrs(line_gap=line_gap, line_width=line_width,
                   line_gap_x=line_gap_x, line_width_x=line_width_x,
                   line_gap_y=line_gap_y, line_width_y=line_width_y)
        self.state = AreaState.GRID
        return self

    def use_pattern_lines(self, axis: str, line_gap: int = None, line_width: int = None) -> Area:
        """
        Sets the area object to use a lines pattern within the selection.

        Args:
            axis (str): The axis the lines should follow. Can either be "x" or "y"
            line_gap (int): The size of the gaps between lines
            line_width (int): The width of the x & y lines

        Returns:
            This area object
        """
        self.attrs(axis=axis.lower(), line_gap=line_gap, line_width=line_width)
        self.state = AreaState.LINES
        return self

    # ============================ Adjustment functions ============================

    def invert(self) -> Area:
        """
        Inverts the inverted boolean. Causes the `to_coords` to return the inverted selection. (Especially useful for
        the grid state. Not as useful for the edge which would be the same as shrinking the selection. When used with
        the fill state an empty set is returned.

        **Please note:** This inverts the INTERNAL selection. Tiles OUTSIDE of the selection will NOT be returned.
        """
        self.inverted = not self.inverted
        return self

    def along_axis(self, axis: str) -> Area:
        """Sets the axis. Can be either "x" or "y". """
        self.axis = axis
        return self

    def attr(self, key: Union[str, AreaAttr], value: int) -> Area:
        """Sets the attribute to the given value. AreaAttr or str can be used as key"""
        if isinstance(key, AreaAttr):
            key = key.value

        keys: List[str]
        if key == 'line_width':
            keys = ['line_width_x', 'line_width_y']
        elif key == 'line_gap':
            keys = ['line_gap_x', 'line_gap_y']
        elif key == 'corner_size':
            keys = ['corner_size_x', 'corner_size_y']
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
            line_gap: int = None,
            line_width: int = None,
            line_gap_x: int = None,
            line_gap_y: int = None,
            line_width_x: int = None,
            line_width_y: int = None,
            axis: str = None,
            corner_size: int = None,
            corner_size_x: int = None,
            corner_size_y: int = None,
    ) -> Area:
        """
        Sets multiple attributes to the corresponding values.

        Returns:
            This area object
        """
        for key, value in locals().items():
            if key == 'self' or value is None:
                continue
            self.attr(key, value)
        return self

    def size(self, n: int) -> Area:
        """
        Sets the selection to a size around the center. If center is (4,4) with a size of 3 the selection will become
        ``((3,3), (5,5))``
        """
        center_x, center_y = self.get_center_int()
        n -= 1  # Ignore center tile
        self.x1 = self._minmax_val(center_x - math.ceil(n / 2))
        self.y1 = self._minmax_val(center_y - math.ceil(n / 2))
        self.x2 = self._minmax_val(center_x + math.floor(n / 2))
        self.y2 = self._minmax_val(center_y + math.floor(n / 2))
        return self

    def height(self, n: int) -> Area:
        """
        Sets the height (y axis) of the selection. Shrinks/Expands both sides equally.
        If the expansion hits the edge of the map, it'll expand on the other side.
        """
        c1, c2 = self._get_length_change(n, self.get_height(), self.y1, self.y2)

        self.y1 = self._minmax_val(self.y1 + c1)
        self.y2 = self._minmax_val(self.y2 + c2)
        return self

    def width(self, n: int) -> Area:
        """
        Sets the width (x axis) of the selection. Shrinks/Expands both sides equally.
        If the expansion hits the edge of the map, it'll expand on the other side.
        """
        c1, c2 = self._get_length_change(n, self.get_width(), self.x1, self.x2)

        self.x1 = self._minmax_val(self.x1 + c1)
        self.x2 = self._minmax_val(self.x2 + c2)
        return self

    def center(self, x: int, y: int) -> Area:
        """
        Moves the selection center to a given position. When the given center forces the selection of the edge of the
        map, the selection is moved to that position and all tiles that are out of the map are removed from the
        selection, effectively decreasing the selection size.

        If you want to limit moving the center without changing the selection box size, use: ``center_bounded``
        """
        center_x, center_y = self.get_center()
        diff_x, diff_y = math.floor(x - center_x), math.floor(y - center_y)
        self.x1 = self._minmax_val(self.x1 + diff_x)
        self.y1 = self._minmax_val(self.y1 + diff_y)
        self.x2 = self._minmax_val(self.x2 + diff_x)
        self.y2 = self._minmax_val(self.y2 + diff_y)
        return self

    def center_bounded(self, x: int, y: int) -> Area:
        """
        Moves the selection center to a given position on the map. This function makes sure it cannot go over the edge
        of the map. The selection will be forced against the edge of the map but the selection will not be decreased.
        """
        center_x, center_y = self.get_center()
        diff_x, diff_y = math.floor(x - center_x), math.floor(y - center_y)
        if diff_x < 0 and abs(diff_x) > self.x1:
            diff_x = -self.x1
        elif diff_x > 0 and diff_x > (distance_x := self._map_size - self.x2):
            diff_x = distance_x
        if diff_y < 0 and abs(diff_y) > self.y1:
            diff_y = -self.y1
        elif diff_y > 0 and diff_y > (distance_y := self._map_size - self.y2):
            diff_y = distance_y
        self.x1 += diff_x
        self.y1 += diff_y
        self.x2 += diff_x
        self.y2 += diff_y
        return self

    def select_entire_map(self) -> Area:
        """Sets the selection to the entire map"""
        self.x1, self.y1, self.x2, self.y2 = 0, 0, self._map_size, self._map_size
        return self

    def select(self, x1: int, y1: int, x2: int = None, y2: int = None) -> Area:
        """Sets the selection to the given coordinates"""
        if x2 is None:
            x2 = x1
        if y2 is None:
            y2 = y1
        self.x1 = self._minmax_val(x1)
        self.y1 = self._minmax_val(y1)
        self.x2 = self._minmax_val(x2)
        self.y2 = self._minmax_val(y2)
        return self

    def select_from_center(self, x: int, y: int, dx: int = 1, dy: int = 1) -> Area:
        """Sets the selection to the given coordinates"""
        half_x, half_y = (dx - 1) / 2, (dy - 1) / 2
        self.select(
            x1=x - math.ceil(half_x),
            y1=y - math.ceil(half_y),
            x2=x + math.floor(half_x),
            y2=y + math.floor(half_y),
        )
        return self

    def shrink(self, n: int) -> Area:
        """Shrinks the selection from all sides"""
        self.shrink_x1(n)
        self.shrink_y1(n)
        self.shrink_x2(n)
        self.shrink_y2(n)
        return self

    def shrink_x1(self, n: int) -> Area:
        """Shrinks the selection from the first corner on the X axis by n"""
        self.x1 = min(self.x1 + n, self.x2)
        return self

    def shrink_y1(self, n: int) -> Area:
        """Shrinks the selection from the first corner on the Y axis by n"""
        self.y1 = min(self.y1 + n, self.y2)
        return self

    def shrink_x2(self, n: int) -> Area:
        """Shrinks the selection from the second corner on the X axis by n"""
        self.x2 = max(self.x1, self.x2 - n)
        return self

    def shrink_y2(self, n: int) -> Area:
        """Shrinks the selection from the second corner on the Y axis by n"""
        self.y2 = max(self.y1, self.y2 - n)
        return self

    def expand(self, n: int) -> Area:
        """Expands the selection from all sides"""
        self.expand_x1(n)
        self.expand_y1(n)
        self.expand_x2(n)
        self.expand_y2(n)
        return self

    def expand_x1(self, n: int) -> Area:
        """Expands the selection from the first corner on the X axis by n"""
        self.x1 = self._minmax_val(self.x1 - n)
        return self

    def expand_y1(self, n: int) -> Area:
        """Expands the selection from the first corner on the Y axis by n"""
        self.y1 = self._minmax_val(self.y1 - n)
        return self

    def expand_x2(self, n: int) -> Area:
        """Expands the selection from the second corner on the X axis by n"""
        self.x2 = self._minmax_val(self.x2 + n)
        return self

    def expand_y2(self, n: int) -> Area:
        """Expands the selection from the second corner on the Y axis by n"""
        self.y2 = self._minmax_val(self.y2 + n)
        return self

    # ============================ Test against ... functions ============================

    def is_within_selection(self, x: int, y: int) -> bool:
        """
        If a given (x,y) location is within the selection.

        Args:
            x (int): The X coordinate
            y (int): The Y coordinate

        Returns:
            True if (x,y) is within the selection, False otherwise
        """
        if not (self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2):
            return False

        is_within: bool
        if self.state == AreaState.EDGE:
            is_within = self._is_edge_tile(x, y)
        elif self.state == AreaState.GRID:
            is_within = self._is_a_grid_tile(x, y)
        elif self.state == AreaState.LINES:
            is_within = self._is_a_line_tile(x, y)
        elif self.state == AreaState.CORNERS:
            is_within = self._is_a_corner_tile(x, y)
        else:
            is_within = True
        return self._invert_if_inverted(is_within)

    # ============================ Miscellaneous functions ============================

    def copy(self):
        """
        Copy this instance of an Area. Useful for when you want to do multiple extractions (to_...) from the same source
        with small tweaks.

        Examples:

            Get a grid and the edge around it::

                area = Area.select(10,10,20,20)
                edge = area.copy().expand(1).use_only_edge().to_coords()
                # Without copy you'd have to add `.shrink(1)`
                grid = area.use_pattern_grid().to_coords()

        Returns:
            A copy of this Area object
        """
        return copy.copy(self)

    # ============================ Support functions ============================

    def _get_length_change(self, new_len: int, cur_len: int, first_coord: int, second_coord) -> Tuple[int, int]:
        """
        Calculate the differences in tiles for the 2 points (x1 & x2) or (y1 & y2) when the length of an edge is changed

        Args:
            new_len (int): The new length
            cur_len (int): The current length
            first_coord (int): Coord of the first corner (x1 or y1)
            second_coord (int): Coord of the first corner (x2 or y2)

        Returns:
            The differences for the first and second coordinate. Can be negative and positive ints.
        """
        half: float = (new_len - cur_len) / 2
        half1, half2 = -half, half
        if half > 0:
            if half > first_coord:
                half1 = -first_coord
                half2 += half - first_coord
            if half > (dist := self._map_size - second_coord):
                half2 = dist
                half1 += half - dist
            return math.floor(half1), math.floor(half2)
        return math.ceil(half1), math.ceil(half2)

    def _is_edge_tile(self, x: int, y: int) -> bool:
        """ Returns if a given tile (x,y) is an edge tile of the set selection given a certain edge width."""
        return any((
            0 <= x - self.x1 < self.line_width_x,
            0 <= y - self.y1 < self.line_width_y,
            0 <= self.x2 - x < self.line_width_x,
            0 <= self.y2 - y < self.line_width_y
        ))

    def _invert_if_inverted(self, bool_: bool) -> bool:
        """Inverts the boolean if the area is in inverted state."""
        return not bool_ if self.inverted else bool_

    def _is_a_corner_tile(self, x: int, y: int) -> bool:
        """If a given (x,y) location is a corner tile."""
        return ((self.x1 <= x < self.x1 + self.corner_size_x) or (self.x2 - self.corner_size_x < x <= self.x2)) and \
               ((self.y1 <= y < self.y1 + self.corner_size_y) or (self.y2 - self.corner_size_y < y <= self.y2))

    def _is_a_grid_tile(self, x: int, y: int) -> bool:
        """If a given (x,y) location is within the grid selection."""
        return (x - self.x1) % (self.line_gap_x + self.line_width_x) < self.line_width_x and \
               (y - self.y1) % (self.line_gap_y + self.line_width_y) < self.line_width_y

    def _is_a_line_tile(self, x: int, y: int) -> bool:
        """If a given (x,y) location is within the grid selection."""
        if self.axis == "x":
            return (y - self.y1) % (self.line_gap_y + self.line_width_y) < self.line_width_y
        elif self.axis == "y":
            return (x - self.x1) % (self.line_gap_x + self.line_width_x) < self.line_width_x
        raise ValueError("Invalid axis value. Should be either x or y")

    def _minmax_val(self, val: Union[int, float]) -> Union[int, float]:
        """Keeps a given value within the bounds of ``0 <= val <= map_size``."""
        return max(0, min(val, self._map_size))
