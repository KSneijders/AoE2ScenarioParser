# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog]

---

## [Unreleased]

**Please note:** This patch includes a big backend rework. This was added through a pull request made by [pvallet]. Instead of the reconstructing phase (started when writing the new scenario file), the Pieces are directly linked to the Objects! If you find any issues please report them!

[pvallet]: https://github.com/pvallet

### Added

- `remove_condition()` and `revmove_effect()` to TriggerObject
- `get_condition()` and `get_effect()` to TriggerObject
- The index and display index to the `trigger.get_content_as_string()` 
- Four very powerful trigger features! Please check the triggers cheatsheet for the how-to.
  - `copy_trigger`
  - `copy_trigger_per_player`
  - `copy_trigger_tree`
  - `replace_player`
- **A Very much WIP** [Documentation API]

[Documentation API]: https://aoe2scenarioparser.readthedocs.io/en/master/

### Discovered (in byte structure)

- the `layer` property for terrain tiles. Used for layering terrain types.

### Changed

- Within the library the use of `\x00` character for line endings is no longer a necessity. 
  - This mainly affects checking names: (eg. `trigger.name == "name\x00"`) (Credits: Alian713)
- The parameter `trigger_id` has been renamed to `trigger_index` in all functions in TriggersObject (trigger_manager)
- Renamend `Operator` to `Operation`.
- Managers can now be accessed directly from the scenario. Eg: `scenario.trigger_manager`.
- Renamed `player` attribute in the `Condition` object to `source_player`
- Renamed `player_source` attribute in the `Effect` object to `source_player`
- Renamed `player_target` attribute in the `Effect` object to `target_player`

### Fixed

- Bug causing the local `trigger_id` attributes to be out of sync when removing triggers.
- Bug causing the `ValueError` to not get raised when trying to construct a piece with invalid data length.
- Bug causing `Conditions` and `Effects` not to show in 'get_as_string' functions when set directly using: `trigger.effects = [...]`
- Bug causing a crash when `selected_object_id` in `Effects` held a single ID. 
- Bug causing a crash when setting `selected_object_id` to an uniterable object. (Like an int instead of List[int])
- Bug causing Variables to not show up when no triggers were present when using the `get_summary_as_string` in the trigger_manager.
- Bug making it impossible to set unit IDs negative. (Supported by the game)
- Typo in Condition dataset "OWH" to "OWN" in `OWH_FEWER_OBJECTS`.

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

[Keep a Changelog]:     https://keepachangelog.com/en/1.0.0/
[Github edit Scenario]: https://github.com/KSneijders/AoE2ScenarioParser#editing-a-scenario
[T-West]:               https://github.com/twestura/
