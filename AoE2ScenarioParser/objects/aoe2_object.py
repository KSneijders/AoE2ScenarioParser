from __future__ import annotations

from collections import OrderedDict
from typing import List, Type, TYPE_CHECKING

from AoE2ScenarioParser.helper import helper

if TYPE_CHECKING:
    from typing import OrderedDict as OrderedDictType
    from AoE2ScenarioParser.helper.retriever import RetrieverObjectLink
    from AoE2ScenarioParser.pieces.aoe2_piece import AoE2Piece


class AoE2Object:
    _link_list: List[RetrieverObjectLink] = []

    def __init__(self, **kwargs):
        self._instance_number_history = []
        self._pieces: OrderedDictType[str, AoE2Piece] = OrderedDict()

    @classmethod
    def _construct(cls, pieces: OrderedDictType[str, AoE2Piece], instance_number_history=None):
        if instance_number_history is None:
            instance_number_history = []

        object_parameters: dict = {}
        for link in cls._link_list:
            object_parameters[link.name] = link.construct(pieces, instance_number_history)

        obj = cls(**object_parameters)
        obj._pieces = pieces
        obj._instance_number_history = instance_number_history
        return obj

    def commit(self, pieces: OrderedDictType[str, AoE2Piece] = None, local_link_list: Type[List[RetrieverObjectLink]] = None):
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
        if pieces is None:
            pieces = self._pieces

        for link in local_link_list:
            link.commit(pieces, host_obj=self)

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
        self_dict = self.__dict__
        self_dict['_pieces'] = f"OrderDict"
        return str(self.__class__.__name__) + ": " + helper.pretty_print_dict(self_dict)
