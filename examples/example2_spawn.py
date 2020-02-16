from AoE2ScenarioParser.datasets import conditions, effects
from AoE2ScenarioParser.aoe2_scenario import AoE2Scenario

"""Reordering Display Order"""
input_path = "..."
output_path = "..."

scenario = AoE2Scenario(input_path)
trigger_object = scenario.object_manager.get_triggers()

add_after = 38
move_all_from_x_to_end = 57

tdo = trigger_object.data_dict['trigger_display_order']
added_len = len(tdo[tdo.index(move_all_from_x_to_end):])
tdo[tdo.index(add_after)+1:tdo.index(add_after)+1] = tdo[move_all_from_x_to_end:]
trigger_object.data_dict['trigger_display_order'] = tdo[0:-added_len]

scenario.write_to_file(output_path)


"""Adding unit spawn triggers"""
input_path = "..."
output_path = "..."

scenario = AoE2Scenario(input_path)
trigger_object = scenario.object_manager.get_triggers()

# Disable all current spawn triggers
to_be_disabled = [25, 30, 31, 21, 16, 26, 27]
castle_age_trigger = trigger_object.get_trigger(37)

for x in to_be_disabled:
    effect = castle_age_trigger.add_effect(effects.deactivate_trigger)
    effect.set_trigger_id(x)

trigger = trigger_object.add_trigger("__Castle Age__")
trigger.set_enabled(0)

"""Name, delay, spawn speed, chance"""
new_triggers = [
    ["Long Swordsman", 0, 10, 100],
    ["Elite Skirmisher", 0, 20, 100],
    ["Petard", 0, 60, 100],
    ["Crossbowman", 0, 8, 100],
    ["Pikeman", 0, 6, 100],
    ["Light Cavalry", 0, 30, 100],
    ["Eagle Warrior", 0, 15, 100],
    ["Knight", 0, 20, 100],
    ["Cavalry Archer", 0, 30, 100],
    ["Camel Rider", 0, 20, 100],
    ["Battle Elephant", 4, 30, 50],
    ["Scorpion", 0, 30, 50],
    ["Battle Ram", 0, 20, 50],
    ["Mangonel", 6, 30, 50],
]

for trigger_info in new_triggers:
    unit = trigger_info[0]
    delay = trigger_info[1] * 60
    spawn_speed = trigger_info[2]
    chance = trigger_info[3]
    chance_text = (", " + str(chance) + "%" if chance != 100 else "")
    trigger = trigger_object.add_trigger(str(spawn_speed) + chance_text + " > Spawn " + unit)

    trigger.set_enabled(0)
    trigger.set_looping(1)

    condition = trigger.add_condition(conditions.timer)
    condition.set_timer(spawn_speed)

    if chance != 100:
        condition = trigger.add_condition(conditions.chance)
        condition.set_amount_or_quantity(chance)

    effect = trigger.add_effect(effects.create_object)
    effect.set_player_source(8)

    if delay != 0:
        trigger = trigger_object.add_trigger("Activate: 'Spawn " + unit + "'")
        trigger.set_enabled(0)

        condition = trigger.add_condition(conditions.timer)
        condition.set_timer(delay)
        effect = trigger.add_effect(effects.activate_trigger)
        effect.set_trigger_id(len(trigger_object.data_dict['trigger_data']) - 2)

    effect = castle_age_trigger.add_effect(effects.activate_trigger)
    effect.set_trigger_id(len(trigger_object.data_dict['trigger_data']) - 1)

