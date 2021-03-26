# Introduction

This document shows the changes that have to be made to `0.0.20` code for it to function properly in the new `0.1.0` release.

---

## Changes

- The class to call the `from_file(...)` function on has changed from: `AoE2Scenario` to `AoE2DEScenario`.   
  You can import the new class using:  
  `from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario`
- The `trigger.add_effect(...)` and `trigger.add_condition(...)` are now private functions in a trigger. So now: (`trigger._add_effect(...)` and `trigger._add_condition(...)`)  
  The reason for this is the introduction of the `new_effect` and `new_condition` objects!  
  These objects have all conditions and effects as functions. This makes it easier in combination with autocomplete to know what attributes can be used!  
  You can transform your function as follows:  
  ```py
  # From, To:
  trigger.add_effect(Effect.SEND_CHAT, message="Hello")
  trigger.new_effect.send_chat(message="Hello")  # All parameters (like 'message') remain unchanged
  ```
- The dataset, object and manager naming conventions have changed slightly.
  - The datasets got an `Id` suffix on all object-like sets. Example: `Unit` -> `UnitId`  
    The same goes for: `Building`, `GaiaBuilding`, `Tech`, `Hero`, `Terrain`, `Player`, `PlayerColor`, `Effect` and `Condition`.
  - The managers got their suffix changed and location changed:
    - The location changed from: `objects/map_obj` -> `objects/managers/de/map_manager_de`. 
    - The managers renaming: `MapObject` -> `MapManagerDE`  
      The same with location and renaming goes for: `UnitsObject` and `TriggersObject`
  - The objects had their suffix removed and location changed:
    - The location changed from: `objects/terrain_obj` -> `objects/data_objects/terrain_tile`
    - The objects renaming: `TerrainObject` -> `TerrainTile`  
      The same with location and renaming goes for: `UnitObject`, `TriggerObject`, `EffectObject`, `ConditionObject` and `VariableObject`.
- Certain objects got their own file. 
  - `Tile`, `TriggerSelect` (Alias `TS`) and `TriggerCELock`  
    You can now import them using: `from AoE2ScenarioParser.objects.support.<filename> import <classname>`
  - The enum `GroupBy` got moved too. You can import it using: `from AoE2ScenarioParser.objects.support.enums.group_by import GroupBy`
- The way you 'hide' the status messages like: `Creating MapPiece finished successfully.` has been changed. Before you had to set a param like `log_reading` to True in the `from_file` function. Now you can do it globally through settings. So: 
  ```py
  # This will disable most console update messages
  from AoE2ScenarioParser import settings
  settings.PRINT_STATUS_UPDATES = False

  # Importing it this way WILL NOT work. Why: https://stackoverflow.com/a/10501768/7230293
  from AoE2ScenarioParser.settings import PRINT_STATUS_UPDATES
  PRINT_STATUS_UPDATES = False
  ```
- The retrievers `aa_quantity` and `aa_armor_or_attack_type` in effects were renamed to: `armour_attack_quantity` and `armour_attack_class`.

After these changes everything should function like it did before. If you used internal parts of the parser, below is a list of what you should change. Note that these are the most obvious changes. If you used very complex internal functionality, I cannot guarentee anything.

---

## Changes made to the backend that might affect your code:

**This only applies if you used code outside of the managers.**

- `Pieces` are now named `Sections`. So accessing those can be done using: `scenario.sections['name']`
- Reading has changed from hardcoded pieces to json files. So all hardcoded retrievers etc. have been removed.
- `Section` information is no longer seperated between the `FileHeader` and all compressed data.
- Section names no longer have a 'piece' suffix. These are the new names:
  - `FileHeader`, `DataHeader`, `Messages`, `Cinematics`, `BackgroundImage`, `PlayerDataTwo`, `GlobalVictory`, `Diplomacy`, `Options`, `Map`, `Units`, `Triggers`, `Files`.  
    _Please note that these may change again in the future._
- There is no longer a parser object (just a small module). Parsing is now done mostly in the appropriate objects / modules.
- The location of many scripts have changed. Most notably, `retriever`, `retriever_object_link` and `datatype` have moved.  
  From: `helper/...` to: `sections/retrievers/...`
- `Retrievers` and `Datatypes` now use the python `__slots__` property for faster access.
- Many unused helper scripts have been removed (from `datasets/helper_scripts`).
- Dependency objects all have their own files which can now be found at: `sections/dependencies/...`
  - `dependency`: General dependency functions.
  - `dependency_action`: The `DependencyAction` enum.
  - `dependency_eval`: The `DependencyEval` class.
  - `dependency_target`: The `DependencyTarget` class.
  - `retriever_dependency`: The `RetrieverDependency` class.
- The way generators work has changed. Instead of an actual python generator which runs byte-by-byte, slicing is used.
