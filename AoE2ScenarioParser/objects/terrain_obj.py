from AoE2ScenarioParser.helper.retriever import RetrieverObjectLink, get_piece_from_retriever_object_link
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object, CommittingUnbasedObjectError, RemovedFlagRaisedError


class TerrainObject(AoE2Object):
    terrain_id: int
    elevation: int
    layer: int

    def __init__(self, pieces=None, instance_number: int = -1):
        if pieces is None and instance_number is not -1:
            raise ValueError("Cannot create a based object with instance_number reference without pieces.")

        self._link_list = [
            RetrieverObjectLink("terrain_id", "MapPiece.terrain_data[__index__].terrain_id"),
            RetrieverObjectLink("elevation", "MapPiece.terrain_data[__index__].elevation"),
            RetrieverObjectLink("layer", "MapPiece.terrain_data[__index__].layer"),
        ]

        self._based: bool = pieces is not None
        """Flag used to determine if an object is based on a corresponding piece or struct"""
        self._removed: bool = False
        """Flag used to determine that this object and it's corresponding piece or struct needs deletion"""

        self._pieces = pieces
        self._instance_number = instance_number

        if not self._based:
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
        if value is not -1:
            self._based = True
        self._hidden_instance_number = value

    def _construct(self):
        for link in self._link_list:
            value = eval(link.link, {}, {
                'pieces': self._pieces,
                '__index__': self._instance_number
            })

            if link.process_as_object is not None:
                value_list = []
                for index, struct in enumerate(value):
                    value_list.append(link.process_as_object(self._pieces, instance_number=index))
                value = value_list

            self.__setattr__(link.name, value)

    def _commit(self):
        if not self._based:
            raise CommittingUnbasedObjectError("Unable to commit unbased object.")
        if self._removed:
            raise RemovedFlagRaisedError("Object's removed flag has been raised. Cannot commit changes.")

        for link in self._link_list:
            if link.process_as_object is not None:
                to_struct = get_piece_from_retriever_object_link(self._pieces, link)
                object_list = self.__getattribute__(link.name)
                for index, obj in enumerate(object_list):
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
