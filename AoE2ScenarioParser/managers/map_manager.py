from __future__ import annotations

import itertools
import math
from collections import deque
from collections.abc import Iterable
from typing import Sequence

from binary_file_parser import Manager, ret, RetrieverRef
from ordered_set import OrderedSet
from typing_extensions import Literal

from AoE2ScenarioParser.helper.coordinates import i_to_xy
from AoE2ScenarioParser.helper.list_functions import list_chunks, tuple_chunks
from AoE2ScenarioParser.helper.maffs import sign
from AoE2ScenarioParser.managers.support import TerrainDataSupport
from AoE2ScenarioParser.objects.support import (
    Area, AreaPattern, AreaT, TerrainData, Tile,
    TileSequence, TileT,
)
from AoE2ScenarioParser.objects.support.enums.direction import Direction
from AoE2ScenarioParser.sections import MapData, Options, ScenarioSections, Settings, TerrainTile


class MapManager(Manager):
    _struct: ScenarioSections

    # @formatter:off
    color_mood: str             = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.options), ret(Options.color_mood))
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
            invalid = next((len(row) for row in value if len(row) != map_size), None)
            if invalid is not None:
                raise ValueError(
                    f"Encountered unexpected length for nested sequence, "
                    f"expected sequence with: {map_size}x{map_size}. Found length: {invalid}"
                )

            self._terrain_2d = tuple(map(tuple, value))
            self._terrain = list(itertools.chain(*value))
        elif isinstance(value, Sequence) and isinstance(first, TerrainTile):
            value: Sequence[TerrainTile]  # ThxPyCharm

            if math.sqrt(len(value)) % 1 != 0:
                raise ValueError(
                    f"Invalid length for terrain sequence, should be perfect square. Got: {len(value)}"
                )

            map_size = math.floor(math.sqrt(len(value)))

            self._terrain_2d = tuple_chunks(value, map_size)
            self._terrain = list(value)
        else:
            raise ValueError("Invalid value given for terrain")

        # Assign a Tile reference to all TerrainTiles for ease of access
        for y, row in enumerate(self._terrain_2d):
            for x, tile in enumerate(row):
                if not isinstance(tile, TerrainTile):
                    raise TypeError(f"Invalid object in terrain sequence. Tile: ({x},{y}) & Type: `{type(tile)}`")
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
        self.change_map_size(map_size = value, direction = Direction.EAST)

    def shrink_map_by(
        self,
        shrink_by: int,
        direction: Direction = Direction.EAST,
        unit_overflow_action: Literal['remove', 'error'] = 'error',
        trigger_overflow_action: Literal['remove', 'error'] = 'error',
    ) -> OrderedSet[Tile]:
        """
        Shrink the map by the given value from the given direction. Also moves units & triggers to their new relative
        location if necessary.

        Args:
            shrink_by: The size to expand the map by (with a 20x20 map, setting this to 10, would result in a 30x30 map)
            direction: The direction to where the map is increased. (New area is created at this corner)
            unit_overflow_action: What action should be taken with units if they are out of the map after shrinking it.
            trigger_overflow_action: What action should be taken with triggers (effects / conditions) if they are
                partially out of the map after shrinking it.

        See Also:
            ``change_map_size``: For more information on specifics
        """
        return self.change_map_size(
            map_size = self.map_size - shrink_by,
            direction = direction,
            unit_overflow_action = unit_overflow_action,
            trigger_overflow_action = trigger_overflow_action
        )

    def expand_map_by(
        self,
        expand_by: int,
        direction: Direction = Direction.EAST,
        terrain_template: TerrainTile = None,
    ) -> OrderedSet[Tile]:
        """
        Expand the map by the given value in the given direction. Also moves units & triggers to their new relative
        location if necessary.

        Args:
            expand_by: The size to expand the map by (with a 20x20 map, setting this to 10, would result in a 30x30 map)
            direction: The direction to where the map is increased. (New area is created at this corner)
            terrain_template: The tile template to use for all new tiles that will be created. Use a TerrainTile
                instance as a Template like: ```TerrainTile(...)``.

        See Also:
            change_map_size: For more information
        """
        return self.change_map_size(
            map_size = self.map_size + expand_by,
            direction = direction,
            terrain_template = terrain_template
        )

    def change_map_size(
        self,
        map_size: int,
        direction: Direction = Direction.EAST,
        *,
        terrain_template: TerrainTile = None,
        unit_overflow_action: Literal['remove', 'error'] = 'error',
        trigger_overflow_action: Literal['remove', 'error'] = 'error',
    ) -> OrderedSet[Tile]:
        """
        Change the map size from the given direction. The direction indicates from which corner it will shrink or
        expand. So given direction ``Direction.NORTH`` means both shrinking or expanding changes than section of the
        map and the south section is completely not effected. Also moves units & triggers to their new relative
        location if necessary.

        Args:
            map_size: The new map size of the map (with a 20x20 map, setting this to 10, would result in a 10x10 map)
            direction: The direction from which the map is affected
            terrain_template: The tile template to use for all new tiles that will be created. Use a TerrainTile
                instance as a Template like: ```TerrainTile(...)``.
            unit_overflow_action: What action should be taken with units if they are out of the map after shrinking it.
            trigger_overflow_action: What action should be taken with triggers (effects / conditions) if they are
                partially out of the map after shrinking it.
        """
        if map_size == self.map_size:
            return OrderedSet()

        diff = map_size - self.map_size
        is_expansion = diff > 0
        abs_diff = abs(diff)

        x_offset = abs_diff if direction in (Direction.SOUTH, Direction.WEST) else 0
        y_offset = abs_diff if direction in (Direction.NORTH, Direction.WEST) else 0

        original_area = self.new_area_pattern().move(x_offset, y_offset)

        # Todo: !!!!!!! ADD TESTSS!!! NOT TESTED YET!!
        # Todo: !Move units using: ``self._struct.unit_manager...``
        # Todo: !Move trigger  using: ``self._struct.trigger_manager...``

        terrain_support = TerrainDataSupport(self)
        self.terrain = terrain_support.compute_resized_terrain_data(
            new_map_size = map_size,
            direction = direction,
            terrain_template = terrain_template
        )

        if is_expansion:
            # Fix elevation of newly generated tiles
            outline_original_area = original_area.copy().use_only_edge(line_width = 1)

            # terrain_tiles = self.terrain_from(outline_original_area)
            # protected_tiles = set(terrain_tiles.keys())

            self._update_elevation_around_tiles(outline_original_area.to_coords())

        else:
            ...
            # Todo self._struct.unit_manager(...)
            # Todo self._struct.trigger_manager(...)

        # Shrinking changes the original area coordinates which results in a "difference" below whilst it should never
        # return any tiles. This is faster & prevents the issue caused below.
        if not is_expansion:
            return OrderedSet()

        return self.new_area_pattern() \
            .to_coords() \
            .difference(original_area.to_coords())

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

        def to_tiles(obj: TileSequence | Tile) -> OrderedSet[Tile] | set[Tile]:
            if isinstance(obj, TileSequence):
                return obj.to_tiles()
            if isinstance(obj, Tile):
                return {obj}
            raise TypeError("Invalid argument type, should be either Tile, Area or AreaPattern")

        if isinstance(tile_sequence, (TileSequence, Tile)):
            tile_sequence = [tile_sequence]

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

        x = y = None
        if tile is not None:
            if not Tile.from_value(tile).is_within_bounds(self.map_size, resolve_negative_coords = False):
                raise ValueError('Parameter [tile] needs to be within the bounds of the map')
            x, y = tile

        if i is not None:
            if not 0 <= i < self.map_size:
                raise ValueError('Parameter [i] needs to be [0 <= i < map_size]')
            x, y = i_to_xy(i, self.map_size)

        if x is None or y is None:
            raise ValueError(f'Unable to determine coordinates based on given value: [{tile or i}]')

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
        return list(self.terrain_from(Area.from_value(area)).values())

    def get_square_2d(self, area: AreaT) -> list[list[TerrainTile]]:
        """
        Get a rectangular area of TerrainTiles in a two-dimensional list

        Args:
            area: The location (x1,y1,x2,y2) of the wanted area

        Returns:
            A two-dimensional list (of lists) of TerrainTiles based on given area
        """
        area = Area.from_value(area)

        return list_chunks(self.terrain_from(area).values(), area.width)

    def new_area(self) -> Area:
        """
        Get an area object spanning the entire map::

            ((0, 0), (n - 1, n - 1))

        Returns:
            A new Area object
        """
        return Area((0, 0), (self.map_size - 1, self.map_size - 1))

    def new_area_pattern(self, selection: AreaT | TileT = None) -> AreaPattern:
        """
        Get an area pattern object spanning the given area or the entire map if default

        Args:
            selection: The area-like or tile-like object used for the selection. Defaults to the entire map

        Returns:
            A new AreaPattern object
        """
        return AreaPattern(area = selection or self.new_area(), map_size = self.map_size)

    def set_elevation(self, area: AreaT | TileT, elevation: int) -> None:
        """
        Sets elevation  elevation mechanics.
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

        self._update_elevation_around_tiles(edge_tiles)

    def _update_elevation_around_tiles(self, queue: Iterable[Tile]) -> None:
        """
        Updates the elevation around the given tiles

        Args:
            queue: A queue of tiles that will be checked and tiles around them will be adjusted accordingly
        """
        if not isinstance(queue, deque):
            queue = deque(queue)

        while len(queue):
            tile = queue.popleft()
            terrain_tile = self.get_tile_safe(tile)

            if terrain_tile is None:
                continue

            for x_offset, y_offset in itertools.product(range(-1, 2), repeat = 2):
                if x_offset == 0 and y_offset == 0:
                    continue

                xx, yy = tile.x + x_offset, tile.y + y_offset
                neighbour = self.get_tile_safe((xx, yy))
                if neighbour is None:
                    continue

                if abs(neighbour.elevation - terrain_tile.elevation) > 1:
                    neighbour.elevation = terrain_tile.elevation + sign(neighbour.elevation, terrain_tile.elevation)

                    if neighbour.tile not in queue:
                        queue.append(neighbour.tile)

                xx, yy = tile.x + x_offset * 2, tile.y + y_offset * 2
                behind = self.get_tile_safe((xx, yy))
                if behind is None:
                    continue

                if not neighbour.elevation < terrain_tile.elevation == behind.elevation:
                    continue

                if x_offset == 0 or y_offset == 0:
                    neighbour.elevation = terrain_tile.elevation
                    continue

                edge_adjacent_equal_elevation_count = 0
                neighbour_tile: Tile = neighbour.tile

                for xx_offset, yy_offset in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    neighbour_neighbour = self.get_tile_safe((neighbour_tile.x + xx_offset, neighbour_tile.y + yy_offset))

                    if neighbour_neighbour and neighbour_neighbour.elevation == terrain_tile.elevation:
                        edge_adjacent_equal_elevation_count += 1

                if edge_adjacent_equal_elevation_count != 2:
                    neighbour.elevation = terrain_tile.elevation
