from __future__ import annotations

import pickle
from typing import Dict

from AoE2ScenarioParser import settings
from AoE2ScenarioParser.helper import bytes_parser, string_manipulations
from AoE2ScenarioParser.helper.bytes_conversions import parse_bytes_to_val, parse_val_to_bytes
from AoE2ScenarioParser.helper.list_functions import listify
from AoE2ScenarioParser.helper.pretty_format import pretty_format_list
from AoE2ScenarioParser.helper.printers import warn
from AoE2ScenarioParser.sections.dependencies.dependency_action import DependencyAction
from AoE2ScenarioParser.sections.dependencies.retriever_dependency import RetrieverDependency
from AoE2ScenarioParser.sections.retrievers.datatype import DataType


class Retriever:
    """ A Class for defining how to retrieve data.
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
        'is_dirty',
    ]

    on_construct: RetrieverDependency
    on_commit: RetrieverDependency
    on_refresh: RetrieverDependency

    def __init__(self, name, default_value=None, datatype=DataType(), is_list=None, log_value=False):
        """
        Args:
            name (str): The name of the item. Has to be unique within the Section or Struct
            default_value (Any): The default value of this retriever
            datatype (DataType): A datatype object
            is_list (Union[None, bool]): If this retriever data should be presented using a list. If None, it's unknown.
            log_value (bool): A boolean for, mostly, debugging. This will log information about this retrievers when the
                data is changed, when this retriever is constructed and when it's committed.
        """
        self.name: str = name
        self.default_value = default_value
        self.datatype: DataType = datatype
        self.is_list = is_list
        self.log_value = log_value
        self.is_dirty = False
        self._data = None

        if log_value:
            self.datatype.log_value = True
            self.datatype._debug_retriever_name = name

    def get_data_as_bytes(self):
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

    def set_data_from_bytes(self, bytes_list):
        if self.datatype.repeat > 0 and len(bytes_list) == 0:
            raise ValueError("Unable to set bytes when no bytes are given")
        if self.datatype.repeat > 0 and self.datatype.repeat != len(bytes_list):
            raise ValueError("Unable to set bytes when bytes list isn't equal to repeat")

        result = [parse_bytes_to_val(self, entry_bytes) for entry_bytes in bytes_list]
        self.data = bytes_parser.vorl(self, result)

    def update_datatype_repeat(self):
        if type(self.data) == list:
            self.datatype.repeat = len(self.data)

    @property
    def data(self):
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
        if self.name == 'ascii_instructions':
            print(self)

        if self.is_dirty and not affect_dirty:
            if settings.ALLOW_DIRTY_RETRIEVER_OVERWRITE:
                if not settings.DISABLE_DIRTY_RETRIEVER_WARNING:
                    warn(f"Attribute {self.name} was overwritten by a writing process.")
            else:
                return

        if self.log_value:
            old_value = self._data
            self.print_value_update(old_value, value)

        # If repeat is 0 and value being said is truthy (mainly not an empty list) set repeat to one
        if self.datatype.repeat == 0 and value:
            self.datatype.repeat = 1

        if affect_dirty and self._data is not None:
            self.is_dirty = True
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

    def print_value_update(self, old, new) -> None:
        """
        Function to print when data is changed. Can also be called for when data is changed but the property doesn't
        fire. This happens when an array is adjusted in size by appending to it ([...] += [...]).

        Args:
            old (str): The old value represented using a string
            new (str): The new value represented using a string
        """
        print(f"{self.to_simple_string()} >>> set to: {string_manipulations.q_str(new)} "
              f"(was: {string_manipulations.q_str(old)})")

    def get_short_str(self):
        if self.data is not None:
            if type(self.data) is list:
                data = pretty_format_list(self.data)
            else:
                data = string_manipulations.q_str(self.data)
        else:
            data = "<None>"
        return f"{self.name} ({self.datatype.to_simple_string()}): {data}"

    def to_simple_string(self):
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


def _evaluate_is_list_attribute(retriever, dependency):
    if dependency.dependency_action == DependencyAction.SET_REPEAT and retriever.is_list is None:
        retriever.is_list = True


attributes = ['on_refresh', 'on_construct', 'on_commit']
