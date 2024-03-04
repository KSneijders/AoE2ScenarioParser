from __future__ import annotations

import pickle
from time import sleep
from typing import Dict, List, Any

from AoE2ScenarioParser import settings
from AoE2ScenarioParser.exceptions.asp_warnings import UpdateDirtyWarning
from AoE2ScenarioParser.helper import bytes_parser, string_manipulations
from AoE2ScenarioParser.helper.bytes_conversions import parse_bytes_to_val, parse_val_to_bytes
from AoE2ScenarioParser.helper.list_functions import listify
from AoE2ScenarioParser.helper.pretty_format import pretty_format_list
from AoE2ScenarioParser.helper.printers import warn, s_print
from AoE2ScenarioParser.sections.dependencies.dependency_action import DependencyAction
from AoE2ScenarioParser.sections.dependencies.retriever_dependency import RetrieverDependency
from AoE2ScenarioParser.sections.retrievers.datatype import DataType


class Retriever:
    """
    A retriever forms the fundamental unit of data in a scenario.
    All retrievers contain only one single value related to a particular thing in the scenario.
    This class is used to correctly interpret and store all the different types of fundamental data that can be
    present in a scenario
    """
    __slots__ = [
        'on_construct',
        'on_commit',
        'on_refresh',
        'name',
        'datatype',
        'is_list',
        'log_value',
        '_data',
        'default_value',
        'is_dirty',
    ]

    on_construct: RetrieverDependency
    on_commit: RetrieverDependency
    on_refresh: RetrieverDependency

    def __init__(
            self,
            name: str,
            default_value: Any = None,
            datatype: DataType = DataType(),
            is_list: bool | None = None,
            log_value: bool = False,
            data: Any = None
    ):
        """
        Args:
            name: The name of the item/piece of information to retrieved. Has to be unique within the Section or Struct
            default_value: The default value of this retriever
            datatype: An instance of the DataType class, specifying the datatype of the retriever
            is_list: If this retriever data should be presented using a list. If None, it's unknown.
            log_value: This will log information about this retriever when (Default: False)
                1. the data linked to it changes,
                2. it is constructed or committed
        """
        self.name: str = name
        self.default_value: Any = default_value
        self.datatype: DataType = datatype
        self.is_list: bool = is_list
        self.log_value: bool = log_value
        self.is_dirty: bool = False
        self._data: Any = data

        if log_value:
            self.datatype.log_value = True
            self.datatype._debug_retriever_name = name

    def get_data_as_bytes(self) -> bytes:
        """
        Get the data of a retriever in byte form

        Returns:
            Bytes that consist of the data from the retriever
        """
        self.update_datatype_repeat()

        if self.data is not None and self.datatype.repeat != 0:
            result = []
            if self.datatype.type == "struct":
                if isinstance(self.data, list):
                    for struct in self.data:
                        result.append(struct.get_data_as_bytes())
                else:
                    result.append(self.data.get_data_as_bytes())
            else:
                try:
                    for value in listify(self.data):
                        result.append(parse_val_to_bytes(self, value))
                except Exception as e:
                    print("\nException occurred during non-struct list creation: ")
                    print(self)
                    print(pretty_format_list(result))
                    raise e

            joined_result = b''.join(result)
        else:
            joined_result = b''

        if self.log_value:
            print(f"{self.to_simple_string()} (Data: {self.data}) retrieved: {joined_result}")

        return joined_result

    def set_data_from_bytes(self, bytes_list: List[bytes]) -> None:
        """
        Sets the data of a retriever from the list of bytes provided.

        Args:
            bytes_list (List(bytes)): a list of bytes

        Raises:
            ValueError: if no bytes are provided or if the repeat value of the retriever is not equal to the length of
                the list of bytes provided
        """
        if self.datatype.repeat > 0 and len(bytes_list) == 0:
            raise ValueError("Unable to set bytes when no bytes are given")
        if self.datatype.repeat > 0 and self.datatype.repeat != len(bytes_list):
            raise ValueError(f"Unable to set bytes when bytes list isn't equal to repeat (repeat: {self.datatype.repeat} vs list: {len(bytes_list)})")

        result = [parse_bytes_to_val(self, entry_bytes) for entry_bytes in bytes_list]
        self.data = bytes_parser.vorl(self, result)

    def update_datatype_repeat(self) -> None:
        """Sets all the datatype repeat values to the lengths of their containing lists"""
        if type(self.data) is list:
            self.datatype.repeat = len(self.data)

    @property
    def data(self):
        """The data contained in the retriever"""
        return self._data

    @data.setter
    def data(self, value):
        self.set_data(value)

    def set_data(self, value, affect_dirty: bool = True) -> None:
        """
        Setter wrapper to be able to circumvent updating the `dirty` attribute when called internally.

        Args:
            value: The value to set the data to
            affect_dirty: If the `dirty` attribute should be affected (set to true) by updating the data
        """
        if self.is_dirty and not affect_dirty:
            if settings.ALLOW_DIRTY_RETRIEVER_OVERWRITE:
                warn(f"Attribute {self.name} was overwritten by a writing process.", category=UpdateDirtyWarning)
            else:
                return
    
        if self.log_value:
            old_value = self._data
            self.print_value_update(old_value, value)

        # If repeat is 0 and value being said is truthy (mainly not an empty list) set repeat to one (convenience)
        if self.datatype.repeat == 0 and value:
            self.datatype.repeat = 1

        if affect_dirty and self._data is not None:
            self.is_dirty = True
        self._data = value

    def set_data_to_default(self):
        """Sets the values of all the data in the retriever to their default values"""
        if self.datatype.type == "data":
            data = bytes.fromhex(self.default_value)
        elif type(self.default_value) is list:
            data = self.default_value.copy()
        else:
            data = self.default_value

        self.data = data

    def duplicate(self) -> Retriever:
        """
        Creates and returns a copy of the retriever object

        Returns:
            A Retriever instance
        """
        retriever = Retriever(
            name=self.name,
            default_value=self.default_value,
            datatype=self.datatype.duplicate(),
            is_list=self.is_list,
            log_value=self.log_value
        )
        for attr in ['on_refresh', 'on_construct', 'on_commit']:
            if hasattr(self, attr):
                setattr(retriever, attr, getattr(self, attr))
        return retriever

    @classmethod
    def from_structure(cls, name: str, structure: dict) -> Retriever:
        """
        Creates a Retriever object from the given name and structure

        Args:
            name: The name of the retriever to create
            structure: A dict representation of the specified retriever's properties

        Returns:
            A Retriever instance
        """

        datatype = DataType(var=structure.get('type'), repeat=structure.get('repeat', 1))
        retriever = cls(
            name=name,
            default_value=structure.get('default'),
            datatype=datatype,
            is_list=structure.get('is_list', None),
            log_value=structure.get('log', False)
        )
        # Go through dependencies if exist, else empty dict
        for dependency_name, properties in structure.get('dependencies', {}).items():
            if type(properties) is not list:
                r_dep = RetrieverDependency.from_structure(properties)
                _evaluate_is_list_attribute(retriever, r_dep)
                setattr(retriever, dependency_name, r_dep)
            else:
                dependency_list = []
                for dependency_struct in properties:
                    r_dep = RetrieverDependency.from_structure(dependency_struct)
                    _evaluate_is_list_attribute(retriever, r_dep)
                    dependency_list.append(r_dep)
                setattr(retriever, dependency_name, dependency_list)

        return retriever

    def print_value_update(self, old: Any, new: Any) -> None:
        """
        Prints when data is changed. Can also be called for when data is changed but the property doesn't fire.
        This happens when an array is adjusted in size by appending to it ([...] += [...]).

        Prints the retriever, its new value and its old value

        Args:
            old: The old value
            new: The new value
        """
        print(f"{self.to_simple_string()} >>> set to: {string_manipulations.q_str(new)} "
              f"(was: {string_manipulations.q_str(old)})")

    def get_short_str(self):
        """
        Get a shorter string representation of the retriever containing its name, datatype and data

        Returns:
            A shorter string representation of the retriever
        """
        if self.data is not None:
            if type(self.data) is list:
                data = pretty_format_list(self.data)
            else:
                data = string_manipulations.q_str(self.data)
        else:
            data = "<None>"
        return f"{self.name} ({self.datatype.to_simple_string()}): {data}"

    def to_simple_string(self):
        """
        Get a string representation of the retriever containing its name, datatype, and default values

        Returns:
            A string representation of the retriever
        """
        return f"[Retriever] {self.name}: {self.datatype} (Default: {string_manipulations.q_str(self.default_value)})"

    def __repr__(self):
        if type(self.data) is list:
            data = str(pretty_format_list(self.data))
        else:
            data = string_manipulations.q_str(self.data)
        return f"{self.to_simple_string()} >>> {data}"


def duplicate_retriever_map(retriever_map: Dict[str, Retriever]) -> Dict[str, Retriever]:
    """
    Copies and returns the given dict of retrievers. This method is preferred over copy() or deepcopy()
    because of speed. Yes.

    Args:
        retriever_map: A dictionary with strings as keys and Retrievers as their values

    Returns:
        A copied version of the given dictionary
    """
    return pickle.loads(pickle.dumps(retriever_map))


def reset_retriever_map(retriever_map: Dict[str, Retriever]) -> None:
    """
    Sets all the values of the retrievers in the map to their default values.

    Args:
        retriever_map: The retriever map with retrievers to reset
    """
    for retriever in retriever_map.values():
        retriever.set_data_to_default()


def _evaluate_is_list_attribute(retriever: Retriever, dependency: RetrieverDependency) -> None:
    """
    Sets the is_list attribute of the given retriever to true if the dependency action of the specified
    dependency is SET_REPEAT and if the is_list attribute is not already set

    Args:
        retriever: The retriever to change the is_list value for
        dependency: The dependency to check the action for
    """
    if dependency.dependency_action == DependencyAction.SET_REPEAT and retriever.is_list is None:
        retriever.is_list = True
