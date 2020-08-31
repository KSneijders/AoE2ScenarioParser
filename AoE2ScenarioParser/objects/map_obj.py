from __future__ import annotations

from typing import List

from AoE2ScenarioParser.helper.retriever import RetrieverObjectLink, get_piece_from_retriever_object_link
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object, CommittingUnbasedObjectError, RemovedFlagRaisedError
from AoE2ScenarioParser.objects.terrain_obj import TerrainObject


class MapObject(AoE2Object):
    map_color_mood: str
    collide_and_correct: bool
    villager_force_drop: bool
    _map_width: int
    _map_height: int
    terrain: List[TerrainObject]

    def __init__(self, pieces=None, instance_number: int = -1):
        if pieces is None and instance_number is not -1:
            raise ValueError("Cannot create a based object with instance_number reference without pieces.")

        self._link_list = [
            RetrieverObjectLink("map_color_mood", "MapPiece.map_color_mood"),
            RetrieverObjectLink("collide_and_correct", "MapPiece.collide_and_correct"),
            RetrieverObjectLink("villager_force_drop", "MapPiece.villager_force_drop"),
            RetrieverObjectLink("_map_width", "MapPiece.map_width"),
            RetrieverObjectLink("_map_height", "MapPiece.map_height"),
            RetrieverObjectLink("terrain", "MapPiece.terrain_data", process_as_object=TerrainObject),
        ]

        self._based: bool = pieces is not None
        """Flag used to determine if an object is based on a corresponding piece or struct"""
        self._removed: bool = False
        """Flag used to determine that this object and it's corresponding piece or struct needs to be deleted"""

        self._pieces = pieces
        self._instance_number = instance_number

        if not self._based:
            self._pieces = {}
        else:
            self._construct()

        super().__init__()

    @property
    def _removed(self):
        return self._removed_flag

    @_removed.setter
    def _removed(self, value: bool):
        if value is not False:
            if self._instance_number is -1:
                raise ValueError("Objects without instance_number reference cannot set the removed flag.")
        self._removed_flag = value

    @property
    def _instance_number(self):
        return self._hidden_instance_number

    @_instance_number.setter
    def _instance_number(self, value):
        if self._pieces == {}:
            raise ValueError("Cannot set instance_number reference without pieces.")
        if value is not -1:
            self._based = True
        self._hidden_instance_number = value

    def _construct(self):
        for link in self._link_list:
            value = eval(link.link, {}, {'pieces': self._pieces, '__index__': self._instance_number})

            if link.process_as_object is not None:
                value_list = []
                for index, struct in enumerate(value):
                    value_list.append(link.process_as_object(self._pieces, instance_number=index))
                value = value_list
                print(value[0])

            self.__setattr__(link.name, value)

    def _commit(self):
        print("Committing map_manager...")
        if not self._based:
            raise CommittingUnbasedObjectError("Unable to commit unbased object.")
        if self._removed:
            raise RemovedFlagRaisedError("Object's removed flag has been raised. Cannot commit changes.")

        for link in self._link_list:
            if link.process_as_object is not None:
                object_list: List[TerrainObject] = self.__getattribute__(link.name)
                for index, obj in enumerate(object_list):
                    try:
                        obj._commit()
                    except CommittingUnbasedObjectError:
                        to_struct = get_piece_from_retriever_object_link(self._pieces, link)
                        struct = to_struct()
                        index_to_be = eval(f"len({link.link})", {}, {'pieces': self._pieces})
                        eval(f"{link.link}.append(struct)", {}, {'pieces': self._pieces, 'struct': struct})
                        obj._pieces = self._pieces
                        obj._instance_number = index_to_be
                        obj._commit()
                    except RemovedFlagRaisedError:
                        exec(f"del {link.link}[__index__]", {}, {
                            'pieces': self._pieces,
                            '__index__': self._instance_number
                        })

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
