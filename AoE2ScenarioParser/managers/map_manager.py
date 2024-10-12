from __future__ import annotations

import itertools
import math
from collections.abc import Iterable
from typing import Generator, Sequence

from binary_file_parser import Manager, ret, RetrieverRef
from ordered_set import OrderedSet

from AoE2ScenarioParser.helper.coordinates import i_to_xy, xy_to_i
from AoE2ScenarioParser.helper.list_functions import tuple_chunks
from AoE2ScenarioParser.helper.maffs import sign
from AoE2ScenarioParser.objects.support import (
    Area, AreaPattern, AreaT, TerrainData, TerrainDataRow, Tile,
    TileSequence, TileT,
)
from AoE2ScenarioParser.objects.support.enums.direction import Direction
from AoE2ScenarioParser.sections import MapData, Options, ScenarioSections, Settings, TerrainTile


class MapManager(Manager):
    # @formatter:off
    color_mood: str             = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.options), ret(Options.color_mood))
    collide_and_correct: bool   = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.options), ret(Options.collide_and_correct))
    villager_force_drop: bool   = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.options), ret(Options.villager_force_drop))
    _terrain: list[TerrainTile] = RetrieverRef(ret(ScenarioSections.map_data), ret(MapData.terrain_tiles))
    _map_width: int             = RetrieverRef(ret(ScenarioSections.map_data), ret(MapData.width))
    _map_height: int            = RetrieverRef(ret(ScenarioSections.map_data), ret(MapData.height))
    # @formatter:on

    _terrain_2d: TerrainData | None = None

    @property
    def terrain(self) -> TerrainData:
        if self._terrain_2d is None:
            self.terrain = self._terrain
        return self._terrain_2d

    @terrain.setter
    def terrain(self, value: Sequence[Sequence[TerrainTile]] | Sequence[TerrainTile]) -> None:
        if len(value) == 0:
            raise ValueError(f"Terrain sequence must at least contain one TerrainTile")

        first = value[0]
        if isinstance(value, Sequence) and isinstance(first, Sequence):
            map_size = len(value)
            if any(map(lambda x: len(x) != map_size, value)):
                raise ValueError(
                    f"Encountered unexpected length for nested sequence, "
                    f"expected {map_size} sequences with length {map_size}"
                )

            self._terrain_2d = tuple(map(tuple, value))
            self._terrain = list(itertools.chain(*value))
        elif isinstance(value, Sequence) and isinstance(first, TerrainTile):
            value: Sequence[TerrainTile]  # ThxPyCharm

            if math.sqrt(len(value)) % 1 != 0:
                raise ValueError(
                    f"Invalid length given for terrain sequence, should be perfect square. Got: {len(value)}"
                )

            map_size = math.floor(math.sqrt(len(value)))

            self._terrain_2d = tuple_chunks(value, map_size)
            self._terrain = list(value)
        else:
            raise ValueError("Invalid value given for terrain")

        # Assign a Tile reference to all TerrainTiles for ease of access
        for y, row in enumerate(self._terrain_2d):
            for x, tile in enumerate(row):
                tile._tile = Tile(x, y)

        self._map_width = map_size
        self._map_height = map_size

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
    def map_size(self, value):
        # Todo: Implement terrain data changes
        # Todo: Don't implement here, use change_map_size function

        self._map_width = value
        self._map_height = value

    def change_map_size(
        self,
        new_map_size: int,
        direction: Direction = Direction.EAST,
    ) -> None:
        if new_map_size == self.map_size:
            return

        def create_tiles(length: int) -> TerrainDataRow:
            return tuple(TerrainTile() for _ in range(length))

        def create_tile_rows(length: int) -> TerrainData:
            return tuple(create_tiles(length) for _ in range(length))

        def add_rows(terrain: TerrainData, num_rows: int, in_front: bool) -> TerrainData:
            new_rows = create_tile_rows(num_rows)
            return new_rows + terrain if in_front else terrain + new_rows

        def add_cols(terrain: TerrainData, num_cols: int, in_front: bool) -> TerrainData:
            return tuple(
                (create_tiles(num_cols) + row) if in_front else (row + create_tiles(num_cols))
                    for row in terrain
            )

        def slice_rows(terrain: TerrainData, num_rows: int, from_front: bool):
            if from_front:
                return terrain[num_rows:]
            else:
                return terrain[:-num_rows]

        def slice_cols(terrain: TerrainData, num_cols: int, from_front: bool):
            return tuple(row[num_cols:] if from_front else row[:-num_cols] for row in terrain)

        # Todo: Move units
        # Todo: Move trigger
        # Todo: Fix elevation after extending (?)
        # Todo: ADD TESTSS!!! NOT TESTED YET!!

        diff = new_map_size - self.map_size
        is_expanding = diff > 0
        abs_diff = abs(diff)

        terrain_2d = self._terrain_2d
        if is_expanding:
            terrain_2d = add_rows(terrain_2d, abs_diff, in_front = direction in (Direction.NORTH, Direction.WEST))
            terrain_2d = add_cols(terrain_2d, abs_diff, in_front = direction in (Direction.SOUTH, Direction.WEST))
        else:
            terrain_2d = slice_rows(terrain_2d, abs_diff, from_front = direction in (Direction.NORTH, Direction.WEST))
            terrain_2d = slice_cols(terrain_2d, abs_diff, from_front = direction in (Direction.SOUTH, Direction.WEST))

        self.terrain = terrain_2d

    def terrain_from(
        self,
        tile_sequence: TileSequence | Tile | Iterable[TileSequence | Tile],
        ordered: bool = False
    ) -> dict[Tile, TerrainTile]:
        """
        Transform different objects into corresponding ``TerrainTile`` s.
        If multiple objects are given, the resulting dict is ordered based on the objects given and (Y first, X second)
        afterward.

        Using the ``ordered`` parameter can re-order the results based on the corresponding tile (Y first, X second).

        Args:
            tile_sequence: The tile-sequence objects: tile, area or area_pattern objects
            ordered: If the result should be ordered based on Y first and X second

        Returns:
            A dict with the tile as key and the corresponding TerrainTile as value
        """

        # Todo: Add more tests

        def to_terrain_dict(obj: TileSequence | Tile) -> dict[Tile, TerrainTile] | None:
            if isinstance(obj, TileSequence):
                return obj.map(self.get_tile)
            if isinstance(obj, Tile):
                return {obj: self.get_tile(obj)}
            return None

        def to_tiles(obj: TileSequence | Tile) -> OrderedSet[Tile] | set[Tile]:
            if isinstance(obj, TileSequence):
                return obj.to_tiles()
            if isinstance(obj, Tile):
                return {obj}
            return set()

        if isinstance(tile_sequence, (TileSequence, Tile)):
            return to_terrain_dict(tile_sequence)

        tiles = set()
        if isinstance(tile_sequence, Iterable):
            for obj in tile_sequence:
                tiles.update(to_tiles(obj))
        else:
            raise TypeError(f"Unable to turn object of type [{type(tile_sequence)}] into terrain tiles")

        if ordered:
            tiles = sorted(tiles)

        return {tile: self.get_tile(tile) for tile in sorted(tiles)}

    def get_tile(self, tile: TileT = None, i: int = None) -> TerrainTile:
        """
        Get a TerrainTile on the map based on a tile or using its index

        Args:
            tile: The location (x & y) of the wanted TerrainTile
            i: The index of the wanted TerrainTile

        Raises:
            ValueError: If parameters `tile` and `i` are both set
            ValueError: If the index requested is outside the index range of the TerrainTiles

        Returns:
            The requested TerrainTile
        """
        if i and tile or not i and not tile:
            raise ValueError('The use of exactly one of the parameters [i] or [tile] is required')

        # Will never stay None but PyCharm really thinks it does
        x = y = None

        if tile is not None:
            if not Tile.from_value(tile).is_within_bounds(self.map_size):
                raise ValueError('Parameter [tile] needs to be within the bounds of the map')
            x, y = tile

        if i is not None:
            if not 0 <= i < self.map_size:
                raise ValueError('Parameter [i] needs to be [0 <= i < map_size]')
            x, y = i_to_xy(i, self.map_size)

        return self.terrain[y][x]

    def get_tile_safe(self, tile: TileT = None, i: int = None) -> TerrainTile | None:
        """
        Get a TerrainTile on the map based on the location or using the index.
        If the index is outside the map, `None` is returned instead of throwing an error

        Args:
            tile: The location (x & y) of the wanted TerrainTile
            i: The index of the wanted TerrainTile

        Returns:
            The requested TerrainTile or `None` if it doesn't exist
        """
        try:
            return self.get_tile(tile, i)
        except (IndexError, ValueError):
            return None

    def get_square_1d(self, area: AreaT) -> list[TerrainTile]:
        """
        Get a rectangular area of TerrainTiles in a one-dimensional list

        Args:
            area: The location (x1,y1,x2,y2) of the wanted area

        Returns:
            A one-dimensional list of TerrainTiles based on given area
        """
        result = []
        for row in self._get_square_rows(area):
            result.extend(row)
        return result

    def get_square_2d(self, area: AreaT) -> list[list[TerrainTile]]:
        """
        Get a rectangular area of TerrainTiles in a two-dimensional list

        Args:
            area: The location (x1,y1,x2,y2) of the wanted area

        Returns:
            A two-dimensional list (of lists) of TerrainTiles based on given area
        """
        return [row for row in self._get_square_rows(area)]

    def _get_square_rows(self, area: AreaT) -> Generator[list[TerrainTile], None, None]:
        """
        Returns rows of TerrainTiles in a list one by one through a generator

        Args:
            area: The location (x1,y1,x2,y2) of the wanted area

        Returns:
            A generator generating single rows of TerrainTiles
        """
        area = Area.from_value(area)

        for y in range(area.height):
            i1 = xy_to_i(area.x1, y, self.map_size)
            i2 = xy_to_i(area.x2, y, self.map_size)
            tiles = self.terrain[i1:i2 + 1]
            yield tiles

    def set_elevation(self, area: AreaT, elevation: int) -> None:
        """
        Sets elevation like the in-game elevation mechanics.
        Can set a hill to a certain height and all tiles around it are adjusted accordingly.

        Args:
            area: The location (x1,y1,x2,y2) of the wanted area
            elevation: The elevation height to create within the given area
        """
        tiles: set[Tile]

        area = Area.from_value(area)

        if area.surface_area == 1:
            result = self.terrain_from(area.corner1)

            tiles = {area.corner1}
            edge_tiles = [area.corner1]
        else:
            area_pattern = AreaPattern(area, map_size = self.map_size)

            result = self.terrain_from(area_pattern)

            tiles = {*area_pattern.to_coords()}
            edge_tiles = area_pattern.use_only_edge().to_coords()

        # Set the given area to the right elevation
        for terrain in result.values():
            terrain.elevation = elevation

        for terrain_tile in self.terrain_from(edge_tiles).values():
            self._update_elevation_around_terrain_tile(terrain_tile, tiles)

    def _update_elevation_around_terrain_tile(
        self,
        terrain_tile: TerrainTile,
        initial: set[Tile],
        visited: set[Tile] = None
    ):
        """
        Updates the elevation around the given TerrainTile and calls itself for all surrounding neighbours
        that need to be updated.

        Args:
            terrain_tile: The TerrainTile to check around
            initial: The Tiles from the initial square
            visited: The visited Tiles with this recursion tree path
        """
        tile = terrain_tile.tile

        visited = set() if visited is None else visited.copy()
        visited.add(tile)

        for x_offset, y_offset in itertools.product(range(-1, 2), repeat = 2):
            if x_offset == 0 and y_offset == 0:
                continue

            xx, yy = tile.x + x_offset, tile.y + y_offset

            neighbour_tile = Tile(xx, yy)
            if neighbour_tile in initial or neighbour_tile in visited:
                continue

            neighbour = self.get_tile_safe(neighbour_tile)
            if neighbour is None:
                continue

            behind = self.get_tile_safe((tile.x + x_offset * 2, tile.y + y_offset * 2))
            if behind is None:
                continue

            if neighbour.elevation < terrain_tile.elevation == behind.elevation:
                neighbour.elevation = terrain_tile.elevation
            elif abs(neighbour.elevation - terrain_tile.elevation) > 1:
                neighbour.elevation = terrain_tile.elevation + int(sign(neighbour.elevation, terrain_tile.elevation))
                self._update_elevation_around_terrain_tile(neighbour, initial, visited)
