from __future__ import annotations

import pickle
from typing import Dict, List

from AoE2ScenarioParser.helper import bytes_parser, string_manipulations
from AoE2ScenarioParser.helper.bytes_conversions import parse_bytes_to_val, parse_val_to_bytes
from AoE2ScenarioParser.helper.list_functions import listify
from AoE2ScenarioParser.helper.pretty_format import pretty_format_list
from AoE2ScenarioParser.sections.dependencies.dependency_action import DependencyAction
from AoE2ScenarioParser.sections.dependencies.retriever_dependency import RetrieverDependency
from AoE2ScenarioParser.sections.retrievers.datatype import DataType


class Retriever:
    """
    A Class for defining how to retrieve data.
    The Constructor has quite some parameters which can all be used for getting the proper data
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
        # 'string_end_char'
    ]

    on_construct: RetrieverDependency
    on_commit: RetrieverDependency
    on_refresh: RetrieverDependency

    def __init__(self,
        name: str,
        default_value=None,
        datatype: DataType=DataType(),
        is_list: bool=None,
        log_value: bool=False
    ):
        """
        Args:
            name (str): The name of the item/piece of information to retrieved. Has to be unique within the Section or Struct
            default_value: The default value of this retriever
            datatype (DataType): An instance of the DataType class, specifying the datatype of the retriever
            is_list: (bool) If this retriever data should be stored using a list. Unknown if not set
            log_value: (bool) This will log information about this retriever when (Default: False)
                1. the data linked to it changes,
                2. it is constructed or committed
        """
        self.name: str = name
        self.default_value = default_value
        self.datatype: DataType = datatype
        self.is_list = is_list
        self.log_value = log_value
        self._data = None

        if log_value:
            self.datatype.log_value = True
            self.datatype._debug_retriever_name = name

        # self.string_end_char = False

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
                for struct in self.data:
                    result.append(struct.get_data_as_bytes())
            else:
                for value in listify(self.data):
                    result.append(parse_val_to_bytes(self, value))

            joined_result = b''.join(result)
        else:
            joined_result = b''

        if self.log_value:
            print(f"{self.to_simple_string()} (Data: {self.data}) retrieved: {joined_result}")

        return joined_result

    def set_data_from_bytes(self, bytes_list: List[bytes]) -> None:
        """
        This function sets the data of a retriever from the list of bytes provided.

        Args:
            bytes_list (List(bytes)): a list of bytes

        Returns:
            This function does not return anything

        Raises:
            ValueError: if no bytes are provided or if the repeat value of the retriever is not equal to the length of
                the list of bytes provided
        """
        if self.datatype.repeat > 0 and len(bytes_list) == 0:
            raise ValueError("Unable to set bytes when no bytes are given")
        if self.datatype.repeat > 0 and self.datatype.repeat != len(bytes_list):
            raise ValueError("Unable to set bytes when bytes list isn't equal to repeat")

        result = [parse_bytes_to_val(self, entry_bytes) for entry_bytes in bytes_list]
        self.data = bytes_parser.vorl(self, result)

    def update_datatype_repeat(self) -> None:
        """
        This function sets all the datatype repeat values to the lengths of their containing lists

        Returns:
            This function does not return anything
        """
        if type(self.data) == list:
            self.datatype.repeat = len(self.data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if self.log_value:
            old_value = self._data
            self._print_value_update(old_value, value)
        self._data = value

    def set_data_to_default(self):
        if self.datatype.type == "data":
            data = bytes.fromhex(self.default_value)
        elif type(self.default_value) is list:
            data = self.default_value.copy()
            assert data is not self.default_value
        else:
            data = self.default_value

        self.data = data

    def duplicate(self):
        retriever = Retriever(
            name=self.name,
            default_value=self.default_value,
            datatype=self.datatype.duplicate(),
            is_list=self.is_list,
            log_value=self.log_value
        )
        for attr in attributes:
            if hasattr(self, attr):
                setattr(retriever, attr, getattr(self, attr))
        return retriever

    @classmethod
    def from_structure(cls, name, structure):
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

    def _print_value_update(self, old, new) -> None:
        """
        Function to print when data is changed. Can also be called for when data is changed but the property doesn't
        fire. This happens when an array is adjusted in size by appending to it ([...] += [...]).

        This function prints the retriever, its new value and its old value

        Args:
            old (str): The old value represented using a string
            new (str): The new value represented using a string

        Returns:
            This function does not return anything
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
    return pickle.loads(pickle.dumps(retriever_map))


def reset_retriever_map(retriever_map: Dict[str, Retriever]) -> None:
    for retriever in retriever_map.values():
        retriever.set_data_to_default()


def _evaluate_is_list_attribute(retriever: Retriever, dependency: RetrieverDependency) -> None:
    """
    This function sets the is_list attribute of the given retriever to true if the dependency action of the specified
    dependency is SET_REPEAT and if the is_list attribute is not already set

    Args:
        retriever (Retriever): The retriever to change the is_list value for
        dependency (RetrieverDependency): The dependency to check the action for

    Returns:
        This function does not return anything
    """
    if dependency.dependency_action == DependencyAction.SET_REPEAT and retriever.is_list is None:
        retriever.is_list = True


attributes = ['on_refresh', 'on_construct', 'on_commit']
