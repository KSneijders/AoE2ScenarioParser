from __future__ import annotations

from AoE2ScenarioParser.datasets.conditions import ConditionId
from AoE2ScenarioParser.objects.data_objects.condition import Condition


class NewConditionSupport:
    def __init__(self, trigger_ref):
        self._trigger_ref = trigger_ref

    def none(
            self,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.NONE,
        )

    def bring_object_to_area(
            self,
            unit_object: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            inverted: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.BRING_OBJECT_TO_AREA,
            unit_object=unit_object,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            inverted=inverted,
        )

    def bring_object_to_object(
            self,
            unit_object: int | None = None,
            next_object: int | None = None,
            inverted: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.BRING_OBJECT_TO_OBJECT,
            unit_object=unit_object,
            next_object=next_object,
            inverted=inverted,
        )

    def own_objects(
            self,
            quantity: int | None = None,
            object_list: int | None = None,
            source_player: int | None = None,
            object_group: int | None = None,
            object_type: int | None = None,
            include_changeable_weapon_objects: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.OWN_OBJECTS,
            quantity=quantity,
            object_list=object_list,
            source_player=source_player,
            object_group=object_group,
            object_type=object_type,
            include_changeable_weapon_objects=include_changeable_weapon_objects,
        )

    def own_fewer_objects(
            self,
            quantity: int | None = None,
            object_list: int | None = None,
            source_player: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            object_group: int | None = None,
            object_type: int | None = None,
            include_changeable_weapon_objects: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.OWN_FEWER_OBJECTS,
            quantity=quantity,
            object_list=object_list,
            source_player=source_player,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            object_group=object_group,
            object_type=object_type,
            include_changeable_weapon_objects=include_changeable_weapon_objects,
        )

    def objects_in_area(
            self,
            quantity: int | None = None,
            object_list: int | None = None,
            source_player: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            object_group: int | None = None,
            object_type: int | None = None,
            inverted: int | None = None,
            object_state: int | None = None,
            include_changeable_weapon_objects: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.OBJECTS_IN_AREA,
            quantity=quantity,
            object_list=object_list,
            source_player=source_player,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            object_group=object_group,
            object_type=object_type,
            inverted=inverted,
            object_state=object_state,
            include_changeable_weapon_objects=include_changeable_weapon_objects,
        )

    def destroy_object(
            self,
            unit_object: int | None = None,
            inverted: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.DESTROY_OBJECT,
            unit_object=unit_object,
            inverted=inverted,
        )

    def capture_object(
            self,
            unit_object: int | None = None,
            source_player: int | None = None,
            inverted: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.CAPTURE_OBJECT,
            unit_object=unit_object,
            source_player=source_player,
            inverted=inverted,
        )

    def accumulate_attribute(
            self,
            quantity: int | None = None,
            attribute: int | None = None,
            source_player: int | None = None,
            inverted: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.ACCUMULATE_ATTRIBUTE,
            quantity=quantity,
            attribute=attribute,
            source_player=source_player,
            inverted=inverted,
        )

    def research_technology(
            self,
            source_player: int | None = None,
            technology: int | None = None,
            inverted: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.RESEARCH_TECHNOLOGY,
            source_player=source_player,
            technology=technology,
            inverted=inverted,
        )

    def timer(
            self,
            timer: int | None = None,
            inverted: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.TIMER,
            timer=timer,
            inverted=inverted,
        )

    def object_selected(
            self,
            unit_object: int | None = None,
            inverted: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.OBJECT_SELECTED,
            unit_object=unit_object,
            inverted=inverted,
        )

    def ai_signal(
            self,
            ai_signal: int | None = None,
            inverted: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.AI_SIGNAL,
            ai_signal=ai_signal,
            inverted=inverted,
        )

    def player_defeated(
            self,
            source_player: int | None = None,
            inverted: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.PLAYER_DEFEATED,
            source_player=source_player,
            inverted=inverted,
        )

    def object_has_target(
            self,
            unit_object: int | None = None,
            next_object: int | None = None,
            object_list: int | None = None,
            object_group: int | None = None,
            object_type: int | None = None,
            inverted: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.OBJECT_HAS_TARGET,
            unit_object=unit_object,
            next_object=next_object,
            object_list=object_list,
            object_group=object_group,
            object_type=object_type,
            inverted=inverted,
        )

    def object_visible(
            self,
            unit_object: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.OBJECT_VISIBLE,
            unit_object=unit_object,
        )

    def object_not_visible(
            self,
            unit_object: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.OBJECT_NOT_VISIBLE,
            unit_object=unit_object,
        )

    def researching_tech(
            self,
            source_player: int | None = None,
            technology: int | None = None,
            inverted: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.RESEARCHING_TECH,
            source_player=source_player,
            technology=technology,
            inverted=inverted,
        )

    def units_garrisoned(
            self,
            quantity: int | None = None,
            unit_object: int | None = None,
            inverted: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.UNITS_GARRISONED,
            quantity=quantity,
            unit_object=unit_object,
            inverted=inverted,
        )

    def difficulty_level(
            self,
            quantity: int | None = None,
            inverted: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.DIFFICULTY_LEVEL,
            quantity=quantity,
            inverted=inverted,
        )

    def chance(
            self,
            quantity: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.CHANCE,
            quantity=quantity,
        )

    def technology_state(
            self,
            quantity: int | None = None,
            source_player: int | None = None,
            technology: int | None = None,
            inverted: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.TECHNOLOGY_STATE,
            quantity=quantity,
            source_player=source_player,
            technology=technology,
            inverted=inverted,
        )

    def variable_value(
            self,
            quantity: int | None = None,
            inverted: int | None = None,
            variable: int | None = None,
            comparison: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.VARIABLE_VALUE,
            quantity=quantity,
            inverted=inverted,
            variable=variable,
            comparison=comparison,
        )

    def object_hp(
            self,
            quantity: int | None = None,
            unit_object: int | None = None,
            inverted: int | None = None,
            comparison: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.OBJECT_HP,
            quantity=quantity,
            unit_object=unit_object,
            inverted=inverted,
            comparison=comparison,
        )

    def diplomacy_state(
            self,
            quantity: int | None = None,
            source_player: int | None = None,
            inverted: int | None = None,
            target_player: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.DIPLOMACY_STATE,
            quantity=quantity,
            source_player=source_player,
            inverted=inverted,
            target_player=target_player,
        )

    def script_call(
            self,
            xs_function: str | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.SCRIPT_CALL,
            xs_function=xs_function,
        )

    def object_visible_multiplayer(
            self,
            unit_object: int | None = None,
            source_player: int | None = None,
            inverted: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.OBJECT_VISIBLE_MULTIPLAYER,
            unit_object=unit_object,
            source_player=source_player,
            inverted=inverted,
        )

    def object_selected_multiplayer(
            self,
            unit_object: int | None = None,
            source_player: int | None = None,
            inverted: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.OBJECT_SELECTED_MULTIPLAYER,
            unit_object=unit_object,
            source_player=source_player,
            inverted=inverted,
        )

    def object_has_action(
            self,
            unit_object: int | None = None,
            next_object: int | None = None,
            object_list: int | None = None,
            object_group: int | None = None,
            object_type: int | None = None,
            inverted: int | None = None,
            unit_ai_action: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.OBJECT_HAS_ACTION,
            unit_object=unit_object,
            next_object=next_object,
            object_list=object_list,
            object_group=object_group,
            object_type=object_type,
            inverted=inverted,
            unit_ai_action=unit_ai_action,
        )

    def or_(
            self,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.OR,
        )

    def ai_signal_multiplayer(
            self,
            ai_signal: int | None = None,
            inverted: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.AI_SIGNAL_MULTIPLAYER,
            ai_signal=ai_signal,
            inverted=inverted,
        )

    def and_(
            self,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.AND,
        )

    def building_is_trading(
            self,
            unit_object: int | None = None,
            inverted: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.BUILDING_IS_TRADING,
            unit_object=unit_object,
            inverted=inverted,
        )

    def display_timer_triggered(
            self,
            timer_id: int | None = None,
            inverted: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.DISPLAY_TIMER_TRIGGERED,
            timer_id=timer_id,
            inverted=inverted,
        )

    def victory_timer(
            self,
            quantity: int | None = None,
            source_player: int | None = None,
            inverted: int | None = None,
            comparison: int | None = None,
            victory_timer_type: int | None = None,
    ) -> Condition:
        return self._trigger_ref._add_condition(
            ConditionId.VICTORY_TIMER,
            quantity=quantity,
            source_player=source_player,
            inverted=inverted,
            comparison=comparison,
            victory_timer_type=victory_timer_type,
        )
