import copy

from src.datasets import condition
from src.helper.retriever import find_retriever
from src.objects.aoe2_object import AoE2Object
from src.pieces.structs.condition import ConditionStruct


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

    def set_condition_type(self, val):
        self.data_dict['condition_type'] = val

    def set_amount_or_quantity(self, val):
        self.data_dict['amount_or_quantity'] = val

    def set_resource_type_or_tribute_list(self, val):
        self.data_dict['resource_type_or_tribute_list'] = val

    def set_unit_object(self, val):
        self.data_dict['unit_object'] = val

    def set_next_object(self, val):
        self.data_dict['next_object'] = val

    def set_object_list(self, val):
        self.data_dict['object_list'] = val

    def set_player(self, val):
        self.data_dict['player'] = val

    def set_technology(self, val):
        self.data_dict['technology'] = val

    def set_timer(self, val):
        self.data_dict['timer'] = val

    def set_area_1_x(self, val):
        self.data_dict['area_1_x'] = val

    def set_area_1_y(self, val):
        self.data_dict['area_1_y'] = val

    def set_area_2_x(self, val):
        self.data_dict['area_2_x'] = val

    def set_area_2_y(self, val):
        self.data_dict['area_2_y'] = val

    def set_object_group(self, val):
        self.data_dict['object_group'] = val

    def set_object_type(self, val):
        self.data_dict['object_type'] = val

    def set_ai_signal(self, val):
        self.data_dict['ai_signal'] = val

    def set_inverted(self, val):
        self.data_dict['inverted'] = val

    def set_variable(self, val):
        self.data_dict['variable'] = val

    def set_comparison(self, val):
        self.data_dict['comparison'] = val

    def set_target_player(self, val):
        self.data_dict['target_player'] = val
