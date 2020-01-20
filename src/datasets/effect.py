# All effects and their IDs
none = 0
"""Parameters for the **none** effect are: \n
... none... Just like Conditions... People these days... """
change_diplomacy = 1
"""Parameters for the **change_diplomacy** effect are: \n
- diplomacy
- player_source
- player_target"""
research_technology = 2
"""Parameters for the **research_technology** effect are: \n
- player_source
- technology
- force_research_technology"""
send_chat = 3
"""Parameters for the **send_chat** effect are: \n
- player_source
- string_id
- message
- sound_name"""
play_sound = 4
"""Parameters for the **play_sound** effect are: \n
- player_source
- location_x
- location_y
- sound_name"""
tribute = 5
"""Parameters for the **tribute** effect are: \n
- quantity
- tribute_list
- player_source
- player_target"""
unlock_gate = 6
"""Parameters for the **unlock_gate** effect are: \n
- number_of_units_selected
- selected_object_id"""
lock_gate = 7
"""Parameters for the **lock_gate** effect are: \n
- number_of_units_selected
- selected_object_id"""
activate_trigger = 8
"""Parameters for the **activate_trigger** effect are: \n
- trigger_id"""
deactivate_trigger = 9
"""Parameters for the **deactivate_trigger** effect are: \n
- trigger_id"""
create_object = 11
"""Parameters for the **create_object** effect are: \n
- object_list_unit_id
- player_source
- location_x
- location_y
- item_id
- facet"""
task_object = 12
"""Parameters for the **task_object** effect are: \n
- number_of_units_selected
- object_list_unit_id
- player_source
- location_x
- location_y
- area_1_x
- area_1_y
- area_2_x
- area_2_y
- object_group
- object_type
- selected_object_id"""
declare_victory = 13
"""Parameters for the **declare_victory** effect are: \n
- player_source
- enabled_or_victory"""
kill_object = 14
"""Parameters for the **kill_object** effect are: \n
- number_of_units_selected
- object_list_unit_id
- player_source
- area_1_x
- area_1_y
- area_2_x
- area_2_y
- object_group
- object_type
- selected_object_id"""
remove_object = 15
"""Parameters for the **remove_object** effect are: \n
- number_of_units_selected
- object_list_unit_id
- player_source
- area_1_x
- area_1_y
- area_2_x
- area_2_y
- object_group
- object_type
- selected_object_id"""
change_view = 16
"""Parameters for the **change_view** effect are: \n
- player_source
- location_x
- location_y
- scroll"""
unload = 17
"""Parameters for the **unload** effect are: \n
- number_of_units_selected
- object_list_unit_id
- player_source
- location_x
- location_y
- area_1_x
- area_1_y
- area_2_x
- area_2_y
- object_group
- object_type
- selected_object_id"""
change_ownership = 18
"""Parameters for the **change_ownership** effect are: \n
- number_of_units_selected
- object_list_unit_id
- player_source
- player_target
- area_1_x
- area_1_y
- area_2_x
- area_2_y
- object_group
- object_type
- flash_object
- selected_object_id"""
patrol = 19
"""Parameters for the **patrol** effect are: \n
- number_of_units_selected
- object_list_unit_id
- player_source
- location_x
- location_y
- area_1_x
- area_1_y
- area_2_x
- area_2_y
- object_group
- object_type
- selected_object_id"""
display_instructions = 20
"""Parameters for the **display_instructions** effect are: \n
- object_list_unit_id
- player_source
- string_id
- display_time
- instruction_panel_position
- play_sound
- message
- sound_name"""
clear_instructions = 21
"""Parameters for the **clear_instructions** effect are: \n
- instruction_panel_position"""
freeze_object = 22
"""Parameters for the **freeze_object** effect are: \n
- number_of_units_selected
- object_list_unit_id
- player_source
- area_1_x
- area_1_y
- area_2_x
- area_2_y
- object_group
- object_type
- selected_object_id"""
use_advanced_buttons = 23
"""Parameters for the **use_advanced_
damage_object = 24buttons** effect are: \n"""
"""Parameters for the **damage_object** effect are: \n
- quantity
- number_of_units_selected
- object_list_unit_id
- player_source
- area_1_x
- area_1_y
- area_2_x
- area_2_y
- object_group
- object_type
- selected_object_id"""
place_foundation = 25
"""Parameters for the **place_foundation** effect are: \n
- object_list_unit_id
- player_source
- location_x
- location_y"""
change_object_name = 26
"""Parameters for the **change_object_name** effect are: \n
- number_of_units_selected
- object_list_unit_id
- player_source
- string_id
- area_1_x
- area_1_y
- area_2_x
- area_2_y
- message
- selected_object_id"""
change_object_hp = 27
"""Parameters for the **change_object_hp** effect are: \n
- quantity
- number_of_units_selected
- object_list_unit_id
- player_source
- area_1_x
- area_1_y
- area_2_x
- area_2_y
- object_group
- object_type
- operation
- selected_object_id"""
change_object_attack = 28
"""Parameters for the **change_object_attack** effect are: \n
- aa_quantity
- aa_armor_or_attack_type
- number_of_units_selected
- object_list_unit_id
- player_source
- area_1_x
- area_1_y
- area_2_x
- area_2_y
- object_group
- object_type
- operation
- selected_object_id"""
stop_object = 29
"""Parameters for the **stop_object** effect are: \n
- number_of_units_selected
- object_list_unit_id
- player_source
- area_1_x
- area_1_y
- area_2_x
- area_2_y
- object_group
- object_type
- selected_object_id"""
attack_move = 30
"""Parameters for the **attack_move** effect are: \n
- number_of_units_selected
- object_list_unit_id
- player_source
- location_x
- location_y
- area_1_x
- area_1_y
- area_2_x
- area_2_y
- object_group
- object_type
- selected_object_id"""
change_object_armor = 31
"""Parameters for the **change_object_armor** effect are: \n
- aa_quantity
- aa_armor_or_attack_type
- number_of_units_selected
- object_list_unit_id
- player_source
- area_1_x
- area_1_y
- area_2_x
- area_2_y
- object_group
- object_type
- operation
- selected_object_id"""
change_object_range = 32
"""Parameters for the **change_object_range** effect are: \n
- quantity
- number_of_units_selected
- object_list_unit_id
- player_source
- area_1_x
- area_1_y
- area_2_x
- area_2_y
- object_group
- object_type
- operation
- selected_object_id"""
change_object_speed = 33
"""Parameters for the **change_object_speed** effect are: \n
- quantity
- number_of_units_selected
- object_list_unit_id
- player_source
- area_1_x
- area_1_y
- area_2_x
- area_2_y
- object_group
- object_type
- selected_object_id"""
heal_object = 34
"""Parameters for the **heal_object** effect are: \n
- quantity
- number_of_units_selected
- object_list_unit_id
- player_source
- area_1_x
- area_1_y
- area_2_x
- area_2_y
- object_group
- object_type
- selected_object_id"""
teleport_object = 35
"""Parameters for the **teleport_object** effect are: \n
- number_of_units_selected
- object_list_unit_id
- player_source
- location_x
- location_y
- area_1_x
- area_1_y
- area_2_x
- area_2_y
- object_group
- object_type
- selected_object_id"""
change_object_stance = 36
"""Parameters for the **change_object_stance** effect are: \n
- number_of_units_selected
- object_list_unit_id
- player_source
- area_1_x
- area_1_y
- area_2_x
- area_2_y
- object_group
- object_type
- attack_stance
- selected_object_id"""
display_timer = 37
"""Parameters for the **display_timer** effect are: \n
- string_id
- display_time
- time_unit
- variable_or_timer
- message"""
enable_disable_object = 38
"""Parameters for the **enable_disable_object** effect are: \n
- object_list_unit_id
- player_source
- enabled_or_victory
- item_id"""
enable_disable_technology = 39
"""Parameters for the **enable_disable_technology** effect are: \n
- player_source
- technology
- enabled_or_victory
- item_id"""
change_object_cost = 40
"""Parameters for the **change_object_cost** effect are: \n
- object_list_unit_id
- player_source
- food
- wood
- stone
- gold"""
set_player_visibility = 41
"""Parameters for the **set_player_visibility** effect are: \n
- player_source
- player_target
- visibility_state"""
change_object_icon = 42
"""Parameters for the **change_object_icon** effect are: \n
- number_of_units_selected
- object_list_unit_id
- player_source
- area_1_x
- area_1_y
- area_2_x
- area_2_y
- object_group
- object_type
- object_list_unit_id_2
- selected_object_id"""
replace_object = 43
"""Parameters for the **replace_object** effect are: \n
- number_of_units_selected
- object_list_unit_id
- player_source
- player_target
- area_1_x
- area_1_y
- area_2_x
- area_2_y
- object_group
- object_type
- object_list_unit_id_2
- selected_object_id"""
change_object_description = 44
"""Parameters for the **change_object_description** effect are: \n
- object_list_unit_id
- player_source
- string_id
- message"""
change_player_name = 45
"""Parameters for the **change_player_name** effect are: \n
- player_source
- string_id
- message"""
change_train_location = 46
"""Parameters for the **change_train_location** effect are: \n
- object_list_unit_id
- player_source
- object_list_unit_id_2
- button_location"""
change_research_location = 47
"""Parameters for the **change_research_location** effect are: \n
- player_source
- technology
- object_list_unit_id_2
- button_location"""
change_civilization_name = 48
"""Parameters for the **change_civilization_name** effect are: \n
- player_source
- string_id
- message"""
create_garrisoned_object = 49
"""Parameters for the **create_garrisoned_object** effect are: \n
- number_of_units_selected
- object_list_unit_id
- player_source
- area_1_x
- area_1_y
- area_2_x
- area_2_y
- object_list_unit_id_2
- selected_object_id"""
acknowledge_ai_signal = 50
"""Parameters for the **acknowledge_ai_signal** effect are: \n
- ai_signal_value"""
modify_attribute = 51
"""Parameters for the **modify_attribute** effect are: \n
- quantity
- object_list_unit_id
- player_source
- item_id
- operation
- object_attributes"""
modify_resource = 52
"""Parameters for the **modify_resource** effect are: \n
- quantity
- tribute_list
- player_source
- item_id
- operation"""
modify_resource_by_variable = 53
"""Parameters for the **modify_resource_by_variable** effect are: \n
- tribute_list
- player_source
- item_id
- operation
- from_variable"""
change_variable = 56
"""Parameters for the **change_variable** effect are: \n
- quantity
- operation
- from_variable
- message"""
clear_timer = 57
"""Parameters for the **clear_timer** effect are: \n
- variable_or_timer"""

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

