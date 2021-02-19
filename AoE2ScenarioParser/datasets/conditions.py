from enum import IntEnum

from bidict import bidict


class ConditionId(IntEnum):
    NONE = 0
    """
    Attributes for the **none**  condition are:\n
    ... It's called none... What parameters do **you** think it has?! ❤ 
    """
    BRING_OBJECT_TO_AREA = 1
    """
    Attributes for the **bring_object_to_area** condition are:\n
    - unit_object  
    - area_1_x
    - area_1_y
    - area_2_x
    - area_2_y
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
    - amount_or_quantity
    - object_list
    - source_player
    - object_group
    - object_type
    """
    OWN_FEWER_OBJECTS = 4
    """
    Attributes for the **own_fewer_objects** condition are:\n
    - amount_or_quantity
    - object_list
    - source_player
    - area_1_x
    - area_1_y
    - area_2_x
    - area_2_y
    - object_group
    - object_type
    """
    OBJECT_IN_AREA = 5
    """
    Attributes for the **object_in_area** condition are:\n
    - amount_or_quantity
    - object_list
    - source_player
    - area_1_x
    - area_1_y
    - area_2_x
    - area_2_y
    - object_group
    - object_type
    - inverted
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
    - amount_or_quantity
    - resource_type_or_tribute_list
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
    - amount_or_quantity
    - unit_object
    - inverted
    """
    DIFFICULTY_LEVEL = 19
    """
    Attributes for the **units_garrisoned** condition are:\n
    - condition_type
    - amount_or_quantity
    - inverted
    """
    CHANCE = 20
    """
    Attributes for the **chance** condition are:\n
    - amount_or_quantity
    """
    TECHNOLOGY_STATE = 21
    """
    Attributes for the **technology_state** condition are:\n
    - amount_or_quantity
    - source_player
    - technology
    - inverted
    """
    VARIABLE_VALUE = 22
    """
    Attributes for the **variable_value** condition are:\n
    - amount_or_quantity
    - inverted
    - variable
    - comparison
    """
    OBJECT_HP = 23
    """
    Attributes for the **object_hp** condition are:\n
    - amount_or_quantity
    - unit_object
    - inverted
    - comparison
    """
    DIPLOMACY_STATE = 24
    """
    Attributes for the **diplomacy_state** condition are:\n
    - amount_or_quantity
    - source_player
    - inverted
    - target_player
    """
    # Todo: Mark as 1.40 feature
    SCRIPT_CALL = 25
    """
    Attributes for the **script_call** condition are:\n
    - xs_function
    """
    # Todo: Mark as 1.40 feature
    OBJECT_VISIBLE_MULTIPLAYER = 26
    """
    Attributes for the **object_visible_multiplayer** condition are:\n
    - unit_object
    - source_player
    - inverted
    """
    # Todo: Mark as 1.40 feature
    OBJECT_SELECTED_MULTIPLAYER = 27
    """
    Attributes for the **object_selected_multiplayer** condition are:\n
    - unit_object
    - source_player
    - inverted
    """
    # Todo: Mark as 1.40 feature
    OBJECT_HAS_ACTION = 28
    """
    Attributes for the **object_has_action** condition are:\n
    - unit_object
    - next_object
    - inverted
    - unit_ai_action
    """
    # Todo: Mark as 1.40 feature
    OR = 29
    """
    The **OR** condition does not have any attributes
    """
    # Todo: Mark as 1.40 feature
    AI_SIGNAL_MULTIPLAYER = 30
    """
    Attributes for the **ai_signal_multiplayer** condition are:\n
    - ai_signal
    - inverted
    """


condition_names = bidict({
    0: "none",
    1: "bring_object_to_area",
    2: "bring_object_to_object",
    3: "own_objects",
    4: "own_fewer_objects",
    5: "objects_in_area",
    6: "destroy_object",
    7: "capture_object",
    8: "accumulate_attribute",
    9: "research_technology",
    10: "timer",
    11: "object_selected",
    12: "ai_signal",
    13: "player_defeated",
    14: "object_has_target",
    15: "object_visible",
    16: "object_not_visible",
    17: "researching_tech",
    18: "units_garrisoned",
    19: "difficulty_level",
    20: "chance",
    21: "technology_state",
    22: "variable_value",
    23: "object_hp",
    24: "diplomacy_state",
    25: "script_call",
    26: "object_visible_multiplayer",
    27: "object_selected_multiplayer",
    28: "object_has_action",
    29: "or",
    30: "ai_signal_multiplayer"
})

