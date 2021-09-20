# Datasets

The project currently contains multiple datasets. You can get access to the datasets by importing them.

```py
# Information about the conditions & effects and their attributes
from AoE2ScenarioParser.datasets.conditions import ConditionId
from AoE2ScenarioParser.datasets.effects import EffectId
from AoE2ScenarioParser.datasets.trigger_lists import \
    DiplomacyState, Operation, ButtonLocation, PanelLocation, \
    TimeUnit, VisibilityState, DifficultyLevel, TechnologyState, \
    Comparison, ObjectAttribute, Attribute, UnitAIAction, \
    AttackStance, ObjectType, ObjectClass, DamageClass, \
    HeroStatusFlag, Hotkey, BlastLevel, TerrainRestrictions, \
    ColorMood, ObjectState

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

The condition and effect datasets aren't really necessary in regular scripting after adding the new methods for adding
effects & conditions:

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

## Conditions & Effects lists

Many conditions and effects have dropdown lists with options. These options are, like everything else, impossible to
remember. That's why these datasets have been added:

|        Names        |                                  Explanation                                   |              Example               |
| ------------------- | ------------------------------------------------------------------------------ | ---------------------------------- |
| DiplomacyState      | Used in the `Change Diplomacy` effect and the `Diplomacy State` condition.     | `DiplomacyState.ALLY`              |
| Operation           | Used in many effects. Generally related to variables.                          | `Operation.MULTIPLY`               |
| ButtonLocation *    | Used in the `Change Research Location` and `Change Train Location` effects. *  | `ButtonLocation.r2c3`              |
| PanelLocation       | Used in the `Display Instructions` effect.                                     | `PanelLocation.CENTER`             |
| TimeUnit            | Used in the `Display Timer` effect.                                            | `TimeUnit.YEARS`                   |
| VisibilityState     | Used in the `Set Player Visibility` effect.                                    | `VisibilityState.EXPLORED`         |
| DifficultyLevel     | Used in the `Difficulty Level` condition.                                      | `DifficultyLevel.HARDEST`          |
| TechnologyState     | Used in the `Technology State` condition.                                      | `TechnologyState.RESEARCHING`      |
| Comparison          | Used in many effects and conditions. Generally related to variables.           | `Comparison.EQUAL`                 |
| ObjectAttribute     | Used in the `Modify Attribute` effect.                                         | `ObjectAttribute.CARRY_CAPACITY`   |
| Attribute           | Used in the `Accumulate Attribute` effect.                                     | `Attribute.ALL_TECHS_ACHIEVED`     |
| UnitAIAction        | Used in the `Object has Action` condition.                                     | `UnitAIAction.ATTACK`              |
| AttackStance        | Used in the `Change Object Stance` effect.                                     | `AttackStance.AGGRESSIVE_STANCE`   |
| ObjectType          | Used in every unit selection effect & condition.                               | `ObjectType.DOPPELGANGER`          |
| ObjectClass         | Used in every unit selection effect & condition.                               | `ObjectClass.INFANTRY`             |
| DamageClass         | Used in the `Change Object Attack/Armour` effects.                             | `DamageClass.SPEARMEN`             |
| HeroStatusFlag *    | Can be used for changing the `HERO_STATUS` in `ObjectAttribute`. *             | `HeroStatusFlag.HERO_REGENERATION` |
| Hotkey              | Can be used for changing the `HOTKEY_ID` in `ObjectAttribute`.                 | `Hotkey.SPACE`                     |
| BlastLevel          | Can be used for changing the `BLAST_<>_LEVEL` properties in `ObjectAttribute`. | `BlastLevel.NEARBY_UNITS`          |
| TerrainRestrictions | Can be used for changing the `TERRAIN_RESTRICTION_ID` in `ObjectAttribute`.    | `TerrainRestrictions.LAND`         |
| SmartProjectile     | Can be used for changing the `ENABLE_SMART_PROJECTILES` in `ObjectAttribute`.  | `SmartProjectile.ENABLED`          |
| ColorMood           | Used in the `Change Color Mood` effect.                                        | `ColorMood.WINTER`                 |
| ObjectState         | Used in the `Objects in area` condition.                                       | `ObjectState.DEAD`                 |

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
    source_player=PlayerId.TWO,
    target_player=PlayerId.THREE
)

effect = trigger.new_effect.display_instructions(
    source_player=PlayerId.ONE,
    message="Spy: Your ally has betrayed you! He allied the enemy!",
    instruction_panel_position=PanelLocation.CENTER,  # <-- PanelLocation dataset
    display_time=10
)
```

