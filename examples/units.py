import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from AoE2ScenarioParser.aoe2_scenario import AoE2Scenario
from AoE2ScenarioParser.datasets.players import Player
from AoE2ScenarioParser.datasets.units import Unit

scenario = AoE2Scenario("../resources/maps/TwoUnits.aoe2scenario")
unit_manager = scenario.unit_manager

unit_manager.add_unit(Player.TWO, Unit.PALADIN, 20, 5)

print("Units of player 1:")
print(unit_manager.units[1])
# Wololo the blue paladin to red
unit_manager.change_ownership(unit_manager.units[1][0], Player.TWO)

print('\n')
print("All units:")
print(*unit_manager.get_all_units(), sep='\n')
# Remove the cow from Gaia
unit_manager.remove_unit(unit_manager.units[0][0])

print('\n')
print("Units in square [(0,0), (20,20)]")
print(*unit_manager.get_units_in_area(0,0,20,20), sep='\n')

scenario.write_to_file("../resources/maps/TwoUnits_mod.aoe2scenario", log_reconstructing=True)