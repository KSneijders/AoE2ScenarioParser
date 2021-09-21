from __future__ import annotations

from typing import List

from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.helper.list_functions import list_chuncks
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.data_objects.terrain_tile import TerrainTile
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink


class MapManager(AoE2Object):
    """Manager of the everything map related."""

    _link_list = [
        RetrieverObjectLink("map_width", "Map", "map_width"),
        RetrieverObjectLink("map_height", "Map", "map_height"),
        RetrieverObjectLink("terrain", "Map", "terrain_data", process_as_object=TerrainTile),
    ]

    def __init__(self,
                 map_width: int,
                 map_height: int,
                 terrain: List[TerrainTile],
                 **kwargs
                 ):
        self._map_width = map_width
        self._map_height = map_height
        self.terrain = terrain
        super().__init__(**kwargs)

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
                    row = next(chunck_gen) + [TerrainTile(host_uuid=self._host_uuid) for _ in range(difference)]
                else:
                    row = [TerrainTile(host_uuid=self._host_uuid) for _ in range(new_size)]
                new_terrain.extend(row)
        self.terrain = new_terrain

    def create_hill(self, x1, y1, x2, y2, elevation) -> None:
        """
        Function that takes the coordinates and the height of a plateau and applies it to the map
        by also setting the surrounding slopes so that it is smooth.

        Args:
            x1 (int): The x coordinate of the west corner
            y1 (int): The y coordinate of the west corner
            x2 (int): The x coordinate of the east corner
            y2 (int): The y coordinate of the east corner
            elevation (int): The elevation of the map. Default in-game = 1, in-game max = 7. If the given value is over
                20 the game camera will 'clip' into the hill. So the in-game camera hovers around the height of 20/21
                when fully zoomed in, without Ultra Graphics.

        :Author:
            pvallet
        """
        for x in range(max(0, x1 - elevation), min(self.map_size, x2 + elevation)):
            for y in range(max(0, y1 - elevation), min(self.map_size, y2 + elevation)):
                if x1 <= x <= x2 and y1 <= y <= y2:
                    intended_elevation = elevation
                else:
                    distance_to_hill = max(x1 - x, x - x2, y1 - y, y - y2)
                    intended_elevation = elevation - distance_to_hill

                tile = self.terrain[helper.xy_to_i(x, y, self.map_size)]
                tile.elevation = max(intended_elevation, tile.elevation)
