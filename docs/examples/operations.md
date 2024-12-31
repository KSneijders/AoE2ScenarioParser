# Operation examples

## Convert a scenario to or from a Return of Rome scenario

Convert a scenario from AoE2 to **Return of Rome**.  

!!! warning "**Return of Rome** units"
    When converting from or to a **Return of Rome** scenario, make sure units are valid for the target variant or 
    make sure there's no conflicting units on the map. 

!!! warning "**Return of Rome** version"
    When converting from or to a **Return of Rome** scenario, make sure your scenario is on v1.49 or later. 
    To do this, open the scenario in the in-game editor and save it once.

```py
# Import the scenario object & scenario variant dataset
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.scenario_variant import ScenarioVariant

# Define Scenario file
scenario = AoE2DEScenario.from_file(file_path_here)

# To Return of Rome scenario:
scenario.variant = ScenarioVariant.ROR
# To usual Age 2 scenario:
scenario.variant = ScenarioVariant.AOE2

scenario.write_to_file(file_output_path_here)
```

---