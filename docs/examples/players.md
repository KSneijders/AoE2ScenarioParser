# Player Examples

### Set a player's civilization

```py
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.datasets.object_support import Civilization

scenario = AoE2DEScenario.from_file("your_scenario.aoe2scenario")
player_manager = scenario.player_manager

player_manager.players[PlayerId.ONE].civilization = Civilization.BRITONS

scenario.write_to_file("your_scenario_output.aoe2scenario")
```

---

### Set starting resources

```py
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.players import PlayerId

scenario = AoE2DEScenario.from_file("your_scenario.aoe2scenario")
player_manager = scenario.player_manager

player = player_manager.players[PlayerId.ONE]
player.food  = 500
player.wood  = 500
player.gold  = 250
player.stone = 250

scenario.write_to_file("your_scenario_output.aoe2scenario")
```

---

### Set diplomacy between players

```py
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.datasets.trigger_lists import DiplomacyState

scenario = AoE2DEScenario.from_file("your_scenario.aoe2scenario")
player_manager = scenario.player_manager

# Set players 1, 3 as one team and players 2, 4 as another — both ways
player_manager.set_diplomacy_teams([PlayerId.ONE, PlayerId.THREE], [PlayerId.TWO, PlayerId.FOUR])

scenario.write_to_file("your_scenario_output.aoe2scenario")
```

---

### Set starting age

```py
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.datasets.object_support import StartingAge

scenario = AoE2DEScenario.from_file("your_scenario.aoe2scenario")
player_manager = scenario.player_manager

player_manager.players[PlayerId.ONE].starting_age = StartingAge.CASTLE_AGE

scenario.write_to_file("your_scenario_output.aoe2scenario")
```
