from __future__ import annotations

from typing import List

from AoE2ScenarioParser.helper.retriever import find_retriever
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.terrain_obj import TerrainObject


class MapObject(AoE2Object):
    def __init__(self, map_piece):
        super().__init__(map_piece)

    def dump_raw_data(self, required_attr = ['terrain_id', 'elevation', 'layer']) -> []:
        """
        @param required_attr: list of attribute names that we want to use in the final concatenated list
        @return: terrain attribute values concatenated in a single list
        """
        # Put the required attributes as a list in a list
        raw_attrs = [[getattr(tile, attr) for attr in required_attr] for tile in self.terrain_data]
        # Flatten the list of lists into a simple list
        return [attr for tile in raw_attrs for attr in tile]

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

    @property
    def map_height(self) -> int:
        return self._map_height
