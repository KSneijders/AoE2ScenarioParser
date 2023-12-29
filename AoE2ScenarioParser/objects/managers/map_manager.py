from __future__ import annotations

import itertools
import math
from typing import List, Union, Tuple, Set, Optional

from AoE2ScenarioParser.helper.helper import xy_to_i
from AoE2ScenarioParser.helper.list_functions import list_chuncks
from AoE2ScenarioParser.helper.maffs import sign
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.data_objects.terrain_tile import TerrainTile
from AoE2ScenarioParser.objects.support.uuid_list import UuidList
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.sections.retrievers.retriever_object_link_group import RetrieverObjectLinkGroup


class MapManager(AoE2Object):
    """
    Manager of everything map related.
    This class does not include the logic for DE specific features.
    For those see: `MapManagerDE`
    """

    _link_list = [
        RetrieverObjectLinkGroup("Map", group=[
            RetrieverObjectLink("map_width", "map_width"),
            RetrieverObjectLink("map_height", "map_height"),
            RetrieverObjectLink("terrain", "terrain_data", process_as_object=TerrainTile),
        ])
    ]

    def __init__(
            self,
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

    @map_size.setter
    def map_size(self, new_size: int):
        old_size = self._map_width
        difference = new_size - old_size

        if difference == 0:
            return

        self._map_width = new_size
        self._map_height = new_size

        new_terrain = []
        if difference < 0:
            # Remove ends of rows (x) & remove final rows entirely (y)
            for index, chunk in enumerate(list_chuncks(self.terrain, old_size)):
                if index == new_size:
                    break
                new_terrain.extend(chunk[:new_size])
        elif difference > 0:
            # Add ends to rows (x) & add entirely new rows  (y)
            chunk_gen = list_chuncks(self.terrain, old_size)
            for index in range(new_size):
                if index < old_size:
                    row = next(chunk_gen) + [TerrainTile(uuid=self._uuid) for _ in range(difference)]
                else:
                    row = [TerrainTile(uuid=self._uuid) for _ in range(new_size)]
                new_terrain.extend(row)
        self.terrain = new_terrain

    @property
    def terrain(self) -> List[TerrainTile]:
        return self._terrain

    @terrain.setter
    def terrain(self, value: List[TerrainTile]):
        sqrt = math.sqrt(len(value))
        if sqrt % 1 != 0:
            raise ValueError(f"Tiles do not represent a square map. (Given tile count: {len(value)})")

        def reset_indices(lst):
            tile: TerrainTile
            for index, tile in enumerate(lst):
                tile._reset_terrain_index(index)

        reset_indices(value)

        if value is not None:
            self._terrain = UuidList(
                uuid=self._uuid,
                seq=value,
                on_update_execute_list=reset_indices
            )
        self._map_width = int(sqrt)
        self._map_height = int(sqrt)

    def get_tile(self, x: int = None, y: int = None, i: int = None) -> TerrainTile:
        """
        Get a tile on the map based on xy coordinates or using the index (`i`)

        Args:
            x: The x coordinate of the wanted tile (used together with y)
            y: The y coordinate of the wanted tile (used together with x)
            i: The index of the wanted tile

        Raises:
            ValueError: If parameters (`x` and/or `y`) and `i` are all set
            ValueError: If the index requested is outside the index range of the terrain tiles

        Returns:
            The requested tile
        """
        if i and (x or y):
            raise ValueError("Cannot use both xy and i. Choose or XY or I.")
        if i is not None:
            if 0 <= i < self.map_size:
                return self.terrain[i]
            else:
                raise ValueError("Parameter i needs to be: 0 <= i < map_size")
        return self.terrain[xy_to_i(x, y, self.map_size)]

    def get_tile_safe(self, x: int = None, y: int = None, i: int = None) -> TerrainTile | None:
        """
        Get a tile on the map based on xy coordinates or using the index (`i`).
        If the index is outside the map, `None` is returned instead of an error

        Args:
            x: The x coordinate of the wanted tile (used together with y)
            y: The y coordinate of the wanted tile (used together with x)
            i: The index of the wanted tile

        Returns:
            The requested tile or `None` if it doesn't exist
        """
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

            # Reset current elevation within area
            for row in source_tiles:
                for tile in row:
                    tile.elevation = elevation

            xys = set(t.xy for row in source_tiles for t in row)
            edge_tiles = source_tiles[0] + source_tiles[-1]
            for i in range(1, len(source_tiles) - 1):
                edge_tiles.extend([source_tiles[i][0], source_tiles[i][-1]])

        for tile in edge_tiles:
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