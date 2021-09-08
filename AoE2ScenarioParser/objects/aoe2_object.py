from __future__ import annotations

from copy import deepcopy
from typing import List, Type, TYPE_CHECKING, Dict

from AoE2ScenarioParser.helper.exceptions import UnsupportedAttributeError
from AoE2ScenarioParser.helper.pretty_format import pretty_format_dict

if TYPE_CHECKING:
    from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
    from AoE2ScenarioParser.sections.aoe2_file_section import AoE2FileSection


class AoE2Object:
    _link_list: List[RetrieverObjectLink] = []

    def __init__(self, **kwargs):
        self._instance_number_history = []
        self._sections: Dict[str, AoE2FileSection] = {}
        self._scenario_version = None

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, self._deepcopy_entry(k, v))
        return result

    def _deepcopy_entry(self, k, v):
        """Default copy implementation per key for AoE2Object. Created so this logic can be inherited."""
        if k not in ['_sections', '_link_list']:
            val = deepcopy(v)
        else:
            val = getattr(self, k)
        return val

    @classmethod
    def _construct(cls, scenario_version, sections: Dict[str, AoE2FileSection], number_hist=None):
        if number_hist is None:
            number_hist = []

        object_parameters = {}
        for link in cls._link_list:
            if link.support is not None and not link.support.supports(scenario_version):
                error_msg = f_unsupported_string(link, scenario_version)

                def _get(self):
                    raise UnsupportedAttributeError(error_msg)

                def _set(self, val):
                    if val is not None:
                        raise UnsupportedAttributeError(error_msg)

                setattr(cls, link.name, property(_get, _set))
                object_parameters[link.name] = None
            else:
                object_parameters[link.name] = link.construct(sections, scenario_version, number_hist=number_hist)

        obj = cls(**object_parameters)
        obj._sections = sections
        obj._scenario_version = scenario_version

        return obj

    def commit(self, scenario_version, sections=None, local_link_list=None):
        """
        Commits all changes to the section & struct structure of the object it's called upon.

        Args:
            sections (Dict[str, AoE2FileSection]): A list of sections to reference where to commit to.
                If left empty, the sections default to the sections where this object was constructed from.
            scenario_version (str): The current scenario version
            local_link_list (Type[List[RetrieverObjectLink]]): a separate list of RetrieverObjectLinks. This way it's
                possible to commit only specific properties instead of all from an object.
        """
        if self._sections == {} and sections is None:
            raise ValueError("Unable to commit object. No reference to sections set.")
        if scenario_version is None:
            raise ValueError("Scenario version cannot be None.")

        if local_link_list is None:
            local_link_list = self._link_list
        if sections is None:
            sections = self._sections

        for link in local_link_list[::-1]:
            link.commit(sections, scenario_version, host_obj=self)

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
        return str(self.__class__.__name__) + ": " + pretty_format_dict(self_dict)


def f_unsupported_string(link: RetrieverObjectLink, version: str):
    return f"The property '{link.name}' is {link.support}. Current version: {version}.\n"
