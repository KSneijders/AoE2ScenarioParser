import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from AoE2ScenarioParser.aoe2_scenario import AoE2Scenario

scenario = AoE2Scenario("../resources/maps/SavannahDE_grass.aoe2scenario")

# Check the elevation values of the scenario
print(scenario.map.dump_raw_data(['elevation']))

# Set the Savannah to be covered by a layer of grass
for tile in scenario.map.terrain_data:
    tile.layer = 0

# Hill of height 7 from [3,0] to [8,2]
scenario.map.create_hill(3, 0, 8, 2, 7)

scenario.map.save()

scenario.write_to_file("../resources/maps/SavannahDE_grass_hill.aoe2scenario")