# This file was generated based on: versions/DE/v1.41/effects.json
from AoE2ScenarioParser.datasets.effects import EffectId


class NewEffectSupport:
    def __init__(self, trigger_ref):
        self.trigger_ref = trigger_ref

    def none(
            self,
    ):
        self.trigger_ref._add_effect(
            EffectId.NONE,
        )

    def change_diplomacy(
            self,
            diplomacy=None,
            source_player=None,
            target_player=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CHANGE_DIPLOMACY,
            diplomacy=diplomacy,
            source_player=source_player,
            target_player=target_player,
        )

    def research_technology(
            self,
            source_player=None,
            technology=None,
            force_research_technology=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.RESEARCH_TECHNOLOGY,
            source_player=source_player,
            technology=technology,
            force_research_technology=force_research_technology,
        )

    def send_chat(
            self,
            source_player=None,
            string_id=None,
            message=None,
            sound_name=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.SEND_CHAT,
            source_player=source_player,
            string_id=string_id,
            message=message,
            sound_name=sound_name,
        )

    def play_sound(
            self,
            source_player=None,
            location_x=None,
            location_y=None,
            location_object_reference=None,
            sound_name=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.PLAY_SOUND,
            source_player=source_player,
            location_x=location_x,
            location_y=location_y,
            location_object_reference=location_object_reference,
            sound_name=sound_name,
        )

    def tribute(
            self,
            quantity=None,
            tribute_list=None,
            source_player=None,
            target_player=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.TRIBUTE,
            quantity=quantity,
            tribute_list=tribute_list,
            source_player=source_player,
            target_player=target_player,
        )

    def unlock_gate(
            self,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.UNLOCK_GATE,
            selected_object_ids=selected_object_ids,
        )

    def lock_gate(
            self,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.LOCK_GATE,
            selected_object_ids=selected_object_ids,
        )

    def activate_trigger(
            self,
            trigger_id=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.ACTIVATE_TRIGGER,
            trigger_id=trigger_id,
        )

    def deactivate_trigger(
            self,
            trigger_id=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.DEACTIVATE_TRIGGER,
            trigger_id=trigger_id,
        )

    def ai_script_goal(
            self,
            ai_script_goal=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.AI_SCRIPT_GOAL,
            ai_script_goal=ai_script_goal,
        )

    def create_object(
            self,
            object_list_unit_id=None,
            source_player=None,
            location_x=None,
            location_y=None,
            item_id=None,
            facet=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CREATE_OBJECT,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            location_x=location_x,
            location_y=location_y,
            item_id=item_id,
            facet=facet,
        )

    def task_object(
            self,
            object_list_unit_id=None,
            source_player=None,
            location_x=None,
            location_y=None,
            location_object_reference=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            object_group=None,
            object_type=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.TASK_OBJECT,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            location_x=location_x,
            location_y=location_y,
            location_object_reference=location_object_reference,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            object_group=object_group,
            object_type=object_type,
            selected_object_ids=selected_object_ids,
        )

    def declare_victory(
            self,
            source_player=None,
            enabled_or_victory=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.DECLARE_VICTORY,
            source_player=source_player,
            enabled_or_victory=enabled_or_victory,
        )

    def kill_object(
            self,
            object_list_unit_id=None,
            source_player=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            object_group=None,
            object_type=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.KILL_OBJECT,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            object_group=object_group,
            object_type=object_type,
            selected_object_ids=selected_object_ids,
        )

    def remove_object(
            self,
            object_list_unit_id=None,
            source_player=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            object_group=None,
            object_type=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.REMOVE_OBJECT,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            object_group=object_group,
            object_type=object_type,
            selected_object_ids=selected_object_ids,
        )

    def change_view(
            self,
            source_player=None,
            location_x=None,
            location_y=None,
            location_object_reference=None,
            scroll=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CHANGE_VIEW,
            source_player=source_player,
            location_x=location_x,
            location_y=location_y,
            location_object_reference=location_object_reference,
            scroll=scroll,
        )

    def unload(
            self,
            object_list_unit_id=None,
            source_player=None,
            location_x=None,
            location_y=None,
            location_object_reference=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            object_group=None,
            object_type=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.UNLOAD,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            location_x=location_x,
            location_y=location_y,
            location_object_reference=location_object_reference,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            object_group=object_group,
            object_type=object_type,
            selected_object_ids=selected_object_ids,
        )

    def change_ownership(
            self,
            object_list_unit_id=None,
            source_player=None,
            target_player=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            object_group=None,
            object_type=None,
            flash_object=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CHANGE_OWNERSHIP,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            target_player=target_player,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            object_group=object_group,
            object_type=object_type,
            flash_object=flash_object,
            selected_object_ids=selected_object_ids,
        )

    def patrol(
            self,
            object_list_unit_id=None,
            source_player=None,
            location_x=None,
            location_y=None,
            location_object_reference=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            object_group=None,
            object_type=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.PATROL,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            location_x=location_x,
            location_y=location_y,
            location_object_reference=location_object_reference,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            object_group=object_group,
            object_type=object_type,
            selected_object_ids=selected_object_ids,
        )

    def display_instructions(
            self,
            object_list_unit_id=None,
            source_player=None,
            string_id=None,
            display_time=None,
            instruction_panel_position=None,
            play_sound=None,
            message=None,
            sound_name=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.DISPLAY_INSTRUCTIONS,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            string_id=string_id,
            display_time=display_time,
            instruction_panel_position=instruction_panel_position,
            play_sound=play_sound,
            message=message,
            sound_name=sound_name,
        )

    def clear_instructions(
            self,
            instruction_panel_position=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CLEAR_INSTRUCTIONS,
            instruction_panel_position=instruction_panel_position,
        )

    def freeze_object(
            self,
            object_list_unit_id=None,
            source_player=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            object_group=None,
            object_type=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.FREEZE_OBJECT,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            object_group=object_group,
            object_type=object_type,
            selected_object_ids=selected_object_ids,
        )

    def use_advanced_buttons(
            self,
    ):
        self.trigger_ref._add_effect(
            EffectId.USE_ADVANCED_BUTTONS,
        )

    def damage_object(
            self,
            quantity=None,
            object_list_unit_id=None,
            source_player=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            object_group=None,
            object_type=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.DAMAGE_OBJECT,
            quantity=quantity,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            object_group=object_group,
            object_type=object_type,
            selected_object_ids=selected_object_ids,
        )

    def place_foundation(
            self,
            object_list_unit_id=None,
            source_player=None,
            location_x=None,
            location_y=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.PLACE_FOUNDATION,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            location_x=location_x,
            location_y=location_y,
        )

    def change_object_name(
            self,
            object_list_unit_id=None,
            source_player=None,
            string_id=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            message=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_NAME,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            string_id=string_id,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            message=message,
            selected_object_ids=selected_object_ids,
        )

    def change_object_hp(
            self,
            quantity=None,
            object_list_unit_id=None,
            source_player=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            object_group=None,
            object_type=None,
            operation=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_HP,
            quantity=quantity,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            object_group=object_group,
            object_type=object_type,
            operation=operation,
            selected_object_ids=selected_object_ids,
        )

    def change_object_attack(
            self,
            armour_attack_quantity=None,
            armour_attack_class=None,
            object_list_unit_id=None,
            source_player=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            object_group=None,
            object_type=None,
            operation=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_ATTACK,
            armour_attack_quantity=armour_attack_quantity,
            armour_attack_class=armour_attack_class,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            object_group=object_group,
            object_type=object_type,
            operation=operation,
            selected_object_ids=selected_object_ids,
        )

    def stop_object(
            self,
            object_list_unit_id=None,
            source_player=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            object_group=None,
            object_type=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.STOP_OBJECT,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            object_group=object_group,
            object_type=object_type,
            selected_object_ids=selected_object_ids,
        )

    def attack_move(
            self,
            object_list_unit_id=None,
            source_player=None,
            location_x=None,
            location_y=None,
            location_object_reference=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            object_group=None,
            object_type=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.ATTACK_MOVE,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            location_x=location_x,
            location_y=location_y,
            location_object_reference=location_object_reference,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            object_group=object_group,
            object_type=object_type,
            selected_object_ids=selected_object_ids,
        )

    def change_object_armor(
            self,
            armour_attack_quantity=None,
            armour_attack_class=None,
            object_list_unit_id=None,
            source_player=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            object_group=None,
            object_type=None,
            operation=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_ARMOR,
            armour_attack_quantity=armour_attack_quantity,
            armour_attack_class=armour_attack_class,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            object_group=object_group,
            object_type=object_type,
            operation=operation,
            selected_object_ids=selected_object_ids,
        )

    def change_object_range(
            self,
            quantity=None,
            object_list_unit_id=None,
            source_player=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            object_group=None,
            object_type=None,
            operation=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_RANGE,
            quantity=quantity,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            object_group=object_group,
            object_type=object_type,
            operation=operation,
            selected_object_ids=selected_object_ids,
        )

    def change_object_speed(
            self,
            quantity=None,
            object_list_unit_id=None,
            source_player=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            object_group=None,
            object_type=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_SPEED,
            quantity=quantity,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            object_group=object_group,
            object_type=object_type,
            selected_object_ids=selected_object_ids,
        )

    def heal_object(
            self,
            quantity=None,
            object_list_unit_id=None,
            source_player=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            object_group=None,
            object_type=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.HEAL_OBJECT,
            quantity=quantity,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            object_group=object_group,
            object_type=object_type,
            selected_object_ids=selected_object_ids,
        )

    def teleport_object(
            self,
            object_list_unit_id=None,
            source_player=None,
            location_x=None,
            location_y=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            object_group=None,
            object_type=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.TELEPORT_OBJECT,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            location_x=location_x,
            location_y=location_y,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            object_group=object_group,
            object_type=object_type,
            selected_object_ids=selected_object_ids,
        )

    def change_object_stance(
            self,
            object_list_unit_id=None,
            source_player=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            object_group=None,
            object_type=None,
            attack_stance=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_STANCE,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            object_group=object_group,
            object_type=object_type,
            attack_stance=attack_stance,
            selected_object_ids=selected_object_ids,
        )

    def display_timer(
            self,
            string_id=None,
            display_time=None,
            time_unit=None,
            timer=None,
            message=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.DISPLAY_TIMER,
            string_id=string_id,
            display_time=display_time,
            time_unit=time_unit,
            timer=timer,
            message=message,
        )

    def enable_disable_object(
            self,
            object_list_unit_id=None,
            source_player=None,
            enabled_or_victory=None,
            item_id=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.ENABLE_DISABLE_OBJECT,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            enabled_or_victory=enabled_or_victory,
            item_id=item_id,
        )

    def enable_disable_technology(
            self,
            source_player=None,
            technology=None,
            enabled_or_victory=None,
            item_id=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.ENABLE_DISABLE_TECHNOLOGY,
            source_player=source_player,
            technology=technology,
            enabled_or_victory=enabled_or_victory,
            item_id=item_id,
        )

    def change_object_cost(
            self,
            object_list_unit_id=None,
            source_player=None,
            food=None,
            wood=None,
            stone=None,
            gold=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_COST,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            food=food,
            wood=wood,
            stone=stone,
            gold=gold,
        )

    def set_player_visibility(
            self,
            source_player=None,
            target_player=None,
            visibility_state=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.SET_PLAYER_VISIBILITY,
            source_player=source_player,
            target_player=target_player,
            visibility_state=visibility_state,
        )

    def change_object_icon(
            self,
            object_list_unit_id=None,
            source_player=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            object_group=None,
            object_type=None,
            object_list_unit_id_2=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_ICON,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            object_group=object_group,
            object_type=object_type,
            object_list_unit_id_2=object_list_unit_id_2,
            selected_object_ids=selected_object_ids,
        )

    def replace_object(
            self,
            object_list_unit_id=None,
            source_player=None,
            target_player=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            object_group=None,
            object_type=None,
            object_list_unit_id_2=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.REPLACE_OBJECT,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            target_player=target_player,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            object_group=object_group,
            object_type=object_type,
            object_list_unit_id_2=object_list_unit_id_2,
            selected_object_ids=selected_object_ids,
        )

    def change_object_description(
            self,
            object_list_unit_id=None,
            source_player=None,
            string_id=None,
            message=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_DESCRIPTION,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            string_id=string_id,
            message=message,
        )

    def change_player_name(
            self,
            source_player=None,
            string_id=None,
            message=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CHANGE_PLAYER_NAME,
            source_player=source_player,
            string_id=string_id,
            message=message,
        )

    def change_train_location(
            self,
            object_list_unit_id=None,
            source_player=None,
            object_list_unit_id_2=None,
            button_location=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CHANGE_TRAIN_LOCATION,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            object_list_unit_id_2=object_list_unit_id_2,
            button_location=button_location,
        )

    def change_research_location(
            self,
            source_player=None,
            technology=None,
            object_list_unit_id_2=None,
            button_location=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CHANGE_RESEARCH_LOCATION,
            source_player=source_player,
            technology=technology,
            object_list_unit_id_2=object_list_unit_id_2,
            button_location=button_location,
        )

    def change_civilization_name(
            self,
            source_player=None,
            string_id=None,
            message=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CHANGE_CIVILIZATION_NAME,
            source_player=source_player,
            string_id=string_id,
            message=message,
        )

    def create_garrisoned_object(
            self,
            object_list_unit_id=None,
            source_player=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            object_list_unit_id_2=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CREATE_GARRISONED_OBJECT,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            object_list_unit_id_2=object_list_unit_id_2,
            selected_object_ids=selected_object_ids,
        )

    def acknowledge_ai_signal(
            self,
            ai_signal_value=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.ACKNOWLEDGE_AI_SIGNAL,
            ai_signal_value=ai_signal_value,
        )

    def modify_attribute(
            self,
            quantity=None,
            object_list_unit_id=None,
            source_player=None,
            item_id=None,
            operation=None,
            object_attributes=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.MODIFY_ATTRIBUTE,
            quantity=quantity,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            item_id=item_id,
            operation=operation,
            object_attributes=object_attributes,
        )

    def modify_resource(
            self,
            quantity=None,
            tribute_list=None,
            source_player=None,
            item_id=None,
            operation=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.MODIFY_RESOURCE,
            quantity=quantity,
            tribute_list=tribute_list,
            source_player=source_player,
            item_id=item_id,
            operation=operation,
        )

    def modify_resource_by_variable(
            self,
            tribute_list=None,
            source_player=None,
            item_id=None,
            operation=None,
            variable=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.MODIFY_RESOURCE_BY_VARIABLE,
            tribute_list=tribute_list,
            source_player=source_player,
            item_id=item_id,
            operation=operation,
            variable=variable,
        )

    def set_building_gather_point(
            self,
            object_list_unit_id=None,
            source_player=None,
            location_x=None,
            location_y=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.SET_BUILDING_GATHER_POINT,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            location_x=location_x,
            location_y=location_y,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            selected_object_ids=selected_object_ids,
        )

    def script_call(
            self,
            string_id=None,
            message=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.SCRIPT_CALL,
            string_id=string_id,
            message=message,
        )

    def change_variable(
            self,
            quantity=None,
            operation=None,
            variable=None,
            message=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CHANGE_VARIABLE,
            quantity=quantity,
            operation=operation,
            variable=variable,
            message=message,
        )

    def clear_timer(
            self,
            timer=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CLEAR_TIMER,
            timer=timer,
        )

    def change_object_player_color(
            self,
            object_list_unit_id=None,
            source_player=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_PLAYER_COLOR,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            selected_object_ids=selected_object_ids,
        )

    def change_object_civilization_name(
            self,
            string_id=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_CIVILIZATION_NAME,
            string_id=string_id,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            selected_object_ids=selected_object_ids,
        )

    def change_object_player_name(
            self,
            object_list_unit_id=None,
            source_player=None,
            string_id=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_PLAYER_NAME,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            string_id=string_id,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            selected_object_ids=selected_object_ids,
        )

    def disable_unit_targeting(
            self,
            object_list_unit_id=None,
            source_player=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.DISABLE_UNIT_TARGETING,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            selected_object_ids=selected_object_ids,
        )

    def enable_unit_targeting(
            self,
            object_list_unit_id=None,
            source_player=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.ENABLE_UNIT_TARGETING,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            selected_object_ids=selected_object_ids,
        )

    def change_technology_cost(
            self,
            source_player=None,
            technology=None,
            food=None,
            wood=None,
            stone=None,
            gold=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CHANGE_TECHNOLOGY_COST,
            source_player=source_player,
            technology=technology,
            food=food,
            wood=wood,
            stone=stone,
            gold=gold,
        )

    def change_technology_research_time(
            self,
            quantity=None,
            source_player=None,
            technology=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CHANGE_TECHNOLOGY_RESEARCH_TIME,
            quantity=quantity,
            source_player=source_player,
            technology=technology,
        )

    def change_technology_name(
            self,
            source_player=None,
            technology=None,
            string_id=None,
            message=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CHANGE_TECHNOLOGY_NAME,
            source_player=source_player,
            technology=technology,
            string_id=string_id,
            message=message,
        )

    def change_technology_description(
            self,
            source_player=None,
            technology=None,
            string_id=None,
            message=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.CHANGE_TECHNOLOGY_DESCRIPTION,
            source_player=source_player,
            technology=technology,
            string_id=string_id,
            message=message,
        )

    def enable_technology_stacking(
            self,
            source_player=None,
            technology=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.ENABLE_TECHNOLOGY_STACKING,
            source_player=source_player,
            technology=technology,
        )

    def disable_technology_stacking(
            self,
            source_player=None,
            technology=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.DISABLE_TECHNOLOGY_STACKING,
            source_player=source_player,
            technology=technology,
        )

    def acknowledge_multiplayer_ai_signal(
            self,
            ai_signal_value=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.ACKNOWLEDGE_MULTIPLAYER_AI_SIGNAL,
            ai_signal_value=ai_signal_value,
        )

    def disable_object_selection(
            self,
            object_list_unit_id=None,
            source_player=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.DISABLE_OBJECT_SELECTION,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            selected_object_ids=selected_object_ids,
        )

    def enable_object_selection(
            self,
            object_list_unit_id=None,
            source_player=None,
            area_1_x=None,
            area_1_y=None,
            area_2_x=None,
            area_2_y=None,
            selected_object_ids=None,
    ):
        self.trigger_ref._add_effect(
            EffectId.ENABLE_OBJECT_SELECTION,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_1_x=area_1_x,
            area_1_y=area_1_y,
            area_2_x=area_2_x,
            area_2_y=area_2_y,
            selected_object_ids=selected_object_ids,
        )
