from typing import List

from AoE2ScenarioParser.datasets import effects, conditions
from AoE2ScenarioParser.datasets.conditions import Condition
from AoE2ScenarioParser.datasets.effects import Effect
from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.helper.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.condition_obj import ConditionObject
from AoE2ScenarioParser.objects.effect_obj import EffectObject


class TriggerObject(AoE2Object):
    """Object for handling a trigger."""

    _link_list = [
        RetrieverObjectLink("name", "TriggerPiece", "trigger_data[__index__].trigger_name"),
        RetrieverObjectLink("description", "TriggerPiece", "trigger_data[__index__].trigger_description"),
        RetrieverObjectLink("description_stid", "TriggerPiece", "trigger_data[__index__].description_string_table_id"),
        RetrieverObjectLink("display_as_objective", "TriggerPiece", "trigger_data[__index__].display_as_objective"),
        RetrieverObjectLink("short_description", "TriggerPiece", "trigger_data[__index__].short_description"),
        RetrieverObjectLink("short_description_stid", "TriggerPiece",
                            "trigger_data[__index__].short_description_string_table_id"),
        RetrieverObjectLink("display_on_screen", "TriggerPiece", "trigger_data[__index__].display_on_screen"),
        RetrieverObjectLink("description_order", "TriggerPiece", "trigger_data[__index__].objective_description_order"),
        RetrieverObjectLink("enabled", "TriggerPiece", "trigger_data[__index__].enabled"),
        RetrieverObjectLink("looping", "TriggerPiece", "trigger_data[__index__].looping"),
        RetrieverObjectLink("header", "TriggerPiece", "trigger_data[__index__].make_header"),
        RetrieverObjectLink("mute_objectives", "TriggerPiece", "trigger_data[__index__].mute_objectives"),
        RetrieverObjectLink("conditions", "TriggerPiece", "trigger_data[__index__].condition_data",
                            process_as_object=ConditionObject),
        RetrieverObjectLink("condition_order", "TriggerPiece", "trigger_data[__index__].condition_display_order_array"),
        RetrieverObjectLink("effects", "TriggerPiece", "trigger_data[__index__].effect_data",
                            process_as_object=EffectObject),
        RetrieverObjectLink("effect_order", "TriggerPiece", "trigger_data[__index__].effect_display_order_array"),
        RetrieverObjectLink("trigger_id", retrieve_instance_number=True),
    ]

    def __init__(self,
                 name: str,
                 description: str = "",
                 description_stid: int = -1,
                 display_as_objective: int = 0,
                 short_description: str = "",
                 short_description_stid: int = -1,
                 display_on_screen: int = 0,
                 description_order: int = 0,
                 enabled: int = 1,
                 looping: int = 0,
                 header: int = 0,
                 mute_objectives: int = 0,
                 conditions: List[ConditionObject] = None,
                 condition_order: List[int] = None,
                 effects: List[EffectObject] = None,
                 effect_order: List[int] = None,
                 trigger_id: int = -1,
                 ):

        if conditions is None:
            conditions = []
        if condition_order is None:
            condition_order = []
        if effects is None:
            effects = []
        if effect_order is None:
            effect_order = []

        self.name: str = name
        self.description: str = description
        self.description_stid: int = description_stid
        self.display_as_objective: int = display_as_objective
        self.short_description: str = short_description
        self.short_description_stid: int = short_description_stid
        self.display_on_screen: int = display_on_screen
        self.description_order: int = description_order
        self.enabled: int = enabled
        self.looping: int = looping
        self.header: int = header
        self.mute_objectives: int = mute_objectives
        self.conditions: List[ConditionObject] = conditions
        self.condition_order: List[int] = condition_order
        self.effects: List[EffectObject] = effects
        self.effect_order: List[int] = effect_order
        self.trigger_id: int = trigger_id

        super().__init__()

    @property
    def conditions(self) -> List[ConditionObject]:
        return self._conditions

    @conditions.setter
    def conditions(self, val: List[ConditionObject]) -> None:
        self._conditions = val
        self.condition_order = list(range(0, len(val)))

    @property
    def effects(self) -> List[EffectObject]:
        return self._effects

    @effects.setter
    def effects(self, val: List[EffectObject]) -> None:
        self._effects = val
        self.effect_order = list(range(0, len(val)))

    def add_effect(self, effect_type: Effect, ai_script_goal=None, aa_quantity=None, aa_armor_or_attack_type=None,
                   quantity=None, tribute_list=None, diplomacy=None, number_of_units_selected=None,
                   object_list_unit_id=None, source_player=None, target_player=None, technology=None, string_id=None,
                   display_time=None, trigger_id=None, location_x=None, location_y=None, location_object_reference=None,
                   area_1_x=None, area_1_y=None, area_2_x=None, area_2_y=None, object_group=None, object_type=None,
                   instruction_panel_position=None, attack_stance=None, time_unit=None, enabled_or_victory=None,
                   food=None, wood=None, stone=None, gold=None, item_id=None, flash_object=None,
                   force_research_technology=None, visibility_state=None, scroll=None, operation=None,
                   object_list_unit_id_2=None, button_location=None, ai_signal_value=None, object_attributes=None,
                   from_variable=None, variable_or_timer=None, facet=None, play_sound=None, message=None,
                   sound_name=None, selected_object_ids=None) -> EffectObject:
        effect_defaults = effects.default_attributes[effect_type]
        effect_attr = {}
        for key, value in effect_defaults.items():
            effect_attr[key] = (locals()[key] if locals()[key] is not None else value)
        new_effect = EffectObject(**{**effect_defaults, **effect_attr})
        self.effects.append(new_effect)
        helper.update_order_array(self.effect_order, len(self.effects))
        return new_effect

    def add_condition(self, condition_type: Condition, amount_or_quantity=None,
                      resource_type_or_tribute_list=None, unit_object=None, next_object=None, object_list=None,
                      source_player=None, technology=None, timer=None, area_1_x=None, area_1_y=None, area_2_x=None,
                      area_2_y=None, object_group=None, object_type=None, ai_signal=None, inverted=None, variable=None,
                      comparison=None, target_player=None) -> ConditionObject:
        condition_defaults = conditions.default_attributes[condition_type]
        condition_attr = {}
        for key, value in condition_defaults.items():
            condition_attr[key] = (locals()[key] if locals()[key] is not None else value)
        new_cond = ConditionObject(**conditions.default_attributes[condition_type.value])
        self.conditions.append(new_cond)
        helper.update_order_array(self.condition_order, len(self.conditions))
        return new_cond

    def get_effect(self, effect_index: int = None, display_index: int = None) -> EffectObject:
        helper.evaluate_index_params(effect_index, display_index, "effect")

        if effect_index is None:
            effect_index = self.effect_order[display_index]

        return self.effects[effect_index]

    def get_condition(self, condition_index: int = None, display_index: int = None) -> ConditionObject:
        helper.evaluate_index_params(condition_index, display_index, "condition")

        if condition_index is None:
            condition_index = self.condition_order[display_index]

        return self.conditions[condition_index]

    def remove_effect(self, effect_index: int = None, display_index: int = None, effect: EffectObject = None) -> None:
        if effect is None:
            helper.evaluate_index_params(effect_index, display_index, "effect")
        else:
            effect_index = self.effects.index(effect)

        if effect_index is None:
            effect_index = self.effect_order[display_index]
        else:
            display_index = self.effect_order.index(effect_index)

        del self.effects[effect_index]
        del self.effect_order[display_index]

        self.effect_order = [x - 1 if x > effect_index else x for x in self.effect_order]

    def remove_condition(self, condition_index: int = None, display_index: int = None, condition: EffectObject = None) \
            -> None:
        if condition is None:
            helper.evaluate_index_params(condition_index, display_index, "condition")
        else:
            condition_index = self.conditions.index(condition)

        if condition_index is None:
            condition_index = self.condition_order[display_index]
        else:
            display_index = self.condition_order.index(condition_index)

        del self.conditions[condition_index]
        del self.condition_order[display_index]

        self.condition_order = [x - 1 if x > condition_index else x for x in self.condition_order]

    def get_content_as_string(self) -> str:
        return_string = ""
        data_tba = {
            'enabled': self.enabled != 0,
            'looping': self.looping != 0
        }

        if self.description != "":
            data_tba['description'] = f"'{self.description}'"
        if self.description_stid != -1:
            data_tba['description_stid'] = self.description_stid
        if self.short_description != "":
            data_tba['short_description'] = f"'{self.short_description}'"
        if self.short_description_stid != -1:
            data_tba['short_description_stid'] = self.short_description_stid
        if self.display_as_objective != 0:
            data_tba['display_as_objective'] = (self.display_as_objective != 0)
        if self.display_on_screen != 0:
            data_tba['display_on_screen'] = (self.display_on_screen != 0)
        if self.description_order != 0:
            data_tba['description_order'] = self.description_order
        if self.header != 0:
            data_tba['header'] = (self.header != 0)
        if self.mute_objectives != 0:
            data_tba['mute_objectives'] = (self.mute_objectives != 0)

        for key, value in data_tba.items():
            return_string += f"\t\t{key}: {value}\n"

        if len(self.condition_order) > 0:
            return_string += "\t\tconditions:\n"
            for c_display_order, condition_id in enumerate(self.condition_order):
                condition = self.conditions[condition_id]

                return_string += f"\t\t\t{conditions.condition_names[condition.condition_type]} " \
                                 f"[Index: {condition_id}, Display: {c_display_order}]:\n"
                return_string += condition.get_content_as_string()

        if len(self.effect_order) > 0:
            return_string += "\t\teffects:\n"
            for e_display_order, effect_id in enumerate(self.effect_order):
                effect = self.effects[effect_id]

                try:
                    return_string += f"\t\t\t{effects.effect_names[effect.effect_type]}"
                except KeyError:
                    return_string += f"\t\t\tUnknown Effect. ID: {effect.effect_type}"
                return_string += f" [Index: {effect_id}, Display: {e_display_order}]:\n"
                return_string += effect.get_content_as_string()

        return return_string

    def get_summary_as_string(self) -> str:
        pass
