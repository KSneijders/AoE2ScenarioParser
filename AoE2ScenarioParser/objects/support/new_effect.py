# This file was generated based on: versions/DE/v1.41/effects.json
from typing import Union

from AoE2ScenarioParser.datasets.effects import EffectId
from AoE2ScenarioParser.objects.data_objects.effect import Effect


class NewEffectSupport:
    def __init__(self, trigger_ref):
        self.trigger_ref = trigger_ref

    def none(
            self,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.NONE,
        )

    def change_diplomacy(
            self,
            diplomacy: Union[int, None] = None,
            source_player: Union[int, None] = None,
            target_player: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.CHANGE_DIPLOMACY,
            diplomacy=diplomacy,
            source_player=source_player,
            target_player=target_player,
        )

    def research_technology(
            self,
            source_player: Union[int, None] = None,
            technology: Union[int, None] = None,
            force_research_technology: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.RESEARCH_TECHNOLOGY,
            source_player=source_player,
            technology=technology,
            force_research_technology=force_research_technology,
        )

    def send_chat(
            self,
            source_player: Union[int, None] = None,
            string_id: Union[int, None] = None,
            message: Union[str, None] = None,
            sound_name: Union[str, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.SEND_CHAT,
            source_player=source_player,
            string_id=string_id,
            message=message,
            sound_name=sound_name,
        )

    def play_sound(
            self,
            source_player: Union[int, None] = None,
            location_x: Union[int, None] = None,
            location_y: Union[int, None] = None,
            location_object_reference: Union[int, None] = None,
            sound_name: Union[str, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.PLAY_SOUND,
            source_player=source_player,
            location_x=location_x,
            location_y=location_y,
            location_object_reference=location_object_reference,
            sound_name=sound_name,
        )

    def tribute(
            self,
            quantity: Union[int, None] = None,
            tribute_list: Union[int, None] = None,
            source_player: Union[int, None] = None,
            target_player: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.TRIBUTE,
            quantity=quantity,
            tribute_list=tribute_list,
            source_player=source_player,
            target_player=target_player,
        )

    def unlock_gate(
            self,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.UNLOCK_GATE,
            selected_object_ids=selected_object_ids,
        )

    def lock_gate(
            self,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.LOCK_GATE,
            selected_object_ids=selected_object_ids,
        )

    def activate_trigger(
            self,
            trigger_id: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.ACTIVATE_TRIGGER,
            trigger_id=trigger_id,
        )

    def deactivate_trigger(
            self,
            trigger_id: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.DEACTIVATE_TRIGGER,
            trigger_id=trigger_id,
        )

    def ai_script_goal(
            self,
            ai_script_goal: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.AI_SCRIPT_GOAL,
            ai_script_goal=ai_script_goal,
        )

    def create_object(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            location_x: Union[int, None] = None,
            location_y: Union[int, None] = None,
            facet: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.CREATE_OBJECT,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            location_x=location_x,
            location_y=location_y,
            facet=facet,
        )

    def task_object(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            location_x: Union[int, None] = None,
            location_y: Union[int, None] = None,
            location_object_reference: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            object_group: Union[int, None] = None,
            object_type: Union[int, None] = None,
            action_type: Union[int, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.TASK_OBJECT,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            location_x=location_x,
            location_y=location_y,
            location_object_reference=location_object_reference,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            object_group=object_group,
            object_type=object_type,
            action_type=action_type,
            selected_object_ids=selected_object_ids,
        )

    def declare_victory(
            self,
            source_player: Union[int, None] = None,
            enabled: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.DECLARE_VICTORY,
            source_player=source_player,
            enabled=enabled,
        )

    def kill_object(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            object_group: Union[int, None] = None,
            object_type: Union[int, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.KILL_OBJECT,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            object_group=object_group,
            object_type=object_type,
            selected_object_ids=selected_object_ids,
        )

    def remove_object(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            object_group: Union[int, None] = None,
            object_type: Union[int, None] = None,
            object_state: Union[int, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.REMOVE_OBJECT,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            object_group=object_group,
            object_type=object_type,
            object_state=object_state,
            selected_object_ids=selected_object_ids,
        )

    def change_view(
            self,
            source_player: Union[int, None] = None,
            location_x: Union[int, None] = None,
            location_y: Union[int, None] = None,
            scroll: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.CHANGE_VIEW,
            source_player=source_player,
            location_x=location_x,
            location_y=location_y,
            scroll=scroll,
        )

    def unload(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            location_x: Union[int, None] = None,
            location_y: Union[int, None] = None,
            location_object_reference: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            object_group: Union[int, None] = None,
            object_type: Union[int, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.UNLOAD,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            location_x=location_x,
            location_y=location_y,
            location_object_reference=location_object_reference,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            object_group=object_group,
            object_type=object_type,
            selected_object_ids=selected_object_ids,
        )

    def change_ownership(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            target_player: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            object_group: Union[int, None] = None,
            object_type: Union[int, None] = None,
            flash_object: Union[int, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.CHANGE_OWNERSHIP,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            target_player=target_player,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            object_group=object_group,
            object_type=object_type,
            flash_object=flash_object,
            selected_object_ids=selected_object_ids,
        )

    def patrol(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            location_x: Union[int, None] = None,
            location_y: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            object_group: Union[int, None] = None,
            object_type: Union[int, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.PATROL,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            location_x=location_x,
            location_y=location_y,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            object_group=object_group,
            object_type=object_type,
            selected_object_ids=selected_object_ids,
        )

    def display_instructions(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            string_id: Union[int, None] = None,
            display_time: Union[int, None] = None,
            instruction_panel_position: Union[int, None] = None,
            play_sound: Union[int, None] = None,
            message: Union[str, None] = None,
            sound_name: Union[str, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
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
            instruction_panel_position: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.CLEAR_INSTRUCTIONS,
            instruction_panel_position=instruction_panel_position,
        )

    def freeze_object(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            object_group: Union[int, None] = None,
            object_type: Union[int, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.FREEZE_OBJECT,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            object_group=object_group,
            object_type=object_type,
            selected_object_ids=selected_object_ids,
        )

    def use_advanced_buttons(
            self,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.USE_ADVANCED_BUTTONS,
        )

    def damage_object(
            self,
            quantity: Union[int, None] = None,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            object_group: Union[int, None] = None,
            object_type: Union[int, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.DAMAGE_OBJECT,
            quantity=quantity,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            object_group=object_group,
            object_type=object_type,
            selected_object_ids=selected_object_ids,
        )

    def place_foundation(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            location_x: Union[int, None] = None,
            location_y: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.PLACE_FOUNDATION,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            location_x=location_x,
            location_y=location_y,
        )

    def change_object_name(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            string_id: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            message: Union[str, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_NAME,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            string_id=string_id,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            message=message,
            selected_object_ids=selected_object_ids,
        )

    def change_object_hp(
            self,
            quantity: Union[int, None] = None,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            object_group: Union[int, None] = None,
            object_type: Union[int, None] = None,
            operation: Union[int, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_HP,
            quantity=quantity,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            object_group=object_group,
            object_type=object_type,
            operation=operation,
            selected_object_ids=selected_object_ids,
        )

    def change_object_attack(
            self,
            armour_attack_quantity: Union[int, None] = None,
            armour_attack_class: Union[int, None] = None,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            object_group: Union[int, None] = None,
            object_type: Union[int, None] = None,
            operation: Union[int, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_ATTACK,
            armour_attack_quantity=armour_attack_quantity,
            armour_attack_class=armour_attack_class,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            object_group=object_group,
            object_type=object_type,
            operation=operation,
            selected_object_ids=selected_object_ids,
        )

    def stop_object(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            object_group: Union[int, None] = None,
            object_type: Union[int, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.STOP_OBJECT,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            object_group=object_group,
            object_type=object_type,
            selected_object_ids=selected_object_ids,
        )

    def attack_move(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            location_x: Union[int, None] = None,
            location_y: Union[int, None] = None,
            location_object_reference: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            object_group: Union[int, None] = None,
            object_type: Union[int, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.ATTACK_MOVE,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            location_x=location_x,
            location_y=location_y,
            location_object_reference=location_object_reference,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            object_group=object_group,
            object_type=object_type,
            selected_object_ids=selected_object_ids,
        )

    def change_object_armor(
            self,
            armour_attack_quantity: Union[int, None] = None,
            armour_attack_class: Union[int, None] = None,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            object_group: Union[int, None] = None,
            object_type: Union[int, None] = None,
            operation: Union[int, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_ARMOR,
            armour_attack_quantity=armour_attack_quantity,
            armour_attack_class=armour_attack_class,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            object_group=object_group,
            object_type=object_type,
            operation=operation,
            selected_object_ids=selected_object_ids,
        )

    def change_object_range(
            self,
            quantity: Union[int, None] = None,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            object_group: Union[int, None] = None,
            object_type: Union[int, None] = None,
            operation: Union[int, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_RANGE,
            quantity=quantity,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            object_group=object_group,
            object_type=object_type,
            operation=operation,
            selected_object_ids=selected_object_ids,
        )

    def change_object_speed(
            self,
            quantity: Union[int, None] = None,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            object_group: Union[int, None] = None,
            object_type: Union[int, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_SPEED,
            quantity=quantity,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            object_group=object_group,
            object_type=object_type,
            selected_object_ids=selected_object_ids,
        )

    def heal_object(
            self,
            quantity: Union[int, None] = None,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            object_group: Union[int, None] = None,
            object_type: Union[int, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.HEAL_OBJECT,
            quantity=quantity,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            object_group=object_group,
            object_type=object_type,
            selected_object_ids=selected_object_ids,
        )

    def teleport_object(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            location_x: Union[int, None] = None,
            location_y: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            object_group: Union[int, None] = None,
            object_type: Union[int, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.TELEPORT_OBJECT,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            location_x=location_x,
            location_y=location_y,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            object_group=object_group,
            object_type=object_type,
            selected_object_ids=selected_object_ids,
        )

    def change_object_stance(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            object_group: Union[int, None] = None,
            object_type: Union[int, None] = None,
            attack_stance: Union[int, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_STANCE,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            object_group=object_group,
            object_type=object_type,
            attack_stance=attack_stance,
            selected_object_ids=selected_object_ids,
        )

    def display_timer(
            self,
            string_id: Union[int, None] = None,
            display_time: Union[int, None] = None,
            time_unit: Union[int, None] = None,
            timer: Union[int, None] = None,
            reset_timer: Union[int, None] = None,
            message: Union[str, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.DISPLAY_TIMER,
            string_id=string_id,
            display_time=display_time,
            time_unit=time_unit,
            timer=timer,
            reset_timer=reset_timer,
            message=message,
        )

    def enable_disable_object(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            enabled: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.ENABLE_DISABLE_OBJECT,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            enabled=enabled,
        )

    def enable_disable_technology(
            self,
            source_player: Union[int, None] = None,
            technology: Union[int, None] = None,
            enabled: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.ENABLE_DISABLE_TECHNOLOGY,
            source_player=source_player,
            technology=technology,
            enabled=enabled,
        )

    def change_object_cost(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            food: Union[int, None] = None,
            wood: Union[int, None] = None,
            stone: Union[int, None] = None,
            gold: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
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
            source_player: Union[int, None] = None,
            target_player: Union[int, None] = None,
            visibility_state: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.SET_PLAYER_VISIBILITY,
            source_player=source_player,
            target_player=target_player,
            visibility_state=visibility_state,
        )

    def change_object_icon(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            object_group: Union[int, None] = None,
            object_type: Union[int, None] = None,
            object_list_unit_id_2: Union[int, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_ICON,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            object_group=object_group,
            object_type=object_type,
            object_list_unit_id_2=object_list_unit_id_2,
            selected_object_ids=selected_object_ids,
        )

    def replace_object(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            target_player: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            object_group: Union[int, None] = None,
            object_type: Union[int, None] = None,
            object_list_unit_id_2: Union[int, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.REPLACE_OBJECT,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            target_player=target_player,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            object_group=object_group,
            object_type=object_type,
            object_list_unit_id_2=object_list_unit_id_2,
            selected_object_ids=selected_object_ids,
        )

    def change_object_description(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            string_id: Union[int, None] = None,
            message: Union[str, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_DESCRIPTION,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            string_id=string_id,
            message=message,
        )

    def change_player_name(
            self,
            source_player: Union[int, None] = None,
            string_id: Union[int, None] = None,
            message: Union[str, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.CHANGE_PLAYER_NAME,
            source_player=source_player,
            string_id=string_id,
            message=message,
        )

    def change_train_location(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            object_list_unit_id_2: Union[int, None] = None,
            button_location: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.CHANGE_TRAIN_LOCATION,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            object_list_unit_id_2=object_list_unit_id_2,
            button_location=button_location,
        )

    def change_research_location(
            self,
            source_player: Union[int, None] = None,
            technology: Union[int, None] = None,
            object_list_unit_id_2: Union[int, None] = None,
            button_location: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.CHANGE_RESEARCH_LOCATION,
            source_player=source_player,
            technology=technology,
            object_list_unit_id_2=object_list_unit_id_2,
            button_location=button_location,
        )

    def change_civilization_name(
            self,
            source_player: Union[int, None] = None,
            string_id: Union[int, None] = None,
            message: Union[str, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.CHANGE_CIVILIZATION_NAME,
            source_player=source_player,
            string_id=string_id,
            message=message,
        )

    def create_garrisoned_object(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            object_list_unit_id_2: Union[int, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.CREATE_GARRISONED_OBJECT,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            object_list_unit_id_2=object_list_unit_id_2,
            selected_object_ids=selected_object_ids,
        )

    def acknowledge_ai_signal(
            self,
            ai_signal_value: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.ACKNOWLEDGE_AI_SIGNAL,
            ai_signal_value=ai_signal_value,
        )

    def modify_attribute(
            self,
            quantity: Union[int, None] = None,
            armour_attack_quantity: Union[int, None] = None,
            armour_attack_class: Union[int, None] = None,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            operation: Union[int, None] = None,
            object_attributes: Union[int, None] = None,
    ) -> Effect:
        """
        The parameters 'armour_attack_quantity' and 'armour_attack_class' are only used when object_attributes is Armor
        or Attack (8 or 9). Use, 'quantity' otherwise.
        """
        if (armour_attack_quantity is not None or armour_attack_class is not None) and quantity is not None:
            raise ValueError("Cannot use 'armour_attack' attributes together with the 'quantity' attribute.")

        return self.trigger_ref._add_effect(
            EffectId.MODIFY_ATTRIBUTE,
            quantity=quantity,
            armour_attack_quantity=armour_attack_quantity,
            armour_attack_class=armour_attack_class,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            operation=operation,
            object_attributes=object_attributes,
        )

    def modify_resource(
            self,
            quantity: Union[int, None] = None,
            tribute_list: Union[int, None] = None,
            source_player: Union[int, None] = None,
            operation: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.MODIFY_RESOURCE,
            quantity=quantity,
            tribute_list=tribute_list,
            source_player=source_player,
            operation=operation,
        )

    def modify_resource_by_variable(
            self,
            tribute_list: Union[int, None] = None,
            source_player: Union[int, None] = None,
            operation: Union[int, None] = None,
            variable: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.MODIFY_RESOURCE_BY_VARIABLE,
            tribute_list=tribute_list,
            source_player=source_player,
            operation=operation,
            variable=variable,
        )

    def set_building_gather_point(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            location_x: Union[int, None] = None,
            location_y: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.SET_BUILDING_GATHER_POINT,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            location_x=location_x,
            location_y=location_y,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            selected_object_ids=selected_object_ids,
        )

    def script_call(
            self,
            string_id: Union[int, None] = None,
            message: Union[str, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.SCRIPT_CALL,
            string_id=string_id,
            message=message,
        )

    def change_variable(
            self,
            quantity: Union[int, None] = None,
            operation: Union[int, None] = None,
            variable: Union[int, None] = None,
            message: Union[str, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.CHANGE_VARIABLE,
            quantity=quantity,
            operation=operation,
            variable=variable,
            message=message,
        )

    def clear_timer(
            self,
            timer: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.CLEAR_TIMER,
            timer=timer,
        )

    def change_object_player_color(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            player_color: Union[int, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_PLAYER_COLOR,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            player_color=player_color,
            selected_object_ids=selected_object_ids,
        )

    def change_object_civilization_name(
            self,
            string_id: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            message: Union[str, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_CIVILIZATION_NAME,
            string_id=string_id,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            message=message,
            selected_object_ids=selected_object_ids,
        )

    def change_object_player_name(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            string_id: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            message: Union[str, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_PLAYER_NAME,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            string_id=string_id,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            message=message,
            selected_object_ids=selected_object_ids,
        )

    def disable_unit_targeting(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.DISABLE_UNIT_TARGETING,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            selected_object_ids=selected_object_ids,
        )

    def enable_unit_targeting(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.ENABLE_UNIT_TARGETING,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            selected_object_ids=selected_object_ids,
        )

    def change_technology_cost(
            self,
            source_player: Union[int, None] = None,
            technology: Union[int, None] = None,
            food: Union[int, None] = None,
            wood: Union[int, None] = None,
            stone: Union[int, None] = None,
            gold: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
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
            quantity: Union[int, None] = None,
            source_player: Union[int, None] = None,
            technology: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.CHANGE_TECHNOLOGY_RESEARCH_TIME,
            quantity=quantity,
            source_player=source_player,
            technology=technology,
        )

    def change_technology_name(
            self,
            source_player: Union[int, None] = None,
            technology: Union[int, None] = None,
            string_id: Union[int, None] = None,
            message: Union[str, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.CHANGE_TECHNOLOGY_NAME,
            source_player=source_player,
            technology=technology,
            string_id=string_id,
            message=message,
        )

    def change_technology_description(
            self,
            source_player: Union[int, None] = None,
            technology: Union[int, None] = None,
            string_id: Union[int, None] = None,
            message: Union[str, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.CHANGE_TECHNOLOGY_DESCRIPTION,
            source_player=source_player,
            technology=technology,
            string_id=string_id,
            message=message,
        )

    def enable_technology_stacking(
            self,
            source_player: Union[int, None] = None,
            technology: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.ENABLE_TECHNOLOGY_STACKING,
            source_player=source_player,
            technology=technology,
        )

    def disable_technology_stacking(
            self,
            source_player: Union[int, None] = None,
            technology: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.DISABLE_TECHNOLOGY_STACKING,
            source_player=source_player,
            technology=technology,
        )

    def acknowledge_multiplayer_ai_signal(
            self,
            ai_signal_value: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.ACKNOWLEDGE_MULTIPLAYER_AI_SIGNAL,
            ai_signal_value=ai_signal_value,
        )

    def disable_object_selection(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.DISABLE_OBJECT_SELECTION,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            selected_object_ids=selected_object_ids,
        )

    def enable_object_selection(
            self,
            object_list_unit_id: Union[int, None] = None,
            source_player: Union[int, None] = None,
            area_x1: Union[int, None] = None,
            area_y1: Union[int, None] = None,
            area_x2: Union[int, None] = None,
            area_y2: Union[int, None] = None,
            selected_object_ids: Union[int, None] = None,
    ) -> Effect:
        return self.trigger_ref._add_effect(
            EffectId.ENABLE_OBJECT_SELECTION,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            selected_object_ids=selected_object_ids,
        )

    def change_color_mood(
            self,
            quantity: Union[int, None] = None,
            color_mood: Union[int, None] = None):
        return self.trigger_ref._add_effect(
            EffectId.CHANGE_COLOR_MOOD,
            quantity=quantity,
            color_mood=color_mood
        )
