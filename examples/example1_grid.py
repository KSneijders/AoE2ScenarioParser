from AoE2ScenarioParser.datasets import conditions, effects
from AoE2ScenarioParser.aoe2_scenario import AoE2Scenario

input_path = "..."
output_path = "..."

scenario = AoE2Scenario(input_path)
trigger_object = scenario.object_manager.get_triggers()

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
        target = (-1, -1)
        if abs(x - middle) >= abs(y - middle):
            additionX = (step if x < middle else -step) + (step-1 if x < middle else 0)
            additionY = (step-1 if y < middle else 0)
            target = (x + additionX, y + additionY)
        if abs(x - middle) <= abs(y - middle):
            additionX = (step-1 if x < middle else 0)
            additionY = (step if y < middle else -step) + (step-1 if y < middle else 0)
            target = (x + additionX, y + additionY)

        effect = trigger.add_effect(effects.attack_move)
        effect.set_player_source(8)
        effect.set_area_1_x(x)
        effect.set_area_1_y(y)
        effect.set_area_2_x(x + step - 1)
        effect.set_area_2_y(y + step - 1)
        effect.set_location_x(target[0])
        effect.set_location_y(target[1])

scenario.write_to_file(output_path)
