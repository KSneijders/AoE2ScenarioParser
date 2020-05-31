from __future__ import annotations

from enum import Enum
from typing import List

from AoE2ScenarioParser.datasets import effects
from AoE2ScenarioParser.datasets.techs import Tech
from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.helper.retriever import find_retriever
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.pieces.structs.effect import EffectStruct


class EffectObject(AoE2Object):
    def __init__(self,
                 effect_type,
                 ai_script_goal,
                 aa_quantity,
                 aa_armor_or_attack_type,
                 quantity,
                 tribute_list,
                 diplomacy,
                 number_of_units_selected,
                 object_list_unit_id,
                 player_source,
                 player_target,
                 technology,
                 string_id,
                 display_time,
                 trigger_id,
                 location_x,
                 location_y,
                 area_1_x,
                 area_1_y,
                 area_2_x,
                 area_2_y,
                 object_group,
                 object_type,
                 instruction_panel_position,
                 attack_stance,
                 time_unit,
                 enabled_or_victory,
                 food,
                 wood,
                 stone,
                 gold,
                 item_id,
                 flash_object,
                 force_research_technology,
                 visibility_state,
                 scroll,
                 operation,
                 object_list_unit_id_2,
                 button_location,
                 ai_signal_value,
                 object_attributes,
                 from_variable,
                 variable_or_timer,
                 facet,
                 play_sound,
                 message="",
                 sound_name="",
                 selected_object_id: List = None,
                 ):

        if selected_object_id is None:
            selected_object_id = []

        self.effect_type = effect_type
        self.ai_script_goal = ai_script_goal
        self.aa_quantity = aa_quantity
        self.aa_armor_or_attack_type = aa_armor_or_attack_type
        self.quantity = quantity
        self.tribute_list = tribute_list
        self.diplomacy = diplomacy
        self.number_of_units_selected = number_of_units_selected
        self.object_list_unit_id = object_list_unit_id
        self.player_source = player_source
        self.player_target = player_target
        self.technology = technology
        self.string_id = string_id
        self.display_time = display_time
        self.trigger_id = trigger_id
        self.location_x = location_x
        self.location_y = location_y
        self.area_1_x = area_1_x
        self.area_1_y = area_1_y
        self.area_2_x = area_2_x
        self.area_2_y = area_2_y
        self.object_group = object_group
        self.object_type = object_type
        self.instruction_panel_position = instruction_panel_position
        self.attack_stance = attack_stance
        self.time_unit = time_unit
        self.enabled_or_victory = enabled_or_victory
        self.food = food
        self.wood = wood
        self.stone = stone
        self.gold = gold
        self.item_id = item_id
        self.flash_object = flash_object
        self.force_research_technology = force_research_technology
        self.visibility_state = visibility_state
        self.scroll = scroll
        self.operation = operation
        self.object_list_unit_id_2 = object_list_unit_id_2
        self.button_location = button_location
        self.ai_signal_value = ai_signal_value
        self.object_attributes = object_attributes
        self.from_variable = from_variable
        self.variable_or_timer = variable_or_timer
        self.facet = facet
        self.play_sound = play_sound
        self.message = message
        self.sound_name = sound_name
        self.selected_object_id = selected_object_id

        super().__init__()

    def get_content_as_string(self):
        attributes_list = effects.attributes[self.effect_type]

        return_string = ""
        for attribute in attributes_list:
            attr = getattr(self, attribute)
            if attribute == "effect_type" or attr == [] or attr == "" or attr == " " or attr == -1:
                continue
            return_string += "\t\t\t\t" + attribute + ": " + str(attr) + "\n"

        if return_string == "":
            return "\t\t\t\t<< No Attributes >>\n"

        return return_string

    @staticmethod
    def _parse_object(parsed_data, **kwargs):  # Expected {effect=effectStruct}
        effect_struct = kwargs['effect']

        effect_type = find_retriever(effect_struct.retrievers, "effect_type").data
        parameters = effects.attributes.get(effect_type)

        parameter_dict = effects.empty_attributes.copy()
        for param in parameters:
            parameter_dict[param] = find_retriever(effect_struct.retrievers, param).data

        return EffectObject(
            **parameter_dict
        )

    @staticmethod
    def _reconstruct_object(parsed_header, parsed_data, objects, **kwargs):  # Expected {effect=effect_obj, effects=effectsList}
        effect_obj = kwargs['effect']
        effects_list = kwargs['effects']

        data_list = [value for key, value in vars(effect_obj).items()]
        data_list.insert(1, 46)  # static_value_46
        data_list.insert(9, -1)  # unknown
        data_list.insert(15, -1)  # unknown_2
        data_list.insert(43, -1)  # unknown_3
        data_list.insert(48, -1)  # unknown_4

        effects_list.append(EffectStruct(data=data_list))
