from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from AoE2ScenarioParser.helper import helper, parser
from AoE2ScenarioParser.helper.bytes_to_x import parse_bytes_to_val, parse_val_to_bytes
from AoE2ScenarioParser.sections.retrievers.datatype import DataType
from AoE2ScenarioParser.helper.parser import attributes
from AoE2ScenarioParser.sections.dependencies.retriever_dependency import RetrieverDependency

if TYPE_CHECKING:
    from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink


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
        'potential_list',
        'log_value',
        '_data',
        'default_value'
    ]

    on_construct: RetrieverDependency
    on_commit: RetrieverDependency
    on_refresh: RetrieverDependency

    def __init__(self, name, default_value, datatype=DataType(), potential_list=True, log_value=False):
        """
        Args:
            name (str): The name of the item. Has to be unique within the Section or Struct
            datatype (DataType): A datatype object
            log_value (bool): A boolean for, mostly, debugging. This will log this Retriever with it's data when the
                data is changed, when this retriever is constructed and committed.
        """
        self.name: str = name
        self.default_value = default_value
        self.datatype: DataType = datatype
        if log_value:
            self.datatype.log_value = True
        self.datatype._debug_retriever_name = name
        self.potential_list = potential_list
        self.log_value = log_value
        self._data = None

    def get_data_as_bytes(self):
        self.update_datatype_repeat()

        if self.data is not None and self.datatype.repeat != 0:
            result = []
            if self.datatype.type == "struct":
                for struct in self.data:
                    result.append(struct.get_data_as_bytes())
            else:
                for value in parser.listify(self.data):
                    result.append(parse_val_to_bytes(self, value))

            joined_result = b''.join(result)
        else:
            joined_result = b''

        if self.log_value:
            print(f"{self.to_simple_string()} (Data: {self.data}) retrieved: {joined_result}")

        return joined_result

    def set_data_from_bytes(self, bytes_list):
        if self.datatype.repeat > 0 and len(bytes_list) == 0:
            print(type(bytes_list), bytes_list)
            raise ValueError("Unable to set bytes when no bytes are given")
        if self.datatype.repeat > 0 and self.datatype.repeat != len(bytes_list):
            raise ValueError("Unable to set bytes when bytes list isn't equal to repeat")

        result = [parse_bytes_to_val(self.datatype, entry_bytes) for entry_bytes in bytes_list]
        self.data = parser.vorl(self, result)

    def update_datatype_repeat(self):
        if type(self.data) == list:
            self.datatype.repeat = len(self.data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        old_value = self._data
        self._data = value
        if self.log_value:
            self._print_value_update(old_value, value)

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
            potential_list=self.potential_list,
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
            potential_list=structure.get('potential_list', True),
            log_value=structure.get('log', False)
        )
        # Go through dependencies if exist, else empty dict
        for dependency_name, properties in structure.get('dependencies', {}).items():
            if type(properties) is not list:
                setattr(retriever, dependency_name, RetrieverDependency.from_structure(properties))
            else:
                dependency_list = []
                for dependency_struct in properties:
                    dependency_list.append(RetrieverDependency.from_structure(dependency_struct))
                setattr(retriever, dependency_name, dependency_list)
        return retriever

    def _print_value_update(self, old, new) -> None:
        """
        Function to print when data is changed. Can also be called for when data is changed but the property doesn't
        fire. This happens when an array is adjusted in size by appending to it ([...] += [...]).

        Args:
            old (str): The old value represented using a string
            new (str): The new value represented using a string
        """
        print(f"{self.to_simple_string()} >>> set to: {helper.q_str(new)} (was: {helper.q_str(old)})")

    def get_short_str(self):
        if self.data is not None:
            if type(self.data) is list:
                data = helper.pretty_print_list(self.data)
            else:
                data = helper.q_str(self.data)
            return self.name + " (" + self.datatype.to_simple_string() + "): " + data
        else:
            return "<None>"

    def to_simple_string(self):
        return f"[Retriever] {self.name}: {self.datatype} (Default: {helper.q_str(self.default_value)})"

    def __repr__(self):
        if type(self.data) is list:
            data = str(helper.pretty_print_list(self.data))
        else:
            data = helper.q_str(self.data)
        return f"{self.to_simple_string()} >>> {data}"


def duplicate_retriever_list(retriever_list):
    return [r.duplicate() for r in retriever_list]


def get_retriever_by_name(retriever_list: List[Union[Retriever, RetrieverObjectLink]], name: str) \
        -> Union[Retriever, RetrieverObjectLink]:
    for retriever in retriever_list:
        if retriever.name == name:
            return retriever
