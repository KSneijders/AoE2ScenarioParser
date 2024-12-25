from typing import List, Any

import AoE2ScenarioParser.datasets.conditions as condition_dataset
import AoE2ScenarioParser.datasets.effects as effect_dataset
from AoE2ScenarioParser.datasets.conditions import ConditionId
from AoE2ScenarioParser.datasets.effects import EffectId
from AoE2ScenarioParser.exceptions.asp_exceptions import UnsupportedAttributeError
from AoE2ScenarioParser.helper.helper import mutually_exclusive
from AoE2ScenarioParser.helper.list_functions import list_changed, update_order_array, hash_list
from AoE2ScenarioParser.helper.string_manipulations import add_tabs
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.data_objects.condition import Condition
from AoE2ScenarioParser.objects.data_objects.effect import Effect
from AoE2ScenarioParser.objects.support.new_condition import NewConditionSupport
from AoE2ScenarioParser.objects.support.new_effect import NewEffectSupport
from AoE2ScenarioParser.objects.support.trigger_object import TriggerComponent
from AoE2ScenarioParser.objects.support.uuid_list import UuidList
from AoE2ScenarioParser.scenarios.scenario_store import getters
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.sections.retrievers.retriever_object_link_group import RetrieverObjectLinkGroup


class Trigger(AoE2Object, TriggerComponent):
    """Object for handling a trigger."""

    _link_list = [
        RetrieverObjectLinkGroup("Triggers", "trigger_data[__index__]", group=[
            RetrieverObjectLink("name", link="trigger_name"),
            RetrieverObjectLink("description", link="trigger_description"),
            RetrieverObjectLink("description_stid", link="description_string_table_id"),
            RetrieverObjectLink("display_as_objective"),
            RetrieverObjectLink("short_description"),
            RetrieverObjectLink("short_description_stid", link="short_description_string_table_id"),
            RetrieverObjectLink("display_on_screen"),
            RetrieverObjectLink("description_order", link="objective_description_order"),
            RetrieverObjectLink("enabled"),
            RetrieverObjectLink("looping"),
            RetrieverObjectLink("header", link="make_header"),
            RetrieverObjectLink("mute_objectives"),
            RetrieverObjectLink("conditions", link="condition_data", process_as_object=Condition),
            RetrieverObjectLink("condition_order", link="condition_display_order_array"),
            RetrieverObjectLink("effects", link="effect_data", process_as_object=Effect),
            RetrieverObjectLink("effect_order", link="effect_display_order_array"),
        ]),
        RetrieverObjectLink("trigger_id", retrieve_history_number=0),
    ]

    def __init__(
            self,
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
            conditions: List[Condition] = None,
            condition_order: List[int] = None,
            effects: List[Effect] = None,
            effect_order: List[int] = None,
            trigger_id: int = -1,
            **kwargs
    ):
        super().__init__(**kwargs)

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
        self._condition_hash = hash_list(conditions)
        self.conditions: List[Condition] = conditions
        self.condition_order: List[int] = condition_order
        self._effect_hash = hash_list(effects)
        self.effects: List[Effect] = effects
        self.effect_order: List[int] = effect_order
        self.trigger_id: int = trigger_id

        self.new_effect: NewEffectSupport = NewEffectSupport(self)
        self.new_condition: NewConditionSupport = NewConditionSupport(self)

    def _deepcopy_entry(self, result, k, v, memo) -> Any:
        if k == 'new_effect':
            return NewEffectSupport(result)
        elif k == 'new_condition':
            return NewConditionSupport(result)
        else:
            return super()._deepcopy_entry(result, k, v, memo)

    @property
    def condition_order(self) -> List[int]:
        """The condition display order """
        if list_changed(self.conditions, self._condition_hash):
            update_order_array(self._condition_order, len(self.conditions))
            self._condition_hash = hash_list(self.conditions)
        return self._condition_order

    @condition_order.setter
    def condition_order(self, val):
        self._condition_order = val

    @property
    def effect_order(self) -> List[int]:
        """The effect display order """
        if list_changed(self.effects, self._effect_hash):
            update_order_array(self._effect_order, len(self.effects))
            self._effect_hash = hash_list(self.effects)
        return self._effect_order

    @effect_order.setter
    def effect_order(self, val):
        self._effect_order = val

    @property
    def conditions(self) -> List[Condition]:
        """All conditions in this trigger"""
        return self._conditions

    @conditions.setter
    def conditions(self, val: List[Condition]) -> None:
        self._conditions = UuidList(self._uuid, val)
        self.condition_order = list(range(0, len(val)))

    @property
    def effects(self) -> List[Effect]:
        """All effects in this trigger"""
        return self._effects

    @effects.setter
    def effects(self, val: List[Effect]) -> None:
        self._effects = UuidList(self._uuid, val)
        self.effect_order = list(range(0, len(val)))

    def _add_effect(self, effect_type: EffectId, ai_script_goal=None, armour_attack_quantity=None,
                    armour_attack_class=None, quantity=None, tribute_list=None, diplomacy=None,
                    object_list_unit_id=None, source_player=None, target_player=None, technology=None, string_id=None,
                    display_time=None, trigger_id=None, location_x=None, location_y=None,
                    location_object_reference=None, area_x1=None, area_y1=None, area_x2=None, area_y2=None,
                    object_group=None, object_type=None, instruction_panel_position=None, attack_stance=None,
                    time_unit=None, enabled=None, food=None, wood=None, stone=None, gold=None, item_id=None,
                    flash_object=None, force_research_technology=None, visibility_state=None, scroll=None,
                    operation=None, object_list_unit_id_2=None, button_location=None, ai_signal_value=None,
                    object_attributes=None, variable=None, timer=None, facet=None, play_sound=None, message=None,
                    player_color=None, sound_name=None, selected_object_ids=None, color_mood=None, reset_timer=None,
                    object_state=None, action_type=None, resource_1=None, resource_1_quantity=None, resource_2=None,
                    resource_2_quantity=None, resource_3=None, resource_3_quantity=None, unused_string_1=None,
                    unused_string_2=None, ) -> Effect:
        """Used to add new effect to trigger. Please use trigger.new_effect.<effect_name> instead"""

        def get_default_effect_attributes(eff_type):
            """Gets the default effect attributes based on a certain effect type, with exception handling"""
            sv = getters.get_scenario_version(self._uuid)
            try:
                # Get None defaults and overwrite them with effect specific defaults
                none_default = effect_dataset.default_attributes[0]
                effect_default = effect_dataset.default_attributes[eff_type]

                return {**none_default, **effect_default}
            except KeyError:
                effect = EffectId(eff_type)
                raise UnsupportedAttributeError(
                    f"The effect {effect.name} is not supported in scenario version {sv}"
                ) from None

        effect_defaults = get_default_effect_attributes(effect_type)
        effect_attr = {}
        for key, value in effect_defaults.items():
            effect_attr[key] = (locals()[key] if locals()[key] is not None else value)
        new_effect = Effect(**effect_attr, uuid=self._uuid)
        self.effects.append(new_effect)
        return new_effect

    def _add_condition(self, condition_type: ConditionId, quantity=None,
                       attribute=None, unit_object=None, next_object=None, object_list=None,
                       source_player=None, technology=None, timer=None, area_x1=None, area_y1=None, area_x2=None,
                       area_y2=None, object_group=None, object_type=None, ai_signal=None, inverted=None, variable=None,
                       comparison=None, target_player=None, unit_ai_action=None, xs_function=None, object_state=None,
                       timer_id=None, victory_timer_type=None, include_changeable_weapon_objects=None,
                       ) -> Condition:
        """Used to add new condition to trigger. Please use trigger.new_condition.<condition_name> instead"""

        def get_default_condition_attributes(cond_type):
            """Gets the default condition attributes based on a certain condition type, with exception handling"""
            sv = getters.get_scenario_version(self._uuid)
            try:
                # Get None defaults and overwrite them with condition specific defaults
                none_default = condition_dataset.default_attributes[0]
                condition_default = condition_dataset.default_attributes[cond_type]

                return {**none_default, **condition_default}
            except KeyError:
                condition = ConditionId(cond_type)
                raise UnsupportedAttributeError(
                    f"The condition {condition.name} is not supported in scenario version {sv}"
                ) from None

        condition_defaults = get_default_condition_attributes(condition_type)
        condition_attr = {}
        for key, value in condition_defaults.items():
            condition_attr[key] = (locals()[key] if locals()[key] is not None else value)
        new_condition = Condition(**condition_attr, uuid=self._uuid)
        self.conditions.append(new_condition)
        return new_condition

    def get_effect(self, effect_index: int = None, display_index: int = None) -> Effect:
        """
        Retrieve an effect based on its (display) index

        Args:
            effect_index: The effect index of the effect to retrieve
            display_index: The display index of the effect to retrieve

        Raises:
            ValueError: If more than one parameter is used simultaneously
            IndexError: If the effect could not be found

        Returns:
            The wanted effect
        """
        if not mutually_exclusive(effect_index is not None, display_index is not None):
            raise ValueError(f"Please identify an effect using either effect_index or display_index.")

        if effect_index is None:
            effect_index = self.effect_order[display_index]

        return self.effects[effect_index]

    def get_condition(self, condition_index: int = None, display_index: int = None) -> Condition:
        """
        Retrieve a condition based on its (display) index

        Args:
            condition_index: The condition index of the condition to retrieve
            display_index: The display index of the condition to retrieve

        Raises:
            ValueError: If more than one parameter is used simultaneously
            IndexError: If the condition could not be found

        Returns:
            The wanted condition
        """
        if not mutually_exclusive(condition_index is not None, display_index is not None):
            raise ValueError(f"Please identify a condition using either condition_index or display_index.")

        if condition_index is None:
            condition_index = self.condition_order[display_index]

        return self.conditions[condition_index]

    def remove_effect(self, effect_index: int = None, display_index: int = None, effect: Effect = None) -> None:
        """
        Remove an effect from this trigger

        Args:
            effect_index: The effect index of the condition to remove
            display_index: The display index of the condition to remove
            effect: A reference to the effect object to remove from this trigger

        Raises:
            ValueError: If more than one parameter is used simultaneously
        """
        if not mutually_exclusive(effect_index is not None, display_index is not None, effect is not None):
            raise ValueError(f"Please identify an effect using either effect_index, display_index or effect.")

        if effect is not None:
            effect_index = self.effects.index(effect)
        if effect_index is None:
            effect_index = self.effect_order[display_index]

        del self.effects[effect_index]

    def remove_condition(self, condition_index: int = None, display_index: int = None, condition: Condition = None) \
            -> None:
        """
        Remove a condition from this trigger

        Args:
            condition_index: The condition index of the condition to remove
            display_index: The display index of the condition to remove
            condition: A reference to the condition object to remove from this trigger

        Raises:
            ValueError: If more than one parameter is used simultaneously
        """
        if not mutually_exclusive(condition_index is not None, display_index is not None, condition is not None):
            raise ValueError(f"Please identify a condition using either condition_index, display_index or condition.")

        if condition is not None:
            condition_index = self.conditions.index(condition)

        if condition_index is None:
            condition_index = self.condition_order[display_index]

        del self.conditions[condition_index]

    def get_content_as_string(self, include_trigger_definition: bool = False) -> str:
        """
        Create a human-readable string showcasing all content of this trigger.
        This includes all the content within the conditions and effects of this trigger.

        This is also the function that is called when doing: `print(trigger)`

        Args:
            include_trigger_definition: If the trigger meta-data should be added by this function

        Returns:
            The created string
        """
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
            return_string += f"{key}: {value}\n"

        if len(self.condition_order) > 0:
            return_string += "conditions:\n"
            for c_display_order, condition_id in enumerate(self.condition_order):
                condition = self.conditions[condition_id]

                name = f"Unknown ({condition.condition_type})"
                if condition.condition_type in condition_dataset.condition_names:
                    name = condition_dataset.condition_names[condition.condition_type]

                return_string += f"\t{name} [Index: {condition_id}, Display: {c_display_order}]:\n"
                return_string += add_tabs(condition.get_content_as_string(), 2)

        if len(self.effect_order) > 0:
            return_string += "effects:\n"
            for e_display_order, effect_id in enumerate(self.effect_order):
                effect = self.effects[effect_id]

                name = f"Unknown ({effect.effect_type})"
                if effect.effect_type in effect_dataset.effect_names:
                    name = effect_dataset.effect_names[effect.effect_type]

                return_string += f"\t{name} [Index: {effect_id}, Display: {e_display_order}]:\n"
                return_string += add_tabs(effect.get_content_as_string(), 2)

        if include_trigger_definition:
            return f"\"{self.name}\" [Index: {self.trigger_id}]\n" + add_tabs(return_string, 1)
        return return_string

    def __str__(self) -> str:
        return f"[Trigger] {self.get_content_as_string(include_trigger_definition=True)}"
