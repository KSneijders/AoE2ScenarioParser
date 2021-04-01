# Datasets
The project currently contains multiple datasets. These are currently pretty basic and only contain the in-editor options. You can retrieve access to the datasets by importing them.
```py
# Information about the conditions & effects and their attributes
from AoE2ScenarioParser.datasets.conditions import ConditionId
from AoE2ScenarioParser.datasets.effects import EffectId
from AoE2ScenarioParser.datasets.trigger_lists import DiplomacyState, Operation, ButtonLocation, PanelLocation, \
    TimeUnit, VisibilityState, DifficultyLevel, TechnologyState, Comparison, ObjectAttribute, Attribute, \
    ObjectType, ObjectClass

# Information of unit/building/hero and tech IDs
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.datasets.units import UnitInfo

# Information about terrain IDs
from AoE2ScenarioParser.datasets.terrains import TerrainId

# Information about player IDs
from AoE2ScenarioParser.datasets.players import PlayerId, PlayerColorId
```

Current datasets are:

- conditions
- effects
- trigger related items mostly found in dropdown lists (Operation, ButtonLocation, Comparison etc.)
- Buildings
  - Gaia & Non gaia building IDs
  - Building icon IDs
  - Destroyed (dead) building IDs
- Units
  - Gaia & Non gaia unit IDs
  - Unit icon IDs
  - Dead unit IDs
- Heroes
  - Hero IDs
  - Hero icon IDs
  - Dead hero IDs
- Techs
  - Tech IDs
  - Tech icon IDs
- Players
- terrain type IDs

A special thanks to **Alian713** for doing almost all the work in contributing the data needed for these datasets. <3

---

## Conditions & Effects

The condition and effect datasets aren't really necessary in regular scripting after adding the new methods for adding effects & conditions:

```py
effect = trigger.new_effect.change_diplomacy(...)
```

They can still be used if you want the effect & condition IDs for other purposes. 

```py
Condition.OBJECT_IN_AREA    # 5
Effect.PATROL               # 19
```

```py
# Checking the docs for EffectId.CHANGE_DIPLOMACY will show:
"""
Attributes for the **change_diplomacy** effect are:
- diplomacy
- player_source
- player_target
"""
```

---

## Conditions & Effects dropdown lists

Many conditions and effects have dropdown lists with options. These options are, like everything else, impossible to remember. That's why these datasets have been added:

| Names           | Explanation                                                                   | Example                          |
| --------------- | ----------------------------------------------------------------------------- | -------------------------------- |
| DiplomacyState  | Used in the `Change Diplomacy` effect and the `Diplomacy State` condition.    | `DiplomacyState.ALLY`            |
| Operator        | Used in many effects. Generally related to variables.                         | `Operator.MULTIPLY`              |
| ButtonLocation  | Used in the `Change Research Location` and `Change Train Location` effects. * | `ButtonLocation.r2c3`            |
| PanelLocation   | Used in the `Display Instructions` effect.                                    | `PanelLocation.CENTER`           |
| TimeUnit        | Used in the `Display Timer` effect.                                           | `TimeUnit.YEARS`                 |
| VisibilityState | Used in the `Set Player Visibility` effect.                                   | `VisibilityState.EXPLORED`       |
| DifficultyLevel | Used in the `Difficulty Level` condition.                                     | `DifficultyLevel.HARDEST`        |
| TechnologyState | Used in the `Technology State` condition.                                     | `TechnologyState.RESEARCHING`    |
| Comparison      | Used in many effects and conditions. Generally related to variables.          | `Comparison.EQUAL`               |
| ObjectAttribute | Used in the `Modify Attribute` effect.                                        | `ObjectAttribute.CARRY_CAPACITY` |
| Attribute       | Used in the `Accumulate Attribute` efect.                                     | `Attribute.ALL_TECHS_ACHIEVED`   |
| UnitAIAction    | Used in the `Object has Action` condition.                                    | `UnitAIAction.ATTACK`            |
| AttackStance    | Used in the `Change Object Stance` effect.                                    | `AttackStance.AGGRESSIVE_STANCE` |
| ObjectType      | Used in every unit selection effect & condition                               | `ObjectType.DOPPELGANGER`        |
| ObjectClass     | Used in every unit selection effect & condition                               | `ObjectClass.INFANTRY`           |

