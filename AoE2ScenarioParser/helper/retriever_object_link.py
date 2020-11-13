from collections import OrderedDict
from typing import Type, List

from AoE2ScenarioParser.helper.parser import handle_retriever_dependency
from AoE2ScenarioParser.helper.retriever import get_retriever_by_name
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.pieces.aoe2_piece import AoE2Piece


class RetrieverObjectLink:
    def __init__(self,
                 variable_name: str,
                 piece: str = None,
                 link: str = None,
                 process_as_object: Type[AoE2Object] = None,
                 retrieve_instance_number: bool = False,
                 retrieve_history_number=-1
                 ):
        if (link is not None) + retrieve_instance_number + (retrieve_history_number != -1) != 1:
            raise ValueError("Use one and only one of the following parameters: 'link', 'retrieve_instance_number' or "
                             "'retrieve_history_number'.")
        self.name: str = variable_name
        self.piece = piece
        self.link = link
        self.is_special_unit_case = self._self_is_special_unit_case()
        self.process_as_object: Type[AoE2Object] = process_as_object
        self.retrieve_instance_number: bool = retrieve_instance_number
        self.retrieve_history_number: int = retrieve_history_number

    def construct(self, pieces, instance_number_history=None):
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
            temp_link = temp_link.replace("__index__", str(instance_number), 1)

            value = pieces[self.piece]
            for x in temp_link.split("."):
                if "[" in x:
                    indexing = x.index('[')
                    value = getattr(value, x[:indexing])
                    value = value[int(x[indexing+1:len(x)-1])]
                else:
                    value = getattr(value, x)

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
        # Object-only retrievers for the ease of access of information.
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
        temp_link = temp_link.replace("__index__", str(instance_number), 1)

        if self.is_special_unit_case:
            temp_link = temp_link.replace('[]', '[0]', 1)

        split_temp_link: List[str] = temp_link.split(".")
        retriever = None

        piece = pieces[self.piece]
        for attribute in split_temp_link:
            if '[' in attribute:
                index_location = attribute.index('[')
                index = int(attribute[index_location+1:len(attribute)-1])
                piece = get_retriever_by_name(piece.retrievers, attribute[:index_location]).data[index]
            else:
                retriever = get_retriever_by_name(piece.retrievers, attribute)

        if retriever is None:
            raise ValueError("RetrieverObjectLink is unable to connect to retriever")

        retriever_list = piece.retrievers

        if self.process_as_object is not None:
            link_piece = retriever.datatype.var

            if self.is_special_unit_case:
                self._commit_special_unit_case(host_obj, pieces, link_piece, value)
                return

            try:
                old_length = len(retriever.data)
            except TypeError:
                # retriever.data was not set before (list of 0 -> None)
                retriever.data = []
                old_length = 0
            new_length = len(value)

            if new_length < old_length:
                retriever.data = retriever.data[:new_length]
            elif new_length > old_length:
                retriever.data += [link_piece() for x in range(new_length - old_length)]

            for index, obj in enumerate(value):
                obj._pieces = pieces
                obj._instance_number_history = host_obj._instance_number_history + [index]
                obj.commit()
        else:
            retriever.data = value

        if hasattr(retriever, 'on_commit'):
            handle_retriever_dependency(retriever, retriever_list, "commit", pieces)

    def _self_is_special_unit_case(self):
        if self.link is not None:
            return "[]" in self.link
        return False

    def _construct_special_unit_case(self, pieces):
        list_notation_location = self.link.find("[]")
        struct_list = getattr(pieces[self.piece], self.link[:list_notation_location])
        list_len = len(struct_list)
        result_list = [[] for _ in range(list_len)]
        for i in range(list_len):
            list_of_attributes = struct_list[i].__getattr__(self.link[list_notation_location + 3:])
            for j in range(len(list_of_attributes)):
                result_list[i].append(self.process_as_object._construct(pieces, [i, j]))
        return result_list

    def _commit_special_unit_case(self, host_obj, pieces, link_piece, units):
        for player_number in range(len(units)):
            pieces['UnitsPiece'].players_units[player_number].unit_count = len(units[player_number])
            pieces['UnitsPiece'].players_units[player_number].units = \
                [link_piece() for _ in range(len(units[player_number]))]

            for index, obj in enumerate(units[player_number]):
                obj._pieces = pieces
                obj._instance_number_history = [player_number, index]
                obj.commit()

    def __repr__(self):
        return "[RetrieverObjectLink] " + self.name + ": " + str(self.piece) + "." + str(self.link) + \
               (f"\n\t- Process as: {self.process_as_object.__name__}" if self.process_as_object else "") + \
               (f"\n\t- Get Instance Number: True" if self.retrieve_instance_number else "") + \
               (f"\n\t- Get Hist Number: {self.retrieve_history_number}" if self.retrieve_history_number >= 0 else "")
