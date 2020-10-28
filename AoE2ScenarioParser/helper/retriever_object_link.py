from collections import OrderedDict
from typing import Type, List

from AoE2ScenarioParser.helper.parser import handle_retriever_dependency
from AoE2ScenarioParser.helper.retriever import get_retriever_by_name
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.pieces.aoe2_piece import AoE2Piece


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

    def get_piece_datatype(self, pieces, custom_link="", host_obj=None) -> Type[AoE2Piece]:
        """

        Args:
            pieces (OrderedDict[str, AoE2Piece]):
            custom_link (str):
            host_obj ():

        Returns:

        """
        if self.process_as_object is None:
            raise ValueError("Cannot get piece type from RetrieverObjectLink when parameter process_as_object has not "
                             "been set.")
        custom_link = self.link if custom_link == "" else custom_link
        split_link = custom_link.split(".")
        link_end = split_link.pop()

        return eval("get_retriever_by_name(" + ".".join(split_link) + ".retrievers, '" + link_end + "').datatype.var",
                    {}, {
                        'pieces': dict(pieces),
                        'get_retriever_by_name': get_retriever_by_name,
                        '__index__': AoE2Object.get_instance_number(host_obj)
                    })

    def construct(self, pieces, instance_number_history=None):
        """

        Args:
            pieces (OrderedDict[str, AoE2Piece]):
            instance_number_history (List[int]):

        Returns:

        """
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

    def commit(self, pieces, host_obj):
        """

        Args:
            pieces (OrderedDict[str, AoE2Piece]):
            host_obj (AoE2Object):

        Returns:

        """
        # Object only retrievers for the ease of access of information.
        # Not actually representing a value in the scenario file.
        if self.retrieve_instance_number or self.retrieve_history_number >= 0:
            return

        instance_number_history = host_obj._instance_number_history
        instance_number = AoE2Object.get_instance_number(obj=host_obj)
        value = host_obj.__getattribute__(self.name)

        # Replace __index__ values
        temp_link = self.link
        if instance_number_history:
            for i in instance_number_history:
                temp_link = temp_link.replace("__index__", str(i), 1)

        if self.is_special_unit_case:
            temp_link = temp_link.replace('[]', '[0]', 1)

        # Get retriever and update/save value
        split_temp_link = temp_link.split(".")
        retriever_name = split_temp_link.pop()
        retriever_list = eval('.'.join(split_temp_link) + ".retrievers", {}, {
            'pieces': pieces,
            '__index__': instance_number
        })
        retriever = get_retriever_by_name(retriever_list, retriever_name)

        if self.process_as_object is not None:
            link_piece = self.get_piece_datatype(pieces, custom_link=temp_link, host_obj=host_obj)

            if self.is_special_unit_case:
                self._commit_special_unit_case(host_obj, pieces, link_piece, value)
                return

            exec(f"{temp_link} = [link_piece() for x in range(r)]", locals(), {
                'r': len(value),
                'pieces': pieces,
                'link_piece': link_piece,
                '__index__': instance_number
            })

            for index, obj in enumerate(value):
                obj._pieces = pieces
                obj._instance_number_history = host_obj._instance_number_history + [index]
                obj.commit()
        else:
            exec(f"{temp_link} = value", {}, {
                'value': value,
                'pieces': pieces,
                '__index__': instance_number
            })

        if retriever.on_commit is not None:
            handle_retriever_dependency(retriever, retriever_list, "commit", pieces)

    def _self_is_special_unit_case(self):
        if self.link is not None:
            return "[]" in self.link
        return False

    def _construct_special_unit_case(self, pieces):
        """

        Args:
            pieces (OrderedDict[str, AoE2Piece]):

        Returns:

        """
        list_notation_location = self.link.find("[]")
        struct_list = eval(self.link[:list_notation_location], {}, {'pieces': pieces})
        list_len = len(struct_list)
        result_list = [[] for _ in range(list_len)]
        for i in range(list_len):
            list_of_attributes = struct_list[i].__getattr__(self.link[list_notation_location + 3:])
            for j in range(len(list_of_attributes)):
                result_list[i].append(self.process_as_object._construct(pieces, [i, j]))
        return result_list

    def _commit_special_unit_case(self, host_obj, pieces, link_piece, units):
        """

        Args:
            pieces (OrderedDict[str, AoE2Piece]):
            link_piece ():
            units (List[List[AoE2Object]]):

        Returns:

        """
        for player_number in range(len(units)):
            pieces['UnitsPiece'].players_units[player_number].unit_count = len(units[player_number])
            pieces['UnitsPiece'].players_units[player_number].units = \
                [link_piece() for _ in range(len(units[player_number]))]

            for index, obj in enumerate(units[player_number]):
                obj._pieces = pieces
                obj._instance_number_history = [player_number, index]
                obj.commit()

    def __repr__(self):
        return "[RetrieverObjectLink] " + self.name + ": " + str(self.link) + \
               (f"\n\t- Process as: {self.process_as_object.__name__}" if self.process_as_object else "") + \
               (f"\n\t- Get Instance Number: True" if self.retrieve_instance_number else "") + \
               (f"\n\t- Get Hist Number: {self.retrieve_history_number}" if self.retrieve_history_number >= 0 else "")
