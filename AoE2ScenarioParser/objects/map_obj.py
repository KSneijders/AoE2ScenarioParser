from __future__ import annotations

from typing import List

from AoE2ScenarioParser.helper.retriever import RetrieverObjectLink
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.terrain_obj import TerrainObject


class MapObject(AoE2Object):
    """Manager of the everything map related."""

    _link_list = [
        RetrieverObjectLink("map_color_mood", "MapPiece.map_color_mood"),
        RetrieverObjectLink("collide_and_correct", "MapPiece.collide_and_correct"),
        RetrieverObjectLink("villager_force_drop", "MapPiece.villager_force_drop"),
        RetrieverObjectLink("map_width", "MapPiece.map_width"),
        RetrieverObjectLink("map_height", "MapPiece.map_height"),
        RetrieverObjectLink("terrain", "MapPiece.terrain_data", process_as_object=TerrainObject),
    ]

    def __init__(self,
                 map_color_mood: str,
                 collide_and_correct: bool,
                 villager_force_drop: bool,
                 map_width: int,
                 map_height: int,
                 terrain: List[TerrainObject]
                 ):
        if map_width != map_height:
            raise ValueError("Age of Empires II:DE Does not support non-square maps.")

        self.map_color_mood = map_color_mood
        self.collide_and_correct = collide_and_correct
        self.villager_force_drop = villager_force_drop
        self._map_width = map_width
        self._map_height = map_height
        self.terrain = terrain
        super().__init__()

    @property
    def map_size(self) -> int:
        if self._map_height == self._map_width:
            return self._map_height
        else:
            raise ValueError("Map is not a square. Use the attributes 'map_width' and 'map_height' instead.")

    @map_size.setter
    def map_size(self, val: int):
        self._map_width = val
        self._map_height = val

    @property
    def map_width(self) -> int:
        return self._map_width

    @map_width.setter
    def map_width(self, val: int):
        self._map_width = val

    @property
    def map_height(self) -> int:
        return self._map_height

    @map_height.setter
    def map_height(self, val: int):
        self._map_height = val
