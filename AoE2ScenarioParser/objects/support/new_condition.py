# This file was generated based on: versions/DE/v1.41/conditions.json
from AoE2ScenarioParser.datasets.conditions import ConditionId


class NewConditionSupport:
    def __init__(self, trigger_ref):
        self.trigger_ref = trigger_ref

    def none(
            self,
    ):
        self.trigger_ref._add_condition(
            ConditionId.NONE,
        )

    def bring_object_to_area(
            self,
            unit_object=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            inverted=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.BRING_OBJECT_TO_AREA,
            unit_object=unit_object,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            inverted=inverted,
        )

    def bring_object_to_object(
            self,
            unit_object=None,
            next_object=None,
            inverted=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.BRING_OBJECT_TO_OBJECT,
            unit_object=unit_object,
            next_object=next_object,
            inverted=inverted,
        )

    def own_objects(
            self,
            quantity=None,
            object_list=None,
            source_player=None,
            object_group=None,
            object_type=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.OWN_OBJECTS,
            quantity=quantity,
            object_list=object_list,
            source_player=source_player,
            object_group=object_group,
            object_type=object_type,
        )

    def own_fewer_objects(
            self,
            quantity=None,
            object_list=None,
            source_player=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            object_group=None,
            object_type=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.OWN_FEWER_OBJECTS,
            quantity=quantity,
            object_list=object_list,
            source_player=source_player,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            object_group=object_group,
            object_type=object_type,
        )

    def objects_in_area(
            self,
            quantity=None,
            object_list=None,
            source_player=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            object_group=None,
            object_type=None,
            inverted=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.OBJECTS_IN_AREA,
            quantity=quantity,
            object_list=object_list,
            source_player=source_player,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            object_group=object_group,
            object_type=object_type,
            inverted=inverted,
        )

    def destroy_object(
            self,
            unit_object=None,
            inverted=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.DESTROY_OBJECT,
            unit_object=unit_object,
            inverted=inverted,
        )

    def capture_object(
            self,
            unit_object=None,
            source_player=None,
            inverted=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.CAPTURE_OBJECT,
            unit_object=unit_object,
            source_player=source_player,
            inverted=inverted,
        )

    def accumulate_attribute(
            self,
            quantity=None,
            attribute=None,
            source_player=None,
            inverted=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.ACCUMULATE_ATTRIBUTE,
            quantity=quantity,
            attribute=attribute,
            source_player=source_player,
            inverted=inverted,
        )

    def research_technology(
            self,
            source_player=None,
            technology=None,
            inverted=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.RESEARCH_TECHNOLOGY,
            source_player=source_player,
            technology=technology,
            inverted=inverted,
        )

    def timer(
            self,
            timer=None,
            inverted=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.TIMER,
            timer=timer,
            inverted=inverted,
        )

    def object_selected(
            self,
            unit_object=None,
            inverted=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.OBJECT_SELECTED,
            unit_object=unit_object,
            inverted=inverted,
        )

    def ai_signal(
            self,
            ai_signal=None,
            inverted=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.AI_SIGNAL,
            ai_signal=ai_signal,
            inverted=inverted,
        )

    def player_defeated(
            self,
            source_player=None,
            inverted=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.PLAYER_DEFEATED,
            source_player=source_player,
            inverted=inverted,
        )

    def object_has_target(
            self,
            unit_object=None,
            next_object=None,
            object_list=None,
            object_group=None,
            object_type=None,
            inverted=None,
    ):
        self.trigger_ref._add_condition(
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
            unit_object=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.OBJECT_VISIBLE,
            unit_object=unit_object,
        )

    def object_not_visible(
            self,
            unit_object=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.OBJECT_NOT_VISIBLE,
            unit_object=unit_object,
        )

    def researching_tech(
            self,
            source_player=None,
            technology=None,
            inverted=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.RESEARCHING_TECH,
            source_player=source_player,
            technology=technology,
            inverted=inverted,
        )

    def units_garrisoned(
            self,
            quantity=None,
            unit_object=None,
            inverted=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.UNITS_GARRISONED,
            quantity=quantity,
            unit_object=unit_object,
            inverted=inverted,
        )

    def difficulty_level(
            self,
            quantity=None,
            inverted=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.DIFFICULTY_LEVEL,
            quantity=quantity,
            inverted=inverted,
        )

    def chance(
            self,
            quantity=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.CHANCE,
            quantity=quantity,
        )

    def technology_state(
            self,
            quantity=None,
            source_player=None,
            technology=None,
            inverted=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.TECHNOLOGY_STATE,
            quantity=quantity,
            source_player=source_player,
            technology=technology,
            inverted=inverted,
        )

    def variable_value(
            self,
            quantity=None,
            inverted=None,
            variable=None,
            comparison=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.VARIABLE_VALUE,
            quantity=quantity,
            inverted=inverted,
            variable=variable,
            comparison=comparison,
        )

    def object_hp(
            self,
            quantity=None,
            unit_object=None,
            inverted=None,
            comparison=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.OBJECT_HP,
            quantity=quantity,
            unit_object=unit_object,
            inverted=inverted,
            comparison=comparison,
        )

    def diplomacy_state(
            self,
            quantity=None,
            source_player=None,
            inverted=None,
            target_player=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.DIPLOMACY_STATE,
            quantity=quantity,
            source_player=source_player,
            inverted=inverted,
            target_player=target_player,
        )

    def script_call(
            self,
            xs_function=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.SCRIPT_CALL,
            xs_function=xs_function,
        )

    def object_visible_multiplayer(
            self,
            unit_object=None,
            source_player=None,
            inverted=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.OBJECT_VISIBLE_MULTIPLAYER,
            unit_object=unit_object,
            source_player=source_player,
            inverted=inverted,
        )

    def object_selected_multiplayer(
            self,
            unit_object=None,
            source_player=None,
            inverted=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.OBJECT_SELECTED_MULTIPLAYER,
            unit_object=unit_object,
            source_player=source_player,
            inverted=inverted,
        )

    def object_has_action(
            self,
            unit_object=None,
            next_object=None,
            inverted=None,
            unit_ai_action=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.OBJECT_HAS_ACTION,
            unit_object=unit_object,
            next_object=next_object,
            inverted=inverted,
            unit_ai_action=unit_ai_action,
        )

    def or_(
            self,
    ):
        self.trigger_ref._add_condition(
            ConditionId.OR,
        )

    def ai_signal_multiplayer(
            self,
            ai_signal=None,
            inverted=None,
    ):
        self.trigger_ref._add_condition(
            ConditionId.AI_SIGNAL_MULTIPLAYER,
            ai_signal=ai_signal,
            inverted=inverted,
        )
