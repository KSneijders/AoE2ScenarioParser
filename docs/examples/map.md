# Map Examples

### Change terrain in an area

```py
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.terrains import TerrainId

scenario = AoE2DEScenario.from_file("your_scenario.aoe2scenario")
map_manager = scenario.map_manager

for tile in map_manager.get_square_1d(x1=0, y1=0, x2=20, y2=20):
    tile.terrain_id = TerrainId.BEACH

scenario.write_to_file("your_scenario_output.aoe2scenario")
```

---

### Set elevation in an area

```py
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

scenario = AoE2DEScenario.from_file("your_scenario.aoe2scenario")
map_manager = scenario.map_manager

# Creates a hill — surrounding terrain adjusts automatically
map_manager.set_elevation(elevation=4, x1=10, y1=10, x2=20, y2=20)

scenario.write_to_file("your_scenario_output.aoe2scenario")
```

---

### Resize the map

> [!WARNING]
> The maximum supported map size is `480x480`. Going above this will cause the game to crash.

```py
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

scenario = AoE2DEScenario.from_file("your_scenario.aoe2scenario")

scenario.map_manager.map_size = 120

scenario.write_to_file("your_scenario_output.aoe2scenario")
```
