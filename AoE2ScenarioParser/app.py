from AoE2ScenarioParser.aoe2_scenario import AoE2Scenario
from AoE2ScenarioParser.datasets import effects
from AoE2ScenarioParser.datasets import conditions

# Input:
#   Tiny Flat Grass
#   AllEffects
#   AllConditions
# Output:
#   generated_from_parsed

input_path = "C:\\Users\\Kerwin Sneijders\\Games\\Age of Empires 2 DE\\" \
             "76561198140740017\\resources\\_common\\scenario\\Tiny Flat Grass.aoe2scenario"
# output_path = "C:\\Users\\Kerwin Sneijders\\Games\\Age of Empires 2 DE\\" \
#               "76561198140740017\\resources\\_common\\scenario\\generated_from_parsed.aoe2scenario"

scenario = AoE2Scenario(input_path)
trigger_object = scenario.object_manager.get_triggers()

print(trigger_object.get_trigger_overview_as_string())

scenario.write_to_file(output_path)
