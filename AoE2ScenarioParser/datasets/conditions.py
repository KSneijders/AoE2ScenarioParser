from enum import IntEnum


class ConditionId(IntEnum):
    """
    This enum class provides the integer values used to reference the conditions in the game. Used in every condition
    to indicate which type of condition it is

    **Examples**

    >>> ConditionId.BRING_OBJECT_TO_AREA
    >>> 1
    """
    NONE = 0
    """
    Attributes for the **none**  condition are:\n
    ... It's called none... What parameters do **you** think it has?! ❤ 
    """
    BRING_OBJECT_TO_AREA = 1
    """
    Attributes for the **bring_object_to_area** condition are:\n
    - unit_object  
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - inverted
    """
    BRING_OBJECT_TO_OBJECT = 2
    """
    Attributes for the **bring_object_to_object** condition are:\n
    - unit_object
    - next_object
    - inverted
    """
    OWN_OBJECTS = 3
    """
    Attributes for the **own_objects** condition are:\n
    - quantity
    - object_list
    - source_player
    - object_group
    - object_type
    - include_changeable_weapon_objects
    """
    OWN_FEWER_OBJECTS = 4
    """
    Attributes for the **own_fewer_objects** condition are:\n
    - quantity
    - object_list
    - source_player
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - object_group
    - object_type
    - include_changeable_weapon_objects
    """
    OBJECTS_IN_AREA = 5
    """
    Attributes for the **object_in_area** condition are:\n
    - quantity
    - object_list
    - source_player
    - area_x1
    - area_y1
    - area_x2
    - area_y2
    - object_group
    - object_type
    - object_state
    - inverted
    - include_changeable_weapon_objects
    """
    DESTROY_OBJECT = 6
    """
    Attributes for the **destroy_object** condition are:\n
    - unit_object
    - inverted
    """
    CAPTURE_OBJECT = 7
    """
    Attributes for the **capture_object** condition are:\n
    - unit_object
    - source_player
    - inverted
    """
    ACCUMULATE_ATTRIBUTE = 8
    """
    Attributes for the **accumulate_attribute** condition are:\n
    - quantity
    - attribute
    - source_player
    - inverted
    """
    RESEARCH_TECHNOLOGY = 9
    """
    Attributes for the **research_technology** condition are:\n
    - source_player
    - technology
    - inverted
    """
    TIMER = 10
    """
    Attributes for the **timer** condition are:\n
    - timer
    - inverted
    """
    OBJECT_SELECTED = 11
    """
    Attributes for the **object_selected** condition are:\n
    - unit_object
    - inverted
    """
    AI_SIGNAL = 12
    """
    Attributes for the **ai_signal** condition are:\n
    - ai_signal
    - inverted
    """
    PLAYER_DEFEATED = 13
    """
    Attributes for the **player_defeated** condition are:\n
    - source_player
    - inverted
    """
    OBJECT_HAS_TARGET = 14
    """
    Attributes for the **object_has_target** condition are:\n
    - unit_object
    - next_object
    - object_list
    - object_group
    - object_type
    - inverted
    """
    OBJECT_VISIBLE = 15
    """
    Attributes for the **object_visible** condition are:\n
    - unit_object
    """
    OBJECT_NOT_VISIBLE = 16
    """
    Attributes for the **object_not_visible** condition are:\n
    - unit_object
    """
    RESEARCHING_TECH = 17
    """
    Attributes for the **researching_tech** condition are:\n
    - source_player
    - technology
    - inverted
    """
    UNITS_GARRISONED = 18
    """
    Attributes for the **units_garrisoned** condition are:\n
    - quantity
    - unit_object
    - inverted
    """
    DIFFICULTY_LEVEL = 19
    """
    Attributes for the **difficulty_level** condition are:\n
    - condition_type
    - quantity
    - inverted
    """
    CHANCE = 20
    """
    Attributes for the **chance** condition are:\n
    - quantity
    """
    TECHNOLOGY_STATE = 21
    """
    Attributes for the **technology_state** condition are:\n
    - quantity
    - source_player
    - technology
    - inverted
    """
    VARIABLE_VALUE = 22
    """
    Attributes for the **variable_value** condition are:\n
    - quantity
    - inverted
    - variable
    - comparison
    """
    OBJECT_HP = 23
    """
    Attributes for the **object_hp** condition are:\n
    - quantity
    - unit_object
    - inverted
    - comparison
    """
    DIPLOMACY_STATE = 24
    """
    Attributes for the **diplomacy_state** condition are:\n
    - quantity
    - source_player
    - inverted
    - target_player
    """
    SCRIPT_CALL = 25
    """
    Attributes for the **script_call** condition are:\n
    - xs_function
    
    **Version notice**: \n
    This condition was added in: 1.40
    """
    OBJECT_SELECTED_MULTIPLAYER = 26
    """
    Attributes for the **object_selected_multiplayer** condition are:\n
    - unit_object
    - source_player
    - inverted
    
    **Version notice**: \n
    This condition was added in: 1.40
    """
    OBJECT_VISIBLE_MULTIPLAYER = 27
    """
    Attributes for the **object_visible_multiplayer** condition are:\n
    - unit_object
    - source_player
    - inverted
    
    **Version notice**: \n
    This condition was added in: 1.40
    """
    OBJECT_HAS_ACTION = 28
    """
    Attributes for the **object_has_action** condition are:\n
    - unit_object
    - next_object
    - inverted
    - unit_ai_action
    
    **Version notice**: \n
    This condition was added in: 1.40
    """
    OR = 29
    """
    The **OR** condition does not have any attributes
    
    **Version notice**: \n
    This condition was added in: 1.40
    """
    AI_SIGNAL_MULTIPLAYER = 30
    """
    Attributes for the **ai_signal_multiplayer** condition are:\n
    - ai_signal
    - inverted
    
    **Version notice**: \n
    This condition was added in: 1.40
    """
    BUILDING_IS_TRADING = 54
    """
    Attributes for the **building_is_trading** condition are:\n
    - unit_object
    - inverted
    
    **Version notice**: \n
    This condition was added in: 1.46
    """
    DISPLAY_TIMER_TRIGGERED = 55
    """
    Attributes for the **display_timer_triggered** condition are:\n
    - timer_id
    - inverted
    
    **Version notice**: \n
    This condition was added in: 1.46
    """
    VICTORY_TIMER = 56
    """
    Attributes for the **victory_timer** condition are:\n
    - quantity
    - source_player
    - inverted
    - comparison
    - victory_timer_type
    
    **Version notice**: \n
    This condition was added in: 1.46
    """
    AND = 57
    """
    The **AND** condition does not have any attributes
    
    **Version notice**: \n
    This condition was added in: 1.46
    """


empty_attributes = {
    "condition_type": -1,
    "quantity": -1,
    "attribute": -1,
    "unit_object": -1,
    "next_object": -1,
    "object_list": -1,
    "source_player": -1,
    "technology": -1,
    "timer": -1,
    "area_x1": -1,
    "area_y1": -1,
    "area_x2": -1,
    "area_y2": -1,
    "object_group": -1,
    "object_type": -1,
    "ai_signal": -1,
    "inverted": -1,
    "variable": -1,
    "comparison": -1,
    "target_player": -1,
    "unit_ai_action": -1,
    "object_state": -1,
    "timer_id": -1,
    "victory_timer_type": -1,
    "include_changeable_weapon_objects": -1,
    "xs_function": ""
}

# Set using the version json files
condition_names = {}
default_attributes = {}
attributes = {}
attribute_presentation = {}
"""
This dict maps the condition attributes by their name to the dataset used to represent them
"""