---

## Unit, Building, Techs etc.

The Units and Buildings datasets are very useful when adding units.  
They're also, together with the `Tech` dataset, very useful when adding or editing triggers.

### General Usage

These are the biggest datasets and most powerful datasets:

| Dataset        | Description                                          |
|----------------|------------------------------------------------------|
| `UnitInfo`     | Dataset for units                                    |
| `BuildingInfo` | Dataset for buildings                                |
| `HeroInfo`     | Dataset for heroes                                   |
| `OtherInfo`    | Dataset for other units (like relics and gold piles) |
| `TechInfo`     | Dataset for technologies                             |

For adding units it'll look something like the following:

```py
unit_manager.add_unit(PlayerId.ONE,  UnitInfo.CONQUISTADOR.ID,    x=10, y=20)
unit_manager.add_unit(PlayerId.TWO,  UnitInfo.PALADIN.ID,         x=20, y=20)
unit_manager.add_unit(PlayerId.GAIA, BuildingInfo.FEITORIA.ID,    x=30, y=20)
unit_manager.add_unit(PlayerId.GAIA, HeroInfo.WILLIAM_WALLACE.ID, x=40, y=20)
unit_manager.add_unit(PlayerId.GAIA, OtherInfo.GOLD_MINE.ID,      x=50, y=20)
```

With the triggers you can do similar stuff like:

```py
...
effect = trigger.new_effect.create_object(
    object_list_unit_id=OtherInfo.RELIC.ID
)
...
effect = trigger.new_effect.research_technology(
    source_player=PlayerId.THREE,
    technology=TechInfo.BLOODLINES.ID
)
...
```

### UnitInfo functions

Some useful functions for the `UnitInfo` dataset is `vils()` and `unique_units()`

```py
# Get all villager units (e.g. FARMER, HUNTER, LUMBERJACK etc.) 
# You can disable certain categories like:
# - exclude_male
# - exclude_female
# Example:
male_vils = UnitInfo.vils(exclude_female=True)  
```

```py
# Get all unique units (e.g. HUSKARL, CONQUISTADOR, LONGBOAT, SLINGER etc.)
# You can disable certain categories like:
# - exclude_elite_units
# - exclude_non_elite_units
# - exclude_castle_units  (From the castle building)
# - exclude_non_castle_units  (From anything but the castle building)
# Example:
all_unique_non_castle_non_elite_units = UnitInfo.unique_units(exclude_elite_units=True, exclude_castle_units=True)  
```

### TechInfo functions

Some useful functions for the `TechInfo` dataset are:

- `unique_techs()`

```py
# Get all unique techs (e.g. BEARDED_AXE, CHIEFTAINS, FIRST_CRUSADE etc.)
# You can disable certain categories like:
# - exclude_castle_techs
# - exclude_imp_techs
# Example:
imp_unique_techs = TechInfo.unique_techs(exclude_castle_techs=True)  
```

- `unique_unit_upgrades()`

```py
# Get all unique unit techs (e.g. ELITE_LONGBOWMAN, ELITE_TEUTONIC_KNIGHT etc.)
# You can disable certain categories like:
# - exclude_castle_techs
# - exclude_non_castle_techs  (Excludes stuff like: ELITE_LONGBOAT, IMPERIAL_SKIRMISHER)
# Example:
uu_castle_upgrades = TechInfo.unique_unit_upgrades(exclude_non_castle_techs=True)  
```

- `blacksmith_techs()`
- `monastery_techs()`
- `university_techs()`
- `town_center_techs()`

```py
# Get all blacksmith/monastery/university techs
# You can filter on ages, like so:
all_blacksmith_techs = TechInfo.blacksmith_techs()
feudal_blacksmith_techs = TechInfo.blacksmith_techs(Age.FEUDAL_AGE)
non_imp_blacksmith_techs = TechInfo.blacksmith_techs([Age.FEUDAL_AGE, Age.CASTLE_AGE])
# Same goes for:
#   - TechInfo.monastery_techs(...)
#   - TechInfo.university_techs(...)
#   - TechInfo.town_center_techs(...)
```

