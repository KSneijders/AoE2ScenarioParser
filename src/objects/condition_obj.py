import copy

from src.datasets import condition
from src.helper.retriever import find_retriever
from src.objects.aoe2_object import AoE2Object


class ConditionObject(AoE2Object):
    def __init__(self,
                 condition_type,
                 amount_or_quantity=-1,
                 resource_type_or_tribute_list=-1,
                 unit_object=-1,
                 next_object=-1,
                 object_list=-1,
                 player=1,
                 technology=-1,
                 timer=-1,
                 area_1_x=-1,
                 area_1_y=-1,
                 area_2_x=-1,
                 area_2_y=-1,
                 object_group=-1,
                 object_type=-1,
                 ai_signal=-1,
                 inverted=0,
                 variable=-1,
                 comparison=-1,
                 target_player=-1
                 ):

        super().__init__(locals())

    @staticmethod
    def parse_object(parsed_data, **kwargs):  # Expected {condition=conditionStruct}
        condition_struct = kwargs['condition']

        effect_type = find_retriever(condition_struct.retrievers, "Condition type").data
        parameters = condition.parameters.get(effect_type)

        parameter_dict = copy.copy(condition.empty_parameters)
        for param in parameters:
            parameter_dict[param] = find_retriever(condition_struct.retrievers, condition.naming_conversion[param]).data

        return ConditionObject(
            **parameter_dict
        )

    @staticmethod
    def reconstruct_object(parsed_data, objects, **kwargs):
        # Expected {condition=condition_obj, conditions=conditionsList}
        condition_obj = kwargs['condition']
        conditions = kwargs['conditions']

        data_list = list(condition_obj.data_dict.values())
        data_list.insert(1, 21)  # Check, (21)
        data_list.insert(10, -1)  # Unknown
        data_list.insert(19, -1)  # Unknown (3)
        conditions.append(ConditionStruct(data=data_list))
