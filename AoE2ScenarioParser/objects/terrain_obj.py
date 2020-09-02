from typing import List

from AoE2ScenarioParser.helper.retriever import RetrieverObjectLink, get_piece_from_retriever_object_link
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object


class TerrainObject(AoE2Object):
    """Object for handling a tile in the map."""

    # List of attributes
    terrain_id: int
    elevation: int
    layer: int

    _link_list = [
        RetrieverObjectLink("terrain_id", "MapPiece.terrain_data[__index__].terrain_id"),
        RetrieverObjectLink("elevation", "MapPiece.terrain_data[__index__].elevation"),
        RetrieverObjectLink("layer", "MapPiece.terrain_data[__index__].layer"),
    ]

    def __init__(self, pieces=None, instance_number: int = -1):
        if pieces is None and instance_number is not -1:
            raise ValueError("Cannot create a based object with instance_number reference without pieces.")

        self._pieces = pieces if pieces is not None else {}
        self._instance_number = instance_number

        if pieces is not None:
            self._construct()

        super().__init__()

    @property
    def _instance_number(self):
        return self._hidden_instance_number

    @_instance_number.setter
    def _instance_number(self, value):
        if value != -1:
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
                print(value[0])

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

    @staticmethod
    def _parse_object(parsed_data, **kwargs):
        pass

    @staticmethod
    def _reconstruct_object(parsed_header, parsed_data, objects, **kwargs):
        pass
