import copy

from AoE2ScenarioParser.datasets import effects
from AoE2ScenarioParser.helper.retriever import find_retriever
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.pieces.structs.effect import EffectStruct


class EffectObject(AoE2Object):
    def __init__(self,
                 effect_type,
                 ai_script_goal=-1,
                 aa_quantity=-1,
                 aa_armor_or_attack_type=-1,
                 quantity=-1,
                 tribute_list=-1,
                 diplomacy=-1,
                 number_of_units_selected=-1,
                 object_list_unit_id=-1,
                 player_source=-1,
                 player_target=-1,
                 technology=-1,
                 string_id=-1,
                 display_time=-1,
                 trigger_id=-1,
                 location_x=-1,
                 location_y=-1,
                 area_1_x=-1,
                 area_1_y=-1,
                 area_2_x=-1,
                 area_2_y=-1,
                 object_group=-1,
                 object_type=-1,
                 instruction_panel_position=-1,
                 attack_stance=-1,
                 time_unit=-1,
                 enabled_or_victory=-1,
                 food=-1,
                 wood=-1,
                 stone=-1,
                 gold=-1,
                 item_id=-1,
                 flash_object=-1,
                 force_research_technology=-1,
                 visibility_state=-1,
                 scroll=-1,
                 operation=-1,
                 object_list_unit_id_2=-1,
                 button_location=-1,
                 ai_signal_value=-1,
                 object_attributes=-1,
                 from_variable=-1,
                 variable_or_timer=-1,
                 facet=-1,
                 play_sound=-1,
                 message="",
                 sound_name="",
                 selected_object_id=-1,
                 ):
        super().__init__(locals())

    @staticmethod
    def parse_object(parsed_data, **kwargs):  # Expected {effect=effectStruct}
        effect_struct = kwargs['effect']

        effect_type = find_retriever(effect_struct.retrievers, "Effect type").data
        parameters = effects.parameters.get(effect_type)

        parameter_dict = copy.copy(effects.empty_parameters)
        for param in parameters:
            parameter_dict[param] = find_retriever(effect_struct.retrievers, effects.naming_conversion[param]).data

        return EffectObject(
            **parameter_dict
        )

    @staticmethod
    def reconstruct_object(parsed_data, objects, **kwargs):  # Expected {effect=effect_obj, effects=effectsList}
        effect_obj = kwargs['effect']
        effects = kwargs['effects']

        data_list = list(effect_obj.data_dict.values())
        data_list.insert(1, 46)  # Check, (46)
        data_list.insert(9, -1)   # Unknown
        data_list.insert(15, -1)  # Unknown2
        data_list.insert(43, -1)  # Unknown3
        data_list.insert(48, -1)  # Unknown4

        effects.append(EffectStruct(data=data_list))

    def set_effect_type(self, val):
        self.data_dict['effect_type'] = val

    def set_ai_script_goal(self, val):
        self.data_dict['ai_script_goal'] = val

    def set_aa_quantity(self, val):
        self.data_dict['aa_quantity'] = val

    def set_aa_armor_or_attack_type(self, val):
        self.data_dict['aa_armor_or_attack_type'] = val

    def set_quantity(self, val):
        self.data_dict['quantity'] = val

    def set_tribute_list(self, val):
        self.data_dict['tribute_list'] = val

    def set_diplomacy(self, val):
        self.data_dict['diplomacy'] = val

    def set_number_of_units_selected(self, val):
        self.data_dict['number_of_units_selected'] = val

    def set_object_list_unit_id(self, val):
        self.data_dict['object_list_unit_id'] = val

    def set_player_source(self, val):
        self.data_dict['player_source'] = val

    def set_player_target(self, val):
        self.data_dict['player_target'] = val

    def set_technology(self, val):
        self.data_dict['technology'] = val

    def set_string_id(self, val):
        self.data_dict['string_id'] = val

    def set_display_time(self, val):
        self.data_dict['display_time'] = val

    def set_trigger_id(self, val):
        self.data_dict['trigger_id'] = val

    def set_location_x(self, val):
        self.data_dict['location_x'] = val

    def set_location_y(self, val):
        self.data_dict['location_y'] = val

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

    def set_instruction_panel_position(self, val):
        self.data_dict['instruction_panel_position'] = val

    def set_attack_stance(self, val):
        self.data_dict['attack_stance'] = val

    def set_time_unit(self, val):
        self.data_dict['time_unit'] = val

    def set_enabled_or_victory(self, val):
        self.data_dict['enabled_or_victory'] = val

    def set_food(self, val):
        self.data_dict['food'] = val

    def set_wood(self, val):
        self.data_dict['wood'] = val

    def set_stone(self, val):
        self.data_dict['stone'] = val

    def set_gold(self, val):
        self.data_dict['gold'] = val

    def set_item_id(self, val):
        self.data_dict['item_id'] = val

    def set_flash_object(self, val):
        self.data_dict['flash_object'] = val

    def set_force_research_technology(self, val):
        self.data_dict['force_research_technology'] = val

    def set_visibility_state(self, val):
        self.data_dict['visibility_state'] = val

    def set_scroll(self, val):
        self.data_dict['scroll'] = val

    def set_operation(self, val):
        self.data_dict['operation'] = val

    def set_object_list_unit_id_2(self, val):
        self.data_dict['object_list_unit_id_2'] = val

    def set_button_location(self, val):
        self.data_dict['button_location'] = val

    def set_ai_signal_value(self, val):
        self.data_dict['ai_signal_value'] = val

    def set_object_attributes(self, val):
        self.data_dict['object_attributes'] = val

    def set_from_variable(self, val):
        self.data_dict['from_variable'] = val

    def set_variable_or_timer(self, val):
        self.data_dict['variable_or_timer'] = val

    def set_facet(self, val):
        self.data_dict['facet'] = val

    def set_play_sound(self, val):
        self.data_dict['play_sound'] = val

    def set_message(self, val):
        self.data_dict['message'] = val

    def set_sound_name(self, val):
        self.data_dict['sound_name'] = val

    def set_selected_object_id(self, val):
        self.data_dict['selected_object_id'] = val
