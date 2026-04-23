from enum import IntEnum

# Todo: LEGACY - REMOVE
class ConditionId(IntEnum):
    """
    This enum class provides the integer values used to reference the conditions in the game. Used in every condition
    to indicate which type of condition it is

    **Examples**

    >>> ConditionId.BRING_OBJECT_TO_AREA
    >>> 1
    """
    NONE = 0
    BRING_OBJECT_TO_AREA = 1
    BRING_OBJECT_TO_OBJECT = 2
    OWN_OBJECTS = 3
    OWN_FEWER_OBJECTS = 4
    OBJECTS_IN_AREA = 5
    DESTROY_OBJECT = 6
    CAPTURE_OBJECT = 7
    ACCUMULATE_ATTRIBUTE = 8
    RESEARCH_TECHNOLOGY = 9
    TIMER = 10
    OBJECT_SELECTED = 11
    AI_SIGNAL = 12
    PLAYER_DEFEATED = 13
    OBJECT_HAS_TARGET = 14
    OBJECT_VISIBLE = 15
    OBJECT_NOT_VISIBLE = 16
    RESEARCHING_TECH = 17
    UNITS_GARRISONED = 18
    DIFFICULTY_LEVEL = 19
    CHANCE = 20
    TECHNOLOGY_STATE = 21
    VARIABLE_VALUE = 22
    OBJECT_HP = 23
    DIPLOMACY_STATE = 24
    SCRIPT_CALL = 25
    OBJECT_SELECTED_MULTIPLAYER = 26
    OBJECT_VISIBLE_MULTIPLAYER = 27
    OBJECT_HAS_ACTION = 28
    OR = 29
    AI_SIGNAL_MULTIPLAYER = 30
    BUILDING_IS_TRADING = 54
    DISPLAY_TIMER_TRIGGERED = 55
    VICTORY_TIMER = 56
    AND = 57
    DECISION_TRIGGERED = 75
    OBJECT_ATTACKED = 76
    HERO_POWER_CAST = 77
    COMPARE_VARIABLES = 78
    TRIGGER_ACTIVE = 79
    LOCAL_TECH_RESEARCHED = 80


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
    "trigger_id": -1,
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
    "decision_id": -1,
    "decision_option": -1,
    "variable2":  "",
    "local_technology": -1,
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