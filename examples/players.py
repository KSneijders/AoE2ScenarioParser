import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from AoE2ScenarioParser.aoe2_scenario import AoE2Scenario

scenario = AoE2Scenario("../resources/maps/TwoUnits.aoe2scenario")

# We'll be toying with and modifying player 2
player = scenario.players[2]
print(player)

player.civilization = 23
player.player = 1
player.pop_limit = 100
player.color = 6
player.starting_age = 4

print(player)

scenario.write_to_file("../resources/maps/TwoUnits_change_player.aoe2scenario", log_reconstructing=True)