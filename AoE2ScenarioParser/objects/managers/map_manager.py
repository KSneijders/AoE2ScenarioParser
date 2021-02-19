from __future__ import annotations

from typing import List

from AoE2ScenarioParser.datasets.terrains import Terrain
from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.data_objects.terrain_tile import TerrainTile


class MapManager(AoE2Object):
    """Manager of the everything map related."""

    def __init__(self,
                 map_width: int,
                 map_height: int,
                 terrain: List[TerrainTile]
                 ):
        if map_width != map_height:
            raise ValueError("Age of Empires II:DE Does not support non-square maps.")

        self._map_width = map_width
        self._map_height = map_height
        self.terrain = terrain
        super().__init__()

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
    def map_size(self, size: int):
        new_length = size * size
        difference = new_length - len(self.terrain)

        self._map_width = size
        self._map_height = size

        if difference < 0:
            self.terrain = self.terrain[:new_length]
        elif difference > 0:
            for _ in range(difference):
                self.terrain.append(
                    TerrainTile(
                        Terrain.GRASS_1,
                        elevation=1,
                        layer=-1
                    )
                )

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
