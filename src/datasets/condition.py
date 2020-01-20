none = 0
bring_object_to_area = 1
bring_object_to_object = 2
own_objects = 3
owh_fewer_objects = 4
object_in_area = 5
destroy_object = 6
capture_object = 7
accumulate_attribute = 8
research_technology = 9
timer = 10
object_selected = 11
ai_signal = 12
player_defeated = 13
object_has_target = 14
object_visible = 15
object_not_visible = 16
researching_tech = 17
units_garrisoned = 18
chance = 20
technology_state = 21
variable_value = 22
object_hp = 23
diplomacy_state = 24

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
