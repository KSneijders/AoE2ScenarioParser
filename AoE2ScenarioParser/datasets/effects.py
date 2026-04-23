from enum import IntEnum


# Todo: LEGACY - REMOVE
class EffectId(IntEnum):
    """
    This enum class provides the integer values used to reference the effects in the game. Used in every effect to
    indicate which type of effect it is

    **Examples**

    >>> EffectType.RESEARCH_TECHNOLOGY
    >>> 2
    """
    NONE = 0
    CHANGE_DIPLOMACY = 1
    RESEARCH_TECHNOLOGY = 2
    SEND_CHAT = 3
    PLAY_SOUND = 4
    TRIBUTE = 5
    UNLOCK_GATE = 6
    LOCK_GATE = 7
    ACTIVATE_TRIGGER = 8
    DEACTIVATE_TRIGGER = 9
    AI_SCRIPT_GOAL = 10
    CREATE_OBJECT = 11
    TASK_OBJECT = 12
    DECLARE_VICTORY = 13
    KILL_OBJECT = 14
    REMOVE_OBJECT = 15
    CHANGE_VIEW = 16
    UNLOAD = 17
    CHANGE_OWNERSHIP = 18
    PATROL = 19
    DISPLAY_INSTRUCTIONS = 20
    CLEAR_INSTRUCTIONS = 21
    FREEZE_OBJECT = 22
    USE_ADVANCED_BUTTONS = 23
    DAMAGE_OBJECT = 24
    PLACE_FOUNDATION = 25
    CHANGE_OBJECT_NAME = 26
    CHANGE_OBJECT_HP = 27
    CHANGE_OBJECT_ATTACK = 28
    STOP_OBJECT = 29
    ATTACK_MOVE = 30
    CHANGE_OBJECT_ARMOR = 31
    CHANGE_OBJECT_RANGE = 32
    CHANGE_OBJECT_SPEED = 33
    HEAL_OBJECT = 34
    TELEPORT_OBJECT = 35
    CHANGE_OBJECT_STANCE = 36
    DISPLAY_TIMER = 37
    ENABLE_DISABLE_OBJECT = 38
    ENABLE_DISABLE_TECHNOLOGY = 39
    CHANGE_OBJECT_COST = 40
    SET_PLAYER_VISIBILITY = 41
    CHANGE_OBJECT_ICON = 42
    REPLACE_OBJECT = 43
    CHANGE_OBJECT_DESCRIPTION = 44
    CHANGE_PLAYER_NAME = 45
    CHANGE_TRAIN_LOCATION = 46
    CHANGE_TECHNOLOGY_LOCATION = 47
    CHANGE_CIVILIZATION_NAME = 48
    CREATE_GARRISONED_OBJECT = 49
    ACKNOWLEDGE_AI_SIGNAL = 50
    MODIFY_ATTRIBUTE = 51
    MODIFY_RESOURCE = 52
    MODIFY_RESOURCE_BY_VARIABLE = 53
    SET_BUILDING_GATHER_POINT = 54
    SCRIPT_CALL = 55
    CHANGE_VARIABLE = 56
    CLEAR_TIMER = 57
    CHANGE_OBJECT_PLAYER_COLOR = 58
    CHANGE_OBJECT_CIVILIZATION_NAME = 59
    CHANGE_OBJECT_PLAYER_NAME = 60
    DISABLE_UNIT_TARGETING = 61
    ENABLE_UNIT_TARGETING = 62
    CHANGE_TECHNOLOGY_COST = 63
    CHANGE_TECHNOLOGY_RESEARCH_TIME = 64
    CHANGE_TECHNOLOGY_NAME = 65
    CHANGE_TECHNOLOGY_DESCRIPTION = 66
    ENABLE_TECHNOLOGY_STACKING = 67
    DISABLE_TECHNOLOGY_STACKING = 68
    ACKNOWLEDGE_MULTIPLAYER_AI_SIGNAL = 69
    DISABLE_OBJECT_SELECTION = 70
    ENABLE_OBJECT_SELECTION = 71
    CHANGE_COLOR_MOOD = 72
    ENABLE_OBJECT_DELETION = 73
    DISABLE_OBJECT_DELETION = 74
    TRAIN_UNIT = 75
    INITIATE_RESEARCH = 76
    CREATE_OBJECT_ATTACK = 77
    CREATE_OBJECT_ARMOR = 78
    MODIFY_ATTRIBUTE_BY_VARIABLE = 79
    SET_OBJECT_COST = 80
    LOAD_KEY_VALUE = 81
    STORE_KEY_VALUE = 82
    DELETE_KEY = 83
    CHANGE_TECHNOLOGY_ICON = 84
    CHANGE_TECHNOLOGY_HOTKEY = 85
    MODIFY_VARIABLE_BY_RESOURCE = 86
    MODIFY_VARIABLE_BY_ATTRIBUTE = 87
    CHANGE_OBJECT_CAPTION = 88
    CHANGE_PLAYER_COLOR = 89
    CREATE_DECISION = 90
    DISABLE_UNIT_ATTACKABLE = 98
    ENABLE_UNIT_ATTACKABLE = 99
    MODIFY_VARIABLE_BY_VARIABLE = 100
    COUNT_UNITS_INTO_VARIABLE = 101
    ADD_TRAIN_LOCATION = 102
    RESEARCH_LOCAL_TECHNOLOGY = 103
    MODIFY_ATTRIBUTE_FOR_CLASS = 104
    MODIFY_OBJECT_ATTRIBUTE = 105
    MODIFY_OBJECT_ATTRIBUTE_BY_VARIABLE = 106
    CHANGE_OBJECT_VISIBILITY = 107
    BUILD_OBJECT = 108


