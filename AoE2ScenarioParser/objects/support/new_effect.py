from __future__ import annotations

from typing import List

from typing_extensions import deprecated

from AoE2ScenarioParser.datasets.effects import EffectId
from AoE2ScenarioParser.datasets.trigger_lists import ObjectAttribute
from AoE2ScenarioParser.objects.data_objects.effect import Effect


class NewEffectSupport:
    def __init__(self, trigger_ref):
        self._trigger_ref = trigger_ref

    def none(
            self,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.NONE,
        )

    def change_diplomacy(
            self,
            diplomacy: int | None = None,
            source_player: int | None = None,
            target_player: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.CHANGE_DIPLOMACY,
            diplomacy=diplomacy,
            source_player=source_player,
            target_player=target_player,
        )

    def research_technology(
            self,
            source_player: int | None = None,
            technology: int | None = None,
            force_research_technology: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.RESEARCH_TECHNOLOGY,
            source_player=source_player,
            technology=technology,
            force_research_technology=force_research_technology,
        )

    def send_chat(
            self,
            source_player: int | None = None,
            string_id: int | None = None,
            message: str | None = None,
            sound_name: str | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.SEND_CHAT,
            source_player=source_player,
            string_id=string_id,
            message=message,
            sound_name=sound_name,
        )

    def play_sound(
            self,
            source_player: int | None = None,
            location_x: int | None = None,
            location_y: int | None = None,
            location_object_reference: int | None = None,
            sound_name: str | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.PLAY_SOUND,
            source_player=source_player,
            location_x=location_x,
            location_y=location_y,
            location_object_reference=location_object_reference,
            sound_name=sound_name,
        )

    def tribute(
            self,
            quantity: int | None = None,
            tribute_list: int | None = None,
            source_player: int | None = None,
            target_player: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.TRIBUTE,
            quantity=quantity,
            tribute_list=tribute_list,
            source_player=source_player,
            target_player=target_player,
        )

    def unlock_gate(
            self,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.UNLOCK_GATE,
            selected_object_ids=selected_object_ids,
        )

    def lock_gate(
            self,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.LOCK_GATE,
            selected_object_ids=selected_object_ids,
        )

    def activate_trigger(
            self,
            trigger_id: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.ACTIVATE_TRIGGER,
            trigger_id=trigger_id,
        )

    def deactivate_trigger(
            self,
            trigger_id: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.DEACTIVATE_TRIGGER,
            trigger_id=trigger_id,
        )

    def ai_script_goal(
            self,
            ai_script_goal: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.AI_SCRIPT_GOAL,
            ai_script_goal=ai_script_goal,
        )

    def create_object(
            self,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            location_x: int | None = None,
            location_y: int | None = None,
            facet: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.CREATE_OBJECT,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            location_x=location_x,
            location_y=location_y,
            facet=facet,
        )

    def task_object(
            self,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            location_x: int | None = None,
            location_y: int | None = None,
            location_object_reference: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            object_group: int | None = None,
            object_type: int | None = None,
            action_type: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            source_player: int | None = None,
            enabled: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.DECLARE_VICTORY,
            source_player=source_player,
            enabled=enabled,
        )

    def kill_object(
            self,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            object_group: int | None = None,
            object_type: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            object_group: int | None = None,
            object_type: int | None = None,
            object_state: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            quantity: int | None = None,
            source_player: int | None = None,
            location_x: int | None = None,
            location_y: int | None = None,
            scroll: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.CHANGE_VIEW,
            quantity=quantity,
            source_player=source_player,
            location_x=location_x,
            location_y=location_y,
            scroll=scroll,
        )

    def unload(
            self,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            location_x: int | None = None,
            location_y: int | None = None,
            location_object_reference: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            object_group: int | None = None,
            object_type: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            target_player: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            object_group: int | None = None,
            object_type: int | None = None,
            flash_object: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            location_x: int | None = None,
            location_y: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            object_group: int | None = None,
            object_type: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            string_id: int | None = None,
            display_time: int | None = None,
            instruction_panel_position: int | None = None,
            play_sound: int | None = None,
            message: str | None = None,
            sound_name: str | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            instruction_panel_position: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.CLEAR_INSTRUCTIONS,
            instruction_panel_position=instruction_panel_position,
        )

    def freeze_object(
            self,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            object_group: int | None = None,
            object_type: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
        return self._trigger_ref._add_effect(
            EffectId.USE_ADVANCED_BUTTONS,
        )

    def damage_object(
            self,
            quantity: int | None = None,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            object_group: int | None = None,
            object_type: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            location_x: int | None = None,
            location_y: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.PLACE_FOUNDATION,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            location_x=location_x,
            location_y=location_y,
        )

    def change_object_name(
            self,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            string_id: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            message: str | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            quantity: int | None = None,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            object_group: int | None = None,
            object_type: int | None = None,
            operation: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            armour_attack_quantity: int | None = None,
            armour_attack_class: int | None = None,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            object_group: int | None = None,
            object_type: int | None = None,
            operation: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            object_group: int | None = None,
            object_type: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            location_x: int | None = None,
            location_y: int | None = None,
            location_object_reference: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            object_group: int | None = None,
            object_type: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            armour_attack_quantity: int | None = None,
            armour_attack_class: int | None = None,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            object_group: int | None = None,
            object_type: int | None = None,
            operation: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            quantity: int | None = None,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            object_group: int | None = None,
            object_type: int | None = None,
            operation: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            quantity: int | None = None,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            object_group: int | None = None,
            object_type: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            quantity: int | None = None,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            object_group: int | None = None,
            object_type: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            location_x: int | None = None,
            location_y: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            object_group: int | None = None,
            object_type: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            object_group: int | None = None,
            object_type: int | None = None,
            attack_stance: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            string_id: int | None = None,
            display_time: int | None = None,
            time_unit: int | None = None,
            timer: int | None = None,
            reset_timer: int | None = None,
            message: str | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            enabled: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.ENABLE_DISABLE_OBJECT,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            enabled=enabled,
        )

    def enable_disable_technology(
            self,
            source_player: int | None = None,
            technology: int | None = None,
            enabled: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.ENABLE_DISABLE_TECHNOLOGY,
            source_player=source_player,
            technology=technology,
            enabled=enabled,
        )

    def change_object_cost(
            self,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            resource_1: int | None = None,
            resource_1_quantity: int | None = None,
            resource_2: int | None = None,
            resource_2_quantity: int | None = None,
            resource_3: int | None = None,
            resource_3_quantity: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_COST,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            resource_1=resource_1,
            resource_1_quantity=resource_1_quantity,
            resource_2=resource_2,
            resource_2_quantity=resource_2_quantity,
            resource_3=resource_3,
            resource_3_quantity=resource_3_quantity,
        )

    def set_player_visibility(
            self,
            source_player: int | None = None,
            target_player: int | None = None,
            visibility_state: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.SET_PLAYER_VISIBILITY,
            source_player=source_player,
            target_player=target_player,
            visibility_state=visibility_state,
        )

    def change_object_icon(
            self,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            object_group: int | None = None,
            object_type: int | None = None,
            object_list_unit_id_2: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            target_player: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            object_group: int | None = None,
            object_type: int | None = None,
            object_list_unit_id_2: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            string_id: int | None = None,
            message: str | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_DESCRIPTION,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            string_id=string_id,
            message=message,
        )

    def change_player_name(
            self,
            source_player: int | None = None,
            string_id: int | None = None,
            message: str | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.CHANGE_PLAYER_NAME,
            source_player=source_player,
            string_id=string_id,
            message=message,
        )

    def change_train_location(
            self,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            object_list_unit_id_2: int | None = None,
            button_location: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.CHANGE_TRAIN_LOCATION,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            object_list_unit_id_2=object_list_unit_id_2,
            button_location=button_location,
        )

    @deprecated('Use `change_technology_location` instead')
    def change_research_location(
            self,
            source_player: int | None = None,
            technology: int | None = None,
            object_list_unit_id_2: int | None = None,
            button_location: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.CHANGE_TECHNOLOGY_LOCATION,
            source_player=source_player,
            technology=technology,
            object_list_unit_id_2=object_list_unit_id_2,
            button_location=button_location,
        )

    def change_technology_location(
            self,
            source_player: int | None = None,
            technology: int | None = None,
            object_list_unit_id_2: int | None = None,
            button_location: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.CHANGE_TECHNOLOGY_LOCATION,
            source_player=source_player,
            technology=technology,
            object_list_unit_id_2=object_list_unit_id_2,
            button_location=button_location,
        )

    def change_civilization_name(
            self,
            source_player: int | None = None,
            string_id: int | None = None,
            message: str | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.CHANGE_CIVILIZATION_NAME,
            source_player=source_player,
            string_id=string_id,
            message=message,
        )

    def create_garrisoned_object(
            self,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            object_list_unit_id_2: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            ai_signal_value: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.ACKNOWLEDGE_AI_SIGNAL,
            ai_signal_value=ai_signal_value,
        )

    def modify_attribute(
            self,
            quantity: int | None = None,
            armour_attack_quantity: int | None = None,
            armour_attack_class: int | None = None,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            operation: int | None = None,
            object_attributes: int | None = None,
            message: str | None = None,
    ) -> Effect:
        """
        The parameters 'armour_attack_quantity' and 'armour_attack_class' are only used when object_attributes is Armor
        or Attack (8 or 9). Use, 'quantity' otherwise.
        """
        if (armour_attack_quantity is not None or armour_attack_class is not None) and quantity is not None:
            raise ValueError("Cannot use 'armour_attack' attributes together with the 'quantity' attribute.")

        return self._trigger_ref._add_effect(
            EffectId.MODIFY_ATTRIBUTE,
            quantity=quantity,
            armour_attack_quantity=armour_attack_quantity,
            armour_attack_class=armour_attack_class,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            operation=operation,
            object_attributes=object_attributes,
            message=message
        )

    def modify_resource(
            self,
            quantity: int | None = None,
            tribute_list: int | None = None,
            source_player: int | None = None,
            operation: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.MODIFY_RESOURCE,
            quantity=quantity,
            tribute_list=tribute_list,
            source_player=source_player,
            operation=operation,
        )

    def modify_resource_by_variable(
            self,
            tribute_list: int | None = None,
            source_player: int | None = None,
            operation: int | None = None,
            variable: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.MODIFY_RESOURCE_BY_VARIABLE,
            tribute_list=tribute_list,
            source_player=source_player,
            operation=operation,
            variable=variable,
        )

    def set_building_gather_point(
            self,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            location_x: int | None = None,
            location_y: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            string_id: int | None = None,
            message: str | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.SCRIPT_CALL,
            string_id=string_id,
            message=message,
        )

    def change_variable(
            self,
            quantity: int | None = None,
            operation: int | None = None,
            variable: int | None = None,
            message: str | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.CHANGE_VARIABLE,
            quantity=quantity,
            operation=operation,
            variable=variable,
            message=message,
        )

    def clear_timer(
            self,
            timer: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.CLEAR_TIMER,
            timer=timer,
        )

    def change_object_player_color(
            self,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            player_color: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            source_player: int | None = None,
            string_id: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            message: str | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_CIVILIZATION_NAME,
            source_player=source_player,
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
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            string_id: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            message: str | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            source_player: int | None = None,
            technology: int | None = None,
            resource_1: int | None = None,
            resource_1_quantity: int | None = None,
            resource_2: int | None = None,
            resource_2_quantity: int | None = None,
            resource_3: int | None = None,
            resource_3_quantity: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.CHANGE_TECHNOLOGY_COST,
            source_player=source_player,
            technology=technology,
            resource_1=resource_1,
            resource_1_quantity=resource_1_quantity,
            resource_2=resource_2,
            resource_2_quantity=resource_2_quantity,
            resource_3=resource_3,
            resource_3_quantity=resource_3_quantity,
        )

    def change_technology_research_time(
            self,
            quantity: int | None = None,
            source_player: int | None = None,
            technology: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.CHANGE_TECHNOLOGY_RESEARCH_TIME,
            quantity=quantity,
            source_player=source_player,
            technology=technology,
        )

    def change_technology_name(
            self,
            source_player: int | None = None,
            technology: int | None = None,
            string_id: int | None = None,
            message: str | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.CHANGE_TECHNOLOGY_NAME,
            source_player=source_player,
            technology=technology,
            string_id=string_id,
            message=message,
        )

    def change_technology_description(
            self,
            source_player: int | None = None,
            technology: int | None = None,
            string_id: int | None = None,
            message: str | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.CHANGE_TECHNOLOGY_DESCRIPTION,
            source_player=source_player,
            technology=technology,
            string_id=string_id,
            message=message,
        )

    def enable_technology_stacking(
            self,
            source_player: int | None = None,
            technology: int | None = None,
            quantity: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.ENABLE_TECHNOLOGY_STACKING,
            source_player=source_player,
            technology=technology,
            quantity=quantity,
        )

    def disable_technology_stacking(
            self,
            source_player: int | None = None,
            technology: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.DISABLE_TECHNOLOGY_STACKING,
            source_player=source_player,
            technology=technology,
        )

    def acknowledge_multiplayer_ai_signal(
            self,
            ai_signal_value: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.ACKNOWLEDGE_MULTIPLAYER_AI_SIGNAL,
            ai_signal_value=ai_signal_value,
        )

    def disable_object_selection(
            self,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
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
            quantity: int | None = None,
            color_mood: int | None = None):
        return self._trigger_ref._add_effect(
            EffectId.CHANGE_COLOR_MOOD,
            quantity=quantity,
            color_mood=color_mood
        )

    def enable_object_deletion(
            self,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ):
        return self._trigger_ref._add_effect(
            EffectId.ENABLE_OBJECT_DELETION,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            selected_object_ids=selected_object_ids,
        )

    def disable_object_deletion(
            self,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ):
        return self._trigger_ref._add_effect(
            EffectId.DISABLE_OBJECT_DELETION,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            selected_object_ids=selected_object_ids,
        )

    def train_unit(
            self,
            quantity: int | None = None,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            location_x: int | None = None,
            location_y: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ):
        return self._trigger_ref._add_effect(
            EffectId.TRAIN_UNIT,
            quantity=quantity,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            location_x=location_x,
            location_y=location_y,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            selected_object_ids=selected_object_ids
        )

    def initiate_research(
            self,
            source_player: int | None = None,
            technology: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ):
        return self._trigger_ref._add_effect(
            EffectId.INITIATE_RESEARCH,
            source_player=source_player,
            technology=technology,
            selected_object_ids=selected_object_ids
        )

    def create_object_attack(
            self,
            armour_attack_quantity: int | None = None,
            armour_attack_class: int | None = None,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            object_group: int | None = None,
            object_type: int | None = None,
            operation: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ):
        return self._trigger_ref._add_effect(
            EffectId.CREATE_OBJECT_ATTACK,
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
            selected_object_ids=selected_object_ids
        )

    def create_object_armor(
            self,
            armour_attack_quantity: int | None = None,
            armour_attack_class: int | None = None,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            object_group: int | None = None,
            object_type: int | None = None,
            operation: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ):
        return self._trigger_ref._add_effect(
            EffectId.CREATE_OBJECT_ARMOR,
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
            selected_object_ids=selected_object_ids
        )

    def modify_attribute_by_variable(
            self,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            operation: int | None = None,
            object_attributes: int | None = None,
            variable: int | None = None,
            message: str | None = None,
            armour_attack_class: int | None = None,
    ):
        if armour_attack_class is not None and object_attributes not in (ObjectAttribute.ATTACK, ObjectAttribute.ARMOR):
            raise ValueError("Cannot use 'armour_attack_class' for non attack/armor attributes.")

        return self._trigger_ref._add_effect(
            EffectId.MODIFY_ATTRIBUTE_BY_VARIABLE,
            armour_attack_class=armour_attack_class,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            operation=operation,
            object_attributes=object_attributes,
            variable=variable,
            message=message,
        )

    def set_object_cost(
            self,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            quantity: int | None = None,
            tribute_list: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.SET_OBJECT_COST,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            quantity=quantity,
            tribute_list=tribute_list,
        )

    def load_key_value(
            self,
            variable: int | None = None,
            message: str | None = None,
            quantity: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.LOAD_KEY_VALUE,
            variable=variable,
            message=message,
            quantity=quantity,
        )

    def store_key_value(
            self,
            variable: int | None = None,
            message: str | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.STORE_KEY_VALUE,
            variable=variable,
            message=message,
        )

    def delete_key(
            self,
            message: str | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.DELETE_KEY,
            message=message,
        )

    def change_technology_icon(
            self,
            technology: int | None = None,
            source_player: int | None = None,
            quantity: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.CHANGE_TECHNOLOGY_ICON,
            technology=technology,
            source_player=source_player,
            quantity=quantity,
        )

    def change_technology_hotkey(
            self,
            technology: int | None = None,
            source_player: int | None = None,
            quantity: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.CHANGE_TECHNOLOGY_HOTKEY,
            technology=technology,
            source_player=source_player,
            quantity=quantity,
        )

    def modify_variable_by_resource(
            self,
            tribute_list: int | None = None,
            source_player: int | None = None,
            operation: int | None = None,
            variable: int | None = None,
    ) -> Effect:
        return self._trigger_ref._add_effect(
            EffectId.MODIFY_VARIABLE_BY_RESOURCE,
            tribute_list=tribute_list,
            source_player=source_player,
            operation=operation,
            variable=variable,
        )

    def modify_variable_by_attribute(
            self,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            operation: int | None = None,
            object_attributes: int | None = None,
            variable: int | None = None,
            message: str | None = None,
            armour_attack_class: int | None = None,
    ):
        if armour_attack_class is not None and object_attributes not in (ObjectAttribute.ATTACK, ObjectAttribute.ARMOR):
            raise ValueError("Cannot use 'armour_attack_class' for non attack/armor attributes.")

        return self._trigger_ref._add_effect(
            EffectId.MODIFY_VARIABLE_BY_ATTRIBUTE,
            armour_attack_class=armour_attack_class,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            operation=operation,
            object_attributes=object_attributes,
            variable=variable,
            message=message
        )

    def change_object_caption(
            self,
            object_list_unit_id: int | None = None,
            source_player: int | None = None,
            string_id: int | None = None,
            message: str | None = None,
            area_x1: int | None = None,
            area_y1: int | None = None,
            area_x2: int | None = None,
            area_y2: int | None = None,
            selected_object_ids: int | List[int] | None = None,
    ):
        return self._trigger_ref._add_effect(
            EffectId.CHANGE_OBJECT_CAPTION,
            object_list_unit_id=object_list_unit_id,
            source_player=source_player,
            string_id=string_id,
            message=message,
            area_x1=area_x1,
            area_y1=area_y1,
            area_x2=area_x2,
            area_y2=area_y2,
            selected_object_ids=selected_object_ids,
        )

    def change_player_color(
            self,
            source_player: int | None = None,
            player_color: int | None = None,
    ):
        return self._trigger_ref._add_effect(
            EffectId.CHANGE_PLAYER_COLOR,
            source_player=source_player,
            player_color=player_color,
        )
