from __future__ import annotations

from enum import IntEnum

from AoE2ScenarioParser.datasets import conditions
from AoE2ScenarioParser.helper.retriever import find_retriever
from AoE2ScenarioParser.pieces.structs.condition import ConditionStruct


class ConditionObject():
    def __init__(self,
                 condition_type: int,
                 amount_or_quantity: int,
                 resource_type_or_tribute_list: int,
                 unit_object: int,
                 next_object: int,
                 object_list: int,
                 source_player: IntEnum,
                 technology: IntEnum,
                 timer: int,
                 area_1_x: int,
                 area_1_y: int,
                 area_2_x: int,
                 area_2_y: int,
                 object_group: int,
                 object_type: int,
                 ai_signal: int,
                 inverted: int,
                 variable: int,
                 comparison: int,
                 target_player: IntEnum
                 ):

        self.condition_type: int = condition_type
        self.amount_or_quantity: int = amount_or_quantity
        self.resource_type_or_tribute_list: int = resource_type_or_tribute_list
        self.unit_object: int = unit_object
        self.next_object: int = next_object
        self.object_list: int = object_list
        self.source_player: IntEnum = source_player
        self.technology: IntEnum = technology
        self.timer: int = timer
        self.area_1_x: int = area_1_x
        self.area_1_y: int = area_1_y
        self.area_2_x: int = area_2_x
        self.area_2_y: int = area_2_y
        self.object_group: int = object_group
        self.object_type: int = object_type
        self.ai_signal: int = ai_signal
        self.inverted: int = inverted
        self.variable: int = variable
        self.comparison: int = comparison
        self.target_player: IntEnum = target_player

    def get_content_as_string(self) -> str:
        attributes_list = conditions.attributes[self.condition_type]

        return_string = ""
        for attribute in attributes_list:
            attr = getattr(self, attribute)
            if attribute == "condition_type" or attr == [] or attr == "" or attr == " " or attr == -1:
                continue
            return_string += "\t\t\t\t" + attribute + ": " + str(attr) + "\n"

        if return_string == "":
            return "\t\t\t\t<< No Attributes >>\n"

        return return_string

    @staticmethod
    def _parse_object(parsed_data, **kwargs) -> ConditionObject:  # Expected {condition=conditionStruct}
        condition_struct = kwargs['condition']

        condition_type = find_retriever(condition_struct.retrievers, "condition_type").data
        parameters = conditions.attributes.get(condition_type)

        parameter_dict = conditions.empty_attributes.copy()
        for param in parameters:
            parameter_dict[param] = find_retriever(condition_struct.retrievers, param).data

        return ConditionObject(
            **parameter_dict
        )

    @staticmethod
    def _reconstruct_object(parsed_header, parsed_data, objects, **kwargs) -> None:
        # Expected {condition=condition_obj, conditions=conditionsList}
        condition_obj = kwargs['condition']
        conditions_list = kwargs['conditions']

        data_list = [value for key, value in vars(condition_obj).items()]
        data_list.insert(1, 21)  # static_value_21
        data_list.insert(10, -1)  # unknown
        data_list.insert(19, -1)  # unknown_2
        conditions_list.append(ConditionStruct(data=data_list))
