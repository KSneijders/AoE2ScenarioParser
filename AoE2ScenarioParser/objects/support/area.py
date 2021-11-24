from __future__ import annotations

import math
from typing import List, Tuple, Dict, Union, NamedTuple, TYPE_CHECKING

from AoE2ScenarioParser.helper.helper import xy_to_i
from AoE2ScenarioParser.helper.list_functions import list_chuncks
from AoE2ScenarioParser.scenarios.scenario_store import getters

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.data_objects.terrain_tile import TerrainTile
    from AoE2ScenarioParser.scenarios.aoe2_scenario import AoE2Scenario


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

        self.x1 = self.y1 = self.x2 = self.y2 = math.floor(self._map_size / 2)

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

    def selection_to_coords(self) -> List[Tile]:
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
        return [
            Tile(x, y) for y in list(range(self.y1, self.y2 + 1)) for x in list(range(self.x1, self.x2 + 1))
        ]

    def selection_to_coords_2d(self) -> List[List[Tile]]:
        """
        Converts the selection to a 2D list of (x, y) coordinates

        Returns:
            A list of lists with (x, y) tuples of the selection.

        Examples:
            The selection: ``((3,3), (5,5))`` would result in a list with 3 lists with all a length of 3::

                [
                    [(3,3), (4,3)  ...],
                    [...,   ...,   ...],
                    [...,   (4,5), (5,5)]
                ]
        """
        flattened_list = self.selection_to_coords()
        return list(list_chuncks(flattened_list, (self.x2 + 1) - self.x1))

    def selection_to_terrain_tiles(self) -> List['TerrainTile']:
        """
        Converts the selection to a list of terrain tile objects from the map manager.
        Can only be used if the area has been associated with a scenario (created through map manager)

        Returns:
            A list of lists with (x, y) tuples of the selection.
        """
        self._force_association()
        terrain = getters.get_terrain(self.uuid)
        flattened_list = self.selection_to_coords()
        return [terrain[xy_to_i(x, y, self._map_size + 1)] for (x, y) in flattened_list]

    def selection_to_terrain_tiles_2d(self) -> List[List['TerrainTile']]:
        """
        Converts the selection to a list of lists with terrain tile objects from the map manager.
        Can only be used if the area has been associated with a scenario (created through map manager)

        Returns:
            A list of lists with (x, y) tuples of the selection.
        """
        self._force_association()
        terrain = getters.get_terrain(self.uuid)
        flattened_list = self.selection_to_coords()
        return list(list_chuncks(
            [terrain[xy_to_i(x, y, self._map_size + 1)] for (x, y) in flattened_list],
            (self.x2 + 1) - self.x1
        ))

    def selection_to_dict(self) -> Dict[str, int]:
        """
        Converts the 2 corners of the selection to area keys for use in effects etc.
        This can be used by adding double stars (**) before this function.

        Returns:
            A dict with area_x1, area_y1, area_x2, area_y2 as keys and their respective values.

        Examples:
            The selection: ``((3,3), (5,5))`` would result in a dict that looks like:
                ``{'area_x1': 3, 'area_y1': 3, 'area_x2': 5, 'area_y2': 5}``
            Usage: ``**area.selection_to_dict()`` (i.e. in a ``new_effect.something`` function)
        """
        return {f"area_{key}": getattr(self, key) for key in ['x1', 'y1', 'x2', 'y2']}

    # ============================ Getter properties ============================

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

    # ============================ Adjustment functions ============================

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

        If you want to limit moving the center without changing the selection box size, use: ``set_center_bound``
        """
        center_x, center_y = self.center
        diff_x, diff_y = math.floor(x - center_x), math.floor(y - center_y)
        self.x1 = self._minmax_val(self.x1 + diff_x)
        self.y1 = self._minmax_val(self.y1 + diff_y)
        self.x2 = self._minmax_val(self.x2 + diff_x)
        self.y2 = self._minmax_val(self.y2 + diff_y)
        return self

    def set_center_bound(self, x: int, y: int) -> Area:
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

    # ============================ Support functions ============================

    def _minmax_val(self, val: Union[int, float]) -> Union[int, float]:
        """Keeps a given value within the bounds of ``0 <= val <= map_size``"""
        return max(0, min(val, self._map_size))
