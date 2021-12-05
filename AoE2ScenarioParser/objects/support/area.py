from __future__ import annotations

import math
from enum import Enum
from typing import List, Tuple, Dict, Union, NamedTuple, TYPE_CHECKING

from AoE2ScenarioParser.helper.helper import xy_to_i
from AoE2ScenarioParser.scenarios.scenario_store import getters

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.data_objects.terrain_tile import TerrainTile
    from AoE2ScenarioParser.scenarios.aoe2_scenario import AoE2Scenario


class AreaState(Enum):
    FILL = 0
    EDGE = 1
    GRID = 2


class Tile(NamedTuple):
    """NamedTuple for tiles. use tile.x or tile.y for coord access"""
    x: int
    y: int


class Area:
    def __init__(self, map_size: int = None, uuid: str = None) -> None:
        if map_size is None and uuid is None:
            raise ValueError("Cannot create area object without knowing the map size or a UUID from a scenario.")
        super().__init__()

        if map_size is None:
            map_size = getters.get_map_size(uuid)

        self._map_size = map_size - 1
        self.uuid = uuid

        self.state = AreaState.FILL

        center = math.floor(self._map_size / 2)
        self.x1 = center
        self.y1 = center
        self.x2 = center
        self.y2 = center
        # Edge
        self.edge_width = 1
        # Grid
        self.grid_gap_x = 1
        self.grid_gap_y = 1
        self.grid_width_x = 1
        self.grid_width_y = 1

    @classmethod
    def from_uuid(cls, uuid: str) -> Area:
        return cls(uuid=uuid)

    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        self._uuid = value
        if value is not None:
            self._map_size = getters.get_map_size(value) - 1

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

    def to_coords(self) -> List[Tile]:
        """
        Converts the selection to a list of (x, y) coordinates

        Returns:
            A list of (x, y) tuples of the selection.

        Examples:
            The selection: ``((3,3), (5,5))`` would result in a list with a length of 9::

                [
                    (3,3), (4,3)  ...,
                    ...,   ...,   ...,
                    ...,   (4,5), (5,5)
                ]
        """
        if self.edge:
            return [Tile(x, y) for y in self.range_y for x in self.range_x if self.is_within_selection(x, y)]
        # Could have used `self.is_within_selection` here too but for performance reasons this is done without the if.
        return [Tile(x, y) for y in self.range_y for x in self.range_x]

    def to_terrain_tiles(self) -> List['TerrainTile']:
        """
        Converts the selection to a list of terrain tile objects from the map manager.
        Can only be used if the area has been associated with a scenario (created through map manager)

        Returns:
            A list of lists with (x, y) tuples of the selection.
        """
        self._force_association()
        terrain = getters.get_terrain(self.uuid)
        return [terrain[xy_to_i(x, y, self._map_size + 1)] for (x, y) in self.to_coords()]

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

    # ============================ Properties ============================

    @property
    def selection(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        """Get the four values of the selection as: ((x1, y1), (x2, y2))"""
        return (self.x1, self.y1), (self.x2, self.y2)

    @selection.setter
    def selection(self, value: Tuple[Tuple[int, int], Tuple[int, int]]):
        (self.x1, self.y1), (self.x2, self.y2) = value

    @property
    def center(self) -> Tuple[float, float]:
        """Get center of current selection"""
        return (self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2

    @center.setter
    def center(self, value: Tuple[float, float]):
        self.set_center(x=round(value[0]), y=round(value[1]))

    @property
    def center_int(self) -> Tuple[int, int]:
        """Get center of current selection, coords can only be integers. If even length, the value is floored"""
        return math.floor((self.x1 + self.x2) / 2), math.floor((self.y1 + self.y2) / 2)

    @center_int.setter
    def center_int(self, value: Tuple[int, int]):
        self.set_center(x=value[0], y=value[1])

    # ============== READ ONLY PROPERTIES ==============

    @property
    def range_x(self) -> range:
        """Returns a range object for the x coordinates."""
        return range(self.x1, self.x2 + 1)

    @property
    def range_y(self) -> range:
        """Returns a range object for the y coordinates."""
        return range(self.y1, self.y2 + 1)

    @property
    def edge_length_x(self) -> int:
        """Returns the length of the x side of the selection."""
        return self.x2 + 1 - self.x1

    @property
    def edge_length_y(self) -> int:
        """Returns the length of the y side of the selection."""
        return self.y2 + 1 - self.y1

    # ============================ Use functions ============================

    def use_filled(self) -> Area:
        """Sets the area object to use the entire selection"""
        self.state = AreaState.FILL
        return self

    def use_edge(self, edge_width: int = None) -> Area:
        """
        Sets the area object to use the border of the selection

        Args:
            edge_width (int): The edge width to set (can be changed using area.edge_width(x))

        Returns:
            This area object
        """
        self.state = AreaState.EDGE
        if edge_width is not None:
            self.edge_width = edge_width
        return self

    def use_grid(self,
                 grid_gap: int = None,
                 grid_gap_x: int = None,
                 grid_gap_y: int = None,
                 grid_width: int = None,
                 grid_width_x: int = None,
                 grid_width_y: int = None):
        self.state = AreaState.GRID

    # ============================ Adjustment functions ============================

    def edge_width(self, width: int) -> Area:
        """Sets the edge width attribute."""
        self.edge_width = width
        return self

    def set_size(self, n: int) -> Area:
        """
        Sets the selection to a size around the center. If center is (4,4) with a size of 3 the selection will become
        ``((3,3), (5,5))``
        """
        center_x, center_y = self.center_int
        n -= 1  # Ignore center tile
        self.x1 = self._minmax_val(center_x - math.floor(n / 2))
        self.y1 = self._minmax_val(center_y - math.floor(n / 2))
        self.x2 = self._minmax_val(center_x + math.ceil(n / 2))
        self.y2 = self._minmax_val(center_y + math.ceil(n / 2))
        return self

    def set_center(self, x: int, y: int) -> Area:
        """
        Moves the selection center to a given position. When the given center forces the selection of the edge of the
        map, the selection is moved to that position and all tiles that are out of the map are removed from the
        selection, effectively decreasing the selection size.

        If you want to limit moving the center without changing the selection box size, use: ``set_center_bounded``
        """
        center_x, center_y = self.center
        diff_x, diff_y = math.floor(x - center_x), math.floor(y - center_y)
        self.x1 = self._minmax_val(self.x1 + diff_x)
        self.y1 = self._minmax_val(self.y1 + diff_y)
        self.x2 = self._minmax_val(self.x2 + diff_x)
        self.y2 = self._minmax_val(self.y2 + diff_y)
        return self

    def set_center_bounded(self, x: int, y: int) -> Area:
        """
        Moves the selection center to a given position on the map. This function makes sure it cannot go over the edge
        of the map. The selection will be forced against the edge of the map but the selection will not be decreased.
        """
        center_x, center_y = self.center
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

    def select(self, x1, y1, x2, y2) -> Area:
        """Sets the selection to the given coordinates"""
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        return self

    def shrink(self, n) -> Area:
        """Shrinks the selection from all sides"""
        self.shrink_x1(n)
        self.shrink_y1(n)
        self.shrink_x2(n)
        self.shrink_y2(n)
        return self

    def shrink_x1(self, n) -> Area:
        """Shrinks the selection from the first corner on the X axis by n"""
        self.x1 = min(self.x1 + n, self.x2)
        return self

    def shrink_y1(self, n) -> Area:
        """Shrinks the selection from the first corner on the Y axis by n"""
        self.y1 = min(self.y1 + n, self.y2)
        return self

    def shrink_x2(self, n) -> Area:
        """Shrinks the selection from the second corner on the X axis by n"""
        self.x2 = max(self.x1, self.x2 - n)
        return self

    def shrink_y2(self, n) -> Area:
        """Shrinks the selection from the second corner on the Y axis by n"""
        self.y2 = max(self.y1, self.y2 - n)
        return self

    def expand(self, n) -> Area:
        """Expands the selection from all sides"""
        self.expand_x1(n)
        self.expand_y1(n)
        self.expand_x2(n)
        self.expand_y2(n)
        return self

    def expand_x1(self, n) -> Area:
        """Expands the selection from the first corner on the X axis by n"""
        self.x1 = self._minmax_val(self.x1 - n)
        return self

    def expand_y1(self, n) -> Area:
        """Expands the selection from the first corner on the Y axis by n"""
        self.y1 = self._minmax_val(self.y1 - n)
        return self

    def expand_x2(self, n) -> Area:
        """Expands the selection from the second corner on the X axis by n"""
        self.x2 = self._minmax_val(self.x2 + n)
        return self

    def expand_y2(self, n) -> Area:
        """Expands the selection from the second corner on the Y axis by n"""
        self.y2 = self._minmax_val(self.y2 + n)
        return self

    # ============================ Test against ... functions ============================

    def is_edge_tile(self, x: int, y: int, width: int) -> bool:
        """
        Returns if a given tile (x,y) is an edge tile of the set selection given a certain edge width.

        Args:
            x (int): The X coordinate
            y (int): The Y coordinate
            width (int): The width of the border

        Returns:
            True if (x,y) is an edge tile within the selection, False otherwise
        """
        return any((
            0 <= x - self.x1 < width,
            0 <= y - self.y1 < width,
            0 <= self.x2 - x < width,
            0 <= self.y2 - y < width
        ))

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

        if self.edge:
            return self.is_edge_tile(x, y, self.edge_width)
        else:
            return True

    # ============================ Support functions ============================

    def _is_within_grid(self, x: int, y: int):
        """If a given (x,y) location is within the grid selection."""
        return (x - self.x1) % (self.grid_gap_x + self.grid_width_x) < self.grid_width_x and \
               (y - self.y1) % (self.grid_gap_y + self.grid_width_y) < self.grid_width_y

    def _minmax_val(self, val: Union[int, float]) -> Union[int, float]:
        """Keeps a given value within the bounds of ``0 <= val <= map_size``"""
        return max(0, min(val, self._map_size))
