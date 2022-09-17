from __future__ import annotations

import itertools
from typing import List, Tuple, Set

from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.helper.helper import xy_to_i
from AoE2ScenarioParser.helper.list_functions import list_chuncks
from AoE2ScenarioParser.helper.maffs import sign
from AoE2ScenarioParser.helper.printers import warn
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.data_objects.terrain_tile import TerrainTile, reset_terrain_index
from AoE2ScenarioParser.objects.support.uuid_list import UuidList
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.sections.retrievers.retriever_object_link_group import RetrieverObjectLinkGroup


class MapManager(AoE2Object):
    """Manager of the everything map related."""

    _link_list = [
        RetrieverObjectLinkGroup("Map", group=[
            RetrieverObjectLink("map_width", "map_width"),
            RetrieverObjectLink("map_height", "map_height"),
            RetrieverObjectLink("terrain", "terrain_data", process_as_object=TerrainTile),
        ])
    ]

    def __init__(self,
            map_width: int,
            map_height: int,
            terrain: List[TerrainTile],
            **kwargs
    ):
        super().__init__(**kwargs)

        self.terrain: List[TerrainTile] = terrain
        self._map_width: int = map_width
        self._map_height: int = map_height

    @property
    def terrain_2d(self) -> List[List[TerrainTile]]:
        return list(list_chuncks(self.terrain, self.map_size))

    def get_tile(self, x: int = None, y: int = None, i: int = None) -> TerrainTile:
        if i and (x or y):
            raise ValueError("Cannot use both xy and i. Choose or XY or I.")
        if i is not None:
            return self.terrain[i]
        return self.terrain[xy_to_i(x, y, self.map_size)]

    def get_tile_safe(self, x: int = None, y: int = None, i: int = None) -> TerrainTile | None:
        if i and (x or y):
            raise ValueError("Cannot use both xy and i. Choose or XY or I.")
        try:
            return self.get_tile(x, y, i)
        except (IndexError, ValueError):
            return None

    def get_square_1d(self, x1: int, y1: int, x2: int, y2: int) -> List[TerrainTile]:
        """
        Get a square of tiles from the map

        Args:
            x1: The x1 coordinate of the square
            y1: The y1 coordinate of the square
            x2: The x2 coordinate of the square
            y2: The y2 coordinate of the square

        Returns:
            1D list of terrain tiles based on given coordinates
        """
        result = []
        for row in self._get_square_rows(x1, y1, x2, y2):
            result.extend(row)
        return result

    def get_square_2d(self, x1: int, y1: int, x2: int, y2: int) -> List[List[TerrainTile]]:
        """
        Get a square of tiles from the map

        Args:
            x1: The x1 coordinate of the square
            y1: The y1 coordinate of the square
            x2: The x2 coordinate of the square
            y2: The y2 coordinate of the square

        Returns:
            2D list of lists with terrain tiles based on given coordinates
        """
        result = []
        for row in self._get_square_rows(x1, y1, x2, y2):
            result.append(row)
        return result

    def _get_square_rows(self, x1, y1, x2, y2):
        row_nums = range(y1, y2 + 1)
        for row in row_nums:
            i1 = xy_to_i(x1, row, self.map_size)
            i2 = xy_to_i(x2, row, self.map_size)
            tiles = self.terrain[i1:i2 + 1]
            yield tiles

    @property
    def map_width(self) -> int:
        return self._map_width

    @property
    def map_height(self) -> int:
        return self._map_height

    @property
    def map_size(self) -> int:
        if self._map_height == self._map_width:
            return self._map_height
        else:
            raise ValueError("Map is not a square. Use the attributes 'map_width' and 'map_height' instead.")

    @property
    def terrain(self) -> List[TerrainTile]:
        return self._terrain

    @terrain.setter
    def terrain(self, value: List[TerrainTile]):
        def reset_indices(lst):
            tile: TerrainTile
            for index, tile in enumerate(lst):
                reset_terrain_index(tile, index)

        if value is not None:
            self._terrain = UuidList(
                uuid=self._uuid,
                seq=value,
                on_update_execute_list=reset_indices
            )

    @map_size.setter
    def map_size(self, new_size: int):
        old_size = self._map_width
        difference = new_size - old_size

        self._map_width = new_size
        self._map_height = new_size

        new_terrain = []
        if difference < 0:
            # Remove ends of rows (x) & remove final rows entirely (y)
            for index, chunck in enumerate(list_chuncks(self.terrain, old_size)):
                if index == new_size:
                    break
                new_terrain.extend(chunck[:new_size])
        elif difference > 0:
            # Add ends to rows (x) & add entirely new rows  (y)
            chunck_gen = list_chuncks(self.terrain, old_size)
            for index in range(new_size):
                if index < old_size:
                    row = next(chunck_gen) + [TerrainTile(uuid=self._uuid) for _ in range(difference)]
                else:
                    row = [TerrainTile(uuid=self._uuid) for _ in range(new_size)]
                new_terrain.extend(row)
        self.terrain = new_terrain

    def set_elevation(
            self,
            elevation: int,
            x1: int,
            y1: int,
            x2: int | None = None,
            y2: int | None = None
    ) -> None:
        """
        Sets elevation like the in-game elevation mechanics. Can set a hill (or single point) to a certain height and
        all tiles around it are adjusted accordingly.

        If you find that the in-game mechanics work differently than this function please report it.

        Args:
            elevation: The elevation to create at the coordinates
            x1: The x coordinate of the west corner
            y1: The y coordinate of the west corner
            x2: The x coordinate of the east corner
            y2: The y coordinate of the east corner
        """
        x2 = x1 if x2 is None else x2
        y2 = y1 if y2 is None else y2

        if x1 == x2 and y1 == y2:
            edge_tiles = source_tiles = [self.get_tile(x1, y1)]
            xys = [source_tiles[0].xy]
        else:
            source_tiles = self.get_square_2d(x1, y1, x2, y2)
            xys = set(t.xy for row in source_tiles for t in row)
            edge_tiles = source_tiles[0] + source_tiles[-1]
            for i in range(1, len(source_tiles) - 1):
                edge_tiles.extend([source_tiles[i][0], source_tiles[i][-1]])

        for tile in edge_tiles:
            tile.elevation = elevation
            self._elevation_tile_recursion(tile, xys)

    def _elevation_tile_recursion(
            self,
            source_tile: TerrainTile,
            xys: Set[Tuple[int, int]],
            visited: Set[Tuple[int, int]] = None
    ):
        """
        Elevation recursive function. Used in the set_elevation function

        Args:
            source_tile: The tile to check around
            xys: The XY tuples from the initial square
            visited: The visited XY tuples with this recursion tree path
        """
        visited = set() if visited is None else visited.copy()
        x, y = source_tile.xy
        visited.add((x, y))
        for nx, ny in itertools.product(range(-1, 2), repeat=2):
            new_x, new_y = x + nx, y + ny
            if (nx or ny) and (new_x, new_y) not in xys and (new_x, new_y) not in visited:
                other = self.get_tile_safe(new_x, new_y)
                if other is None:
                    continue
                behind = self.get_tile_safe(x + nx * 2, y + ny * 2)
                if behind is not None and other.elevation < source_tile.elevation == behind.elevation:
                    other.elevation = source_tile.elevation
                elif abs(other.elevation - source_tile.elevation) > 1:
                    other.elevation = source_tile.elevation + int(sign(other.elevation, source_tile.elevation))
                    self._elevation_tile_recursion(other, xys, visited)

    def create_hill(self, x1: int, y1: int, x2: int, y2: int, elevation: int) -> None:
        """
        Function that takes the coordinates and the height of a plateau and applies it to the map
        by also setting the surrounding slopes so that it is smooth.

        Warning: This function can only increase terrain height!
            This function can only increase height. It will not lower areas terrain.
            For that, you can use: `map_manager.set_elevation()`.

        Args:
            x1: The x coordinate of the west corner
            y1: The y coordinate of the west corner
            x2: The x coordinate of the east corner
            y2: The y coordinate of the east corner
            elevation: The elevation of the map. Default in-game = 0 (called 1 in the game), in-game max = 6
                (called 7 in game). If the given value is over 20 the game camera will 'clip' into the hill.
                So the in-game camera hovers around the height of 20/21 when fully zoomed in, without Ultra Graphics.

        Author:
            This function was written by: pvallet
        """
        warn(f"The function `MapManager.create_hill()` is deprecated as of 0.1.27. "
             f"It will be removed in the future. Please use map_manager.set_elevation() instead.")

        for x in range(max(0, x1 - elevation), min(self.map_size, x2 + elevation)):
            for y in range(max(0, y1 - elevation), min(self.map_size, y2 + elevation)):
                if x1 <= x <= x2 and y1 <= y <= y2:
                    intended_elevation = elevation
                else:
                    distance_to_hill = max(x1 - x, x - x2, y1 - y, y - y2)
                    intended_elevation = elevation - distance_to_hill

                tile = self.terrain[helper.xy_to_i(x, y, self.map_size)]
                tile.elevation = max(intended_elevation, tile.elevation)
