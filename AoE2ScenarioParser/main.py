import math
from itertools import product

from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.datasets.terrains import TerrainId
from AoE2ScenarioParser.helper.helper import xy_to_i
from AoE2ScenarioParser.local_config import folder_de
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

filename = "defend_gm"
scenario = AoE2DEScenario.from_file(f"{folder_de}{filename}.aoe2scenario")
tm, um, mm, xm = scenario.trigger_manager, scenario.unit_manager, scenario.map_manager, scenario.xs_manager

for index, t in enumerate(mm.terrain):
    print(index, t.index)

exit()

for p in PlayerId.all(True):
    um.units[p] = []

MAP_SIZE = mm.map_size
CENTER = math.floor(MAP_SIZE / 2)
MONUMENT_RANGE = 12
HALF_RANGE = math.floor(MONUMENT_RANGE / 2)

for x, y in product(range(MONUMENT_RANGE), range(MONUMENT_RANGE)):
    tile = mm.terrain[xy_to_i(CENTER + x - HALF_RANGE, CENTER + y - HALF_RANGE, MAP_SIZE)]

    if not (x in [0, MONUMENT_RANGE - 1] or y in [0, MONUMENT_RANGE - 1]):
        tile.terrain_id = TerrainId.ROAD
        tile.elevation = 1
    else:
        tile.layer = TerrainId.ROAD

units = um.get_units_in_area(CENTER - HALF_RANGE - 1, CENTER - HALF_RANGE - 1,
                             CENTER + HALF_RANGE + 1, CENTER + HALF_RANGE + 1)

for u in units:
    um.remove_unit(unit=u)

um.add_unit(
    PlayerId.GAIA,
    BuildingInfo.MONUMENT.ID,
    CENTER, CENTER
)

scenario.write_to_file(f"{folder_de}{filename}_written.aoe2scenario")
