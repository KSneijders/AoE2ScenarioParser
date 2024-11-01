# Players

You can use the player manager to edit many player related attributes.

## Editing

Here's an example of how to view a player and edit their starting civilization, architecture and resources.

```py
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.object_support import Civilization
from AoE2ScenarioParser.datasets.players import PlayerId

# File & Folder setup
# Define paths to the scenario folder.
# You can find this folder by opening AoE2:DE and going to scenarios and clicking on 'open folder'
scenario_folder = "your/path/to/the/scenario/folder/"  # <-- Final slash is important
scenario_name = "name_of_your_scenario"

# Define Scenario file
scenario = AoE2DEScenario.from_file(f"{scenario_folder}{scenario_name}.aoe2scenario")

# Save the player manager and the second player
player_manager = scenario.player_manager
player_two = player_manager.players[PlayerId.TWO]

player_two.civilization = Civilization.BYZANTINES
player_two.architecture_set = Civilization.BYZANTINES
player_two.food = 550
player_two.wood = 450
player_two.gold = 350
player_two.stone = 250

# Write to same folder with name + '_output'
scenario.write_to_file(f"{scenario_folder}{scenario_name}_output.aoe2scenario")
```

Players have many attributes, below is a list of most of their attributes which you can change.

| Attribute name        | Type      | Dataset      | Attributes |
|-----------------------|-----------|--------------|------------|
| player_id             | int       | -            | Read only  |
| active                | bool      | -            | Read onl   |
| starting_age          | int       | StartingAge  |            |
| lock_civ              | bool      | -            |            |
| population_cap        | int       | -            |            |
| food                  | int       | -            |            |
| wood                  | int       | -            |            |
| gold                  | int       | -            |            |
| stone                 | int       | -            |            |
| color                 | int       | ColorId      |            |
| human                 | bool      | -            |            |
| civilization          | int       | Civilization |            |
| architecture_set      | int       | Civilization |            |
| diplomacy             | List[int] | -            | Non-GAIA   |
| ~~initial_camera_x~~* | int       | -            | Non-GAIA   |
| ~~initial_camera_y~~* | int       | -            | Non-GAIA   |
| allied_victory        | bool      | -            | Non-GAIA   |
| disabled_techs        | List[int] | -            | Non-GAIA   |
| disabled_buildings    | List[int] | -            | Non-GAIA   |
| disabled_units        | List[int] | -            | Non-GAIA   |
| tribe_name            | str       | -            | Non-GAIA   |
| base_priority         | int       | -            | Non-GAIA   |
| string_table_name_id  | int       | -            | Non-GAIA   |
| initial_player_view_x | int       | -            | Non-GAIA   |
| initial_player_view_y | int       | -            | Non-GAIA   |

*: Deprecated properties which don't affect anything

## Active Players

You can also set the active players with the player manager. Unfortunately, the game does not
support enabling players in 'gaps'. If you want p4 enabled, you need to have p1, p2 and p3 enabled.
This is why the 'active' attribute in the player object is read-only.

You can set the active player like:

```py
player_manager.active_players = 4  # Enables player 1, 2, 3 and 4
```

## Disables

Disables are used to disable units, buildings and technologies for a certain player.
For example, if you want to disable `archery ranges`, `stables` and `siege workshops` for player two,
and you want to disable the `market`, the tech `loom` and `Paladins` for the fifth player, you can do so like this:

```py
player_two = player_manager.players[PlayerId.TWO]
player_two.disabled_buildings.extend([
    BuildingInfo.ARCHERY_RANGE.ID,
    BuildingInfo.STABLE.ID, 
    BuildingInfo.SIEGE_WORKSHOP.ID
])

player_five = player_manager.players[PlayerId.FIVE]
player_five.disabled_buildings.append(BuildingInfo.MARKET.ID)
player_five.disabled_techs.append(TechInfo.LOOM.ID)
player_five.disabled_units.append(UnitInfo.PALADIN.ID)
```

You can also copy the list of units from one player to another:

```py
player_two = player_manager.players[PlayerId.TWO]
player_five = player_manager.players[PlayerId.FIVE]

player_five.disabled_buildings = player_two.disabled_buildings.copy()
```

## Diplomacy

You can set diplomacy through the player manager or directly per player.

### Set diplomacy teams

If you want to quickly set the diplomacy in teams where everyone is allied to the rest of the team, you can use the `player_manager.set_diplomacy_teams` function.
It accepts a list of lists with integers or `PlayerId` numbers.

The code below creates four teams of two. This sets the players to ally as you can see with the final `diplomacy` argument.

```py
player_manager.set_diplomacy_teams(
    [1, 2], [3, 4], [5, 6], [7, 8], 
    diplomacy=DiplomacyState.ALLY
)
```

### Set diplomacy directly

You can also set the diplomacy directly for a single player. 
For example, below you can see that player one is set to enemy with player 5 and player 2, 3 and 4 are set to ally.

!!! note "This is not mutual!"
    These function calls will only set the diplomacy one-way.  
    All 'target' players (2, 3, 4 and 5) are still on the default Enemy stance.

```py
p1 = player_manager.players[PlayerId.ONE]
p1.set_player_diplomacy(5, DiplomacyState.ENEMY)
p1.set_player_diplomacy([2, 3, 4], DiplomacyState.ALLY)
```