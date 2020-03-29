from AoE2ScenarioParser.datasets import conditions, effects
from AoE2ScenarioParser.aoe2_scenario import AoE2Scenario

"""
These examples are just for show and quickly made because I needed them myself. Eventually there will be proper 
examples. Don't expect a lot.
"""

input_path = "..."
output_path = "..."

scenario = AoE2Scenario(input_path)
trigger_object = scenario.object_manager.get_trigger_object()
castle_age_trigger = trigger_object.get_trigger(37)

new_techs = [
    ["Long Swordsman", 4],
    ["Elite Skirmisher", 2],
    ["Crossbowman", 4],
    ["Pikeman", 1],
    ["Light Cavalry", 2],
    ["Eagle Warrior", 5],
    ["Squires", 1],
    ["Husbandry", 1.5],
    ["Chain Barding Armor", 3],
    ["Bodkin Arrow", 4],
    ["Chain Mail Armor", 6],
    ["Leather Archer Armor", 7],
    ["Iron Casting", 9],
    ["Arson", 10.5],
    ["Thumbring", 12],
    ["Ballistics", 15],
    ["Imperial Age", 18],
]

for new_trigger in new_techs:
    trigger_name = new_trigger[0]
    delay = int(new_trigger[1] * 60)
    seconds = str(int((new_trigger[1] % 1) * 60))
    delay_text = str(int(new_trigger[1] // 1)) + ":" + (seconds if len(seconds) == 2 else "0" + seconds)

    trigger = trigger_object.add_trigger(delay_text + " > " + trigger_name)
    trigger.set_enabled(0)

    condition = trigger.add_condition(conditions.timer)
    condition.set_timer(delay)

    effect = trigger.add_effect(effects.research_technology)
    effect.set_player_source(8)

    effect = castle_age_trigger.add_effect(effects.activate_trigger)
    effect.set_trigger_id(len(trigger_object.data_dict['trigger_data']) - 1)