from __future__ import annotations

from collections import OrderedDict
from copy import deepcopy
from typing import List, Type, TYPE_CHECKING

from AoE2ScenarioParser.helper import helper

if TYPE_CHECKING:
    from typing import OrderedDict as OrderedDictType
    from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
    from AoE2ScenarioParser.sections.aoe2_file_section import AoE2FileSection


class AoE2Object:
    _link_list: List[RetrieverObjectLink] = []

    def __init__(self, **kwargs):
        self._instance_number_history = []
        self._sections: OrderedDictType[str, AoE2FileSection] = OrderedDict()

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            if k not in ['_sections']:
                val = deepcopy(v)
            else:
                val = getattr(self, k)
            setattr(result, k, val)
        return result

    @classmethod
    def _construct(cls, sections: OrderedDictType[str, AoE2FileSection], instance_number_history=None):
        if instance_number_history is None:
            instance_number_history = []

        object_parameters: dict = {}
        for link in cls._link_list:
            object_parameters[link.name] = link.construct(sections, instance_number_history)

        obj = cls(**object_parameters)
        obj._sections = sections
        return obj

    def commit(self, sections=None, local_link_list=None):
        """
        Commits all changes to the section & struct structure of the object it's called upon.

        Args:
            sections (OrderedDictType[str, AoE2FileSection]): A list of sections to reference where to commit to. If left empty,
                the sections default to the sections where this object was constructed from.
            local_link_list (Type[List[RetrieverObjectLink]]): a separate list of RetrieverObjectLinks. This way it's
                possible to commit only specific properties instead of all from an object.
        """
        if self._sections == {} and sections is None:
            raise ValueError("Unable to commit object. No reference to sections set.")

        if local_link_list is None:
            local_link_list = self._link_list
        if sections is None:
            sections = self._sections

        for link in local_link_list[::-1]:
            link.commit(sections, host_obj=self)

    @staticmethod
    def get_instance_number(obj: AoE2Object = None, number_hist=None) -> int:
        if obj is None and number_hist is None:
            raise ValueError("The use of the parameter 'obj' or 'number_hist' is required.")
        if obj is not None and number_hist is not None:
            raise ValueError("Cannot use both the parameter 'obj' and 'number_hist'.")

        if number_hist is None and obj is not None:
            number_hist = obj._instance_number_history
        return number_hist[-1] if len(number_hist) > 0 else None

    def __repr__(self):
        self_dict = self.__dict__
        self_dict['_sections'] = f"OrderDict"
        return str(self.__class__.__name__) + ": " + helper.pretty_print_dict(self_dict)
