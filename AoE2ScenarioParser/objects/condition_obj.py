from __future__ import annotations

from AoE2ScenarioParser.datasets import conditions
from AoE2ScenarioParser.helper.retriever import find_retriever
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.pieces.structs.condition import ConditionStruct


class ConditionObject(AoE2Object):
    def __init__(self,
                 condition_type,
                 amount_or_quantity,
                 resource_type_or_tribute_list,
                 unit_object,
                 next_object,
                 object_list,
                 player,
                 technology,
                 timer,
                 area_1_x,
                 area_1_y,
                 area_2_x,
                 area_2_y,
                 object_group,
                 object_type,
                 ai_signal,
                 inverted,
                 variable,
                 comparison,
                 target_player
                 ):

        self.condition_type = condition_type
        self.amount_or_quantity = amount_or_quantity
        self.resource_type_or_tribute_list = resource_type_or_tribute_list
        self.unit_object = unit_object
        self.next_object = next_object
        self.object_list = object_list
        self.player = player
        self.technology = technology
        self.timer = timer
        self.area_1_x = area_1_x
        self.area_1_y = area_1_y
        self.area_2_x = area_2_x
        self.area_2_y = area_2_y
        self.object_group = object_group
        self.object_type = object_type
        self.ai_signal = ai_signal
        self.inverted = inverted
        self.variable = variable
        self.comparison = comparison
        self.target_player = target_player

        super().__init__()

    def get_content_as_string(self):
        attributes_list = conditions.attributes[self.condition_type]

        return_string = ""
        for attribute in attributes_list:
            attr = getattr(self, attribute)
            if attribute == "condition_type" or attr == [] or attr == "" or attr == " " or attr == -1:
                continue
            return_string += "\t\t\t\t" + attribute + ": " + str(attr) + "\n"

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
    def _reconstruct_object(parsed_data, objects, **kwargs) -> None:
        # Expected {condition=condition_obj, conditions=conditionsList}
        condition_obj = kwargs['condition']
        conditions_list = kwargs['conditions']

        data_list = [value for key, value in vars(condition_obj).items()]
        data_list.insert(1, 21)  # static_value_21
        data_list.insert(10, -1)  # unknown
        data_list.insert(19, -1)  # unknown_2
        conditions_list.append(ConditionStruct(data=data_list))
