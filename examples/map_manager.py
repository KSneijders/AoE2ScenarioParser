import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from AoE2ScenarioParser.aoe2_scenario import AoE2Scenario

scenario = AoE2Scenario("../resources/maps/SavannahDE_grass.aoe2scenario")

# Check the elevation values of the scenario
print(scenario.map_manager.dump_raw_data(['layer']))

# Set the Savannah to be covered by a layer of grass
for tile in scenario.map_manager.terrain_data:
    tile.layer = 0

scenario.map_manager.save()

scenario.write_to_file("../resources/maps/SavannahDE_grass.aoe2scenario")