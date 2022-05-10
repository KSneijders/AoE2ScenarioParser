from __future__ import annotations

from copy import deepcopy
from enum import Enum
from typing import List, Any, Dict

from AoE2ScenarioParser.helper.pretty_format import pretty_format_dict
from AoE2ScenarioParser.helper.string_manipulations import add_tabs
from AoE2ScenarioParser.objects.support.uuid_list import NO_UUID
from AoE2ScenarioParser.sections.retrievers.retriever_object_link_parent import RetrieverObjectLinkParent


class AoE2Object:
    _link_list: List[RetrieverObjectLinkParent] = []

    def __init__(self, **kwargs):
        self._instance_number_history = []
        self._uuid = kwargs.get('uuid', NO_UUID)

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            entry = self._deepcopy_entry(k, v)
            if entry is None:
                continue
            setattr(result, k, entry)
        return result

    @property
    def instance_number_history(self):
        """
        Keeps indexes of the paretns of this object. Should NOT be edited. Used for constructing/committing this object
        """
        return self._instance_number_history

    def _deepcopy_entry(self, k, v):
        if k in ['_sections', '_link_list']:
            val = getattr(self, k)
        else:
            val = deepcopy(v)
        return val

    @classmethod
    def _construct(cls, uuid, number_hist=None):
        if number_hist is None:
            number_hist = []

        object_parameters: Dict[str, Any] = {}

        for link in cls._link_list:
            values = link.pull(uuid, number_hist, cls)
            object_parameters.update(values)

        object_parameters['uuid'] = uuid

        return cls(**object_parameters)

    def commit(self, local_link_list: List[RetrieverObjectLinkParent] = None):
        """
        Commits all changes to the section & struct structure of the object it's called upon.

        Args:
            local_link_list: a separate list of RetrieverObjectLinks. This way it's
                possible to commit only specific properties instead of all from an object.
        """
        if local_link_list is None:
            local_link_list = self._link_list

        for link in reversed(local_link_list):
            link.push(self._uuid, host_obj=self)

    @staticmethod
    def get_instance_number(obj: AoE2Object = None, number_hist=None) -> int:
        if obj is None and number_hist is None:
            raise ValueError("The use of the parameter 'obj' or 'number_hist' is required.")
        if obj is not None and number_hist is not None:
            raise ValueError("Cannot use both the parameter 'obj' and 'number_hist'.")

        if number_hist is None and obj is not None:
            number_hist = obj._instance_number_history
        return number_hist[-1] if len(number_hist) > 0 else None

    def _get_object_attrs(self):
        attrs = ["_instance_number_history", "_uuid"]
        for link in self._link_list:
            attrs.extend(link.get_names())
        return attrs

    def __repr__(self):
        attrs = self._get_object_attrs()

        self_dict = {}
        for attr in attrs:
            value = getattr(self, attr)
            if isinstance(value, Enum):
                self_dict[attr] = value.name
            else:
                self_dict[attr] = value

        return str(self.__class__.__name__) + ": " + add_tabs(pretty_format_dict(self_dict), 1)
