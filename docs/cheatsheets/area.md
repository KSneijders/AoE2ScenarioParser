# Area

The ``Area`` object is a powerful object to get access to specific regions on the map. 
This page will try to explain a bit on how to use it and what the possibilities are.

First of all, the `Area` object uses "Method Chaining". 
This means that methods inside the `Area` object return the `Area` object itself.
This allows you to call another method straight after the first: 

```py
obj.x()
obj.y()
obj.z()
# With method chaining you can do:
obj.x().y().z()
```

This is perfect for a highly configurable and flexible objects like the `Area` object.

---

## Why would I use the `Area` object?

If you want to do anything with more than a single coordinate, it's quite the hassle sometimes.
That's the problem this object is _trying_ (feature suggestions always welcome!) to solve. 

Alright, let's dive in!

## Examples

Below are a couple examples that show why this object can be very useful when working with coordinates.

### Creating a stack of units

Let's say you want to place 16 units, in a 4x4 area on the map. 
This is not necessarily difficult to do, it'd probably look something like the following:

```py
for x in range(10, 14):
    for y in range(50, 54):
        unit_manager.add_unit(
            player=PlayerId.ONE, 
            unit_const=UnitInfo.KNIGHT.ID, 
            x=x+.5, 
            y=y+.5
        )
```

This would create 16 units in a 4x4 area and isn't too bad to read or write. 
BUT, it feels a bit unnecessary, defining variables for your area just to place some units...
Let's see how we'd do it with the `Area` object.

```py
area = scenario.new.area()  # Create a new area object

# Select the area and convert it to a set of all coordinates inside of it
for tile in area.select(10, 50, 13, 53).to_coords():
    # Every tile is a NamedTuple with an 'x' and 'y' value
    unit_manager.add_unit(
        player=PlayerId.ONE, 
        unit_const=UnitInfo.KNIGHT.ID, 
        x=tile.x + .5, 
        y=tile.y + .5
    )
```

Above we can see the creation of a new `Area` object through the new Object Factory inside a scenario.
We use the `select` method to select our area. 

!!! Note
    Keep in mind that `Area.select` uses an inclusive selection. 
    This means that doing: `area.select(1, 1, 3, 3)` will select a 3x3 area.

### Castle surrounded by walls

Now, the above example was quite a simple one. The real power comes with the configuration!
So let's take a more complicated example! Like creating a wall around a castle!
This will be quite the difference, so let's do it in steps, first we create the castle and the area object.

```py
castle = unit_manager.add_unit(player=PlayerId.ONE, unit_const=BuildingInfo.CASTLE.ID, x=30, y=30)
area = scenario.new.area()
```

Now let's select the area of the castle itself, so the 4x4 area.

```py
area.center(castle.x, castle.y).size(4)
# Or using separate width and height calls:
area.center(castle.x, castle.y).width(4).height(4)
```

This sets the center of the area to the castles coordinates. 
After that we change the size of the selection from the default (1x1) to (4x4).
We now have the castle area selected. Let's say we want the wall 6 tiles around the castle.
Let's expand our selection by 6 tiles.

```py
# On it's own line
area.expand_by(6)
# Or add it to the above line
area.center(castle_object.x, castle_object.y).size(4).expand_by(6)
```

Now we have a 16 by 16 tile area selected.
The 4x4 from the castle plus the 6 tiles we expanded to all four sides.

We _could_ do the same thing as above with the knights in the 4x4 but there's a problem.
The selection covers all those 256 (16*16) tiles. So we'd be filling everything with walls. 
We just want the edges so, let's do that. For that we use a so called "use" function.

```py
# On it's own line
area.use_only_edge()
# Or, again, add it to the above line
area.center(castle_object.x, castle_object.y).size(4).expand_by(6).use_only_edge()
```

This tells the area object we only want the outer edge of the selection.
Now let's convert that to coordinates and place those walls! We can use `area.to_coords()` again!

```py
castle = unit_manager.add_unit(player=PlayerId.ONE, unit_const=BuildingInfo.CASTLE.ID, x=30, y=30)
area = scenario.new.area()

for tile in area.center(castle.x, castle.y).size(4).expand_by(6).use_only_edge().to_coords():
    unit_manager.add_unit(
        player=PlayerId.ONE, unit_const=BuildingInfo.STONE_WALL.ID, x=tile.x, y=tile.y
    )
```

And that's it! The castle has walls around it. With such ease!

![Caslte With Walls](./../images/area_castle_walls.png "area with castle walls")










