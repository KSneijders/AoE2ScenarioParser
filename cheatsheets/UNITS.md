# Units

You can retrieve access to the units using the object_manager. 

```py
unit_manager = scenario.object_manager.unit_manager
```

---

## Adding units

You can add units using the `unit_manager`. 

```py
unit = unit_manager.add_unit(
    player=Player.ONE,
    unit_id=Unit.CONQUISTADOR,    # Units dataset
    x=0,
    y=0
)
```
This will add a conquistador for player 1 at 0, 0 (West corner of the map). Besides these 4 required parameters there's a couple you can also use to get it as perfect as you want. You can also add the following:
```py
unit = unit_manager.add_unit(
    player=Player.ONE,
    unit_id=Unit.CONQUISTADOR,
    x=0,
    y=0,
    z=0,                    # The 'height' of the unit. 
    rotation=0,             # Rotation in radians
    animation_frame=0,      # The nth animation frame
)
```

---
&nbsp;  

## Finding units
Getting the right unit is important. For now the 'only' supported methods are finding it using it's location on the map or per player (or both). You can of course filter it further yourself later. You can find units like so:
```py
unit_manager.get_player_units(Player.GAIA)  # Returns all GAIA units 
# Note that all trees and eye candy etc. on the map are also GAIA units.

unit_manager.get_all_units()    # Returns all units on the map
# Naturally, also includes all trees and eye candy etc.
```
### The 'get_units_in_area' function
This function is quite powerfull. You can select an area using coordinates or using tiles. You can also use a whitelist of players or a blacklist of players to (not) select the units from. You can also, if you have, hand it your own list of units to filter through.
```py
unit_manager.get_units_in_area(x1=0, y1=0, x2=10, y2=10)
# Any unit within 0,0 => 10,10

unit_manager.get_units_in_area(tile1=Tile(0, 0), tile2=Tile(10, 10))
# Any unit within 0,0 => 11, 11 (Note the 11, 11)
# This is because Tiles are quares (1x1). So: 
#    Tile(0,0).x1 == 0  # True  
#    Tile(0,0).x2 == 1  # True
```
For all other examples we'll be using the `x, y` notation. But you can use the `Tile` notation interchangably.
```py
unit_manager.get_units_in_area(x1=2, y1=3, x2=4, y2=5, players=[
    Player.ONE, Player.TWO
])
# Any unit within 2,3 => 4,5 from Player 1 and 2.

unit_manager.get_units_in_area(x1=2, y1=3, x2=4, y2=5, ignore_players=[
    Player.GAIA
])
# Any unit within 2,3 => 4,5 from any Player but GAIA.

unit = unit_manager.add_unit(player=Player.ONE, unit_id=units.conquistador, x=5, y=1)
unit2 = unit_manager.add_unit(player=Player.TWO, unit_id=units.conquistador, x=1, y=5)

unit_manager.get_units_in_area(x1=0, y1=0, x2=9, y2=9, unit_list=[unit, unit2], players=[Player.ONE])
# Selects any unit from the given list that belongs to Player 1 within 0,0 => 9,9.
```

---
&nbsp;  

## Editing units
While adding units is fun, you might want to change existing units. You can, for example, change the location of any unit:
```py
from AoE2ScenarioParser.helper.helper import Tile

...

unit.tile = Tile(0, 0)  # Will change the units location to the center of tile 0,0
# Equivelant to:
unit.x = 0.5
unit.y = 0.5
```

Besides it's location you can also change the type of unit:
```py
unit.unit_id = Unit.MAN_AT_ARMS    # Units dataset
```
*Note: Do not confuse this with `reference_id` because that's the unique identifier of that specific unit and you can't have duplicates in the reference_id table.*

You also might want to change the ownership of a unit. This might seem easy as there is a `player` attribute within the unit. Unfortunately that value is read-only and only there so you can easily identify the player. To change a units ownership you need the `unit_manager`.
```py
unit_manager.change_ownership(unit, Player.THREE)
```

---
&nbsp;  

## Other

Some other usefull functions are listed below:

```py
unit_manager.remove_eye_candy()  # Removes All Eye Candy bushes etc.
```
