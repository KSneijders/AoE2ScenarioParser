# Unit Examples

### Add a unit to the map

```py
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.datasets.units import UnitInfo

scenario = AoE2DEScenario.from_file("your_scenario.aoe2scenario")
unit_manager = scenario.unit_manager

unit_manager.add_unit(player=PlayerId.ONE, unit_const=UnitInfo.ARCHER.ID, x=10, y=10)

scenario.write_to_file("your_scenario_output.aoe2scenario")
```

---

### Remove all units of a specific type

```py
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.units import UnitInfo

scenario = AoE2DEScenario.from_file("your_scenario.aoe2scenario")
unit_manager = scenario.unit_manager

for unit in unit_manager.filter_units_by_const([UnitInfo.ARCHER.ID]):
    unit_manager.remove_unit(unit=unit)

scenario.write_to_file("your_scenario_output.aoe2scenario")
```

---

### Change ownership of units in an area

```py
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.players import PlayerId

scenario = AoE2DEScenario.from_file("your_scenario.aoe2scenario")
unit_manager = scenario.unit_manager

units = unit_manager.get_units_in_area(x1=0, y1=0, x2=20, y2=20)
unit_manager.change_ownership(units, to_player=PlayerId.TWO)

scenario.write_to_file("your_scenario_output.aoe2scenario")
```

---

### Remove all eye candy (decorative GAIA objects)

```py
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

scenario = AoE2DEScenario.from_file("your_scenario.aoe2scenario")

scenario.unit_manager.remove_eye_candy()

scenario.write_to_file("your_scenario_output.aoe2scenario")
```