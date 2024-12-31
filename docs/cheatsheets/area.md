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

!!! Note
    The `Area` object strength comes from selecting specific pattern/tiles. If you want to do a similar thing with 
    every tile on the map this object won't help you much. 

---

## API Documentation

For the API Documentation for the Area object, go here: [Area API Documentation](../api_docs/support/area.md).

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
Though, having an object which manages the area would be a lot cleaner than looping through coordinates.
So, let's see how we'd do it with the `Area` object.

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

---

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
area.expand(6)
# Or add it to the above line
area.center(castle_object.x, castle_object.y).size(4).expand(6)
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
area.center(castle_object.x, castle_object.y).size(4).expand(6).use_only_edge()
```

This tells the area object we only want the outer edge of the selection.
Now let's convert that to coordinates and place those walls! We can use `area.to_coords()` again!

```py
castle = unit_manager.add_unit(player=PlayerId.ONE, unit_const=BuildingInfo.CASTLE.ID, x=30, y=30)
area = scenario.new.area()

for tile in area.center(castle.x, castle.y).size(4).expand(6).use_only_edge().to_coords():
    unit_manager.add_unit(
        player=PlayerId.ONE, unit_const=BuildingInfo.STONE_WALL.ID, x=tile.x, y=tile.y
    )
```

And that's it! The castle has walls around it. With such ease!

![Caslte With Walls](./../images/area_castle_walls.png "area with castle walls")

---

### Checkers pattern

So, let's say we want to create a checkers pattern. 
Where we create squares of ice and black terrain alternately.
To do this we basically need all tiles on the map but in separate squares.
So selecting the entire map alone isn't enough here as we want them all separated.

So, what we want is blocks of 3x3 over the course of the map. 
The map we're reading is a tiny 2 player map which has a size of 120 by 120 tiles.

What we'll do is select the entire map and use the grid pattern. 
Then we use a block size of 3 and a gap size of 0. This way we get 3x3 areas.

Though, we cannot use the `area.to_coords()` function we used before. 
The reason for that is because the function returns all tiles in the selection. 
And because we use all tiles in the map, this function will just return a large list of all tiles.
What we need for this is: `area.to_chunks()`. Let's get started and see how it works!

Alright, first, let's create the main `Area` object and select the entire map. 

```py
area = scenario.new.area()
area.select_entire_map()
```

After that, let's set it so that it uses the grid pattern. You can do this in two ways:

```py
# Append to the same line
area = scenario.new.area()
area.select_entire_map().use_pattern_grid()

# Or add it after the last line
area = scenario.new.area()
area.select_entire_map()
area.use_pattern_grid()
```

Now this would be default return a grid with gaps of 1 and blocks of 1x1. We want blocks of 3x3 and no gaps (gap of 0).
Below you can see the steps and the difference these configurations have:

![Area grid 1x1 example](./../images/area_grid_1x1_example.png "Area grid 1x1 example")

Now that we know what we want, we can add some configuration to the function, we can do this in four ways, choose 
the one you like the most (We'll continue with the first option):

```py
# For the third option:
from AoE2ScenarioParser.objects.support.area import AreaAttr

...
area.use_pattern_grid(block_size=3, gap_size=0)
...
area.use_pattern_grid().attr('block_size', 3)
area.use_pattern_grid().attr('gap_size', 0)
...
area.use_pattern_grid().attr(AreaAttr.BLOCK_SIZE, 3)
area.use_pattern_grid().attr(AreaAttr.GAP_SIZE, 0)
...
area.use_pattern_grid().attrs(block_size=3, gap_size=0)
```

!!! Tip "You can differentiate the X and Y"
    In many functions you can use the general option like `gap_size`. 
    But there's also options for `gap_size_x` and `gap_size_y` if you want different selections.

Now that we have the grid, let's add the final piece where we change the terrain itself. 
We can use the function `to_chunks()` to return our grid as 'chunks'.

Chunks will be returned in a list and every chunk will be returned as an `OrderedSet`.
These `OrderedSet`s will contain `Tile` objects by default. These objects just contain their `x` and `y` values.
We can change this behaviour with the `as_terrain` parameter. 
Setting this to `True` will return the `OrderedSet`s with `TerrainTile` objects. 
These objects allow you to directly change the terrain on this tile. 
These are also the same objects returned by the Map Manager.

```py
for index, chunk in enumerate(area.to_chunks(as_terrain=True)):
    for terrain_tile in chunk:
        terrain_tile.terrain_id = TerrainId.BLACK if index % 2 == 0 else TerrainId.ICE
```

So the code above loops through all the 3x3 squares returned by the `to_chunks` function.
Then for each square it loops through all the terrain tiles in the `OrderedSet`.
We then set the terrain to `BLACK` or `ICE` depending on the index reduced by modulo 2.
This will alternate the tiles between the two terrain types.

There's one small adjustment we need to make. Because the map 120 tiles and the squares have a length of 3 we can fit
40 squares per row. This is an even number. So just alternating `BLACK` and `ICE` terrain based on index will cause
it to create lines instead of alternating each row. We can fix this by adding the row with the index and reduce that
by modulo 2 to get our ideal situation. 

```py
for index, chunk in enumerate(area.to_chunks(as_terrain=True)):
    for terrain_tile in chunk:
        row = index // (map_manager.map_size / 3)  # 3 as the size of the grid blocks
        terrain_tile.terrain_id = TerrainId.BLACK if (index + row) % 2 == 0 else TerrainId.ICE
```

Another way to get around this is make sure the squares fit an odd amount of times in the length of the map. 
So using the earlier loop, without the row, with a map size of 117 (39 times) would result in the same pattern as the 
code above.

![area checkers example result](./../images/area_checkers_example_result.png "area checkers example result")

The entire code block for this example:

```py
area = scenario.new.area()
area.select_entire_map().use_pattern_grid(block_size=3, gap_size=0)

for index, chunk in enumerate(area.to_chunks(as_terrain=True)):
    for terrain_tile in chunk:
        row = index // (map_manager.map_size / 3)  # 3 as the size of the grid blocks
        terrain_tile.terrain_id = TerrainId.BLACK if (index + row) % 2 == 0 else TerrainId.ICE
```

---

The API Documentation has existed for some time, and the temporary docs here, have been removed.

They've been moved here: [Area API Documentation](../api_docs/support/area.md).
