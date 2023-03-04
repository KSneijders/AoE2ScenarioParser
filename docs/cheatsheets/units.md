# Units

You can use the unit manager to add, edit and remove units. This
includes buildings and heroes etc.

## Adding

Below you can find examples on how to add units to the scenario. This
will add a conquistador for player 1 at (0, 0) which is the West corner
of the map:

```py

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.datasets.units import UnitInfo

# ... 
# Read scenario etc.
# ...

# Add Unit
unit_manager = scenario.unit_manager

unit = unit_manager.add_unit(
    player=Player.ONE,
    type=UnitInfo.CONQUISTADOR.ID,  # Units dataset
    x=0.5,
    y=0.5
)

# Or, with more detail:
unit = unit_manager.add_unit(
    player=Player.ONE,
    type=UnitInfo.CONQUISTADOR.ID,
    x=0.5,
    y=0.5,
    z=0,  # The 'height' of the unit. 
    rotation=0,  # Rotation in radians
    animation_frame=0,  # The nth animation frame
)
```

## Selecting

To select the units you want there are a couple options. You can select
all the units from a certain player:

```py
gaia_units = unit_manager.get_player_units(Player.GAIA)
```

Or, get all units:

```py
all_units = unit_manager.get_all_units()
```

If you want a more specific search, you can use the `get_units_in_area`
function. This function is quite powerful. You can select an area using
coordinates or using tiles. You can also use a whitelist of players or a
blacklist of players to (not) select the units from. And, if you have,
hand it your own list of units to filter through. You can see a couple
examples below:

```py
unit_manager.get_units_in_area(x1=0, y1=0, x2=10, y2=10)
# Any unit within 0,0 => 10,10

unit_manager.get_units_in_area(tile1=Tile(0, 0), tile2=Tile(10, 10))
# Any unit within 0,0 => 11, 11 (Note the 11, 11)
# This is because Tiles are squares (1x1). So: 
# >>> Tile(0,0).x1 == 0
# >>> Tile(0,0).x2 == 1
```

For all other examples we'll be using the ``[x, y]`` notation. But you can use the ``Tile`` notation interchangeably:

```py
unit_manager.get_units_in_area(x1=2, y1=3, x2=4, y2=5, players=[
    Player.ONE, Player.TWO
])
# Any unit within 2,3 => 4,5 from Player 1 and 2.

unit_manager.get_units_in_area(x1=2, y1=3, x2=4, y2=5, ignore_players=[
    Player.GAIA
])
# Any unit within 2,3 => 4,5 from any Player but GAIA.

unit = unit_manager.add_unit(player=Player.ONE, type=UnitInfo.CONQUISTADOR.ID, x=5, y=1)
unit2 = unit_manager.add_unit(player=Player.TWO, type=UnitInfo.CONQUISTADOR.ID, x=1, y=5)

unit_manager.get_units_in_area(x1=0, y1=0, x2=9, y2=9, unit_list=[unit, unit2], players=[Player.ONE])
# Selects any unit from the given list that belongs to Player 1 within 0,0 => 9,9.
```

You can also filter certain units based on their `type` value.  
For this you can use the `filter_units_by_const` function.

```py
# Get TC object of all players
unit_manager.filter_units_by_type(unit_types=[BuildingInfo.TOWN_CENTER.ID])
# Get TC object of only player one and two
unit_manager.filter_units_by_type(unit_types=[BuildingInfo.TOWN_CENTER.ID], player_list=[Player.ONE, Player.TWO])
# Get all objects of player one except for the villagers
unit_manager.filter_units_by_type(
    unit_types=[UnitInfo.VILLAGER_MALE, UnitInfo.VILLAGER_FEMALE],
    blacklist=True,  # <-- When True, everything in the unit_types list will be excluded instead of included
    player_list=[Player.ONE],
)
# Exclude all unique units from a given list
unit_manager.filter_units_by_type(
    unit_types=UnitInfo.unique_units(),
    blacklist=True,
    unit_list=[some_list_with_Unit_objects]
)
```

## Editing

While adding units is fun, you might want to change existing units. You
can, for example, change the location of any unit:

```py

from AoE2ScenarioParser.objects.support.tile import Tile

...

unit.tile = Tile(0, 0)  # Will change the units location to the center of tile 0,0
# Equivelant to:
unit.x = 0.5
unit.y = 0.5
```

Besides it's location you can also change the type of unit:

```py
unit.type = UnitInfo.MAN_AT_ARMS.ID  # Units dataset
```

You also might want to change the ownership of a unit. You can do this by 
changing the `player` property in the unit object itself or calling 
`change_ownership` from the unit manager.

```py
# Both are identical in functionality
unit.player = Player.THREE
unit_manager.change_ownership(unit, Player.THREE)
```

## Removing

Two ways to delete a unit:

!!! tip "Removing a unit using an object is faster"
    Due to a unit object containing the player value it belongs to, 
    the unit can be found a lot faster. Which, when removing a lot of units,
    can save you some time.

```py
unit_manager.remove_unit(unit=unit)
unit_manager.remove_unit(id=unit.id)
```

If you want to remove all units from the map or a single player 
you can also just set it to an empty list:

```py
# Remove all units from P3
unit_manager.units[Player.THREE] = []
# Remove all units
unit_manager.units = []
```

## Other functions

Ever wanted to get rid of all the eye candy on the map? Now you can:

```py
unit_manager.remove_eye_candy()
```
