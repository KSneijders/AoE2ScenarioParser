none = 0
"""Parameters for the **none**  condition are:\n
... It's called none... What parameters do **you** think it has?! ❤ """
bring_object_to_area = 1
"""Parameters for the **bring_object_to_area** condition are:\n
- unit_object  
- area_1_x
- area_1_y
- area_2_x
- area_2_y
- inverted"""
bring_object_to_object = 2
"""Parameters for the **bring_object_to_object** condition are:\n
- unit_object
- next_object
- inverted"""
own_objects = 3
"""Parameters for the **own_objects** condition are:\n
- amount_or_quantity
- object_list
- player
- object_group
- object_type"""
owh_fewer_objects = 4
"""Parameters for the **owh_fewer_objects** condition are:\n
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
"""Parameters for the **object_in_area** condition are:\n
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
"""Parameters for the **destroy_object** condition are:\n
- unit_object
- inverted"""
capture_object = 7
"""Parameters for the **capture_object** condition are:\n
- unit_object
- player
- inverted"""
accumulate_attribute = 8
"""Parameters for the **accumulate_attribute** condition are:\n
- amount_or_quantity
- resource_type_or_tribute_list
- player
- inverted"""
research_technology = 9
"""Parameters for the **research_technology** condition are:\n
- player
- technology
- inverted"""
timer = 10
"""Parameters for the **timer** condition are:\n
- timer
- inverted"""
object_selected = 11
"""Parameters for the **object_selected** condition are:\n
- unit_object
- inverted"""
ai_signal = 12
"""Parameters for the **ai_signal** condition are:\n
- ai_signal
- inverted"""
player_defeated = 13
"""Parameters for the **player_defeated** condition are:\n
- player
- inverted"""
object_has_target = 14
"""Parameters for the **object_has_target** condition are:\n
- unit_object
- next_object
- object_list
- object_group
- object_type
- inverted"""
object_visible = 15
"""Parameters for the **object_visible** condition are:\n
- unit_object"""
object_not_visible = 16
"""Parameters for the **object_not_visible** condition are:\n
- unit_object"""
researching_tech = 17
"""Parameters for the **researching_tech** condition are:\n
- player
- technology
- inverted"""
units_garrisoned = 18
"""Parameters for the **units_garrisoned** condition are:\n
- amount_or_quantity
- unit_object
- inverted"""
chance = 20
"""Parameters for the **chance** condition are:\n
- amount_or_quantity"""
technology_state = 21
"""Parameters for the **technology_state** condition are:\n
- amount_or_quantity
- player
- technology
- inverted"""
variable_value = 22
"""Parameters for the **variable_value** condition are:\n
- amount_or_quantity
- inverted
- variable
- comparison"""
object_hp = 23
"""Parameters for the **object_hp** condition are:\n
- amount_or_quantity
- unit_object
- inverted
- comparison"""
diplomacy_state = 24
"""Parameters for the **diplomacy_state** condition are:\n
- amount_or_quantity
- player
- inverted
- target_player"""

naming_conversion = {
    "condition_type": "Condition type",
    "amount_or_quantity": "Amount (Quantity)",
    "resource_type_or_tribute_list": "Resource Type/Tribute list",
    "unit_object": "Unit object",
    "next_object": "Next object",
    "object_list": "Object list",
    "player": "Player",
    "technology": "Technology",
    "timer": "Timer",
    "area_1_x": "Area 1 X",
    "area_1_y": "Area 1 Y",
    "area_2_x": "Area 2 X",
    "area_2_y": "Area 2 Y",
    "object_group": "Object Group",
    "object_type": "Object Type",
    "ai_signal": "AI Signal",
    "inverted": "Inverted",
    "variable": "Variable",
    "comparison": "Comparison",
    "target_player": "Target player",
}

# Credits: Eti JS @ https://stackoverflow.com/a/58746861/7230293
naming_conversion.update(dict(map(reversed, naming_conversion.items())))

empty_parameters = {
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

parameters = {
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
#         print("\"\"\"Parameters for the **xxxxx** condition are:\\n", end="")
#         for parameter in params:
#             if parameter is not "condition_type":
#                 print("\n-", parameter, end="")
#     except KeyError:
#         continue
#     print("\"\"\"")
