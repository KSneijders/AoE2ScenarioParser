from __future__ import annotations

from typing import List, Type, TYPE_CHECKING

from AoE2ScenarioParser.helper.retriever import RetrieverObjectLink
from AoE2ScenarioParser.pieces.aoe2_piece import AoE2Piece

if TYPE_CHECKING:
    from typing import OrderedDict


class AoE2Object:
    _link_list: List[RetrieverObjectLink] = []

    def __init__(self, **kwargs):
        self._hidden_instance_number = -1
        self._instance_number_history = []
        self._pieces: List[AoE2Piece] = []

    @classmethod
    def _construct(cls, pieces: OrderedDict[str, AoE2Piece], instance_number_history=None):
        if instance_number_history is None:
            instance_number_history = []

        instance_number = AoE2Object.get_instance_number(instance_number_history=instance_number_history)

        object_parameters: dict = {}
        for link in cls._link_list:
            if link.retrieve_instance_number:
                value = instance_number
            elif link.retrieve_history_number != -1:
                value = instance_number_history[link.retrieve_history_number]
            else:
                special_result = link._process_special_link(pieces)
                if special_result is not None:
                    value = special_result
                else:
                    # Use temp_link to not change the actual links as they are class attributes
                    temp_link = link.link
                    if instance_number_history:
                        for i in instance_number_history:
                            temp_link = temp_link.replace("__index__", str(i), 1)
                    value = eval(temp_link, {}, {'pieces': pieces, '__index__': instance_number})

                    if link.process_as_object is not None:
                        value_list = []
                        for index, struct in enumerate(value):
                            value_list.append(
                                link.process_as_object._construct(
                                    pieces,
                                    instance_number_history=instance_number_history + [index]
                                )
                            )
                        value = value_list

            object_parameters[link.name] = value

        obj = cls(**object_parameters)
        obj._pieces = pieces
        obj._instance_number = instance_number
        obj._instance_number_history = instance_number_history
        return obj

    def commit(self, pieces: Type[List[AoE2Piece]] = None, local_link_list: Type[List[RetrieverObjectLink]] = None):
        """
        Commits all changes to the piece & struct structure of the object it's called upon.

        Args:
            pieces: A list of pieces to reference where to commit to. If left empty, the pieces default to the pieces
                where this object was constructed from. When this object wasn't present when the file was read it's not
                possible to use the
            local_link_list: a separate list of RetrieverObjectLinks. This way it's possible to commit only specific
                properties instead of all from an object.
        """
        if self._pieces == {} and pieces is None:
            raise ValueError("Unable to commit object. No reference to pieces set.")

        if local_link_list is None:
            local_link_list = self._link_list

        instance_number = AoE2Object.get_instance_number(obj=self)

        for link in local_link_list:
            if link.process_as_object is not None:
                object_list: List[AoE2Object] = self.__getattribute__(link.name)
                link_piece = link.get_piece_datatype(self._pieces)

                exec(f"{link.link} = [link_piece() for x in range(r)]", locals(), {
                    'pieces': self._pieces,
                    'link_piece': link_piece,
                    'r': len(object_list)
                })

                for index, obj in enumerate(object_list):
                    obj._pieces = self._pieces
                    obj._instance_number = index
                    obj.commit()

            else:
                exec(link.link + " = value", {}, {
                    'pieces': self._pieces,
                    'value': self.__getattribute__(link.name),
                    '__index__': instance_number
                })

    @staticmethod
    def get_instance_number(obj: AoE2Object = None, instance_number_history=None) -> int:
        if obj is None and instance_number_history is None:
            raise ValueError("The use of the parameter 'obj' or 'instance_number_history' is required.")
        if obj is not None and instance_number_history is not None:
            raise ValueError("Cannot use both the parameter 'obj' and 'instance_number_history'.")

        if instance_number_history is None and obj is not None:
            instance_number_history = obj._instance_number_history
        return instance_number_history[-1] if len(instance_number_history) > 0 else -1

    def __repr__(self):
        return str(self.__class__.__name__) + ": " + str(self.__dict__)
