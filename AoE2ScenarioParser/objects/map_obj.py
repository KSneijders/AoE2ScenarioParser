from __future__ import annotations

from collections import Iterable
from typing import List

from AoE2ScenarioParser.helper.retriever import RetrieverObjectLink, get_piece_from_retriever_object_link
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.terrain_obj import TerrainObject


class MapObject(AoE2Object):
    """Manager of the everything map related."""

    # List of attributes
    map_color_mood: str
    collide_and_correct: bool
    villager_force_drop: bool
    _map_width: int
    _map_height: int
    terrain: List[TerrainObject]

    _link_list = [
        RetrieverObjectLink("map_color_mood", "MapPiece.map_color_mood"),
        RetrieverObjectLink("collide_and_correct", "MapPiece.collide_and_correct"),
        RetrieverObjectLink("villager_force_drop", "MapPiece.villager_force_drop"),
        RetrieverObjectLink("_map_width", "MapPiece.map_width"),
        RetrieverObjectLink("_map_height", "MapPiece.map_height"),
        RetrieverObjectLink("terrain", "MapPiece.terrain_data", process_as_object=TerrainObject),
    ]

    def __init__(self, pieces=None, instance_number: int = -1):
        if pieces is None and instance_number is not -1:
            raise ValueError("Cannot create a based object with instance_number reference without pieces.")

        self._pieces = pieces
        self._instance_number = instance_number

        if pieces is None:
            self._pieces = {}
        else:
            self._construct()

        super().__init__()

    @property
    def _instance_number(self):
        return self._hidden_instance_number

    @_instance_number.setter
    def _instance_number(self, value):
        if self._pieces == {}:
            raise ValueError("Cannot set instance_number reference without pieces.")
        self._hidden_instance_number = value

    def _construct(self):
        for link in self._link_list:
            value = eval(link.link, {}, {'pieces': self._pieces, '__index__': self._instance_number})

            if link.process_as_object is not None:
                value_list = []
                for index, struct in enumerate(value):
                    value_list.append(link.process_as_object(self._pieces, instance_number=index))
                value = value_list

            self.__setattr__(link.name, value)

    def _commit(self, retriever_object_link_list: List[RetrieverObjectLink] = None):
        if retriever_object_link_list is None:
            retriever_object_link_list = self._link_list

        for link in retriever_object_link_list:
            if link.process_as_object is not None:
                object_list: List[AoE2Object] = self.__getattribute__(link.name)
                link_piece = get_piece_from_retriever_object_link(self._pieces, link)

                exec(f"{link.link} = [link_piece() for x in range(r)]", locals(), {
                    'pieces': self._pieces,
                    'link_piece': link_piece,
                    'r': len(object_list)
                })

                for index, obj in enumerate(object_list):
                    obj._pieces = self._pieces
                    obj._instance_number = index
                    obj._commit()

            else:
                exec(link.link + " = value", {}, {
                    'pieces': self._pieces,
                    'value': self.__getattribute__(link.name),
                    '__index__': self._instance_number
                })

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
