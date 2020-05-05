# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog]

---

## 0.0.7
### Added

- The `ai_script_goal` effect
- The `difficulty_level` condition
- The `new_unit_id_to_place` field in the `DataHeader` is updated in the reconstructing phase
- Defaults to all `effects` & `conditions`. (Editor defaults)
- PlayerColor Enum
- **Code Block** - Added code block for adding KOTH + Regicide to any map with (exactly) one monument - Using triggers. This code block adds close to 600 triggers for displaying all years, displaying players holding the monument and victory & defeat conditions.

### Changed

- UnitObject attribute `unit_id` renamed to `unit_const` (Credit: [T-West])
- Effects and Condition constants are now `Enum`s (ie. `Effect.CREATE_OBJECT`)
- Units, Buildings, Techs and Terrains are now `Enum`s (ie. `Unit.MAN_AT_ARMS`)

### Updated

- `Snow`, `Ice, Navigable`, `Beach, Ice` in Terrain dataset. (Fixed in game)

### Fixed

- `get_new_reference_id()` returns `highest_id + 1` instead of `highest_id`
- Bug removing all `Trigger` names.
- Bug causing `Trigger display order` to be incorrect. Wasn't breaking scenarios as the in-game editor was able to handle it properly and fixed it when saving from there. Only caused the Parser from being able to read the file.

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

- `VariableChangeStruct` to `ChangedVariableStruct`.
- The object_manager function `get_x_object` to `x_manager`.
- Some `__repr__` and `__str__` are now more readable

[Keep a Changelog]:     https://keepachangelog.com/en/1.0.0/
[Github edit Scenario]: https://github.com/KSneijders/AoE2ScenarioParser#editing-a-scenario
[T-West]:               https://github.com/twestura/
