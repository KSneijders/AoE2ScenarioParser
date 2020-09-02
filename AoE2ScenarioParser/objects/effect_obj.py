from __future__ import annotations

from enum import IntEnum
from typing import List, Union

from AoE2ScenarioParser.datasets import effects
from AoE2ScenarioParser.helper import parser
from AoE2ScenarioParser.helper.retriever import get_retriever_by_name
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.pieces.structs.effect import EffectStruct


class EffectObject(AoE2Object):
    def __init__(self,
                 effect_type: int,
                 ai_script_goal: int,
                 aa_quantity: int,
                 aa_armor_or_attack_type: int,
                 quantity: int,
                 tribute_list: int,
                 diplomacy: int,
                 number_of_units_selected: int,
                 object_list_unit_id: int,
                 source_player: IntEnum,
                 target_player: IntEnum,
                 technology: IntEnum,
                 string_id: int,
                 display_time: int,
                 trigger_id: int,
                 location_x: int,
                 location_y: int,
                 area_1_x: int,
                 area_1_y: int,
                 area_2_x: int,
                 area_2_y: int,
                 object_group: int,
                 object_type: int,
                 instruction_panel_position: int,
                 attack_stance: int,
                 time_unit: int,
                 enabled_or_victory: int,
                 food: int,
                 wood: int,
                 stone: int,
                 gold: int,
                 item_id: int,
                 flash_object: int,
                 force_research_technology: int,
                 visibility_state: int,
                 scroll: int,
                 operation: int,
                 object_list_unit_id_2: IntEnum,
                 button_location: int,
                 ai_signal_value: int,
                 object_attributes: int,
                 from_variable: int,
                 variable_or_timer: int,
                 facet: int,
                 play_sound: int,
                 message: str = "",
                 sound_name: str = "",
                 selected_object_id: List[int] = None,
                 ):

        if selected_object_id is None:
            selected_object_id = []
        else:
            selected_object_id = parser.listify(selected_object_id)

        self.effect_type: int = effect_type
        self.ai_script_goal: int = ai_script_goal
        self.aa_quantity: int = aa_quantity
        self.aa_armor_or_attack_type: int = aa_armor_or_attack_type
        self.quantity: int = quantity
        self.tribute_list: int = tribute_list
        self.diplomacy: int = diplomacy
        self.number_of_units_selected: int = number_of_units_selected
        self.object_list_unit_id: int = object_list_unit_id
        self.source_player: IntEnum = source_player
        self.target_player: IntEnum = target_player
        self.technology: IntEnum = technology
        self.string_id: int = string_id
        self.display_time: int = display_time
        self.trigger_id: int = trigger_id
        self.location_x: int = location_x
        self.location_y: int = location_y
        self.area_1_x: int = area_1_x
        self.area_1_y: int = area_1_y
        self.area_2_x: int = area_2_x
        self.area_2_y: int = area_2_y
        self.object_group: int = object_group
        self.object_type: int = object_type
        self.instruction_panel_position: int = instruction_panel_position
        self.attack_stance: int = attack_stance
        self.time_unit: int = time_unit
        self.enabled_or_victory: int = enabled_or_victory
        self.food: int = food
        self.wood: int = wood
        self.stone: int = stone
        self.gold: int = gold
        self.item_id: int = item_id
        self.flash_object: int = flash_object
        self.force_research_technology: int = force_research_technology
        self.visibility_state: int = visibility_state
        self.scroll: int = scroll
        self.operation: int = operation
        self.object_list_unit_id_2: IntEnum = object_list_unit_id_2
        self.button_location: int = button_location
        self.ai_signal_value: int = ai_signal_value
        self.object_attributes: int = object_attributes
        self.from_variable: int = from_variable
        self.variable_or_timer: int = variable_or_timer
        self.facet: int = facet
        self.play_sound: int = play_sound
        self.message: str = message
        self.sound_name: str = sound_name
        self.selected_object_id: List[int] = selected_object_id

        super().__init__()

    @property
    def selected_object_id(self) -> List[int]:
        return self._selected_object_id

    @selected_object_id.setter
    def selected_object_id(self, val: List[int]):
        val = parser.listify(val)
        self._selected_object_id = val
        self.number_of_units_selected = len(val)

    def get_content_as_string(self) -> str:
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

        effect_type = get_retriever_by_name(effect_struct.retrievers, "effect_type").data
        parameters = effects.attributes.get(effect_type)

        parameter_dict = effects.empty_attributes.copy()
        for param in parameters:
            parameter_dict[param] = get_retriever_by_name(effect_struct.retrievers, param).data

        return EffectObject(
            **parameter_dict
        )

    @staticmethod
    def _reconstruct_object(parsed_header, parsed_data, objects,
                            **kwargs):  # Expected {effect=effect_obj, effects=effectsList}
        effect_obj = kwargs['effect']
        effects_list = kwargs['effects']

        data_list = [value for key, value in vars(effect_obj).items()]
        data_list.insert(1, 46)  # static_value_46
        data_list.insert(9, -1)  # unknown
        data_list.insert(15, -1)  # unknown_2
        data_list.insert(43, -1)  # unknown_3
        data_list.insert(48, -1)  # unknown_4

        effects_list.append(EffectStruct(data=data_list))
