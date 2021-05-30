# Datasets
The project currently contains multiple datasets. These are currently pretty basic and only contain the in-editor options. You can retrieve access to the datasets by importing them.
```py
# Information about the conditions & effects and their attributes
from AoE2ScenarioParser.datasets.conditions import ConditionId
from AoE2ScenarioParser.datasets.effects import EffectId
from AoE2ScenarioParser.datasets.trigger_lists import DiplomacyState, Operation, ButtonLocation, PanelLocation, \
    TimeUnit, VisibilityState, DifficultyLevel, TechnologyState, Comparison, ObjectAttribute, Attribute, \
    UnitAIAction, AttackStance, ObjectType, ObjectClass, DamageClass, HeroStatusFlag, Hotkey, BlastLevel, \
    TerrainRestrictions

# Information of unit/building/hero and tech IDs
from AoE2ScenarioParser.datasets.projectiles import ProjectileInfo
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


A special thanks to **Alian713** for doing **A LOT** of the work in contributing the data needed for these datasets. :heart:

---

## Conditions & Effects

The condition and effect datasets aren't really necessary in regular scripting after adding the new methods for adding effects & conditions:

```py
effect = trigger.new_effect.change_diplomacy(...)
```

They can still be used if you want the effect & condition IDs for other purposes.

```py
Condition.OBJECTS_IN_AREA  # 5
Effect.PATROL  # 19
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

| Names               | Explanation                                                                   | Example                            |
| ------------------- | ----------------------------------------------------------------------------- | ---------------------------------- |
| DiplomacyState      | Used in the `Change Diplomacy` effect and the `Diplomacy State` condition.    | `DiplomacyState.ALLY`              |
| Operation           | Used in many effects. Generally related to variables.                         | `Operator.MULTIPLY`                |
| ButtonLocation      | Used in the `Change Research Location` and `Change Train Location` effects. * | `ButtonLocation.r2c3`              |
| PanelLocation       | Used in the `Display Instructions` effect.                                    | `PanelLocation.CENTER`             |
| TimeUnit            | Used in the `Display Timer` effect.                                           | `TimeUnit.YEARS`                   |
| VisibilityState     | Used in the `Set Player Visibility` effect.                                   | `VisibilityState.EXPLORED`         |
| DifficultyLevel     | Used in the `Difficulty Level` condition.                                     | `DifficultyLevel.HARDEST`          |
| TechnologyState     | Used in the `Technology State` condition.                                     | `TechnologyState.RESEARCHING`      |
| Comparison          | Used in many effects and conditions. Generally related to variables.          | `Comparison.EQUAL`                 |
| ObjectAttribute     | Used in the `Modify Attribute` effect.                                        | `ObjectAttribute.CARRY_CAPACITY`   |
| Attribute           | Used in the `Accumulate Attribute` efect.                                     | `Attribute.ALL_TECHS_ACHIEVED`     |
| UnitAIAction        | Used in the `Object has Action` condition.                                    | `UnitAIAction.ATTACK`              |
| AttackStance        | Used in the `Change Object Stance` effect.                                    | `AttackStance.AGGRESSIVE_STANCE`   |
| ObjectType          | Used in every unit selection effect & condition                               | `ObjectType.DOPPELGANGER`          |
| ObjectClass         | Used in every unit selection effect & condition                               | `ObjectClass.INFANTRY`             |
| DamageClass         | Used in the `Change Object Attack/Armour` effects                             | `DamageClass.SPEARMEN`             |
| HeroStatusFlag      | Can be used for changing the `HERO_STATUS` in `ObjectAttribute`               | `HeroStatusFlag.HERO_REGENERATION` |
| Hotkey              | Can be used for changing the `HOTKEY_ID` in `ObjectAttribute`                 | `Hotkey.SPACE`                     |
| BlastLevel          | Can be used for changing the `BLAST_<>_LEVEL` properties in `ObjectAttribute` | `BlastLevel.NEARBY_UNITS`          |
| TerrainRestrictions | Can be used for changing the `TERRAIN_RESTRICTION_ID` in `ObjectAttribute`    | `TerrainRestrictions.LAND`         |

\*: Means extra functionality listed below.

### ButtonLocation

```py
ButtonLocation.row_col(1, 3)  # ButtonLocation.r1c3
```

### HeroStatusFlag
```py
# Both have the same result
hsf = HeroStatusFlag.CANNOT_BE_CONVERTED + HeroStatusFlag.DELETE_CONFIRMATION
hsf = HeroStatusFlag.combine(
    cannot_be_converted=True,
    delete_confirmation=True
)
```

