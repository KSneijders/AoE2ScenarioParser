# All effects and their IDs
none = 0
change_diplomacy = 1
research_technology = 2
send_chat = 3
play_sound = 4
tribute = 5
unlock_gate = 6
lock_gate = 7
activate_trigger = 8
deactivate_trigger = 9
create_object = 11
task_object = 12
declare_victory = 13
kill_object = 14
remove_object = 15
change_view = 16
unload = 17
change_ownership = 18
patrol = 19
display_instructions = 20
clear_instructions = 21
freeze_object = 22
use_advanced_buttons = 23
damage_object = 24
place_foundation = 25
change_object_name = 26
change_object_hp = 27
change_object_attack = 28
stop_object = 29
attack_move = 30
change_object_armor = 31
change_object_range = 32
change_object_speed = 33
heal_object = 34
teleport_object = 35
change_object_stance = 36
display_timer = 37
enable_disable_object = 38
enable_disable_technology = 39
change_object_cost = 40
set_player_visibility = 41
change_object_icon = 42
replace_object = 43
change_object_description = 44
change_player_name = 45
change_train_location = 46
change_research_location = 47
change_civilization_name = 48
create_garrisoned_object = 49
acknowledge_ai_signal = 50
modify_attribute = 51
modify_resource = 52
modify_resource_by_variable = 53
change_variable = 56
clear_timer = 57

naming_conversion = {
    "effect_type": "Effect type",
    "ai_script_goal": "AI script goal",
    "quantity": "Quantity",
    "aa_armor_or_attack_type": "AA Armor/Attack Type",
    "aa_quantity": "AA Quantity",
    "tribute_list": "Tribute List",
    "diplomacy": "Diplomacy",
    "number_of_units_selected": "Number of units selected",
    "object_list_unit_id": "Object list unit ID",
    "player_source": "Player Source",
    "player_target": "Player Target",
    "technology": "Technology",
    "string_id": "String ID",
    "display_time": "Display Time (display instructions)",
    "trigger_id": "Trigger ID (activate/deactivate)",
    "location_x": "Location X",
    "location_y": "Location Y",
    "area_1_x": "Area 1 X",
    "area_1_y": "Area 1 Y",
    "area_2_x": "Area 2 X",
    "area_2_y": "Area 2 Y",
    "object_group": "Object Group",
    "object_type": "Object Type",
    "instruction_panel_position": "Instruction Panel Position",
    "attack_stance": "Attack Stance",
    "time_unit": "Time unit (second, minutes, years)",
    "enabled_or_victory": "Enabled/Victory",
    "food": "Food",
    "wood": "Wood",
    "stone": "Stone",
    "gold": "Gold",
    "item_id": "Item ID",
    "flash_object": "Flash Object",
    "force_research_technology": "Force Research Technology",
    "visibility_state": "Visibility State",
    "scroll": "Scroll (Set view)",
    "operation": "Operation",
    "object_list_unit_id_2": "Object list unit ID 2",
    "button_location": "Button Location",
    "ai_signal_value": "AI signal Value",
    "object_attributes": "Object attributes",
    "from_variable": "From Variable",
    "variable_or_timer": "Variable/Timer",
    "facet": "Facet",
    "play_sound": "Play Sound",
    "message": "Message",
    "sound_name": "Sound (event) name",
    "selected_object_id": "Selected Object(s) ID",
}

# Credits: Eti JS @ https://stackoverflow.com/a/58746861/7230293
naming_conversion.update(dict(map(reversed, naming_conversion.items())))
print(naming_conversion)

