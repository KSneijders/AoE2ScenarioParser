from __future__ import annotations

from typing import Type, Any, TYPE_CHECKING, List

from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object

if TYPE_CHECKING:
    from AoE2ScenarioParser.pieces.aoe2_piece import AoE2Piece


class Retriever:
    """ A Class for defining how to retrieve data.
    The Constructor has quite some parameters which can all be used for getting the proper data
        name: The name of the item. Recommended to make this unique within the Piece or Struct
        datatype: A datatype object
        on_success: A lambda which can be used to execute some code once the data is retrieved. You can use one
                    parameter; the data that got retrieved.
        save_as: Save the value retrieved to a dict. Can be used later with the 'set_repeat' parameter
        set_repeat: Use a saved value (from 'save_as') to set repeat value. You can use values from the dict by
                    surrounding them with curly brackets. The string will be executed using eval.
        log_value: A boolean for, mostly, debugging. This will log this Retriever with it's data on retrieval.
    """

    def __init__(self, name, datatype=DataType(), on_success=None, save_as=None, set_repeat=None, log_value=False):
        self.name = name
        self.datatype = datatype
        self.on_success = on_success
        self.save_as = save_as
        self.set_repeat = set_repeat
        self.log_value = log_value
        self.data = None

    def set_data(self, data):
        self.data = data
        if self.on_success is not None:
            self.on_success(data)

    def get_short_str(self):
        if self.data is not None:
            if type(self.data) is str:
                return self.name + " (" + self.datatype.to_simple_string() + "): '" + str(self.data) + "'"
            else:
                return self.name + " (" + self.datatype.to_simple_string() + "): " + str(self.data) + ""

    def __repr__(self):
        if type(self.data) is list:
            data = str(helper.pretty_print_list(self.data))
        else:
            data = str(self.data)
        return "[Retriever] " + self.name + ": " + str(self.datatype) + " >>> " + data


class RetrieverObjectLink:
    def __init__(self, variable_name: str, link: str, process_as_object: Type[AoE2Object] = None):
        self.name: str = variable_name
        self.link: str = self._process_link(link)
        self.process_as_object: Type[AoE2Object] = process_as_object

    @staticmethod
    def _process_link(link) -> str:
        dot = link.find(".")
        # Convert piece attribute to dict key: "MapPiece.x" > "pieces['MapPiece'].x"
        link = "pieces['" + link[0:dot] + "']" + link[dot:]
        return link


def find_retriever(retriever_list: List[Retriever], name: str) -> Retriever:
    for retriever in retriever_list:
        if retriever.name == name:
            return retriever


def get_piece_from_retriever_object_link(pieces, retriever_object_link) -> Type[AoE2Piece]:
    if retriever_object_link.process_as_object is None:
        raise ValueError("Cannot get piece type from RetrieverObjectLink when parameter process_as_object has not "
                         "been set.")
    split_link = retriever_object_link.link.split(".")
    link_end = split_link.pop()
    return eval("find_retriever(" + ".".join(split_link) + ".retrievers, '" + link_end + "').datatype.var", {}, {
        'pieces': dict(pieces),
        'find_retriever': find_retriever
    })
