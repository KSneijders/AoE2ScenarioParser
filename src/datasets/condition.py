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

# Credits: Eti JS @ https://stackoverflow.com/a/58746861/7230293
naming_conversion.update(dict(map(reversed, naming_conversion.items())))

parameters = {
    0: [
        "Condition type",
    ],
    8: [
        "Condition type",
        "Amount (Quantity)",
        "Resource Type/Tribute list",
        "Player",
        "Inverted",
    ],
    12: [
        "Condition type",
        "AI Signal",
        "Inverted",
    ],
    1: [
        "Condition type",
        "Unit object",
        "Area 1 X",
        "Area 1 Y",
        "Area 2 X",
        "Area 2 Y",
        "Inverted",
    ],
    2: [
        "Condition type",
        "Unit object",
        "Next object",
        "Inverted",
    ],
    7: [
        "Condition type",
        "Unit object",
        "Player",
        "Inverted",
    ],
    20: [
        "Condition type",
        "Amount (Quantity)",
    ],
    6: [
        "Condition type",
        "Unit object",
        "Inverted",
    ],
    24: [
        "Condition type",
        "Amount (Quantity)",
        "Player",
        "Inverted",
        "Target player",
    ],
    14: [
        "Condition type",
        "Unit object",
        "Next object",
        "Object list",
        "Object Group",
        "Object Type",
        "Inverted",
    ],
    23: [
        "Condition type",
        "Amount (Quantity)",
        "Unit object",
        "Inverted",
        "Comparison",
    ],
    16: [
        "Condition type",
        "Unit object",
    ],
    11: [
        "Condition type",
        "Unit object",
        "Inverted",
    ],
    15: [
        "Condition type",
        "Unit object",
    ],
    5: [
        "Condition type",
        "Amount (Quantity)",
        "Object list",
        "Player",
        "Area 1 X",
        "Area 1 Y",
        "Area 2 X",
        "Area 2 Y",
        "Object Group",
        "Object Type",
        "Inverted",
    ],
    4: [
        "Condition type",
        "Amount (Quantity)",
        "Object list",
        "Player",
        "Area 1 X",
        "Area 1 Y",
        "Area 2 X",
        "Area 2 Y",
        "Object Group",
        "Object Type",
    ],
    3: [
        "Condition type",
        "Amount (Quantity)",
        "Object list",
        "Player",
        "Object Group",
        "Object Type",
    ],
    13: [
        "Condition type",
        "Player",
        "Inverted",
    ],
    9: [
        "Condition type",
        "Player",
        "Technology",
        "Inverted",
    ],
    17: [
        "Condition type",
        "Player",
        "Technology",
        "Inverted",
    ],
    21: [
        "Condition type",
        "Amount (Quantity)",
        "Player",
        "Technology",
        "Inverted",
    ],
    10: [
        "Condition type",
        "Timer",
        "Inverted",
    ],
    18: [
        "Condition type",
        "Amount (Quantity)",
        "Unit object",
        "Inverted",
    ],
    22: [
        "Condition type",
        "Amount (Quantity)",
        "Inverted",
        "Variable",
        "Comparison",
    ]
}