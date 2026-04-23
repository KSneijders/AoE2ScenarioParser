# General

### Convert a scenario to/from Return of Rome

> [!WARNING]
> Make sure units on the map are valid for the target variant, and that your scenario is on version **v1.49 or later** (open it in the in-game editor and save once).

```py
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.scenario_variant import ScenarioVariant

scenario = AoE2DEScenario.from_file("your_scenario.aoe2scenario")

scenario.variant = ScenarioVariant.ROR   # Convert to Return of Rome
scenario.variant = ScenarioVariant.AOE2  # Convert back to AoE2

scenario.write_to_file("your_scenario_output.aoe2scenario")
```