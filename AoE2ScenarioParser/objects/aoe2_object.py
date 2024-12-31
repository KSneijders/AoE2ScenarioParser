from __future__ import annotations

from copy import deepcopy
from enum import Enum
from typing import List, Any, Dict, TYPE_CHECKING, Optional
from uuid import UUID

from AoE2ScenarioParser.exceptions.asp_exceptions import UnsupportedAttributeError
from AoE2ScenarioParser.helper.pretty_format import pretty_format_dict
from AoE2ScenarioParser.helper.string_manipulations import add_tabs
from AoE2ScenarioParser.objects.support.uuid_list import NO_UUID
from AoE2ScenarioParser.scenarios.scenario_store import store
from AoE2ScenarioParser.sections.retrievers.construct_progress import ConstructProgress
from AoE2ScenarioParser.sections.retrievers.retriever_object_link_parent import RetrieverObjectLinkParent

if TYPE_CHECKING:
    from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario


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
            setattr(result, k, self._deepcopy_entry(result, k, v, memo))
        return result

    def _deepcopy_entry(self, result, k, v, memo) -> Any:
        if k in ['_sections', '_link_list']:
            return getattr(self, k)
        else:
            return deepcopy(v, memo)

    def get_scenario(self) -> 'AoE2DEScenario':
        """ Get the scenario associated with the current object """
        scenario: Optional['AoE2DEScenario'] = store.get_scenario(uuid=self._uuid)
        if scenario:
            return scenario
        raise ValueError("Unable to fetch associated scenario from detached object")

    @property
    def instance_number_history(self):
        """
        Keeps indexes of the parents of this object. Should NOT be edited. Used for constructing/committing this object
        """
        return self._instance_number_history

    @classmethod
    def construct(cls, uuid: UUID, number_hist: List[int] = None, progress: ConstructProgress = None):
        if number_hist is None:
            number_hist = []

        object_parameters: Dict[str, Any] = {}

        for link in cls._link_list:
            # print(f"\n\nCONSTRUCT [{link.link}]")
            # print(f"'{progress}' (progress (CONSTRUCT))")
            values = link.pull(uuid, number_hist, cls, progress)
            object_parameters.update(values)

        object_parameters['uuid'] = uuid

        return cls(**object_parameters)

    def commit(self, link_list: List[RetrieverObjectLinkParent] = None):
        """
        Commits all changes to the section & struct structure of the object it's called upon.

        Args:
            link_list: a separate list of RetrieverObjectLinks. This way it's possible to commit only specific
                properties instead of all from an object.
        """
        if link_list is None:
            link_list = self._link_list

        for link in reversed(link_list):
            link.push(self._uuid, host_obj=self)

    def _get_object_attrs(self):
        attrs = ["_instance_number_history", "_uuid"]
        for link in self._link_list:
            attrs.extend(link.get_names())
        return attrs

    def __repr__(self):
        attrs = self._get_object_attrs()

        self_dict = {}
        for attr in attrs:
            try:
                value = getattr(self, attr)
            except UnsupportedAttributeError as e:
                continue
            if isinstance(value, Enum):
                self_dict[attr] = value.name
            else:
                self_dict[attr] = value

        return str(self.__class__.__name__) + ": " + add_tabs(pretty_format_dict(self_dict), 1)
