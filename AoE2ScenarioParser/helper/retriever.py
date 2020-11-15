from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever_dependency import RetrieverDependency

if TYPE_CHECKING:
    from AoE2ScenarioParser.helper.retriever_object_link import RetrieverObjectLink


class Retriever:
    """ A Class for defining how to retrieve data.
    The Constructor has quite some parameters which can all be used for getting the proper data
    """

    def __init__(self, name, datatype=DataType(),
                 save_as=None,
                 set_repeat=None,
                 log_value=False
                 ):
        """
        Args:
            name (str): The name of the item. Has to be unique within the Piece or Struct
            datatype (DataType): A datatype object
            save_as (str): To Be Removed (Deprecated)
            set_repeat (str): To Be Removed (Deprecated)
            log_value (bool): A boolean for, mostly, debugging. This will log this Retriever with it's data when the
                data is changed, when this retriever is constructed and committed.
        """
        self.name: str = name
        self.datatype: DataType = datatype
        if log_value:
            self.datatype.log_value = True
        self.datatype._debug_retriever_name = name
        self.save_as = save_as
        self.set_repeat = set_repeat
        self.log_value = log_value
        self._data = None

        self.on_construct: RetrieverDependency
        self.on_commit: RetrieverDependency
        self.on_refresh: RetrieverDependency

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        old_value = ""
        if hasattr(self, 'data'):
            old_value = f"(was: {helper.q_str(self.data)})"
        self._data = value
        if self.log_value:
            print(f"{self.to_simple_string()} >>> set to: {helper.q_str(value)} {old_value}")

    def get_short_str(self):
        if self.data is not None:
            return self.name + " (" + self.datatype.to_simple_string() + "): " + helper.q_str(self.data)

    def to_simple_string(self):
        return f"[Retriever] {self.name}: {self.datatype}"

    def __repr__(self):
        if type(self.data) is list:
            data = str(helper.pretty_print_list(self.data))
        else:
            data = helper.q_str(self.data)
        return f"{self.to_simple_string()} >>> {data}"


def get_retriever_by_name(retriever_list: List[Union[Retriever, RetrieverObjectLink]], name: str) \
        -> Union[Retriever, RetrieverObjectLink]:
    for retriever in retriever_list:
        if retriever.name == name:
            return retriever