# The parameters per trigger (trigger ID as dict key) identified by the retriever key
parameters = {
    0: [],
    50: [
        "AI signal Value",
    ],
    8: [
        "Trigger ID (activate/deactivate)",
    ],
    30: [
        "Number of units selected",
        "Object list unit ID",
        "Player Source",
        "Location X",
        "Location Y",
        "Area 1 X",
        "Area 1 Y",
        "Area 2 X",
        "Area 2 Y",
        "Object Group",
        "Object Type",
        "Selected Object(s) ID",
    ],
    48: [
        "Player Source",
        "String ID",
        "Message",
    ],
    1: [
        "Diplomacy",
        "Player Source",
        "Player Target",
    ],
    31: [
        "AA Quantity",
        "AA Armor/Attack Type",
        "Number of units selected",
        "Object list unit ID",
        "Player Source",
        "Area 1 X",
        "Area 1 Y",
        "Area 2 X",
        "Area 2 Y",
        "Object Group",
        "Object Type",
        "Operation",
        "Selected Object(s) ID",
    ],
    28: [
        "AA Quantity",
        "AA Armor/Attack Type",
        "Number of units selected",
        "Object list unit ID",
        "Player Source",
        "Area 1 X",
        "Area 1 Y",
        "Area 2 X",
        "Area 2 Y",
        "Object Group",
        "Object Type",
        "Operation",
        "Selected Object(s) ID",
    ],
    40: [
        "Object list unit ID",
        "Player Source",
        "Food",
        "Wood",
        "Stone",
        "Gold",
    ],
    44: [
        "Object list unit ID",
        "Player Source",
        "String ID",
        "Message",
    ],
    27: [
        "Quantity",
        "Number of units selected",
        "Object list unit ID",
        "Player Source",
        "Area 1 X",
        "Area 1 Y",
        "Area 2 X",
        "Area 2 Y",
        "Object Group",
        "Object Type",
        "Operation",
        "Selected Object(s) ID",
    ],
    42: [
        "Number of units selected",
        "Object list unit ID",
        "Player Source",
        "Area 1 X",
        "Area 1 Y",
        "Area 2 X",
        "Area 2 Y",
        "Object Group",
        "Object Type",
        "Object list unit ID 2",
        "Selected Object(s) ID",
    ],
    26: [
        "Number of units selected",
        "Object list unit ID",
        "Player Source",
        "String ID",
        "Area 1 X",
        "Area 1 Y",
        "Area 2 X",
        "Area 2 Y",
        "Message",
        "Selected Object(s) ID",
    ],
    32: [
        "Quantity",
        "Number of units selected",
        "Object list unit ID",
        "Player Source",
        "Area 1 X",
        "Area 1 Y",
        "Area 2 X",
        "Area 2 Y",
        "Object Group",
        "Object Type",
        "Operation",
        "Selected Object(s) ID",
    ],
    33: [
        "Quantity",
        "Number of units selected",
        "Object list unit ID",
        "Player Source",
        "Area 1 X",
        "Area 1 Y",
        "Area 2 X",
        "Area 2 Y",
        "Object Group",
        "Object Type",
        "Selected Object(s) ID",
    ],
    36: [
        "Number of units selected",
        "Object list unit ID",
        "Player Source",
        "Area 1 X",
        "Area 1 Y",
        "Area 2 X",
        "Area 2 Y",
        "Object Group",
        "Object Type",
        "Attack Stance",
        "Selected Object(s) ID",
    ],
    18: [
        "Number of units selected",
        "Object list unit ID",
        "Player Source",
        "Player Target",
        "Area 1 X",
        "Area 1 Y",
        "Area 2 X",
        "Area 2 Y",
        "Object Group",
        "Object Type",
        "Flash Object",
        "Selected Object(s) ID",
    ],
    45: [
        "Player Source",
        "String ID",
        "Message",
    ],
    47: [
        "Player Source",
        "Technology",
        "Object list unit ID 2",
        "Button Location",
    ],
    46: [
        "Object list unit ID",
        "Player Source",
        "Object list unit ID 2",
        "Button Location",
    ],
    56: [
        "Quantity",
        "Operation",
        "From Variable",
        "Message",
    ],
    16: [
        "Player Source",
        "Location X",
        "Location Y",
        "Scroll (Set view)",
    ],
    21: [
        "Instruction Panel Position",
    ],
    57: [
        "Variable/Timer",
    ],
    49: [
        "Number of units selected",
        "Object list unit ID",
        "Player Source",
        "Area 1 X",
        "Area 1 Y",
        "Area 2 X",
        "Area 2 Y",
        "Object list unit ID 2",
        "Selected Object(s) ID",
    ],
    11: [
        "Object list unit ID",
        "Player Source",
        "Location X",
        "Location Y",
        "Item ID",
        "Facet",
    ],
    24: [
        "Quantity",
        "Number of units selected",
        "Object list unit ID",
        "Player Source",
        "Area 1 X",
        "Area 1 Y",
        "Area 2 X",
        "Area 2 Y",
        "Object Group",
        "Object Type",
        "Selected Object(s) ID",
    ],
    9: [
        "Trigger ID (activate/deactivate)",
    ],
    13: [
        "Player Source",
        "Enabled/Victory",
    ],
    20: [
        "Object list unit ID",
        "Player Source",
        "String ID",
        "Display Time (display instructions)",
        "Instruction Panel Position",
        "Play Sound",
        "Message",
        "Sound (event) name",
    ],
    37: [
        "String ID",
        "Display Time (display instructions)",
        "Time unit (second, minutes, years)",
        "Variable/Timer",
        "Message",
    ],
    38: [
        "Object list unit ID",
        "Player Source",
        "Enabled/Victory",
        "Item ID",
    ],
    39: [
        "Player Source",
        "Technology",
        "Enabled/Victory",
        "Item ID",
    ],
    22: [
        "Number of units selected",
        "Object list unit ID",
        "Player Source",
        "Area 1 X",
        "Area 1 Y",
        "Area 2 X",
        "Area 2 Y",
        "Object Group",
        "Object Type",
        "Selected Object(s) ID",
    ],
    34: [
        "Quantity",
        "Number of units selected",
        "Object list unit ID",
        "Player Source",
        "Area 1 X",
        "Area 1 Y",
        "Area 2 X",
        "Area 2 Y",
        "Object Group",
        "Object Type",
        "Selected Object(s) ID",
    ],
    14: [
        "Number of units selected",
        "Object list unit ID",
        "Player Source",
        "Area 1 X",
        "Area 1 Y",
        "Area 2 X",
        "Area 2 Y",
        "Object Group",
        "Object Type",
        "Selected Object(s) ID",
    ],
    7: [
        "Number of units selected",
        "Selected Object(s) ID",
    ],
    51: [
        "Quantity",
        "Object list unit ID",
        "Player Source",
        "Item ID",
        "Operation",
        "Object attributes",
    ],
    52: [
        "Quantity",
        "Tribute List",
        "Player Source",
        "Item ID",
        "Operation",
    ],
    53: [
        "Tribute List",
        "Player Source",
        "Item ID",
        "Operation",
        "From Variable",
    ],
    19: [
        "Number of units selected",
        "Object list unit ID",
        "Player Source",
        "Location X",
        "Location Y",
        "Area 1 X",
        "Area 1 Y",
        "Area 2 X",
        "Area 2 Y",
        "Object Group",
        "Object Type",
        "Selected Object(s) ID",
    ],
    25: [
        "Object list unit ID",
        "Player Source",
        "Location X",
        "Location Y",
    ],
    4: [
        "Player Source",
        "Location X",
        "Location Y",
        "Sound (event) name",
    ],
    15: [
        "Number of units selected",
        "Object list unit ID",
        "Player Source",
        "Area 1 X",
        "Area 1 Y",
        "Area 2 X",
        "Area 2 Y",
        "Object Group",
        "Object Type",
        "Selected Object(s) ID",
    ],
    43: [
        "Number of units selected",
        "Object list unit ID",
        "Player Source",
        "Player Target",
        "Area 1 X",
        "Area 1 Y",
        "Area 2 X",
        "Area 2 Y",
        "Object Group",
        "Object Type",
        "Object list unit ID 2",
        "Selected Object(s) ID",
    ],
    2: [
        "Player Source",
        "Technology",
        "Force Research Technology",
    ],
    3: [
        "Player Source",
        "String ID",
        "Message",
        "Sound (event) name",
    ],
    41: [
        "Player Source",
        "Player Target",
        "Visibility State",
    ],
    29: [
        "Number of units selected",
        "Object list unit ID",
        "Player Source",
        "Area 1 X",
        "Area 1 Y",
        "Area 2 X",
        "Area 2 Y",
        "Object Group",
        "Object Type",
        "Selected Object(s) ID",
    ],
    12: [
        "Number of units selected",
        "Object list unit ID",
        "Player Source",
        "Location X",
        "Location Y",
        "Area 1 X",
        "Area 1 Y",
        "Area 2 X",
        "Area 2 Y",
        "Object Group",
        "Object Type",
        "Selected Object(s) ID",
    ],
    35: [
        "Number of units selected",
        "Object list unit ID",
        "Player Source",
        "Location X",
        "Location Y",
        "Area 1 X",
        "Area 1 Y",
        "Area 2 X",
        "Area 2 Y",
        "Object Group",
        "Object Type",
        "Selected Object(s) ID",
    ],
    5: [
        "Quantity",
        "Tribute List",
        "Player Source",
        "Player Target",
    ],
    17: [
        "Number of units selected",
        "Object list unit ID",
        "Player Source",
        "Location X",
        "Location Y",
        "Area 1 X",
        "Area 1 Y",
        "Area 2 X",
        "Area 2 Y",
        "Object Group",
        "Object Type",
        "Selected Object(s) ID",
    ],
    6: [
        "Number of units selected",
        "Selected Object(s) ID",
    ],
    23: [
    ]
}