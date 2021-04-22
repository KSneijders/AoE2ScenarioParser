from __future__ import annotations

from enum import IntEnum
from typing import List

from AoE2ScenarioParser.datasets import effects
from AoE2ScenarioParser.helper.helper import raise_if_not_int_subclass
from AoE2ScenarioParser.helper.list_functions import listify
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.sections.retrievers.support import Support


class Effect(AoE2Object):
    """Object for handling an effect."""

    _link_list = [
        RetrieverObjectLink("effect_type", "Triggers", "trigger_data[__index__].effect_data[__index__].effect_type"),
        RetrieverObjectLink("ai_script_goal", "Triggers",
                            "trigger_data[__index__].effect_data[__index__].ai_script_goal"),
        RetrieverObjectLink("armour_attack_quantity", "Triggers",
                            "trigger_data[__index__].effect_data[__index__].armour_attack_quantity"),
        RetrieverObjectLink("armour_attack_class", "Triggers",
                            "trigger_data[__index__].effect_data[__index__].armour_attack_class"),
        RetrieverObjectLink("quantity", "Triggers", "trigger_data[__index__].effect_data[__index__].quantity"),
        RetrieverObjectLink("tribute_list", "Triggers", "trigger_data[__index__].effect_data[__index__].tribute_list"),
        RetrieverObjectLink("diplomacy", "Triggers", "trigger_data[__index__].effect_data[__index__].diplomacy"),
        RetrieverObjectLink("object_list_unit_id", "Triggers",
                            "trigger_data[__index__].effect_data[__index__].object_list_unit_id"),
        RetrieverObjectLink("source_player", "Triggers",
                            "trigger_data[__index__].effect_data[__index__].source_player"),
        RetrieverObjectLink("target_player", "Triggers",
                            "trigger_data[__index__].effect_data[__index__].target_player"),
        RetrieverObjectLink("technology", "Triggers", "trigger_data[__index__].effect_data[__index__].technology"),
        RetrieverObjectLink("string_id", "Triggers", "trigger_data[__index__].effect_data[__index__].string_id"),
        RetrieverObjectLink("display_time", "Triggers", "trigger_data[__index__].effect_data[__index__].display_time"),
        RetrieverObjectLink("trigger_id", "Triggers", "trigger_data[__index__].effect_data[__index__].trigger_id"),
        RetrieverObjectLink("location_x", "Triggers", "trigger_data[__index__].effect_data[__index__].location_x"),
        RetrieverObjectLink("location_y", "Triggers", "trigger_data[__index__].effect_data[__index__].location_y"),
        RetrieverObjectLink("location_object_reference", "Triggers",
                            "trigger_data[__index__].effect_data[__index__].location_object_reference"),
        RetrieverObjectLink("area_1_x", "Triggers", "trigger_data[__index__].effect_data[__index__].area_1_x"),
        RetrieverObjectLink("area_1_y", "Triggers", "trigger_data[__index__].effect_data[__index__].area_1_y"),
        RetrieverObjectLink("area_2_x", "Triggers", "trigger_data[__index__].effect_data[__index__].area_2_x"),
        RetrieverObjectLink("area_2_y", "Triggers", "trigger_data[__index__].effect_data[__index__].area_2_y"),
        RetrieverObjectLink("object_group", "Triggers", "trigger_data[__index__].effect_data[__index__].object_group"),
        RetrieverObjectLink("object_type", "Triggers", "trigger_data[__index__].effect_data[__index__].object_type"),
        RetrieverObjectLink("instruction_panel_position", "Triggers",
                            "trigger_data[__index__].effect_data[__index__].instruction_panel_position"),
        RetrieverObjectLink("attack_stance", "Triggers",
                            "trigger_data[__index__].effect_data[__index__].attack_stance"),
        RetrieverObjectLink("time_unit", "Triggers", "trigger_data[__index__].effect_data[__index__].time_unit"),
        RetrieverObjectLink("enabled", "Triggers",
                            "trigger_data[__index__].effect_data[__index__].enabled"),
        RetrieverObjectLink("food", "Triggers", "trigger_data[__index__].effect_data[__index__].food"),
        RetrieverObjectLink("wood", "Triggers", "trigger_data[__index__].effect_data[__index__].wood"),
        RetrieverObjectLink("stone", "Triggers", "trigger_data[__index__].effect_data[__index__].stone"),
        RetrieverObjectLink("gold", "Triggers", "trigger_data[__index__].effect_data[__index__].gold"),
        RetrieverObjectLink("item_id", "Triggers", "trigger_data[__index__].effect_data[__index__].item_id"),
        RetrieverObjectLink("flash_object", "Triggers", "trigger_data[__index__].effect_data[__index__].flash_object"),
        RetrieverObjectLink("force_research_technology", "Triggers",
                            "trigger_data[__index__].effect_data[__index__].force_research_technology"),
        RetrieverObjectLink("visibility_state", "Triggers",
                            "trigger_data[__index__].effect_data[__index__].visibility_state"),
        RetrieverObjectLink("scroll", "Triggers", "trigger_data[__index__].effect_data[__index__].scroll"),
        RetrieverObjectLink("operation", "Triggers", "trigger_data[__index__].effect_data[__index__].operation"),
        RetrieverObjectLink("object_list_unit_id_2", "Triggers",
                            "trigger_data[__index__].effect_data[__index__].object_list_unit_id_2"),
        RetrieverObjectLink("button_location", "Triggers",
                            "trigger_data[__index__].effect_data[__index__].button_location"),
        RetrieverObjectLink("ai_signal_value", "Triggers",
                            "trigger_data[__index__].effect_data[__index__].ai_signal_value"),
        RetrieverObjectLink("object_attributes", "Triggers",
                            "trigger_data[__index__].effect_data[__index__].object_attributes"),
        RetrieverObjectLink("variable", "Triggers",
                            "trigger_data[__index__].effect_data[__index__].variable"),
        RetrieverObjectLink("timer", "Triggers",
                            "trigger_data[__index__].effect_data[__index__].timer"),
        RetrieverObjectLink("facet", "Triggers", "trigger_data[__index__].effect_data[__index__].facet"),
        RetrieverObjectLink("play_sound", "Triggers", "trigger_data[__index__].effect_data[__index__].play_sound"),
        RetrieverObjectLink("player_color", "Triggers", "trigger_data[__index__].effect_data[__index__].player_color",
                            Support(since=1.40)),
        RetrieverObjectLink("message", "Triggers", "trigger_data[__index__].effect_data[__index__].message"),
        RetrieverObjectLink("sound_name", "Triggers", "trigger_data[__index__].effect_data[__index__].sound_name"),
        RetrieverObjectLink("selected_object_ids", "Triggers",
                            "trigger_data[__index__].effect_data[__index__].selected_object_ids"),
    ]

    def __init__(self,
                 effect_type: int = None,
                 ai_script_goal: int = None,
                 armour_attack_quantity: int = None,
                 armour_attack_class: int = None,
                 quantity: int = None,
                 tribute_list: int = None,
                 diplomacy: int = None,
                 object_list_unit_id: int = None,
                 source_player: int = None,
                 target_player: int = None,
                 technology: int = None,
                 string_id: int = None,
                 display_time: int = None,
                 trigger_id: int = None,
                 location_x: int = None,
                 location_y: int = None,
                 location_object_reference: int = None,
                 area_1_x: int = None,
                 area_1_y: int = None,
                 area_2_x: int = None,
                 area_2_y: int = None,
                 object_group: int = None,
                 object_type: int = None,
                 instruction_panel_position: int = None,
                 attack_stance: int = None,
                 time_unit: int = None,
                 enabled: int = None,
                 food: int = None,
                 wood: int = None,
                 stone: int = None,
                 gold: int = None,
                 item_id: int = None,
                 flash_object: int = None,
                 force_research_technology: int = None,
                 visibility_state: int = None,
                 scroll: int = None,
                 operation: int = None,
                 object_list_unit_id_2: int = None,
                 button_location: int = None,
                 ai_signal_value: int = None,
                 object_attributes: int = None,
                 variable: int = None,
                 timer: int = None,
                 facet: int = None,
                 play_sound: int = None,
                 player_color: int = None,
                 message: str = None,
                 sound_name: str = None,
                 selected_object_ids: List[int] = None,
                 ):
        raise_if_not_int_subclass([object_list_unit_id, technology, object_list_unit_id_2])

        if selected_object_ids is None:
            selected_object_ids = []

        self.effect_type: int = effect_type
        self.ai_script_goal: int = ai_script_goal
        self.armour_attack_quantity: int = armour_attack_quantity
        self.armour_attack_class: int = armour_attack_class
        self.quantity: int = quantity
        self.tribute_list: int = tribute_list
        self.diplomacy: int = diplomacy
        self.object_list_unit_id: int = object_list_unit_id
        self.source_player: int = source_player
        self.target_player: int = target_player
        self.technology: int = technology
        self.string_id: int = string_id
        self.display_time: int = display_time
        self.trigger_id: int = trigger_id
        self.location_x: int = location_x
        self.location_y: int = location_y
        self.location_object_reference: int = location_object_reference
        self.area_1_x: int = area_1_x
        self.area_1_y: int = area_1_y
        self.area_2_x: int = area_2_x
        self.area_2_y: int = area_2_y
        self.object_group: int = object_group
        self.object_type: int = object_type
        self.instruction_panel_position: int = instruction_panel_position
        self.attack_stance: int = attack_stance
        self.time_unit: int = time_unit
        self.enabled: int = enabled
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
        self.object_list_unit_id_2: int = object_list_unit_id_2
        self.button_location: int = button_location
        self.ai_signal_value: int = ai_signal_value
        self.object_attributes: int = object_attributes
        self.variable: int = variable
        self.timer: int = timer
        self.facet: int = facet
        self.play_sound: int = play_sound
        self.player_color: int = player_color
        self.message: str = message
        self.sound_name: str = sound_name
        self.selected_object_ids: List[int] = selected_object_ids

        super().__init__()

    @property
    def selected_object_ids(self) -> List[int]:
        return self._selected_object_ids

    @selected_object_ids.setter
    def selected_object_ids(self, val: List[int]):
        val = listify(val)
        self._selected_object_ids = val

    def get_content_as_string(self) -> str:
        if self.effect_type not in effects.attributes:  # Unknown effect
            attributes_list = effects.empty_attributes
        else:
            attributes_list = effects.attributes[self.effect_type]

        return_string = ""
        for attribute in attributes_list:
            attribute_value = getattr(self, attribute)
            if attribute == "effect_type" or attribute_value in [[], [-1], "", " ", -1]:
                continue
            return_string += "\t\t\t\t" + attribute + ": " + str(attribute_value) + "\n"

        if return_string == "":
            return "\t\t\t\t<< No Attributes >>\n"

        return return_string
