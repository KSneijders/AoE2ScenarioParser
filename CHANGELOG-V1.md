# Changelog for the V1 version

This changelog is **NOT** comprehensive and complete.
It is meant as a temporary file to keep track of all changes made.

The changes listed below will be explained further in an official document at a later date.

---

## Rework: AreaPattern

1. Changed `Area` object to be much simpler (just represents an area)
2. `Area` objects consist of `corner1: Tile` & `corner2: Tile`, instead of: `x1y1x2y2`
3. Added functionality to `Tile` object
4. Moved `AreaState` and `AreaAttr` into their own modules.
5. Added `AreaPattern`. Which implements most of the old `Area` object functions.
6. Moved `AreaState`, `AreaPattern` and `AreaAttr` to `AoE2ScenarioParser/objects/support/area_pattern/` folder.
7. Changed `i_to_xy` to no longer return a `Tile` object. Use `Tile.from_i()` instead.
8. Moved functions to their own module: `AoE2ScenarioParser/helper/coordinates`:
    1. `xy_to_i`
    2. `i_to_xy`
    3. `validate_coords`

## Rework: Remove `DE` suffix

1. Merged the functionality of the below managers into their corresponding super classes:
    1. `MapManagerDE` > `MapManager`
    2. `TriggerManagerDE` > `TriggerManager`
    3. `UnitManagerDE` > `UnitManager`
    4. `XsManagerDE` > `XsManager` (Renamed & Moved)
2. Removed `AoE2DEScenario` class. Use `AoE2Scenario.from_file(...)` from now on.

# Rework: Remove display index (mostly)

1. `display_index` can no longer be used to get a trigger in any trigger function except for:
   `trigger_manager.get_trigger(<num>, use_display_index=True)`
2. `TriggerSelect` (`TS`) class can no longer be used.
3. Printing the trigger manager, (summary & content) now shows trigger in index order instead of display order
4. `display_index` has been removed from Trigger class when retrieving Conditions or Effects
5. `trigger.get_effect` and `trigger.get_condition` have the same `use_display_index=True` attribute
6. Added `condition_id` (**WILL BE CHANGED LATER**) to Conditions and `effect_id` (**WILL BE CHANGED LATER**) to Effects

## Docs rework

1. URLs to certain API doc pages have changed

## Moved Datasets in individual modules

1. Moved all datasets from the `trigger_list` module to their own modules: 
   From: `from AoE2ScenarioParser.datasets.trigger_lists`
   To: `from AoE2ScenarioParser.datasets.trigger_data.object_type`
2. Moved `HeroStatusFlag.split_flags()` (+ Renamed, See #3) to the flag super class so all flag dataset classes can use it now
3. Renamed `_DataSetIntFlags.split_flags()` to `_DataSetIntFlags.split()`