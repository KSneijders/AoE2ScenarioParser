import copy

from src.datasets import effect
from src.helper.retriever import find_retriever
from src.objects.aoe2_object import AoE2Object
from src.pieces.structs.effect import EffectStruct


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
        parameters = effect.parameters.get(effect_type)

        parameter_dict = copy.copy(effect.empty_parameters)
        for param in parameters:
            inverted_name = effect.naming_conversion.get(param)
            parameter_dict[inverted_name] = find_retriever(effect_struct.retrievers, param).data

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
