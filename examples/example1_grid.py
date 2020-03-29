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

trigger = trigger_object.add_trigger("Attack move 10x10 grid")
trigger.set_looping(1)
condition = trigger.add_condition(conditions.timer)
condition.set_timer(30)

map_width = 220
map_height = 220
middle = int(map_width/2)-1
step = int(map_width/10)

for x in range(0, map_width, step):
    for y in range(0, map_height, step):
        effect = trigger.add_effect(effects.attack_move)
        effect.set_player_source(8)
        effect.set_area_1_x(x)
        effect.set_area_1_y(y)
        effect.set_area_2_x(x + step - 1)
        effect.set_area_2_y(y + step - 1)
        effect.set_location_x(middle)
        effect.set_location_y(middle)

scenario.write_to_file(output_path)