empty_parameters = {
    "effect_type": -1,
    "ai_script_goal": -1,
    "aa_quantity": -1,
    "aa_armor_or_attack_type": -1,
    "quantity": -1,
    "tribute_list": -1,
    "diplomacy": -1,
    "number_of_units_selected": -1,
    "object_list_unit_id": -1,
    "player_source": -1,
    "player_target": -1,
    "technology": -1,
    "string_id": -1,
    "display_time": -1,
    "trigger_id": -1,
    "location_x": -1,
    "location_y": -1,
    "area_1_x": -1,
    "area_1_y": -1,
    "area_2_x": -1,
    "area_2_y": -1,
    "object_group": -1,
    "object_type": -1,
    "instruction_panel_position": -1,
    "attack_stance": -1,
    "time_unit": -1,
    "enabled_or_victory": -1,
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
    "from_variable": -1,
    "variable_or_timer": -1,
    "facet": -1,
    "play_sound": -1,
    "message": '',
    "sound_name": '',
    "selected_object_id": -1,
}

# The parameters per trigger (trigger ID as dict key) identified by the retriever key
parameters = {
    0: [
        "effect_type",
    ],
    50: [
        "effect_type",
        "ai_signal_value",
    ],
    8: [
        "effect_type",
        "trigger_id",
    ],
    30: [
        "effect_type",
        "number_of_units_selected",
        "object_list_unit_id",
        "player_source",
        "location_x",
        "location_y",
        "area_1_x",
        "area_1_y",
        "area_2_x",
        "area_2_y",
        "object_group",
        "object_type",
        "selected_object_id",
    ],
    48: [
        "effect_type",
        "player_source",
        "string_id",
        "message",
    ],
    1: [
        "effect_type",
        "diplomacy",
        "player_source",
        "player_target",
    ],
    31: [
        "effect_type",
        "aa_quantity",
        "aa_armor_or_attack_type",
        "number_of_units_selected",
        "object_list_unit_id",
        "player_source",
        "area_1_x",
        "area_1_y",
        "area_2_x",
        "area_2_y",
        "object_group",
        "object_type",
        "operation",
        "selected_object_id",
    ],
    28: [
        "effect_type",
        "aa_quantity",
        "aa_armor_or_attack_type",
        "number_of_units_selected",
        "object_list_unit_id",
        "player_source",
        "area_1_x",
        "area_1_y",
        "area_2_x",
        "area_2_y",
        "object_group",
        "object_type",
        "operation",
        "selected_object_id",
    ],
    40: [
        "effect_type",
        "object_list_unit_id",
        "player_source",
        "food",
        "wood",
        "stone",
        "gold",
    ],
    44: [
        "effect_type",
        "object_list_unit_id",
        "player_source",
        "string_id",
        "message",
    ],
    27: [
        "effect_type",
        "quantity",
        "number_of_units_selected",
        "object_list_unit_id",
        "player_source",
        "area_1_x",
        "area_1_y",
        "area_2_x",
        "area_2_y",
        "object_group",
        "object_type",
        "operation",
        "selected_object_id",
    ],
    42: [
        "effect_type",
        "number_of_units_selected",
        "object_list_unit_id",
        "player_source",
        "area_1_x",
        "area_1_y",
        "area_2_x",
        "area_2_y",
        "object_group",
        "object_type",
        "object_list_unit_id_2",
        "selected_object_id",
    ],
    26: [
        "effect_type",
        "number_of_units_selected",
        "object_list_unit_id",
        "player_source",
        "string_id",
        "area_1_x",
        "area_1_y",
        "area_2_x",
        "area_2_y",
        "message",
        "selected_object_id",
    ],
    32: [
        "effect_type",
        "quantity",
        "number_of_units_selected",
        "object_list_unit_id",
        "player_source",
        "area_1_x",
        "area_1_y",
        "area_2_x",
        "area_2_y",
        "object_group",
        "object_type",
        "operation",
        "selected_object_id",
    ],
    33: [
        "effect_type",
        "quantity",
        "number_of_units_selected",
        "object_list_unit_id",
        "player_source",
        "area_1_x",
        "area_1_y",
        "area_2_x",
        "area_2_y",
        "object_group",
        "object_type",
        "selected_object_id",
    ],
    36: [
        "effect_type",
        "number_of_units_selected",
        "object_list_unit_id",
        "player_source",
        "area_1_x",
        "area_1_y",
        "area_2_x",
        "area_2_y",
        "object_group",
        "object_type",
        "attack_stance",
        "selected_object_id",
    ],
    18: [
        "effect_type",
        "number_of_units_selected",
        "object_list_unit_id",
        "player_source",
        "player_target",
        "area_1_x",
        "area_1_y",
        "area_2_x",
        "area_2_y",
        "object_group",
        "object_type",
        "flash_object",
        "selected_object_id",
    ],
    45: [
        "effect_type",
        "player_source",
        "string_id",
        "message",
    ],
    47: [
        "effect_type",
        "player_source",
        "technology",
        "object_list_unit_id_2",
        "button_location",
    ],
    46: [
        "effect_type",
        "object_list_unit_id",
        "player_source",
        "object_list_unit_id_2",
        "button_location",
    ],
    56: [
        "effect_type",
        "quantity",
        "operation",
        "from_variable",
        "message",
    ],
    16: [
        "effect_type",
        "player_source",
        "location_x",
        "location_y",
        "scroll",
    ],
    21: [
        "effect_type",
        "instruction_panel_position",
    ],
    57: [
        "effect_type",
        "variable_or_timer",
    ],
    49: [
        "effect_type",
        "number_of_units_selected",
        "object_list_unit_id",
        "player_source",
        "area_1_x",
        "area_1_y",
        "area_2_x",
        "area_2_y",
        "object_list_unit_id_2",
        "selected_object_id",
    ],
    11: [
        "effect_type",
        "object_list_unit_id",
        "player_source",
        "location_x",
        "location_y",
        "item_id",
        "facet",
    ],
    24: [
        "effect_type",
        "quantity",
        "number_of_units_selected",
        "object_list_unit_id",
        "player_source",
        "area_1_x",
        "area_1_y",
        "area_2_x",
        "area_2_y",
        "object_group",
        "object_type",
        "selected_object_id",
    ],
    9: [
        "effect_type",
        "trigger_id",
    ],
    13: [
        "effect_type",
        "player_source",
        "enabled_or_victory",
    ],
    20: [
        "effect_type",
        "object_list_unit_id",
        "player_source",
        "string_id",
        "display_time",
        "instruction_panel_position",
        "play_sound",
        "message",
        "sound_name",
    ],
    37: [
        "effect_type",
        "string_id",
        "display_time",
        "time_unit",
        "variable_or_timer",
        "message",
    ],
    38: [
        "effect_type",
        "object_list_unit_id",
        "player_source",
        "enabled_or_victory",
        "item_id",
    ],
    39: [
        "effect_type",
        "player_source",
        "technology",
        "enabled_or_victory",
        "item_id",
    ],
    22: [
        "effect_type",
        "number_of_units_selected",
        "object_list_unit_id",
        "player_source",
        "area_1_x",
        "area_1_y",
        "area_2_x",
        "area_2_y",
        "object_group",
        "object_type",
        "selected_object_id",
    ],
    34: [
        "effect_type",
        "quantity",
        "number_of_units_selected",
        "object_list_unit_id",
        "player_source",
        "area_1_x",
        "area_1_y",
        "area_2_x",
        "area_2_y",
        "object_group",
        "object_type",
        "selected_object_id",
    ],
    14: [
        "effect_type",
        "number_of_units_selected",
        "object_list_unit_id",
        "player_source",
        "area_1_x",
        "area_1_y",
        "area_2_x",
        "area_2_y",
        "object_group",
        "object_type",
        "selected_object_id",
    ],
    7: [
        "effect_type",
        "number_of_units_selected",
        "selected_object_id",
    ],
    51: [
        "effect_type",
        "quantity",
        "object_list_unit_id",
        "player_source",
        "item_id",
        "operation",
        "object_attributes",
    ],
    52: [
        "effect_type",
        "quantity",
        "tribute_list",
        "player_source",
        "item_id",
        "operation",
    ],
    53: [
        "effect_type",
        "tribute_list",
        "player_source",
        "item_id",
        "operation",
        "from_variable",
    ],
    19: [
        "effect_type",
        "number_of_units_selected",
        "object_list_unit_id",
        "player_source",
        "location_x",
        "location_y",
        "area_1_x",
        "area_1_y",
        "area_2_x",
        "area_2_y",
        "object_group",
        "object_type",
        "selected_object_id",
    ],
    25: [
        "effect_type",
        "object_list_unit_id",
        "player_source",
        "location_x",
        "location_y",
    ],
    4: [
        "effect_type",
        "player_source",
        "location_x",
        "location_y",
        "sound_name",
    ],
    15: [
        "effect_type",
        "number_of_units_selected",
        "object_list_unit_id",
        "player_source",
        "area_1_x",
        "area_1_y",
        "area_2_x",
        "area_2_y",
        "object_group",
        "object_type",
        "selected_object_id",
    ],
    43: [
        "effect_type",
        "number_of_units_selected",
        "object_list_unit_id",
        "player_source",
        "player_target",
        "area_1_x",
        "area_1_y",
        "area_2_x",
        "area_2_y",
        "object_group",
        "object_type",
        "object_list_unit_id_2",
        "selected_object_id",
    ],
    2: [
        "effect_type",
        "player_source",
        "technology",
        "force_research_technology",
    ],
    3: [
        "effect_type",
        "player_source",
        "string_id",
        "message",
        "sound_name",
    ],
    41: [
        "effect_type",
        "player_source",
        "player_target",
        "visibility_state",
    ],
    29: [
        "effect_type",
        "number_of_units_selected",
        "object_list_unit_id",
        "player_source",
        "area_1_x",
        "area_1_y",
        "area_2_x",
        "area_2_y",
        "object_group",
        "object_type",
        "selected_object_id",
    ],
    12: [
        "effect_type",
        "number_of_units_selected",
        "object_list_unit_id",
        "player_source",
        "location_x",
        "location_y",
        "area_1_x",
        "area_1_y",
        "area_2_x",
        "area_2_y",
        "object_group",
        "object_type",
        "selected_object_id",
    ],
    35: [
        "effect_type",
        "number_of_units_selected",
        "object_list_unit_id",
        "player_source",
        "location_x",
        "location_y",
        "area_1_x",
        "area_1_y",
        "area_2_x",
        "area_2_y",
        "object_group",
        "object_type",
        "selected_object_id",
    ],
    5: [
        "effect_type",
        "quantity",
        "tribute_list",
        "player_source",
        "player_target",
    ],
    17: [
        "effect_type",
        "number_of_units_selected",
        "object_list_unit_id",
        "player_source",
        "location_x",
        "location_y",
        "area_1_x",
        "area_1_y",
        "area_2_x",
        "area_2_y",
        "object_group",
        "object_type",
        "selected_object_id",
    ],
    6: [
        "effect_type",
        "number_of_units_selected",
        "selected_object_id",
    ],
    23: [
        "effect_type",
    ]
}

# for effect_id in range(0, 58):
#     try:
#         params = parameters[effect_id]
#         print("\"\"\"Parameters for the **xxxxx** effect are: \\n", end="")
#         for parameter in params:
#             if parameter is not "effect_type":
#                 print("\n-", parameter, end="")
#     except KeyError:
#         continue
#     print("\"\"\"")
