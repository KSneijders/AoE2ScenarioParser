from __future__ import annotations

from typing import List

from AoE2ScenarioParser.helper.retriever import find_retriever, RetrieverObjectLink
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.terrain_obj import TerrainObject


class MapObject(AoE2Object):
    map_color_mood: str
    collide_and_correct: bool
    villager_force_drop: bool
    _map_width: int
    _map_height: int
    terrain: List[TerrainObject]

    def __init__(self, parsed_header, parsed_data, instance_number: int = -1):
        self._link_list = [
            RetrieverObjectLink("map_color_mood", "data.MapPiece.map_color_mood"),
            RetrieverObjectLink("collide_and_correct", "data.MapPiece.collide_and_correct"),
            RetrieverObjectLink("villager_force_drop", "data.MapPiece.villager_force_drop"),
            RetrieverObjectLink("_map_width", "data.MapPiece.map_width"),
            RetrieverObjectLink("_map_height", "data.MapPiece.map_height"),
            RetrieverObjectLink("terrain", "data.MapPiece.terrain_data", process_as_object=TerrainObject),
        ]

        self._parsed_header = parsed_header
        self._parsed_data = parsed_data
        self._instance_number = instance_number

        self.construct()

        super().__init__()

    def construct(self):
        for link in self._link_list:
            self.__setattr__(link.name, link.retrieve(self._parsed_header, self._parsed_data, self._instance_number))

    def commit(self):
        for link in self._link_list:
            link.commit(self._parsed_header, self._parsed_data, self.__getattribute__(link.name))

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
        # object_piece = parsed_data['MapPiece']
        # map_width = find_retriever(object_piece.retrievers, "Map Width").data
        # map_height = find_retriever(object_piece.retrievers, "Map Height").data
        # terrain_list = find_retriever(object_piece.retrievers, "Terrain data").data
        # # AoE2 in Game map: Left to top = X. Left to bottom = Y. Tiny map top = [X:119,Y:0]
        # terrain_2d: List[List[TerrainObject]] = []
        #
        # for i in range(0, map_width * map_height):
        #     to = TerrainObject(
        #         terrain_id=find_retriever(terrain_list[i].retrievers, "Terrain ID").data,
        #         elevation=find_retriever(terrain_list[i].retrievers, "Elevation").data,
        #         layer=find_retriever(terrain_list[i].retrievers, "Layer").data
        #     )
        #     map_x = i % map_width
        #     try:
        #         terrain_2d[map_x].append(to)
        #     except IndexError:
        #         if len(terrain_2d) <= map_x:
        #             terrain_2d.append([])
        #             terrain_2d[map_x].append(to)
        #
        # return MapObject(
        #     map_color_mood=find_retriever(object_piece.retrievers, "Map color mood").data,
        #     collide_and_correct=find_retriever(object_piece.retrievers, "Collide and Correcting").data,
        #     villager_force_drop=find_retriever(object_piece.retrievers, "Villager Force Drop").data,
        #     map_width=map_width,
        #     map_height=map_height,
        #     terrain=terrain_2d,
        # )
        pass

    @staticmethod
    def _reconstruct_object(parsed_header, parsed_data, objects, **kwargs):
        pass
