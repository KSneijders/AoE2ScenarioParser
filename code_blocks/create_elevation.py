from typing import List

from AoE2ScenarioParser.aoe2_scenario import AoE2Scenario
from AoE2ScenarioParser.datasets.terrains import Terrain
from AoE2ScenarioParser.pieces.structs.terrain import TerrainStruct

scenario_folder = "C:/Users/Kerwin Sneijders/Games/Age of Empires 2 DE/76561198140740017/resources/_common/scenario/"
read_file = scenario_folder + "test5.aoe2scenario"
write_to_file = scenario_folder + "test7.aoe2scenario"

scenario = AoE2Scenario.from_file(read_file)

scenario.unit_manager.remove_eye_candy()

max_height = 20

tiles: List[List[TerrainStruct]] = []
for x in range(0, 120):
    tiles.append([])
    for y in range(0, 120):
        tiles[x].append(TerrainStruct(data=[Terrain.WATER_DEEP, max_height, 0, b'\xff\xff\xff\xff']))

print(len(tiles))


for init_x in range(25, 30):
    for init_y in range(25, 30):
        initial_x = init_x
        initial_y = init_y
        for height in range(1, max_height + 1):
            for x in range(-height, height+1):
                for y in range(-height, height+1):
                    if abs((initial_x + x) - initial_x) == height or abs((initial_y + y) - initial_y) == height:
                        if tiles[initial_x + x][initial_y + y].retrievers[1].data < abs(height - max_height):
                            try:
                                tiles[initial_x + x][initial_y + y].retrievers[1].data = max_height - abs(height - max_height)
                                tiles[initial_x + x][initial_y + y].retrievers[0].data = Terrain.WATER_DEEP
                            except IndexError:
                                pass

scenario._parsed_data['MapPiece'].retrievers[11].data = [inner for outer in tiles for inner in outer]
scenario.write_to_file(write_to_file)
