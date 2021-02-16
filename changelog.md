# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog]

---

## 0.0.20 - Unreleased

### Fixed

- Issue with reading a very rare scenario file header. Usage of the difference is unknown. 
- Issue with reading the xs script content that was saved to the scenario.
- Some small effect fields to no longer be set in a list when they were single ints.

---

## 0.0.19 - 2021-January-31

### Fixed

- Flemish Militia ID in dataset `Unit` and `UnitIcon`
- IDE autocomplete finding variables with similar names to the Enums

---

## 0.0.18 - 2021-January-31

### Added

- Icon datasets for `Units`, `Heroes` and `Buildings` (Credis: Alian713)
- `TerrainRestrictions` dataset (Used for `ObjectAttribute.TERRAIN_RESTRICTON_ID`, it defines where units can be placed/walk on) (Credis: Alian713)
- The new `Techs`, `Units` and `Buildings` added in the new [44725] update.

[44725]: https://www.ageofempires.com/news/aoeiide-update-44725/

---

## 0.0.17 - 2021-January-26

**Support for the new update!**

### Added

- Support for the new version `1.41` (Version `1.40` is still supported)

Please note that work on reading and versions is still being worked on.

---

## 0.0.16 - 2020-December-30

### Fixed

- Issue with reading bitmap image with certain sizes

---

## 0.0.15 - 2020-December-18

### Added

