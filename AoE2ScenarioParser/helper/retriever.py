from __future__ import annotations

from typing import Type, TYPE_CHECKING, List, Union

from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object

if TYPE_CHECKING:
    from AoE2ScenarioParser.pieces.aoe2_piece import AoE2Piece
    from typing import OrderedDict


class Retriever:
    """ A Class for defining how to retrieve data.
    The Constructor has quite some parameters which can all be used for getting the proper data
    """

    def __init__(self, name, datatype=DataType(), on_construct="", on_commit="", save_as=None, set_repeat=None,
                 log_value=False):
        """
        Args:
            name (str): The name of the item. Has to be unique within the Piece or Struct
            datatype (DataType): A datatype object
            on_construct (str): A string that will be parsed using eval when constructing. It's uses can be found below.
            on_commit (str): A string that will be parsed using eval when committing. It's uses can be found below.
            save_as (): To Be Removed (Deprecated)
            set_repeat (): To Be Removed (Deprecated)
            log_value (bool): A boolean for, mostly, debugging. This will log this Retriever with it's data when the
                data is changed, when this retriever is constructed and committed.
        """
        self.name = name
        self.datatype = datatype
        self.save_as = save_as
        self.set_repeat = set_repeat
        self.log_value = log_value
        self.data = None

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

    def set_data(self, data):
        self.data = data

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


