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
            inverted_name = condition.naming_conversion.get(param)
            parameter_dict[inverted_name] = find_retriever(condition_struct.retrievers, param).data

        return ConditionObject(
            **parameter_dict
        )

    @staticmethod
    def reconstruct_object(parsed_data, objects, **kwargs):
        pass
