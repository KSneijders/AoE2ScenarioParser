# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog]

## 0.0.7
### Added

- The `ai_script_goal` effect
- The `new_unit_id_to_place` is updated in the reconstructing phase

### Changed

- UnitObject attribute `unit_id` to `unit_const`

### Updated

- `Snow`, `Ice, Navigable`, `Beach, Ice` in Terrain dataset. (Fixed in game)

### Fixed

- `get_new_reference_id()` returns `highest_id + 1` instead of `highest_id`

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
