from enum import IntEnum


class EffectId(IntEnum):
    """
    This enum class provides the integer values used to reference the effects in the game. Used in every effect to
    indicate which type of effect it is

    **Examples**

    >>> EffectId.RESEARCH_TECHNOLOGY
    >>> 2
    """
    NONE = 0
    """Attributes for the **none** effect are: \n
    ... none... Just like Conditions... People these days... """
    CHANGE_DIPLOMACY = 1
    """Attributes for the **change_diplomacy** effect are: \n
    - diplomacy
    - source_player
    - target_player"""
    RESEARCH_TECHNOLOGY = 2
    """Attributes for the **research_technology** effect are: \n
    - source_player
    - technology
    - force_research_technology"""
    SEND_CHAT = 3
    """Attributes for the **send_chat** effect are: \n
    - source_player
    - string_id
    - message
    - sound_name"""
    PLAY_SOUND = 4
    """Attributes for the **play_sound** effect are: \n
    - source_player
    - location_x
    - location_y
    - location_object_reference
    - sound_name"""
    TRIBUTE = 5
    """Attributes for the **tribute** effect are: \n
    - quantity
    - tribute_list
    - source_player
    - target_player"""
    UNLOCK_GATE = 6
    """Attributes for the **unlock_gate** effect are: \n
    - selected_object_ids"""
    LOCK_GATE = 7
    """Attributes for the **lock_gate** effect are: \n
    - selected_object_ids"""
    ACTIVATE_TRIGGER = 8
    """Attributes for the **activate_trigger** effect are: \n
    - trigger_id"""
    DEACTIVATE_TRIGGER = 9
    """Attributes for the **deactivate_trigger** effect are: \n
    - trigger_id"""
    AI_SCRIPT_GOAL = 10
    """Attributes for the **deactivate_trigger** effect are: \n
    - ai_script_goal"""
    CREATE_OBJECT = 11
    """Attributes for the **create_object** effect are: \n
    - object_list_unit_id
    - source_player
    - location_x
    - location_y
    - facet"""
    TASK_OBJECT = 12
    """Attributes for the **task_object** effect are: \n
    - object_list_unit_id
    - source_player
    - location_x
    - location_y
    - location_object_reference
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - object_group
    - object_type
    - action_type
    - selected_object_ids"""
    DECLARE_VICTORY = 13
    """Attributes for the **declare_victory** effect are: \n
    - source_player
    - enabled"""
    KILL_OBJECT = 14
    """Attributes for the **kill_object** effect are: \n
    - object_list_unit_id
    - source_player
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - object_group
    - object_type
    - selected_object_ids"""
    REMOVE_OBJECT = 15
    """Attributes for the **remove_object** effect are: \n
    - object_list_unit_id
    - source_player
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - object_group
    - object_type
    - object_state
    - selected_object_ids"""
    CHANGE_VIEW = 16
    """Attributes for the **change_view** effect are: \n
    - quantity
    - source_player
    - location_x
    - location_y
    - scroll"""
    UNLOAD = 17
    """Attributes for the **unload** effect are: \n
    - object_list_unit_id
    - source_player
    - location_x
    - location_y
    - location_object_reference
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - object_group
    - object_type
    - selected_object_ids"""
    CHANGE_OWNERSHIP = 18
    """Attributes for the **change_ownership** effect are: \n
    - object_list_unit_id
    - source_player
    - target_player
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - object_group
    - object_type
    - flash_object
    - selected_object_ids"""
    PATROL = 19
    """Attributes for the **patrol** effect are: \n
    - object_list_unit_id
    - source_player
    - location_x
    - location_y
    - location_object_reference
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - object_group
    - object_type
    - selected_object_ids"""
    DISPLAY_INSTRUCTIONS = 20
    """Attributes for the **display_instructions** effect are: \n
    - object_list_unit_id
    - source_player
    - string_id
    - display_time
    - instruction_panel_position
    - play_sound
    - message
    - sound_name"""
    CLEAR_INSTRUCTIONS = 21
    """Attributes for the **clear_instructions** effect are: \n
    - instruction_panel_position"""
    FREEZE_OBJECT = 22
    """Attributes for the **freeze_object** effect are: \n
    - object_list_unit_id
    - source_player
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - object_group
    - object_type
    - selected_object_ids"""
    USE_ADVANCED_BUTTONS = 23
    """Attributes for the **use_advanced_buttons** effect are: \n
    None. \n
    Please don't use this effect. Please."""
    DAMAGE_OBJECT = 24
    """Attributes for the **damage_object** effect are: \n
    - quantity
    - object_list_unit_id
    - source_player
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - object_group
    - object_type
    - selected_object_ids"""
    PLACE_FOUNDATION = 25
    """Attributes for the **place_foundation** effect are: \n
    - object_list_unit_id
    - source_player
    - location_x
    - location_y"""
    CHANGE_OBJECT_NAME = 26
    """Attributes for the **change_object_name** effect are: \n
    - object_list_unit_id
    - source_player
    - string_id
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - message
    - selected_object_ids"""
    CHANGE_OBJECT_HP = 27
    """Attributes for the **change_object_hp** effect are: \n
    - quantity
    - object_list_unit_id
    - source_player
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - object_group
    - object_type
    - operation
    - selected_object_ids"""
    CHANGE_OBJECT_ATTACK = 28
    """Attributes for the **change_object_attack** effect are: \n
    - armour_attack_quantity
    - armour_attack_class
    - object_list_unit_id
    - source_player
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - object_group
    - object_type
    - operation
    - selected_object_ids"""
    STOP_OBJECT = 29
    """Attributes for the **stop_object** effect are: \n
    - object_list_unit_id
    - source_player
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - object_group
    - object_type
    - selected_object_ids"""
    ATTACK_MOVE = 30
    """Attributes for the **attack_move** effect are: \n
    - object_list_unit_id
    - source_player
    - location_x
    - location_y
    - location_object_reference
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - object_group
    - object_type
    - selected_object_ids"""
    CHANGE_OBJECT_ARMOR = 31
    """Attributes for the **change_object_armor** effect are: \n
    - armour_attack_quantity
    - armour_attack_class
    - object_list_unit_id
    - source_player
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - object_group
    - object_type
    - operation
    - selected_object_ids"""
    CHANGE_OBJECT_RANGE = 32
    """Attributes for the **change_object_range** effect are: \n
    - quantity
    - object_list_unit_id
    - source_player
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - object_group
    - object_type
    - operation
    - selected_object_ids"""
    CHANGE_OBJECT_SPEED = 33
    """Attributes for the **change_object_speed** effect are: \n
    - quantity
    - object_list_unit_id
    - source_player
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - object_group
    - object_type
    - selected_object_ids"""
    HEAL_OBJECT = 34
    """Attributes for the **heal_object** effect are: \n
    - quantity
    - object_list_unit_id
    - source_player
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - object_group
    - object_type
    - selected_object_ids"""
    TELEPORT_OBJECT = 35
    """Attributes for the **teleport_object** effect are: \n
    - object_list_unit_id
    - source_player
    - location_x
    - location_y
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - object_group
    - object_type
    - selected_object_ids"""
    CHANGE_OBJECT_STANCE = 36
    """Attributes for the **change_object_stance** effect are: \n
    - object_list_unit_id
    - source_player
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - object_group
    - object_type
    - attack_stance
    - selected_object_ids"""
    DISPLAY_TIMER = 37
    """Attributes for the **display_timer** effect are: \n
    - string_id
    - display_time
    - time_unit
    - timer
    - reset_timer
    - message"""
    ENABLE_DISABLE_OBJECT = 38
    """Attributes for the **enable_disable_object** effect are: \n
    - object_list_unit_id
    - source_player
    - enabled"""
    ENABLE_DISABLE_TECHNOLOGY = 39
    """Attributes for the **enable_disable_technology** effect are: \n
    - source_player
    - technology
    - enabled"""
    CHANGE_OBJECT_COST = 40
    """Attributes for the **change_object_cost** effect are: \n
    - object_list_unit_id
    - source_player
    - resource_1
    - resource_1_quantity
    - resource_2
    - resource_2_quantity
    - resource_3
    - resource_3_quantity"""
    SET_PLAYER_VISIBILITY = 41
    """Attributes for the **set_player_visibility** effect are: \n
    - source_player
    - target_player
    - visibility_state"""
    CHANGE_OBJECT_ICON = 42
    """Attributes for the **change_object_icon** effect are: \n
    - object_list_unit_id
    - source_player
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - object_group
    - object_type
    - object_list_unit_id_2
    - selected_object_ids"""
    REPLACE_OBJECT = 43
    """Attributes for the **replace_object** effect are: \n
    - object_list_unit_id
    - source_player
    - target_player
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - object_group
    - object_type
    - object_list_unit_id_2
    - selected_object_ids"""
    CHANGE_OBJECT_DESCRIPTION = 44
    """Attributes for the **change_object_description** effect are: \n
    - object_list_unit_id
    - source_player
    - string_id
    - message"""
    CHANGE_PLAYER_NAME = 45
    """Attributes for the **change_player_name** effect are: \n
    - source_player
    - string_id
    - message"""
    CHANGE_TRAIN_LOCATION = 46
    """Attributes for the **change_train_location** effect are: \n
    - object_list_unit_id
    - source_player
    - object_list_unit_id_2
    - button_location"""
    CHANGE_TECHNOLOGY_LOCATION = 47
    """Attributes for the **change_technology_location** effect are: \n
    - source_player
    - technology
    - object_list_unit_id_2
    - button_location"""
    CHANGE_CIVILIZATION_NAME = 48
    """Attributes for the **change_civilization_name** effect are: \n
    - source_player
    - string_id
    - message"""
    CREATE_GARRISONED_OBJECT = 49
    """Attributes for the **create_garrisoned_object** effect are: \n
    - object_list_unit_id
    - source_player
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - object_list_unit_id_2
    - selected_object_ids"""
    ACKNOWLEDGE_AI_SIGNAL = 50
    """Attributes for the **acknowledge_ai_signal** effect are: \n
    - ai_signal_value"""
    MODIFY_ATTRIBUTE = 51
    """Attributes for the **modify_attribute** effect are: \n
    - quantity
    - object_list_unit_id
    - source_player
    - operation
    - object_attributes
    - message"""
    MODIFY_RESOURCE = 52
    """Attributes for the **modify_resource** effect are: \n
    - quantity
    - tribute_list
    - source_player
    - operation"""
    MODIFY_RESOURCE_BY_VARIABLE = 53
    """Attributes for the **modify_resource_by_variable** effect are: \n
    - tribute_list
    - source_player
    - operation
    - variable"""
    SET_BUILDING_GATHER_POINT = 54
    """Attributes for the **set_building_gather_point** effect are: \n
    - object_list_unit_id
    - source_player
    - location_x
    - location_y
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - selected_object_ids"""
    SCRIPT_CALL = 55
    """Attributes for the **script_call** effect are: \n
    - string_id
    - message"""
    CHANGE_VARIABLE = 56
    """Attributes for the **change_variable** effect are: \n
    - quantity
    - operation
    - variable
    - message"""
    CLEAR_TIMER = 57
    """Attributes for the **clear_timer** effect are: \n
    - timer"""
    CHANGE_OBJECT_PLAYER_COLOR = 58
    """Attributes for the **change_object_player_color** effect are: \n
    - object_list_unit_id
    - source_player
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - player_color
    - selected_object_ids"""
    CHANGE_OBJECT_CIVILIZATION_NAME = 59
    """Attributes for the **change_object_civilization_name** effect are: \n
    - string_id
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - selected_object_ids"""
    CHANGE_OBJECT_PLAYER_NAME = 60
    """Attributes for the **change_object_player_name** effect are: \n
    - object_list_unit_id
    - source_player
    - string_id
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - selected_object_ids"""
    DISABLE_UNIT_TARGETING = 61
    """Attributes for the **disable_unit_targeting** effect are: \n
    - object_list_unit_id
    - source_player
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - selected_object_ids"""
    ENABLE_UNIT_TARGETING = 62
    """Attributes for the **enable_unit_targeting** effect are: \n
    - object_list_unit_id
    - source_player
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - selected_object_ids"""
    CHANGE_TECHNOLOGY_COST = 63
    """Attributes for the **change_technology_cost** effect are: \n
    - source_player
    - technology
    - resource_1
    - resource_1_quantity
    - resource_2
    - resource_2_quantity
    - resource_3
    - resource_3_quantity"""
    CHANGE_TECHNOLOGY_RESEARCH_TIME = 64
    """Attributes for the **change_technology_research_time** effect are: \n
    - quantity
    - source_player
    - technology"""
    CHANGE_TECHNOLOGY_NAME = 65
    """Attributes for the **change_technology_name** effect are: \n
    - source_player
    - technology
    - string_id
    - message"""
    CHANGE_TECHNOLOGY_DESCRIPTION = 66
    """Attributes for the **change_technology_description** effect are: \n
    - source_player
    - technology
    - string_id
    - message"""
    ENABLE_TECHNOLOGY_STACKING = 67
    """Attributes for the **enable_technology_stacking** effect are: \n
    - source_player
    - technology"""
    DISABLE_TECHNOLOGY_STACKING = 68
    """Attributes for the **disable_technology_stacking** effect are: \n
    - source_player
    - technology"""
    ACKNOWLEDGE_MULTIPLAYER_AI_SIGNAL = 69
    """Attributes for the **acknowledge_multiplayer_ai_signal** effect are: \n
    - ai_signal_value
    """
    DISABLE_OBJECT_SELECTION = 70
    """Attributes for the **disable_object_selection** effect are: \n
    - object_list_unit_id
    - source_player
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - selected_object_ids"""
    ENABLE_OBJECT_SELECTION = 71
    """Attributes for the **enable_object_selection** effect are: \n
    - object_list_unit_id
    - source_player
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - selected_object_ids"""
    CHANGE_COLOR_MOOD = 72
    """Attributes for the **change_color_mood** effect are: \n
    - quantity
    - color_mood
    
    **Version notice**: \n
    This effect was added in: 1.42
    """
    ENABLE_OBJECT_DELETION = 73
    """Attributes for the **enable_object_deletion** effect are: \n
    - object_list_unit_id
    - source_player
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - selected_object_ids
    
    **Version notice**: \n
    This effect was added in: 1.46
    """
    DISABLE_OBJECT_DELETION = 74
    """Attributes for the **disable_object_deletion** effect are: \n
    - object_list_unit_id
    - source_player
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - selected_object_ids
    
    **Version notice**: \n
    This effect was added in: 1.46
    """
    TRAIN_UNIT = 75
    """Attributes for the **train_unit** effect are: \n
    - quantity
    - object_list_unit_id
    - source_player
    - location_x
    - location_y
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - selected_object_ids
    
    **Version notice**: \n
    This effect was added in: 1.51 & Trigger Version 3.5
    """
    INITIATE_RESEARCH = 76
    """Attributes for the **initiate_research** effect are: \n
    - source_player
    - technology
    - selected_object_ids
    
    **Version notice**: \n
    This effect was added in: 1.51 & Trigger Version 3.5
    """
    CREATE_OBJECT_ATTACK = 77
    """Attributes for the **create_object_attack** effect are: \n
    - armour_attack_quantity
    - armour_attack_class
    - object_list_unit_id
    - source_player
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - object_group
    - object_type
    - operation
    - selected_object_ids
    
    **Version notice**: \n
    This effect was added in: 1.51 & Trigger Version 3.5
    """
    CREATE_OBJECT_ARMOR = 78
    """Attributes for the **create_object_armor** effect are: \n
    - armour_attack_quantity
    - armour_attack_class
    - object_list_unit_id
    - source_player
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - object_group
    - object_type
    - operation
    - selected_object_ids
    
    **Version notice**: \n
    This effect was added in: 1.51 & Trigger Version 3.5
    """
    MODIFY_ATTRIBUTE_BY_VARIABLE = 79
    """Attributes for the **modify_attribute_by_variable** effect are: \n
    - object_list_unit_id
    - source_player
    - operation
    - object_attributes
    - variable
    - message
    - armour_attack_class
    
    **Version notice**: \n
    This effect was added in: 1.51 & Trigger Version 3.5
    """
    SET_OBJECT_COST = 80
    """Attributes for the **set_object_cost** effect are: \n
    - object_list_unit_id
    - source_player
    - quantity
    - tribute_list

    **Version notice**: \n
    This effect was added in: 1.54 & Trigger Version 3.9
    """
    LOAD_KEY_VALUE = 81
    """Attributes for the **load_key_value** effect are: \n
    - variable
    - message
    - quantity

    **Version notice**: \n
    This effect was added in: 1.54 & Trigger Version 3.9
    """
    STORE_KEY_VALUE = 82
    """Attributes for the **store_key_value** effect are: \n
    - variable
    - message

    **Version notice**: \n
    This effect was added in: 1.54 & Trigger Version 3.9
    """
    DELETE_KEY = 83
    """Attributes for the **delete_key** effect are: \n
    - message

    **Version notice**: \n
    This effect was added in: 1.54 & Trigger Version 3.9
    """
    CHANGE_TECHNOLOGY_ICON = 84
    """Attributes for the **change_technology_icon** effect are: \n
    - technology
    - source_player
    - quantity

    **Version notice**: \n
    This effect was added in: 1.54 & Trigger Version 3.9
    """
    CHANGE_TECHNOLOGY_HOTKEY = 85
    """Attributes for the **change_technology_hotkey** effect are: \n
    - technology
    - source_player
    - quantity

    **Version notice**: \n
    This effect was added in: 1.54 & Trigger Version 3.9
    """
    MODIFY_VARIABLE_BY_RESOURCE = 86
    """Attributes for the **modify_variable_by_resource** effect are: \n
    - tribute_list
    - source_player
    - operation
    - variable
        
    **Version notice**: \n
    This effect was added in: 1.54 & Trigger Version 3.9
    """
    MODIFY_VARIABLE_BY_ATTRIBUTE = 87
    """Attributes for the **modify_variable_by_attribute** effect are: \n
    - object_list_unit_id
    - source_player
    - operation
    - object_attributes
    - variable
    - message
    - armour_attack_class

    **Version notice**: \n
    This effect was added in: 1.54 & Trigger Version 3.9
    """
    CHANGE_OBJECT_CAPTION = 88
    """Attributes for the **change_object_caption** effect are: \n
    - object_list_unit_id
    - source_player
    - string_id
    - message
    - selected_object_ids
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    **Version notice**: \n
    This effect was added in: 1.54 & Trigger Version 3.9
    """
    CHANGE_PLAYER_COLOR = 89
    """Attributes for the **change_player_color** effect are: \n
    - source_player
    - player_color
    **Version notice**: \n
    This effect was added in: 1.54 & Trigger Version 3.9
    """


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
    "message": "",
    "sound_name": "",
    "selected_object_ids": -1,
    "unused_string_1": "",
    "unused_string_2": "",
}

# Set using the version json files
effect_names = {}
default_attributes = {}
attributes = {}
attribute_presentation = {}
"""
This dict maps the effect attributes by their name to the dataset used to represent them
"""