class RetrieverObjectLink:
    def __init__(self,
                 variable_name: str,
                 link: str = None,
                 process_as_object: Type[AoE2Object] = None,
                 retrieve_instance_number: bool = False,
                 retrieve_history_number=-1
                 ):
        if (link is not None) + retrieve_instance_number + (retrieve_history_number != -1) != 1:
            raise ValueError("Use one and only one of the following parameters: 'link', 'retrieve_instance_number' or "
                             "'retrieve_history_number'.")

        if link is not None:
            link: str = RetrieverObjectLink._process_link(link)

        self.name: str = variable_name
        self.link = link
        self.is_special_unit_case = self._self_is_special_unit_case()
        self.process_as_object: Type[AoE2Object] = process_as_object
        self.retrieve_instance_number: bool = retrieve_instance_number
        self.retrieve_history_number: int = retrieve_history_number

    @staticmethod
    def _process_link(link: str) -> str:
        dot = link.find(".")
        # Convert piece attribute to dict key: "MapPiece.x" > "pieces['MapPiece'].x"
        link = "pieces['" + link[0:dot] + "']" + link[dot:]
        return link

    def get_piece_datatype(self, pieces: OrderedDict[str, AoE2Piece], custom_link="", host_obj=None) -> Type[AoE2Piece]:
        if self.process_as_object is None:
            raise ValueError("Cannot get piece type from RetrieverObjectLink when parameter process_as_object has not "
                             "been set.")
        custom_link = self.link if custom_link == "" else custom_link
        split_link = custom_link.split(".")
        link_end = split_link.pop()

        return eval("get_retriever_by_name(" + ".".join(split_link) + ".retrievers, '" + link_end + "').datatype.var", {}, {
            'pieces': dict(pieces),
            'get_retriever_by_name': get_retriever_by_name,
            '__index__': AoE2Object.get_instance_number(host_obj)
        })

    def construct(self, pieces: OrderedDict[str, AoE2Piece], instance_number_history=None):
        if instance_number_history is None:
            instance_number_history = []

        instance_number = AoE2Object.get_instance_number(instance_number_history=instance_number_history)

        if self.retrieve_instance_number:
            return instance_number
        elif self.retrieve_history_number != -1:
            return instance_number_history[self.retrieve_history_number]
        else:
            if self.is_special_unit_case:
                return self._construct_special_unit_case(pieces)
            # Use temp_link to not change the actual links as they are class attributes
            temp_link = self.link
            if instance_number_history:
                for i in instance_number_history:
                    temp_link = temp_link.replace("__index__", str(i), 1)
            value = eval(temp_link, {}, {'pieces': pieces, '__index__': instance_number})

            if self.process_as_object is not None:
                value_list = []
                for index, struct in enumerate(value):
                    value_list.append(
                        self.process_as_object._construct(
                            pieces,
                            instance_number_history=instance_number_history + [index]
                        )
                    )
                return value_list
            return value

    def _commit_special_unit_case(self, pieces: OrderedDict[str, AoE2Piece], link_piece, units: List[List[AoE2Object]]):
        for player_number in range(len(units)):
            pieces['UnitsPiece'].players_units[player_number].unit_count = len(units[player_number])
            pieces['UnitsPiece'].players_units[player_number].units = \
                [link_piece() for _ in range(len(units[player_number]))]

            for index, obj in enumerate(units[player_number]):
                obj._pieces = pieces
                obj._instance_number_history.append(index)
                obj.commit()

    def commit(self, pieces: OrderedDict[str, AoE2Piece], host_obj: AoE2Object):
        # Object only retrievers for the ease of access of information.
        # Not actually representing a value in the scenario file.
        if self.retrieve_instance_number or self.retrieve_history_number >= 0:
            return

        instance_number_history = host_obj._instance_number_history
        temp_link = self.link
        if instance_number_history:
            for i in instance_number_history:
                temp_link = temp_link.replace("__index__", str(i), 1)

        if self.is_special_unit_case:
            temp_link = temp_link.replace("[]", "[0]", 1)

        if self.process_as_object is not None:
            link_piece = self.get_piece_datatype(pieces, custom_link=temp_link, host_obj=host_obj)

            if self.is_special_unit_case:
                object_list = host_obj.__getattribute__(self.name)
                self._commit_special_unit_case(pieces, link_piece, object_list)
                return

            object_list = host_obj.__getattribute__(self.name)

            instance_number = AoE2Object.get_instance_number(obj=host_obj)
            exec(f"{temp_link} = [link_piece() for x in range(r)]", locals(), {
                'pieces': pieces,
                'link_piece': link_piece,
                'r': len(object_list),
                '__index__': instance_number
            })

            for index, obj in enumerate(object_list):
                obj._pieces = pieces
                obj._instance_number_history.append(index)
                obj.commit()
        else:
            instance_number = AoE2Object.get_instance_number(obj=host_obj)
            exec(f"{temp_link} = value", {}, {
                'pieces': pieces,
                'value': host_obj.__getattribute__(self.name),
                '__index__': instance_number
            })

    def _self_is_special_unit_case(self):
        if self.link is not None:
            return "[]" in self.link
        return False

    def _construct_special_unit_case(self, pieces: OrderedDict[str, AoE2Piece]):
        list_notation_location = self.link.find("[]")
        struct_list = eval(self.link[:list_notation_location], {}, {'pieces': pieces})
        list_len = len(struct_list)
        result_list = [[] for _ in range(list_len)]
        for i in range(list_len):
            list_of_attributes = struct_list[i].__getattr__(self.link[list_notation_location + 3:])
            for j in range(len(list_of_attributes)):
                result_list[i].append(self.process_as_object._construct(pieces, [i, j]))
        return result_list

    def __repr__(self):
        return "[RetrieverObjectLink] " + self.name + ": " + str(self.link) + \
               (f"\n\t- Process as: {self.process_as_object.__name__}" if self.process_as_object else "") + \
               (f"\n\t- Get Instance Number: True" if self.retrieve_instance_number else "") + \
               (f"\n\t- Get Hist Number: {self.retrieve_history_number}" if self.retrieve_history_number >= 0 else "")


def get_retriever_by_name(retriever_list: List[Union[Retriever, RetrieverObjectLink]], name: str) \
        -> Union[Retriever, RetrieverObjectLink]:
    for retriever in retriever_list:
        if retriever.name == name:
            return retriever