\*: Means extra functionality listed below.

### ButtonLocation

```py
ButtonLocation.row_col(1, 3)  # ButtonLocation.r1c3
```

---

### General usage examples:

```py
trigger = trigger_manager.add_trigger("Inform Betrayal!")
condition = trigger.new_condition.diplomacy_state(
    quantity=DiplomacyState.ALLY,  # <-- DiplomacyState dataset
    player=Player.TWO,
    target_player=Player.THREE
)

effect = trigger.new_effect.display_instructions(
    player_source=Player.ONE,
    message="Spy: Your ally has betrayed you! He allied the enemy!",
    instruction_panel_position=PanelLocation.CENTER,  # <-- PanelLocation dataset
    display_time=10
)
```

---

## Unit, Building, Hero and Tech IDs 

The Units and Buildings datasets are very usefull when adding units. They're also, together with the the Techs dataset, very usefull when adding or editing triggers.

For adding units it'll look something like the following:

```py
unit_manager.add_unit(Player.ONE,   UnitInfo.CONQUISTADOR.ID,      x=10,   y=20)
unit_manager.add_unit(Player.TWO,   UnitInfo.PALADIN.ID,           x=20,   y=20)
unit_manager.add_unit(Player.GAIA,  BuildingInfo.FEITORIA.ID,      x=30,   y=20)
unit_manager.add_unit(Player.GAIA,  HeroInfo.WILLIAM_WALLACE.ID,   x=40,   y=20)
```

With the triggers you can do similiar stuff like:

```py
...
effect = trigger.new_effect.create_object(
    object_list_unit_id = Unit.MAN_AT_ARMS.ID  # Or: Building.BLACKSMITH.ID
)
...
effect = trigger.new_effect.research_technology(
    player_source = Player.THREE, 
    technology = TechInfo.BLOODLINES.ID
)
...
```

## Icon & dead IDs

Besides normal IDs, you might want to access their icon or dead version. Almost every unit, building, hero and tech has an icon. Most units, buildings and heroes also have a dead unit version to represent the dying animation.  
You can access these values using the same datasets:

```py
archer_id = UnitInfo.ARCHER.ID           # 4
archer_icon = UnitInfo.ARCHER.ICON_ID    # 17
archer_death = UnitInfo.ARCHER.DEAD_ID   # 3
```

You can also get the datasets from these values:

```py
UnitInfo.from_id(4)             # UnitInfo.ARCHER
UnitInfo.from_icon_id(17)       # UnitInfo.ARCHER
UnitInfo.from_dead_id(3)        # UnitInfo.ARCHER

# It's also still possible to use the string like normal enums:
UnitInfo["ARCHER"]              # UnitInfo.ARCHER
```

---

## GAIA

If you want to know if a unit/building/other is a gaia only object you can do:

```py
UnitInfo.ARCHER.IS_GAIA_ONLY    # False
UnitInfo.WOLD.IS_GAIA_ONLY      # True
```

For `UnitInfo`, `BuildingInfo` and `OtherInfo` you can also use the following functions:

```py
UnitInfo.gaia_only()  # Returns all units have 'IS_GAIA_ONLY' as True
UnitInfo.non_gaia()   # Returns all units have 'IS_GAIA_ONLY' as False
```

---

## Terrains

The Terrain dataset has been added **but it's currently not very usefull** as it's not supported to interact with terrain. It does exist and works as follows:

```py
Terrain.BEACH               # 2
Terrain.FOREST_OAK          # 10
Terrain.UNDERBUSH_LEAVES    # 71
```

---

## Players

For selecting players it can be as easy as typing `1`. Unfortunately not all parts of the scenario file are structured like: `0: Gaia, 1: Player1 ... 8: Player8`. So because of this a representation layer has been added. It's a simple Enum which looks like this:

```py
class Player(Enum):
    GAIA = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8

class PlayerColor(Enum):
    BLUE = 1
    RED = 2
    GREEN = 3
    YELLOW = 4
    AQUA = 5
    PURPLE = 6
    GREY = 7
    ORANGE = 8
```

---

End of the Datasets cheatsheet. [Return to README](./../README.md)
