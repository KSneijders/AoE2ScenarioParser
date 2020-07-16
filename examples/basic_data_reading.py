import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from AoE2ScenarioParser.aoe2_scenario import AoE2Scenario

scenario = AoE2Scenario("../resources/maps/SavannahDE.aoe2scenario")

print("data_header:")
print(scenario.data_header.filename)
print(scenario.data_header.string_table_player_names)
print(scenario.data_header.player_data_1)
print(scenario.data_header.version)
# print(scenario.data_header_manager.player_names) # doesn't work

print("messages:")
print(scenario.messages.hints)
print(scenario.messages.victory)

print("cinematics:")
print(scenario.cinematics.ascii_victory)

print("background_image:")
print(scenario.background_image.ascii_filename)

print("global_victory:")
print(scenario.global_victory.conquest_required)
print(scenario.global_victory.required_score_for_score_victory)

print("diplomacy:")
print(scenario.diplomacy.per_player_diplomacy[0].stance_with_each_player)
# print(scenario.diplomacy.individual_victories) # doesn't work

print("options:")
print(scenario.options.per_player_number_of_disabled_buildings)