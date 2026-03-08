# Trigger Examples

### Add a trigger with a condition and effect

```py
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.datasets.units import UnitInfo

scenario = AoE2DEScenario.from_file("your_scenario.aoe2scenario")
trigger_manager = scenario.trigger_manager

trigger = trigger_manager.add_trigger("Villager Check")

trigger.new_condition.own_objects(
    source_player=Player.ONE,
    object_list=UnitInfo.VILLAGER.ID,
    quantity=10,
)
trigger.new_effect.send_chat(
    source_player=Player.ONE,
    message="Player 1 has 10 villagers!",
)

scenario.write_to_file("your_scenario_output.aoe2scenario")
```

---

### Enable or disable a trigger

```py
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

scenario = AoE2DEScenario.from_file("your_scenario.aoe2scenario")
trigger_manager = scenario.trigger_manager

for trigger in trigger_manager.triggers:
    if trigger.name == "My Trigger":
        trigger.enabled = False  # Set to True to enable

scenario.write_to_file("your_scenario_output.aoe2scenario")
```

---

### Create a looping trigger

```py
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.player_data import Player

scenario = AoE2DEScenario.from_file("your_scenario.aoe2scenario")
trigger_manager = scenario.trigger_manager

trigger = trigger_manager.add_trigger("Looping Trigger", looping=True)
trigger.new_effect.send_chat(
    source_player=Player.ONE,
    message="This fires every time conditions are met!",
)

scenario.write_to_file("your_scenario_output.aoe2scenario")
```

---

### Copy a trigger for each player

```py
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.player_data import Player

scenario = AoE2DEScenario.from_file("your_scenario.aoe2scenario")
trigger_manager = scenario.trigger_manager

trigger = trigger_manager.add_trigger("Per Player Trigger")
trigger.new_condition.own_objects(
    source_player=Player.ONE,
    quantity=5,
)

# Creates a copy of the trigger for each player, replacing player references
trigger_manager.copy_trigger_per_player(
    from_player=Player.ONE,
    trigger_select=trigger.trigger_id,
    create_copy_for_players=[Player.TWO, Player.THREE, Player.FOUR],
)

scenario.write_to_file("your_scenario_output.aoe2scenario")
```

---

### Replace a sound name across all triggers

```py
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

scenario = AoE2DEScenario.from_file("your_scenario.aoe2scenario")

for trigger in scenario.trigger_manager.triggers:
    for effect in trigger.effects:
        if effect.sound_name == "OldName":
            effect.sound_name = "NewName"

scenario.write_to_file("your_scenario_output.aoe2scenario")
```

---

### Import triggers from another scenario

```py
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

source = AoE2DEScenario.from_file("source.aoe2scenario")
target = AoE2DEScenario.from_file("target.aoe2scenario")

# Import all triggers from source into the beginning of target (index 0)
# Omit the index to append them to the end instead
target.trigger_manager.import_triggers(source.trigger_manager.triggers, 0)

target.write_to_file("target_output.aoe2scenario")
```