---

### General usage examples:

```py
trigger = trigger_manager.add_trigger("Inform Betrayal!")
condition = trigger.new_condition.diplomacy_state(
    quantity=DiplomacyState.ALLY,  # <-- DiplomacyState dataset
    player=PlayerId.TWO,
    target_player=PlayerId.THREE
)

effect = trigger.new_effect.display_instructions(
    player_source=PlayerId.ONE,
    message="Spy: Your ally has betrayed you! He allied the enemy!",
    instruction_panel_position=PanelLocation.CENTER,  # <-- PanelLocation dataset
    display_time=10
)
```

---

## Unit, Building, Hero, Other and Tech IDs 

The Units and Buildings datasets are very usefull when adding units. They're also, together with the the Techs dataset, very usefull when adding or editing triggers.

For adding units it'll look something like the following:

```py
unit_manager.add_unit(PlayerId.ONE,    UnitInfo.CONQUISTADOR.ID,      x=10,   y=20)
unit_manager.add_unit(PlayerId.TWO,    UnitInfo.PALADIN.ID,           x=20,   y=20)
unit_manager.add_unit(PlayerId.GAIA,   BuildingInfo.FEITORIA.ID,      x=30,   y=20)
unit_manager.add_unit(PlayerId.GAIA,   HeroInfo.WILLIAM_WALLACE.ID,   x=40,   y=20)
unit_manager.add_unit(PlayerId.GAIA,   OtherInfo.GOLD_MINE.ID,        x=50,   y=20)
```

With the triggers you can do similiar stuff like:

```py
...
effect = trigger.new_effect.create_object(
    object_list_unit_id = UnitInfo.MAN_AT_ARMS.ID  # Or: BuildingInfo.BLACKSMITH.ID
)
...
effect = trigger.new_effect.research_technology(
    player_source = PlayerId.THREE, 
    technology = TechInfo.BLOODLINES.ID
)
...
```

## Icon, Dead & Hotkey IDs

Besides normal IDs, you might want to access their icon or dead version. Almost every unit, building, hero and tech has an icon. Most units, buildings and heroes also have a dead unit version to represent the dying animation.  
You can access these values using the same datasets:

```py
archer_id        = UnitInfo.ARCHER.ID          # 4
archer_icon      = UnitInfo.ARCHER.ICON_ID     # 17
archer_death     = UnitInfo.ARCHER.DEAD_ID     # 3
archer_hotkey_id = UnitInfo.ARCHER.HOTKEY_ID   # 16083

# You can also get the datasets from these values

UnitInfo.from_id(4)             # UnitInfo.ARCHER
UnitInfo.from_icon_id(17)       # UnitInfo.ARCHER
UnitInfo.from_dead_id(3)        # UnitInfo.ARCHER
UnitInfo.from_hotkey_id(16083)  # UnitInfo.ARCHER

# It's also still possible to use the string like normal enums:
UnitInfo["ARCHER"]              # UnitInfo.ARCHER
```

---

## GAIA

If you want to know if a unit etc. is a gaia only object, you can do:

```py
UnitInfo.ARCHER.IS_GAIA_ONLY    # False
UnitInfo.WOLD.IS_GAIA_ONLY      # True

# Or for a list:
UnitInfo.gaia_only()  # Returns all units which have 'IS_GAIA_ONLY' as True
UnitInfo.non_gaia()   # Returns all units which have 'IS_GAIA_ONLY' as False
```

---

## Projectiles

If you wanted to change a projectile of archers to that of an arambai, you could do:

```py
trigger.new_effect.modify_attribute(
    quantity              = ProjectileInfo.ARAMBAI.ID,
    object_list_unit_id   = UnitInfo.ARCHER.ID,
    source_player         = PlayerId.ONE,
    item_id               = UnitInfo.ARCHER.ID,
    operation             = Operation.SET,
    object_attributes     = ObjectAttribute.PROJECTILE_UNIT
)
```
Not all projectiles have the most obvious names. So you can use the following to find projectiles easier.
```py
# Get the second projectile that a CHU KO NU shoots. (Pre-chemistry arrows)
ProjectileInfo.get_unit_projectile(UnitInfo.CHU_KO_NU.ID, has_chemistry=False, secondary=True)
```

---

## Terrains

The terrain dataset can be used for changing terrain types.

```py
Terrain.BEACH               # 2
Terrain.FOREST_OAK          # 10
Terrain.UNDERBUSH_LEAVES    # 71

# Changing the terrain could be done like so:
map_manager.terrain[0].terrain_id = TerrainId.GRASS_1
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
