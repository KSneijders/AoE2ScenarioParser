from __future__ import annotations

from typing import List

from AoE2ScenarioParser.helper.retriever import find_retriever
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.terrain_obj import TerrainObject


class MapObject(AoE2Object):
    def __init__(self,
                 map_color_mood: str,
                 collide_and_correct: bool,
                 villager_force_drop: bool,
                 map_width: int,
                 map_height: int,
                 terrain: List[List[TerrainObject]]
                 ):

        self.map_color_mood: str = map_color_mood
        self.collide_and_correct: bool = collide_and_correct
        self.villager_force_drop: bool = villager_force_drop
        self._map_width: int = map_width
        self._map_height: int = map_height
        self.terrain: List[List[TerrainObject]] = terrain

        super().__init__()

    def iterable_terrain(self):
        """
        Iterate through the terrain as if it were just a list.
        """
        for list in self.terrain:
            for value in list:
                yield value

    def dump_raw_data(self, required_attr = ['terrain_id', 'elevation', 'layer']) -> []:
        """
        @param required_attr: list of attribute names that we want to use in the final concatenated list
        @return: terrain attribute values concatenated in a single list
        """
        # Put the required attributes as a list in a list
        raw_attrs = [[getattr(tile, attr) for attr in required_attr] for tile in self.iterable_terrain()]
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

    @staticmethod
    def _parse_object(parsed_data, **kwargs) -> MapObject:  # Expected {}
        object_piece = parsed_data['MapPiece']
        map_width = find_retriever(object_piece.retrievers, "Map Width").data
        map_height = find_retriever(object_piece.retrievers, "Map Height").data
        terrain_list = find_retriever(object_piece.retrievers, "Terrain data").data
        # AoE2 in Game map: Left to top = X. Left to bottom = Y. Tiny map top = [X:119,Y:0]
        terrain_2d: List[List[TerrainObject]] = []

        for i in range(0, map_width * map_height):
            to = TerrainObject(
                terrain_id=find_retriever(terrain_list[i].retrievers, "Terrain ID").data,
                elevation=find_retriever(terrain_list[i].retrievers, "Elevation").data,
                layer=find_retriever(terrain_list[i].retrievers, "Layer").data
            )
            map_x = i % map_width
            try:
                terrain_2d[map_x].append(to)
            except IndexError:
                if len(terrain_2d) <= map_x:
                    terrain_2d.append([])
                    terrain_2d[map_x].append(to)

        return MapObject(
            map_color_mood=find_retriever(object_piece.retrievers, "Map color mood").data,
            collide_and_correct=find_retriever(object_piece.retrievers, "Collide and Correcting").data,
            villager_force_drop=find_retriever(object_piece.retrievers, "Villager Force Drop").data,
            map_width=map_width,
            map_height=map_height,
            terrain=terrain_2d,
        )

    @staticmethod
    def _reconstruct_object(parsed_header, parsed_data, objects, **kwargs):
        pass