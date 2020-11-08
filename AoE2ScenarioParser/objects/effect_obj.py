from __future__ import annotations

from enum import IntEnum
from typing import List

from AoE2ScenarioParser.datasets import effects
from AoE2ScenarioParser.helper import parser
from AoE2ScenarioParser.helper.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object


class EffectObject(AoE2Object):
    """Object for handling an effect."""

    _link_list = [
        RetrieverObjectLink("effect_type", "TriggerPiece.trigger_data[__index__].effect_data[__index__].effect_type"),
        RetrieverObjectLink("ai_script_goal",
                            "TriggerPiece.trigger_data[__index__].effect_data[__index__].ai_script_goal"),
        RetrieverObjectLink("aa_quantity", "TriggerPiece.trigger_data[__index__].effect_data[__index__].aa_quantity"),
        RetrieverObjectLink("aa_armor_or_attack_type",
                            "TriggerPiece.trigger_data[__index__].effect_data[__index__].aa_armor_or_attack_type"),
        RetrieverObjectLink("quantity", "TriggerPiece.trigger_data[__index__].effect_data[__index__].quantity"),
        RetrieverObjectLink("tribute_list", "TriggerPiece.trigger_data[__index__].effect_data[__index__].tribute_list"),
        RetrieverObjectLink("diplomacy", "TriggerPiece.trigger_data[__index__].effect_data[__index__].diplomacy"),
        RetrieverObjectLink("number_of_units_selected",
                            "TriggerPiece.trigger_data[__index__].effect_data[__index__].number_of_units_selected"),
        RetrieverObjectLink("object_list_unit_id",
                            "TriggerPiece.trigger_data[__index__].effect_data[__index__].object_list_unit_id"),
        RetrieverObjectLink("source_player",
                            "TriggerPiece.trigger_data[__index__].effect_data[__index__].source_player"),
        RetrieverObjectLink("target_player",
                            "TriggerPiece.trigger_data[__index__].effect_data[__index__].target_player"),
        RetrieverObjectLink("technology", "TriggerPiece.trigger_data[__index__].effect_data[__index__].technology"),
        RetrieverObjectLink("string_id", "TriggerPiece.trigger_data[__index__].effect_data[__index__].string_id"),
        RetrieverObjectLink("display_time", "TriggerPiece.trigger_data[__index__].effect_data[__index__].display_time"),
        RetrieverObjectLink("trigger_id", "TriggerPiece.trigger_data[__index__].effect_data[__index__].trigger_id"),
        RetrieverObjectLink("location_x", "TriggerPiece.trigger_data[__index__].effect_data[__index__].location_x"),
        RetrieverObjectLink("location_y", "TriggerPiece.trigger_data[__index__].effect_data[__index__].location_y"),
        RetrieverObjectLink("area_1_x", "TriggerPiece.trigger_data[__index__].effect_data[__index__].area_1_x"),
        RetrieverObjectLink("area_1_y", "TriggerPiece.trigger_data[__index__].effect_data[__index__].area_1_y"),
        RetrieverObjectLink("area_2_x", "TriggerPiece.trigger_data[__index__].effect_data[__index__].area_2_x"),
        RetrieverObjectLink("area_2_y", "TriggerPiece.trigger_data[__index__].effect_data[__index__].area_2_y"),
        RetrieverObjectLink("object_group", "TriggerPiece.trigger_data[__index__].effect_data[__index__].object_group"),
        RetrieverObjectLink("object_type", "TriggerPiece.trigger_data[__index__].effect_data[__index__].object_type"),
        RetrieverObjectLink("instruction_panel_position",
                            "TriggerPiece.trigger_data[__index__].effect_data[__index__].instruction_panel_position"),
        RetrieverObjectLink("attack_stance",
                            "TriggerPiece.trigger_data[__index__].effect_data[__index__].attack_stance"),
        RetrieverObjectLink("time_unit", "TriggerPiece.trigger_data[__index__].effect_data[__index__].time_unit"),
        RetrieverObjectLink("enabled_or_victory",
                            "TriggerPiece.trigger_data[__index__].effect_data[__index__].enabled_or_victory"),
        RetrieverObjectLink("food", "TriggerPiece.trigger_data[__index__].effect_data[__index__].food"),
        RetrieverObjectLink("wood", "TriggerPiece.trigger_data[__index__].effect_data[__index__].wood"),
        RetrieverObjectLink("stone", "TriggerPiece.trigger_data[__index__].effect_data[__index__].stone"),
        RetrieverObjectLink("gold", "TriggerPiece.trigger_data[__index__].effect_data[__index__].gold"),
        RetrieverObjectLink("item_id", "TriggerPiece.trigger_data[__index__].effect_data[__index__].item_id"),
        RetrieverObjectLink("flash_object", "TriggerPiece.trigger_data[__index__].effect_data[__index__].flash_object"),
        RetrieverObjectLink("force_research_technology",
                            "TriggerPiece.trigger_data[__index__].effect_data[__index__].force_research_technology"),
        RetrieverObjectLink("visibility_state",
                            "TriggerPiece.trigger_data[__index__].effect_data[__index__].visibility_state"),
        RetrieverObjectLink("scroll", "TriggerPiece.trigger_data[__index__].effect_data[__index__].scroll"),
        RetrieverObjectLink("operation", "TriggerPiece.trigger_data[__index__].effect_data[__index__].operation"),
        RetrieverObjectLink("object_list_unit_id_2",
                            "TriggerPiece.trigger_data[__index__].effect_data[__index__].object_list_unit_id_2"),
        RetrieverObjectLink("button_location",
                            "TriggerPiece.trigger_data[__index__].effect_data[__index__].button_location"),
        RetrieverObjectLink("ai_signal_value",
                            "TriggerPiece.trigger_data[__index__].effect_data[__index__].ai_signal_value"),
        RetrieverObjectLink("object_attributes",
                            "TriggerPiece.trigger_data[__index__].effect_data[__index__].object_attributes"),
        RetrieverObjectLink("from_variable",
                            "TriggerPiece.trigger_data[__index__].effect_data[__index__].from_variable"),
        RetrieverObjectLink("variable_or_timer",
                            "TriggerPiece.trigger_data[__index__].effect_data[__index__].variable_or_timer"),
        RetrieverObjectLink("facet", "TriggerPiece.trigger_data[__index__].effect_data[__index__].facet"),
        RetrieverObjectLink("play_sound", "TriggerPiece.trigger_data[__index__].effect_data[__index__].play_sound"),
        RetrieverObjectLink("message", "TriggerPiece.trigger_data[__index__].effect_data[__index__].message"),
        RetrieverObjectLink("sound_name", "TriggerPiece.trigger_data[__index__].effect_data[__index__].sound_name"),
        RetrieverObjectLink("selected_object_id",
                            "TriggerPiece.trigger_data[__index__].effect_data[__index__].selected_object_id"),
    ]

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
        if self.effect_type not in effects.attributes:  # Unknown effect
            attributes_list = effects.empty_attributes
        else:
            attributes_list = effects.attributes[self.effect_type]

        return_string = ""
        for attribute in attributes_list:
            attr = getattr(self, attribute)
            if self.effect_type != 58:
                if attribute == "effect_type" or attr == [] or attr == "" or attr == " " or attr == -1:
                    continue
            return_string += "\t\t\t\t" + attribute + ": " + str(attr) + "\n"

        if return_string == "":
            return "\t\t\t\t<< No Attributes >>\n"

        return return_string