empty_attributes = {
    "effect_type": -1,
    "ai_script_goal": -1,
    "armour_attack_quantity": -1,
    "armour_attack_class": -1,
    "quantity": -1,
    "tribute_list": -1,
    "diplomacy": -1,
    "object_list_unit_id": -1,
    "source_player": -1,
    "target_player": -1,
    "technology": -1,
    "string_id": -1,
    "display_time": -1,
    "trigger_id": -1,
    "location_x": -1,
    "location_y": -1,
    "location_object_reference": -1,
    "area_x1": -1,
    "area_y1": -1,
    "area_x2": -1,
    "area_y2": -1,
    "object_group": -1,
    "object_type": -1,
    "instruction_panel_position": -1,
    "attack_stance": -1,
    "time_unit": -1,
    "enabled": -1,
    "food": -1,
    "wood": -1,
    "stone": -1,
    "gold": -1,
    "item_id": -1,
    "flash_object": -1,
    "force_research_technology": -1,
    "visibility_state": -1,
    "scroll": -1,
    "operation": -1,
    "object_list_unit_id_2": -1,
    "button_location": -1,
    "ai_signal_value": -1,
    "object_attributes": -1,
    "variable": -1,
    "timer": -1,
    "facet": -1,
    "play_sound": -1,
    "player_color": -1,
    "color_mood": -1,
    "reset_timer": -1,
    "object_state": -1,
    "action_type": -1,
    "resource_1": -1,
    "resource_1_quantity": -1,
    "resource_2": -1,
    "resource_2_quantity": -1,
    "resource_3": -1,
    "resource_3_quantity": -1,
    "decision_id": -1,
    "string_id_option1": -1,
    "string_id_option2": -1,
    "variable2": -1,
    "max_units_affected": -1,
    "disable_garrison_unload_sound": -1,
    "hotkey": -1,
    "train_time": -1,
    "local_technology": -1,
    "disable_sound": -1,
    "object_group2": -1,
    "quantity_float": -1,
    "facet2": -1,
    "global_sound": -1,
    "issue_group_command": -1,
    "queue_action": -1,
    "mutual_diplomacy": -1,
    "wall_x1": -1,
    "wall_y1": -1,
    "wall_x2": -1,
    "wall_y2": -1,
    "message": "",
    "sound_name": "",
    "selected_object_ids": -1,
    "message_option1": "",
    "message_option2": "",
}

# Set using the version JSON files
effect_names = {}
default_attributes = {}
attributes = {}
attribute_presentation = {}
"""
This dict maps the effect attributes by their name to the dataset used to represent them
"""