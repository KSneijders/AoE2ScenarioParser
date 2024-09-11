from __future__ import annotations

import itertools
from typing import Generator

from binary_file_parser import Manager, RetrieverRef

from AoE2ScenarioParser.helper.coordinates import xy_to_i
from AoE2ScenarioParser.helper.maffs import sign
from AoE2ScenarioParser.helper.support import r
from AoE2ScenarioParser.objects.support import Area, AreaPattern, AreaT, Tile, TileT
from AoE2ScenarioParser.sections import MapData, Options, ScenarioSections, Settings, TerrainTile


class MapManager(Manager):
    # @formatter:off
    color_mood: str            = RetrieverRef(r(ScenarioSections.settings), r(Settings.options), r(Options.color_mood))
    collide_and_correct: bool  = RetrieverRef(r(ScenarioSections.settings), r(Settings.options), r(Options.collide_and_correct))
    villager_force_drop: bool  = RetrieverRef(r(ScenarioSections.settings), r(Settings.options), r(Options.villager_force_drop))
    terrain: list[TerrainTile] = RetrieverRef(r(ScenarioSections.map_data), r(MapData.terrain_tiles))
    _map_width: int            = RetrieverRef(r(ScenarioSections.map_data), r(MapData.width))
    _map_height: int           = RetrieverRef(r(ScenarioSections.map_data), r(MapData.height))
    # @formatter:on

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

        self._map_width = value
        self._map_height = value

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
        if i and tile:
            raise ValueError('Cannot use both parameters `tile` & `i`')

        if i is not None:
            if 0 <= i < self.map_size:
                return self.terrain[i]
            else:
                raise ValueError('Parameter `i` needs to be: 0 <= i < map_size')

        tile = Tile.from_value(tile)
        return self.terrain[tile.to_i(self.map_size)]

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
            tiles = {area.corner1}
            edge_tiles = [area.corner1]
        else:
            area_pattern = AreaPattern(area, map_size = self.map_size)

            tiles = {*area_pattern.to_coords()}
            edge_tiles = area_pattern.use_only_edge().to_coords()

        # Set the given area to the right elevation
        for tile in tiles:
            self.get_tile(tile).elevation = elevation


        for tile in edge_tiles:
            self._elevation_tile_recursion(tile, tiles)

    def _elevation_tile_recursion(
        self,
        tile: Tile,
        xys: set[Tile],
        visited: set[Tile] = None
    ):
        """
        Elevation recursive function. Used in the set_elevation function

        Args:
            tile: The Tile to check around
            xys: The Tiles from the initial square
            visited: The visited Tiles with this recursion tree path
        """
        visited = set() if visited is None else visited.copy()
        visited.add(tile)

        for x_offset, y_offset in itertools.product(range(-1, 2), repeat = 2):
            if x_offset == 0 and y_offset == 0:
                continue

            xx, yy = tile.x + x_offset, tile.y + y_offset

            neighbour_tile = Tile(xx, yy)
            if neighbour_tile in xys or neighbour_tile in visited:
                continue

            neighbour = self.get_tile_safe(neighbour_tile)
            if neighbour is None:
                continue

            behind = self.get_tile_safe((tile.x + x_offset * 2, tile.y + y_offset * 2))
            if behind is None:
                continue

            source = self.get_tile(tile)

            if neighbour.elevation < source.elevation == behind.elevation:
                neighbour.elevation = source.elevation
            elif abs(neighbour.elevation - source.elevation) > 1:
                neighbour.elevation = source.elevation + int(sign(neighbour.elevation, source.elevation))
                self._elevation_tile_recursion(neighbour_tile, xys, visited)