- Support for bitmap images (Can't be seen, used (or removed) in DE but crashed the parser if present)
- Support for legacy codec `latin-1` (Voobly converted maps). Please note that all text will be written back into `utf-8` when writing a new file.
- Units to the units dataset (Credis: Alian713)

### Updated

- Many Attribute ID names and their description and usages. (Credits: Alian713)

### Fixed

- Error while trying to debug a map with non ASCII characters
- Reading errors with specific uncommon attributes

### Changed

- Changed parameter `unit_id` to `unit_const` in the `add_unit` function

---

## 0.0.14 - 2020-November-29

### Added

- Support for AI files. Since the latest update (42848) AI files are (sometimes) stored differently

### Updated

- [HTML file] with byte structure (Download to view file. Does not contain JS. Just HTML & CSS)

[html file]: https://github.com/KSneijders/AoE2ScenarioParser/blob/master/resources/personal_docs/file_structure.html

### Fixed

- Issue with rotation on objects. Mostly affecting cliffs, certain tree types and other rotatable objects

---

## 0.0.13 - 2020-November-27

### Fixed

- Issue introduced in `0.0.12`

---

## 0.0.12 - 2020-November-27

**Support for the new update!**

**Important notice:** This version does not support older versions of the scenario files. This is temporary due to the amount of changes from the newest version (Update: 42848), sorry for the inconvience.  
When loading a map from an older version, instructions will be provided for downgrading this library or updating the scenario to the newest version.

### Added

- `create_hill` function to the map_manager (Credits: pvallet)
- **[Update 42848]** `script_name` (xs file) to the MapManager
- **[Update 42848]** The new effects!!
  - `Set Building Gather Point`
  - `Script Call`
  - `Change Object Player Color`
  - `Change Object Civilization Name`
  - `Change Object Player Name`
  - `Disable Unit Targeting`
  - `Enable Unit Targeting`
  - `Change Technology Cost`
  - `Change Technology Research Time`
  - `Change Technology Name`
  - `Change Technology Description`
  - `Enable Technology Stacking`
  - `Disable Technology Stacking`
  - `Acknowledge Multiplayer AI Signal`
  - `Disable Object Selection`
  - `Enable Object Selection`
- **[Update 42848]** The new conditions!!
  - `Script Call`
  - `Object Visible (Multiplayer)`
  - `Object Selected (Multiplayer)`
  - `Object has Action`
  - `OR`
  - `Multiplayer AI Signal`
- **[Update 42848]** `UnitAIAction` dataset
- `AttackStance` dataset

### Discovered (in byte structure)

- **[Update 42848]** The new architecture set feature
- **[Update 42848]** script (xs) file path at the end of the file

### Improved

- Defaults for the `create_default()` function when dealing with inconsistent structs

### Fixed

- Adding a trigger with extra arguments will now work properly (Example: `.add_trigger("name", description="desc")`)
- Adding a condition with extra arguments will now work properly (Example: `.add_condition(Cond.TIMER, timer=20)`)
- The 'Fix' in version `0.0.11` for the lazy loading of effect and condition display orders wasn't working properly. Now it is.

### Removed

- `number_of_units_selected` as an attribute for effects. This is now dealt with internally.

---

## 0.0.11 - 2020-November-15

### Added

- Optional arguments for `create_trigger` function (all trigger parameters except for it's internal ID)
- Optional arguments for `add_condition` function (all condition parameters)
- Optional arguments for `add_effect` function (all effect parameters)

### Improved

- Performance:
  - Writing the file, combining strings using `str.join(list)` instead of `str += str`
  - Reusing structs when reconstructing where possible, instead of overwriting all of them.
  - Not initialising RetrieverDependencies for every retriever. Using references instead.
  - Reworked the eval functions to direct code, huge performance boost
  - Removed unnecessary DependencyAction objects creation (From ~500.000 to ~100)
  - Changed trigger display order, condition display order, effect display order attribute to lazy load

### Fixed

- The `AoE2Scenario.create_default()` function. (Incorrect defaults caused the file to corrupt)

---

## 0.0.10 - 2020-November-10

### Changed

- The effect attribute `selected_object_id` to `selected_object_ids` to indicate the use of a list.

### Discovered (in byte structure)

- The `location_object_reference` property for effects. Used for targeting an object as location. For example in the `TaskObject` effect.

### Fixed

- The `AoE2Scenario.create_default()` function. (Defaults from structs weren't actually used in the parent Pieces)

---

## 0.0.9 - 2020-November-09

### Fixed

- All `copy_trigger` related functions take very long to copy per player.

---

## 0.0.8 - 2020-November-08

**Important notice:** The way you read your main file changed. It is now:

    AoE2Scenario.from_file(filename)  # Just add ".from_file". Nothing else changed :)

Also, there has been a massive change to the 'back' portion of the project. If you used this directly, you might need to change quite some code. Sorry :(. If you've got any questions, feel free to reach out. Also, if you encounter any bugs, especially in the new system, please report them! Thanks in advance! <3

### Added

- `remove_condition()` and `remove_effect()` to TriggerObject
- `get_condition()` and `get_effect()` to TriggerObject
- The index and display index to the `trigger.get_content_as_string()`
- Four very powerful trigger features! Please check the readthedocs [Documentation API], or the function docstrings for the how-to.
  - `copy_trigger`
  - `copy_trigger_per_player`
  - `copy_trigger_tree`
  - `copy_trigger_tree_per_player`
  - `replace_player`
- `commit()` function to objects. This will commit the changes to the piece structure. This is also done for all objects automatically when writing the file.
- Every object now has `RetrieverObjectLink` objects to represent how to retrieve and commit their data. (These objects also have a commit function, which are called using the objects commit function)
- The possibility to create a scenario from SCRATCH due to all pieces having default values now! No need for a 'base' scenario file from the game itself! You can achieve this like so: `AoE2Scenario.create_default()`!
- A `TriggerSelect` object. Used to identify a trigger in the trigger_manager functions. Alias: `TS`. Use Alias + class methods (factory methods) for ease of access: `TS.index(3)`, `TS.display(1)` and `TS.trigger(trigger)`.
- A `TriggerCELock` object. Used to define which (or all) conditions and effects should be locked while copying/changing players.
- A `GroupBy` Enum. For selecting the way triggers are grouped after creating them via `copy_trigger_tree_per_player`. You can choose from `NONE` (default), `TRIGGERS` and `PLAYERS`.
- **A Very much WIP** [Documentation API]

[documentation api]: https://aoe2scenarioparser.readthedocs.io/en/master/

### Discovered (in byte structure)

- the `layer` property for terrain tiles. Used for layering terrain types.

### Changed

- **The way a file is read is now done using:** `AoE2Scenario.from_file(filename)`. Nothing changed - just add "_.from_file_" between the class and the brackets :)
- Within the library the use of `\x00` character for line endings is no longer a necessity.
  - This mainly affects checking names: (eg. `trigger.name == "name\x00"`) (Credits: Alian713)
- The parameter `trigger_id` has been renamed to `trigger_index` in all functions in TriggersObject (trigger_manager)
- Renamend `Operator` to `Operation`.
- Managers can now be accessed directly from the scenario. Eg: `scenario.trigger_manager`.
- Renamed `player` attribute in the `Condition` object to `source_player`
- Renamed `player_source` attribute in the `Effect` object to `source_player`
- Renamed `player_target` attribute in the `Effect` object to `target_player`
- Renamed `find_retriever` function to `get_retriever_by_name`
- Renamed all retriever names to be lowercase underscored (Credits: pvallet)
- Progress print statements now replace their current line. So instead of using 2 lines per piece it's now 1.
- Most trigger_manager functions now require the new `TriggerSelect` object instead of 3 parameters for trigger selection. Read the docstring for more detail.

### Fixed

- Bug causing the local `trigger_id` attributes to be out of sync when removing triggers.
- Bug causing the `ValueError` to not get raised when trying to construct a piece with invalid data length.
- Bug causing `Conditions` and `Effects` not to show in 'get_as_string' functions when set directly using: `trigger.effects = [...]`
- Bug causing a crash when `selected_object_id` in `Effects` held a single ID.
- Bug causing a crash when setting `selected_object_id` to an uniterable object. (Like an int instead of List[int])
- Bug causing Variables to not show up when no triggers were present when using the `get_summary_as_string` in the trigger_manager.
- Bug making it impossible to set unit IDs negative. (Supported by the game)
- Typo in Condition dataset "OWH" to "OWN" in `OWH_FEWER_OBJECTS`.
- Typo in Terrain dataset "MAGROVE" to "MANGROVE" in `FOREST_MAGROVE`.

### Removed

- Outdated examples

---

## 0.0.7 - 2019-May-23

### Added

- The `ai_script_goal` effect.
- The `difficulty_level` condition.
- The `new_unit_id_to_place` field in the `DataHeader` is updated in the reconstructing phase.
- VariableObject: `{id: ..., name: ...}`.
- Variable info to `get_content_as_string` and `get_summary_as_string` functions from the trigger_manager.
- `get_variable(id or name)` function to the trigger_manager.
- Defaults to all `effects` & `conditions`. (In-Game Editor defaults)
- PlayerColor Enum. `PlayerColor.PURPLE`.
- The ability to remove units using `unit_mamager.remove_unit(unit=... or reference_id=...)`.
- The abiltiy to remove a trigger using an object reference: `trigger_manager.remove_trigger(trigger=...)`.
- `Hero` dataset (Credits to [T-West] for the hero name list)
- `get_enum_from_unit_const` function
- `GaiaBuilding` and `GaiaUnit` dataset (Like normal Building and Unit dataset but also includes Gaia only buildings & units)
- Datasets for (All?) dropdown lists in conditions and effects.
  - `DiplomacyState`
  - `Operator`
  - `ButtonLocation`
  - `PanelLocation`
  - `TimeUnit`
  - `VisibilityState`
  - `DifficultyLevel`
  - `TechnologyState`
  - `Comparison`
  - `ObjectAttribute`
  - `Attribute`
- **Code Block** - Added code block for adding KOTH + Regicide to any map with (exactly) one monument - Using triggers. This code block adds close to 600 triggers for displaying all years, displaying players holding the monument and victory & defeat conditions.

### Changed

- `ChangedVariableStruct` to `VariableStruct`.
- UnitObject attribute `unit_id` renamed to `unit_const`. (Credit: [T-West])
- Effects and Condition constants are now `IntEnum`s. (ie. `Effect.CREATE_OBJECT`)
- Units, Buildings, Techs and Terrains are now `IntEnum`s. (ie. `Unit.MAN_AT_ARMS`)
- Renamed `delete_trigger` function to `remove_trigger`.
- Renamed `trigger_data` attribute to `triggers`
- Reading and Writing UTF-8 instead of ASCII characters. (The game might not support all characters everywhere)

### Updated

- `Snow`, `Ice, Navigable`, `Beach, Ice` in Terrain dataset. (Fixed in game)

### Fixed

- `get_new_reference_id()` returns `highest_id + 1` instead of `highest_id`.
- Bug removing all `Trigger` names.
- Bug causing `Trigger display order` to be incorrect. Wasn't breaking scenarios as the in-game editor was able to handle it properly and fixed it when saving from there. Only caused the Parser from being able to read the file.

### Removed

- The default attributes in `Condition` and `Effect` constructors.
- The `get_triggers` function. It was redundant as it's equal to the following:
  - 0.0.6: `trigger_manager.trigger_data`
  - 0.0.7: `trigger_manager.triggers`

---

## 0.0.6 - 2019-April-20

### Added

- UnitsObject and UnitObject reconstruct support (AKA: Made Usable).
  - Check the cheatsheets on [Github edit Scenario].
- Player Enum.
- Tile object.
- Logging options for Reading, Parsing, Reconstructing and writing.
- Bidict for units, buildings and techs dataset.
- `pretty_print_name` to the Helper (Credits: [T-West]).

### Changed

- `VariableChangeStruct` to `VariableStruct`.
- The object_manager function `get_x_object` to `x_manager`.
- Some `__repr__` and `__str__` are now more readable

[keep a changelog]: https://keepachangelog.com/en/1.0.0/
[github edit scenario]: https://github.com/KSneijders/AoE2ScenarioParser#editing-a-scenario
[t-west]: https://github.com/twestura/