- `eco_techs()`

```py
# Get all economic techs
all_eco_techs = TechInfo.eco_techs()
# You can filter on ages (like with blacksmith_techs etc.):
dark_age_eco_techs = TechInfo.eco_techs(ages=Age.DARK_AGE)  # Only returns LOOM
# Or filter on buildings
mining_and_lumber_upgrades = TechInfo.eco_techs(
    buildings=[BuildingInfo.MINING_CAMP.ID, BuildingInfo.LUMBER_CAMP.ID]
)
# Or both:
imp_tc_upgrades = TechInfo.eco_techs(
    ages=Age.IMPERIAL_AGE,
    buildings=BuildingInfo.TOWN_CENTER.ID,
)
```

### OtherInfo functions

One useful function for the `OtherInfo` dataset is `trees()`:

```py
# Get all tree objects (e.g. OAK_TREE, PINE_TREE, BAMBOO etc.)
# Example:
all_trees = OtherInfo.trees()  
```

### Icon, Dead & Hotkey IDs

Besides normal IDs, you might want to access their icon or dead version. Almost every unit, building, hero and tech has
an icon. Most units, buildings and heroes also have a dead unit version to represent the dying animation.  
You can access these values using the same datasets:

```py
archer_id =        UnitInfo.ARCHER.ID         # 4
archer_icon =      UnitInfo.ARCHER.ICON_ID    # 17
archer_death =     UnitInfo.ARCHER.DEAD_ID    # 3
archer_hotkey_id = UnitInfo.ARCHER.HOTKEY_ID  # 16083

# You can also get the datasets from these values
UnitInfo.from_id(4)             # UnitInfo.ARCHER
UnitInfo.from_icon_id(17)       # UnitInfo.ARCHER
UnitInfo.from_dead_id(3)        # UnitInfo.ARCHER
UnitInfo.from_hotkey_id(16083)  # UnitInfo.ARCHER

# It's also still possible to use the string like normal enums:
UnitInfo["ARCHER"]  # UnitInfo.ARCHER
```

---

### GAIA

If you want to know if a unit etc. is a gaia only object, you can do:

```py
UnitInfo.ARCHER.IS_GAIA_ONLY  # False
UnitInfo.WOLF.IS_GAIA_ONLY  # True

# Or for a list:
UnitInfo.gaia_only()  # Returns all units which have 'IS_GAIA_ONLY' as True
UnitInfo.non_gaia()  # Returns all units which have 'IS_GAIA_ONLY' as False
```

---

## Projectiles

If you wanted to change a projectile of archers to that of an arambai, you could do:

```py
trigger.new_effect.modify_attribute(
    quantity=ProjectileInfo.ARAMBAI.ID,
    object_list_unit_id=UnitInfo.ARCHER.ID,
    source_player=PlayerId.ONE,
    operation=Operation.SET,
    object_attributes=ObjectAttribute.PROJECTILE_UNIT
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
TerrainId.BEACH  # 2
TerrainId.FOREST_OAK  # 10
TerrainId.UNDERBUSH_LEAVES  # 71

# Changing the terrain could be done like so:
map_manager.terrain[0].terrain_id = TerrainId.GRASS_1
```

---

## Players

For selecting players it can be as easy as typing `1`. Unfortunately not all parts of the scenario file are structured
like: `0: Gaia, 1: Player1 ... 8: Player8`. So because of this a representation layer has been added. It's a simple Enum
which looks like this:

```py
PlayerId.GAIA,
PlayerId.ONE, PlayerId.TWO, PlayerId.THREE, PlayerId.FOUR,
PlayerId.FIVE, PlayerId.SIX, PlayerId.SEVEN, PlayerId.EIGHT
```

If you want to loop through players, you have 2 options:

```py
# Python built-in range function:
for player in range(9):  # Or range(1, 9) if you want to exclude GAIA
# ... code...

# The PlayerId function:
for player in PlayerId.all():  # Or PlayerId.all(exclude_gaia=True) if you want to exclude GAIA
# ... code...    
```

You can also address the players by color if you prefer it:

```py
PlayerColorId.BLUE, PlayerColorId.RED, PlayerColorId.GREEN, PlayerColorId.YELLOW,
PlayerColorId.AQUA, PlayerColorId.PURPLE, PlayerColorId.GREY, PlayerColorId.ORANGE
```

---
