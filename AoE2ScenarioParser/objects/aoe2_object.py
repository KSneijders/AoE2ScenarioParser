from __future__ import annotations

from copy import deepcopy
from typing import List, Type, TYPE_CHECKING

from AoE2ScenarioParser.helper.exceptions import UnsupportedAttributeError
from AoE2ScenarioParser.helper.pretty_format import pretty_format_dict
from AoE2ScenarioParser.scenarios import scenario_store

if TYPE_CHECKING:
    from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink


class AoE2Object:
    _link_list: List[RetrieverObjectLink] = []

    def __init__(self, **kwargs):
        self._instance_number_history = []
        self._host_uuid = kwargs.get('host_uuid', "<<NO_HOST_UUID>>")

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
    def _construct(cls, host_uuid, number_hist=None):
        if number_hist is None:
            number_hist = []

        scenario_version = scenario_store.get_scenario_version(host_uuid)

        object_parameters = {}
        for link in cls._link_list:
            if link.support is not None and not link.support.supports(scenario_version):
                error_msg = f_unsupported_string(link, scenario_version)

                def _get(self):
                    raise UnsupportedAttributeError(error_msg)

                def _set(self, val):
                    if val is not None:
                        raise UnsupportedAttributeError(error_msg)

                # Todo: Runs for each _construct() -- A LOT of overhead
                #  Doesn't work properly when reading an older scenario first, and a newer one later
                #  Properties don't get reset!
                setattr(cls, link.name, property(_get, _set))
                object_parameters[link.name] = None
            else:
                object_parameters[link.name] = link.construct(host_uuid, number_hist=number_hist)

        object_parameters['host_uuid'] = host_uuid
        obj = cls(**object_parameters)

        return obj

    def commit(self, local_link_list=None):
        """
        Commits all changes to the section & struct structure of the object it's called upon.

        Args:
            local_link_list (Type[List[RetrieverObjectLink]]): a separate list of RetrieverObjectLinks. This way it's
                possible to commit only specific properties instead of all from an object.
        """
        if local_link_list is None:
            local_link_list = self._link_list

        for link in local_link_list[::-1]:
            link.commit(self._host_uuid, host_obj=self)

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
