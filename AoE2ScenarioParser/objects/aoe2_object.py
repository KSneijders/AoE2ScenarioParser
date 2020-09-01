import abc
from collections import Iterable
from typing import TYPE_CHECKING

from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.helper.retriever import find_retriever

if TYPE_CHECKING:
    from AoE2ScenarioParser.helper.retriever import RetrieverObjectLink


class AoE2Object:
    def __init__(self):
        pass

    @staticmethod
    @abc.abstractmethod
    def _parse_object(parsed_data, **kwargs):
        pass

    @staticmethod
    @abc.abstractmethod
    def _reconstruct_object(parsed_header, parsed_data, objects, **kwargs):
        pass

    def __repr__(self):
        return str(self.__class__.__name__) + ": " + str(self.__dict__)


def commit_and_overwrite_based_list(obj: AoE2Object, property_name: str):
    """
    This function resets the source (piece/struct) list to the list in the object.
    This can be useful when the list is edited or even replaced directly instead of using functions from the object
    managers.

    `trigger_manager.add_trigger()` - would be a function to edit a list.
    `trigger_manager.triggers = [...]` - would be a direct replacement.

    These direct edits or replacement disconnect the connection every object has to it's corresponding piece or struct.
    To 'restore' these (read replace) run this function. It will completely overwrite the source to the current object
    state.
    Use with caution!
    """
    if not obj._based:
        raise ValueError("Cannot reset and overwrite an unbased object.")

    object_list = obj.__getattribute__(property_name)
    if isinstance(object_list, Iterable):
        for sub_obj in object_list:
            sub_obj._based = False
        retriever_object_link: RetrieverObjectLink = find_retriever(obj._link_list, property_name)
        exec(f"{retriever_object_link.link} = []", {}, {'pieces': obj._pieces})
        obj._commit([retriever_object_link])


class CommittingUnbasedObjectError(Exception):
    """Raised when committing an object using `.commit()` that is not based on a piece or struct."""


class RemovedFlagRaisedError(Exception):
    """Raised when committing an object using `.commit()` but the object's removed flag has been set to True."""
