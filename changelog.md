# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog]

---

## 0.0.7
### Added

- The `ai_script_goal` effect.
- The `difficulty_level` condition.
- The `new_unit_id_to_place` field in the `DataHeader` is updated in the reconstructing phase.
- VariableObject: `{id: ..., name: ...}`.
- Variable info to `get_content_as_string` and `get_summary_as_string` functions from the trigger_manager.
- `get_variable(id or name)` function to the trigger_manager.
- Defaults to all `effects` & `conditions`. (Editor defaults)
- PlayerColor Enum > `PlayerColor.PURPLE`.
- The ability to remove units > `unit_mamager.remove_unit(unit=... or reference_id=...)`.
- **Code Block** - Added code block for adding KOTH + Regicide to any map with (exactly) one monument - Using triggers. This code block adds close to 600 triggers for displaying all years, displaying players holding the monument and victory & defeat conditions.

### Changed

- `ChangedVariableStruct` to `VariableStruct`.
- UnitObject attribute `unit_id` renamed to `unit_const`. (Credit: [T-West])
- Effects and Condition constants are now `IntEnum`s. (ie. `Effect.CREATE_OBJECT`)
- Units, Buildings, Techs and Terrains are now `IntEnum`s. (ie. `Unit.MAN_AT_ARMS`)
- Renamed `delete_trigger` function to `remove_trigger`.
- Renamed `trigger_data` attribute to `triggers`

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

## 0.0.6
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
