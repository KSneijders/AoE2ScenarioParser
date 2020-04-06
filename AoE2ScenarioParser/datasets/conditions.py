none = 0
"""Attributes for the **none**  condition are:\n
... It's called none... What parameters do **you** think it has?! ❤ """
bring_object_to_area = 1
"""Attributes for the **bring_object_to_area** condition are:\n
- unit_object  
- area_1_x
- area_1_y
- area_2_x
- area_2_y
- inverted"""
bring_object_to_object = 2
"""Attributes for the **bring_object_to_object** condition are:\n
- unit_object
- next_object
- inverted"""
own_objects = 3
"""Attributes for the **own_objects** condition are:\n
- amount_or_quantity
- object_list
- player
- object_group
- object_type"""
owh_fewer_objects = 4
"""Attributes for the **owh_fewer_objects** condition are:\n
- amount_or_quantity
- object_list
- player
- area_1_x
- area_1_y
- area_2_x
- area_2_y
- object_group
- object_type"""
object_in_area = 5
"""Attributes for the **object_in_area** condition are:\n
- amount_or_quantity
- object_list
- player
- area_1_x
- area_1_y
- area_2_x
- area_2_y
- object_group
- object_type
- inverted"""
destroy_object = 6
"""Attributes for the **destroy_object** condition are:\n
- unit_object
- inverted"""
capture_object = 7
"""Attributes for the **capture_object** condition are:\n
- unit_object
- player
- inverted"""
accumulate_attribute = 8
"""Attributes for the **accumulate_attribute** condition are:\n
- amount_or_quantity
- resource_type_or_tribute_list
- player
- inverted"""
research_technology = 9
"""Attributes for the **research_technology** condition are:\n
- player
- technology
- inverted"""
timer = 10
"""Attributes for the **timer** condition are:\n
- timer
- inverted"""
object_selected = 11
"""Attributes for the **object_selected** condition are:\n
- unit_object
- inverted"""
ai_signal = 12
"""Attributes for the **ai_signal** condition are:\n
- ai_signal
- inverted"""
player_defeated = 13
"""Attributes for the **player_defeated** condition are:\n
- player
- inverted"""
object_has_target = 14
"""Attributes for the **object_has_target** condition are:\n
- unit_object
- next_object
- object_list
- object_group
- object_type
- inverted"""
object_visible = 15
"""Attributes for the **object_visible** condition are:\n
- unit_object"""
object_not_visible = 16
"""Attributes for the **object_not_visible** condition are:\n
- unit_object"""
researching_tech = 17
"""Attributes for the **researching_tech** condition are:\n
- player
- technology
- inverted"""
units_garrisoned = 18
"""Attributes for the **units_garrisoned** condition are:\n
- amount_or_quantity
- unit_object
- inverted"""
chance = 20
"""Attributes for the **chance** condition are:\n
- amount_or_quantity"""
technology_state = 21
"""Attributes for the **technology_state** condition are:\n
- amount_or_quantity
- player
- technology
- inverted"""
variable_value = 22
"""Attributes for the **variable_value** condition are:\n
- amount_or_quantity
- inverted
- variable
- comparison"""
object_hp = 23
"""Attributes for the **object_hp** condition are:\n
- amount_or_quantity
- unit_object
- inverted
- comparison"""
diplomacy_state = 24
"""Attributes for the **diplomacy_state** condition are:\n
- amount_or_quantity
- player
- inverted
- target_player"""

# attribute_naming_conversion = {
#     "condition_type": "Condition type",
#     "amount_or_quantity": "Amount (Quantity)",
#     "resource_type_or_tribute_list": "Resource Type/Tribute list",
#     "unit_object": "Unit object",
#     "next_object": "Next object",
#     "object_list": "Object list",
#     "player": "Player",
#     "technology": "Technology",
#     "timer": "Timer",
#     "area_1_x": "Area 1 X",
#     "area_1_y": "Area 1 Y",
#     "area_2_x": "Area 2 X",
#     "area_2_y": "Area 2 Y",
#     "object_group": "Object Group",
#     "object_type": "Object Type",
#     "ai_signal": "AI Signal",
#     "inverted": "Inverted",
#     "variable": "Variable",
#     "comparison": "Comparison",
#     "target_player": "Target player",
# }

identifier_conversion = {
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
    20: "chance",
    21: "technology_state",
    22: "variable_value",
    23: "object_hp",
    24: "diplomacy_state",
}

# Credits: Eti JS @ https://stackoverflow.com/a/58746861/7230293
# attribute_naming_conversion.update(dict(map(reversed, attribute_naming_conversion.items())))
identifier_conversion.update(dict(map(reversed, identifier_conversion.items())))

empty_attributes = {
    "condition_type": -1,
    "amount_or_quantity": -1,
    "resource_type_or_tribute_list": -1,
    "unit_object": -1,
    "next_object": -1,
    "object_list": -1,
    "player": -1,
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
}

attributes = {
    0: [
        "condition_type",
    ],
    8: [
        "condition_type",
        "amount_or_quantity",
        "resource_type_or_tribute_list",
        "player",
        "inverted",
    ],
    12: [
        "condition_type",
        "ai_signal",
        "inverted",
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
    7: [
        "condition_type",
        "unit_object",
        "player",
        "inverted",
    ],
    20: [
        "condition_type",
        "amount_or_quantity",
    ],
    6: [
        "condition_type",
        "unit_object",
        "inverted",
    ],
    24: [
        "condition_type",
        "amount_or_quantity",
        "player",
        "inverted",
        "target_player",
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
    23: [
        "condition_type",
        "amount_or_quantity",
        "unit_object",
        "inverted",
        "comparison",
    ],
    16: [
        "condition_type",
        "unit_object",
    ],
    11: [
        "condition_type",
        "unit_object",
        "inverted",
    ],
    15: [
        "condition_type",
        "unit_object",
    ],
    5: [
        "condition_type",
        "amount_or_quantity",
        "object_list",
        "player",
        "area_1_x",
        "area_1_y",
        "area_2_x",
        "area_2_y",
        "object_group",
        "object_type",
        "inverted",
    ],
    4: [
        "condition_type",
        "amount_or_quantity",
        "object_list",
        "player",
        "area_1_x",
        "area_1_y",
        "area_2_x",
        "area_2_y",
        "object_group",
        "object_type",
    ],
    3: [
        "condition_type",
        "amount_or_quantity",
        "object_list",
        "player",
        "object_group",
        "object_type",
    ],
    13: [
        "condition_type",
        "player",
        "inverted",
    ],
    9: [
        "condition_type",
        "player",
        "technology",
        "inverted",
    ],
    17: [
        "condition_type",
        "player",
        "technology",
        "inverted",
    ],
    21: [
        "condition_type",
        "amount_or_quantity",
        "player",
        "technology",
        "inverted",
    ],
    10: [
        "condition_type",
        "timer",
        "inverted",
    ],
    18: [
        "condition_type",
        "amount_or_quantity",
        "unit_object",
        "inverted",
    ],
    22: [
        "condition_type",
        "amount_or_quantity",
        "inverted",
        "variable",
        "comparison",
    ]
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
