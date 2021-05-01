# Units

You can use the unit manager to add, edit and remove units. This
includes buildings and heroes etc.

## Adding Units

Below you can find examples on how to add units to the scenario. This
will add a conquistador for player 1 at (0, 0) which is the West corner
of the map:


```py
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.datasets.units import UnitInfo

# Add Unit
unit_manager = scenario.unit_manager

unit = unit_manager.add_unit(
    player=PlayerId.ONE,
    unit_const=UnitInfo.CONQUISTADOR.ID,  # Units dataset
    x=0.5,
    y=0.5
)

# Or, with more detail:
unit = unit_manager.add_unit(
    player=PlayerId.ONE,
    unit_const=UnitInfo.CONQUISTADOR.ID,
    x=0.5,
    y=0.5,
    z=0,                # The 'height' of the unit. 
    rotation=0,         # Rotation in radians
    animation_frame=0,  # The nth animation frame
)
```

## Select existing Units

To select the units you want there are a couple options. You can select
all the units from a certain player:

```py
gaia_units = unit_manager.get_player_units(PlayerId.GAIA)
```

Or, get all units:

```py
all_units = unit_manager.get_all_units()
```

If you want a more specific search, you can use the `get_units_in_area`
function. This function is quite powerfull. You can select an area using
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
#    Tile(0,0).x1 == 0  # True  
#    Tile(0,0).x2 == 1  # True
```

For all other examples we'll be using the ``[x, y]`` notation. But you can use the ``Tile`` notation interchangably:

```py
unit_manager.get_units_in_area(x1=2, y1=3, x2=4, y2=5, players=[
    PlayerId.ONE, PlayerId.TWO
])
# Any unit within 2,3 => 4,5 from Player 1 and 2.

unit_manager.get_units_in_area(x1=2, y1=3, x2=4, y2=5, ignore_players=[
    PlayerId.GAIA
])
# Any unit within 2,3 => 4,5 from any Player but GAIA.

unit = unit_manager.add_unit(player=PlayerId.ONE, unit_const=UnitInfo.CONQUISTADOR.ID, x=5, y=1)
unit2 = unit_manager.add_unit(player=PlayerId.TWO, unit_const=UnitInfo.CONQUISTADOR.ID, x=1, y=5)

unit_manager.get_units_in_area(x1=0, y1=0, x2=9, y2=9, unit_list=[unit, unit2], players=[PlayerId.ONE])
# Selects any unit from the given list that belongs to Player 1 within 0,0 => 9,9.
```

## Edit Units

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

Besides it\'s location you can also change the type of unit:

```py
unit.unit_const = UnitInfo.MAN_AT_ARMS.ID    # Units dataset
```

You also might want to change the ownership of a unit. This might seem
easy as there is a `player` attribute within the unit.
Unfortunately that value is read-only. It\'s only there so you can
easily identify the player. To change a units ownership you need the
`unit_manager`:

```py
unit_manager.change_ownership(unit, PlayerId.THREE)
```

## Removing Units

Two ways to delete a unit:

```py
unit_manager.remove_unit(unit=unit)
unit_manager.remove_unit(reference_id=unit.reference_id)
```

## Other useful functions

Ever wanted to get rid of all the eye_candy? Now you can:

```py
unit_manager.remove_eye_candy()
```