empty_attributes = {
    "condition_type": -1,
    "amount_or_quantity": -1,
    "resource_type_or_tribute_list": -1,
    "unit_object": -1,
    "next_object": -1,
    "object_list": -1,
    "source_player": -1,
    "technology": -1,
    "timer": -1,
    "area_1_x": -1,
    "area_1_y": -1,
    "area_2_x": -1,
    "area_2_y": -1,
    "object_group": -1,
    "object_type": -1,
    "ai_signal": -1,
    "inverted": -1,
    "variable": -1,
    "comparison": -1,
    "target_player": -1,
    "unit_ai_action": -1,
    "xs_function": ""
}

default_attributes = {
    0: {
        "condition_type": 0,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": -1,
        "technology": -1,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": -1,
        "variable": -1,
        "comparison": -1,
        "target_player": -1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    8: {
        "condition_type": 8,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": 0,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": 1,
        "technology": -1,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": 0,
        "variable": -1,
        "comparison": -1,
        "target_player": -1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    12: {
        "condition_type": 12,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": -1,
        "technology": -1,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": 0,
        "inverted": 0,
        "variable": -1,
        "comparison": -1,
        "target_player": -1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    1: {
        "condition_type": 1,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": -1,
        "technology": -1,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": 0,
        "inverted": 0,
        "variable": -1,
        "comparison": -1,
        "target_player": -1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    2: {
        "condition_type": 2,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": -1,
        "technology": -1,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": 0,
        "variable": -1,
        "comparison": -1,
        "target_player": -1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    7: {
        "condition_type": 7,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": 1,
        "technology": -1,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": 0,
        "variable": -1,
        "comparison": -1,
        "target_player": -1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    20: {
        "condition_type": 20,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": 1,
        "technology": -1,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": 0,
        "variable": -1,
        "comparison": -1,
        "target_player": -1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    6: {
        "condition_type": 6,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": 1,
        "technology": -1,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": 0,
        "variable": -1,
        "comparison": -1,
        "target_player": -1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    19: {
        "condition_type": 19,
        "amount_or_quantity": 3,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": -1,
        "technology": -1,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": 0,
        "variable": -1,
        "comparison": -1,
        "target_player": -1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    24: {
        "condition_type": 24,
        "amount_or_quantity": 0,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": 1,
        "technology": -1,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": 0,
        "variable": -1,
        "comparison": -1,
        "target_player": 1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    14: {
        "condition_type": 14,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": 1,
        "technology": -1,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": 0,
        "variable": -1,
        "comparison": -1,
        "target_player": 1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    23: {
        "condition_type": 23,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": 1,
        "technology": -1,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": 0,
        "variable": -1,
        "comparison": 0,
        "target_player": 1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    16: {
        "condition_type": 16,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": 1,
        "technology": -1,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": 0,
        "variable": -1,
        "comparison": 0,
        "target_player": 1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    11: {
        "condition_type": 11,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": 1,
        "technology": -1,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": 0,
        "variable": -1,
        "comparison": 0,
        "target_player": 1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    15: {
        "condition_type": 15,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": 1,
        "technology": -1,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": 0,
        "variable": -1,
        "comparison": 0,
        "target_player": 1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    5: {
        "condition_type": 5,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": 1,
        "technology": -1,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": 0,
        "variable": -1,
        "comparison": 0,
        "target_player": 1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    4: {
        "condition_type": 4,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": 1,
        "technology": -1,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": 0,
        "variable": -1,
        "comparison": 0,
        "target_player": 1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    3: {
        "condition_type": 3,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": 1,
        "technology": -1,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": 0,
        "variable": -1,
        "comparison": 0,
        "target_player": 1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    13: {
        "condition_type": 13,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": 1,
        "technology": -1,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": 0,
        "variable": -1,
        "comparison": -1,
        "target_player": -1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    9: {
        "condition_type": 9,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": 1,
        "technology": 16,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": 0,
        "variable": -1,
        "comparison": -1,
        "target_player": -1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    17: {
        "condition_type": 17,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": 1,
        "technology": 16,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": 0,
        "variable": -1,
        "comparison": -1,
        "target_player": -1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    21: {
        "condition_type": 21,
        "amount_or_quantity": 3,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": 1,
        "technology": 16,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": 0,
        "variable": -1,
        "comparison": -1,
        "target_player": -1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    10: {
        "condition_type": 10,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": -1,
        "technology": -1,
        "timer": 10,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": 0,
        "variable": -1,
        "comparison": -1,
        "target_player": -1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    18: {
        "condition_type": 18,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": -1,
        "technology": -1,
        "timer": 10,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": 0,
        "variable": -1,
        "comparison": -1,
        "target_player": -1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    22: {
        "condition_type": 22,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": -1,
        "technology": -1,
        "timer": 10,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": 0,
        "variable": 0,
        "comparison": 0,
        "target_player": -1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    25: {
        "condition_type": 25,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": -1,
        "technology": -1,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": -1,
        "variable": -1,
        "comparison": -1,
        "target_player": -1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    26: {
        "condition_type": 26,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": 1,
        "technology": -1,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": 0,
        "variable": -1,
        "comparison": -1,
        "target_player": -1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    27: {
        "condition_type": 27,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": 1,
        "technology": -1,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": 0,
        "variable": -1,
        "comparison": -1,
        "target_player": -1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    28: {
        "condition_type": 28,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": -1,
        "technology": -1,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": 0,
        "variable": -1,
        "comparison": -1,
        "target_player": -1,
        "unit_ai_action": 0,
        "xs_function": ""
    },
    29: {
        "condition_type": 29,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": -1,
        "technology": -1,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": -1,
        "inverted": -1,
        "variable": -1,
        "comparison": -1,
        "target_player": -1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
    30: {
        "condition_type": 30,
        "amount_or_quantity": -1,
        "resource_type_or_tribute_list": -1,
        "unit_object": -1,
        "next_object": -1,
        "object_list": -1,
        "source_player": -1,
        "technology": -1,
        "timer": -1,
        "area_1_x": -1,
        "area_1_y": -1,
        "area_2_x": -1,
        "area_2_y": -1,
        "object_group": -1,
        "object_type": -1,
        "ai_signal": 0,
        "inverted": 0,
        "variable": -1,
        "comparison": -1,
        "target_player": -1,
        "unit_ai_action": -1,
        "xs_function": ""
    },
}

attributes = {
    0: [
        "condition_type",
    ],
    1: [
        "condition_type",
        "unit_object",
        "area_1_x",
        "area_1_y",
        "area_2_x",
        "area_2_y",
        "inverted",
    ],
    2: [
        "condition_type",
        "unit_object",
        "next_object",
        "inverted",
    ],
    3: [
        "condition_type",
        "amount_or_quantity",
        "object_list",
        "source_player",
        "object_group",
        "object_type",
    ],
    4: [
        "condition_type",
        "amount_or_quantity",
        "object_list",
        "source_player",
        "area_1_x",
        "area_1_y",
        "area_2_x",
        "area_2_y",
        "object_group",
        "object_type",
    ],
    5: [
        "condition_type",
        "amount_or_quantity",
        "object_list",
        "source_player",
        "area_1_x",
        "area_1_y",
        "area_2_x",
        "area_2_y",
        "object_group",
        "object_type",
        "inverted",
    ],
    6: [
        "condition_type",
        "unit_object",
        "inverted",
    ],
    7: [
        "condition_type",
        "unit_object",
        "source_player",
        "inverted",
    ],
    8: [
        "condition_type",
        "amount_or_quantity",
        "resource_type_or_tribute_list",
        "source_player",
        "inverted",
    ],
    9: [
        "condition_type",
        "source_player",
        "technology",
        "inverted",
    ],
    10: [
        "condition_type",
        "timer",
        "inverted",
    ],
    11: [
        "condition_type",
        "unit_object",
        "inverted",
    ],
    12: [
        "condition_type",
        "ai_signal",
        "inverted",
    ],
    13: [
        "condition_type",
        "source_player",
        "inverted",
    ],
    14: [
        "condition_type",
        "unit_object",
        "next_object",
        "object_list",
        "object_group",
        "object_type",
        "inverted",
    ],
    15: [
        "condition_type",
        "unit_object",
    ],
    16: [
        "condition_type",
        "unit_object",
    ],
    17: [
        "condition_type",
        "source_player",
        "technology",
        "inverted",
    ],
    18: [
        "condition_type",
        "amount_or_quantity",
        "unit_object",
        "inverted",
    ],
    19: [
        "condition_type",
        "amount_or_quantity",
        "inverted",
    ],
    20: [
        "condition_type",
        "amount_or_quantity",
    ],
    21: [
        "condition_type",
        "amount_or_quantity",
        "source_player",
        "technology",
        "inverted",
    ],
    22: [
        "condition_type",
        "amount_or_quantity",
        "inverted",
        "variable",
        "comparison",
    ],
    23: [
        "condition_type",
        "amount_or_quantity",
        "unit_object",
        "inverted",
        "comparison",
    ],
    24: [
        "condition_type",
        "amount_or_quantity",
        "source_player",
        "inverted",
        "target_player",
    ],
    25: [
        "xs_function"
    ],
    26: [
        "unit_object",
        "source_player",
        "inverted",
    ],
    27: [
        "unit_object",
        "source_player",
        "inverted",
    ],
    28: [
        "unit_object",
        "next_object",
        "inverted",
        "unit_ai_action",
    ],
    29: [],
    30: [
        "ai_signal",
        "inverted",
    ],
}

# for condition_id in range(0, 25):
#     try:
#         params = parameters[condition_id]
#         print("\"\"\"Attributes for the **xxxxx** condition are:\\n", end="")
#         for parameter in params:
#             if parameter is not "condition_type":
#                 print("\n-", parameter, end="")
#     except KeyError:
#         continue
#     print("\"\"\"")
