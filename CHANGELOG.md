# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog]
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## 0.6.7 - 2026-February-08

### Fixes

- `Area.select_entire_map()` causing alignment issues in specific use-cases
- `Area.to_chunks()` could incorrectly group multiple chunks together when the selection wasn't a square

---

## 0.6.6 - 2026-February-07

### Fixes

- Missing `global_sound` parameter in the `trigger.new_effect.play_sound(...)` function
- `xsc-ignore ...` being ignored themselves caused by added xs comments for ASP output 

---

##  0.6.5 - 2025-November-17

### Updates

- Many datasets: by [@mardaravicius] in [#101](https://github.com/KSneijders/AoE2ScenarioParser/pull/101)
  - 15 new entries to `BuildingInfo`
  - 11 new entries to `HeroInfo`
  - 11 new entries to `UnitInfo`
  - Updates many `HOTKEY_ID` values in `OtherInfo`
  - Updates many entries in `ProjectileInfo`
  - Fixes some values in `TechInfo.unique_techs(...)`
  - Renames the Maya~~ns~~ and Inca~~s~~ civilizations in `TechInfo`
  - Adds new terrains to `TerrainId`
  - Adds new techs to `LocalTechnology`
  - Updates values in `UnitInfo.unique_units(...)`
  - Updates many `HOTKEY_ID` values in `UnitInfo`
  - And more!

---

##  0.6.4 - 2025-November-03

### Fixes

- The known issue with the use of Civilization datasets in older scenarios

---

##  0.6.3 - 2025-November-01

### Fixes

- Printing triggers causing errors on older scenarios

---

##  0.6.2 - 2025-November-01

### Added

- `OptionsManager.legacy_execution_order` (When `False`: Run triggers and effects in display order)

### Fixes

- `LATEST_VERSION` not being set to `(1, 56)`
- Missing default scenario for scenario version `1.56`
- Inability to read some campaigns with inconsistent structures
- Reading scenarios with effects that are hidden in the editor

---

##  0.6.1 - 2025-October-31

### Added

- Support for the Xs-Check `v0.2.15` — View the `v0.2.15` release here: https://github.com/Divy1211/xs-check/releases/tag/v0.2.15

---

##  0.6.0 - 2025-October-15

Official support for the new 1.56 scenarios! — Credits: by [@Alian713] in [#98](https://github.com/KSneijders/AoE2ScenarioParser/pull/98)

### Added

- Updated `Civilization` dataset — in [#98](https://github.com/KSneijders/AoE2ScenarioParser/pull/98)
- Support for the Xs-Check `v0.2.14` — View the `v0.2.14` release here: https://github.com/Divy1211/xs-check/releases/tag/v0.2.14
- `JIAN_SWORDSMAN_TWO_HANDED` to `UnitInfo` — in [#98](https://github.com/KSneijders/AoE2ScenarioParser/pull/98)
- The new `issue_group_command` and `queue_action` attributes (bools) to the `Task Object` effect — in [#98](https://github.com/KSneijders/AoE2ScenarioParser/pull/98)

### Fixes

- Data trigger syntax expression priority — in [#98](https://github.com/KSneijders/AoE2ScenarioParser/pull/98)

---

##  0.5.3 - 2025-September-24

### Updates

- `ObjectAttribute` dataset (UGC Page: [Attributes](https://ugc.aoe2.rocks/general/attributes/attributes/))
  - Improves descriptions
  - **BREAKING CHANGES** — Updated Entry names 
    - `MAX_RANGE` → `MAXIMUM_RANGE`
    - `MAX_TOTAL_MISSILES` → `MAXIMUM_TOTAL_MISSILES`
    - `ABILITY_SHORT_TOOLTIP` → `ABILITY_SHORT_TOOLTIP_ID`
    - `ABILITY_EXTENDED_TOOLTIP` → `ABILITY_EXTENDED_TOOLTIP_ID`
    - `DISABLE_UNIT_FLAG` → `DISABLED_UNIT_FLAG`
- `Attribute` dataset (UGC Page: [Resources](https://ugc.aoe2.rocks/general/resources/resources/))
  - Improves descriptions
  - **BREAKING CHANGES** — Updated Entry names
    - `UNUSED_RESOURCE_029` → `ENABLE_SIEGE_CONVERSION`
    - `FOOD_MAINTENANCE` → `EFFECT_FUNCTION_NUMBER`
    - `FAITH` → `UNUSED_RESOURCE_34`
    - `FAITH_RECHARGING_RATE` → `UNUSED_RESOURCE_35`
    - `UNUSED_RESOURCE_038` → `VILLAGER_POPULATION`
    - `UNUSED_RESOURCE_69` → `FARM_FOOD_MULTIPLIER`
    - `UNUSED_RESOURCE_70` → `SOURCE_MARKET_OR_DOCK_X_COORDINATE`
    - `UNUSED_RESOURCE_71` → `SOURCE_MARKET_OR_DOCK_Y_COORDINATE`
    - `CRENELLATIONS` → `UNUSED_RESOURCE_194`
    - `UNUSED_RESOURCE_203` → `REVEAL_MAP`
    - `UNUSED_RESOURCE_204` → `REVEAL_UNIT_ON_MAP`
    - `MERCENARY_KIPCHAK_LIMIT` → `UNUSED_RESOURCE_215`
    - `SPEED_UP_BUILDING_TYPE` → `UNUSED_RESOURCE_255`
    - `SPEED_UP_BUILDING_RANGE` → `UNUSED_RESOURCE_256`
    - `SPEED_UP_PERCENTAGE` → `UNUSED_RESOURCE_257`
    - `SPEED_UP_OBJECT_TYPE` → `UNUSED_RESOURCE_258`
    - `SPEED_UP_EFFECT_TYPE` → `UNUSED_RESOURCE_259`
    - `SPEED_UP_SECONDARY_EFFECT_TYPE` → `UNUSED_RESOURCE_260`
    - `SPEED_UP_SECONDARY_PERCENTAGE` → `UNUSED_RESOURCE_261`
    - `UNUSED_RESOURCE_277` → `RED_CLIFFS_TACTICS_DAMAGE`
    - `TRIGGER_SHARED_VISIBILITY` → `SHARED_VISIBILITY`
    - `TRIGGER_SHARED_EXPLORATION` → `SHARED_EXPLORATION`
    - `UNUSED_RESOURCE_287` → `MILITARY_FOOD_PRODUCTIVITY`
    - `UNUSED_RESOURCE_288` → `PASTURE_FOOD_AMOUNT`
    - `UNUSED_RESOURCE_289` → `PASTURE_ANIMAL_COUNT`
    - `UNUSED_RESOURCE_290` → `PASTURE_HERDER_COUNT`
    - `UNUSED_RESOURCE_291` → `CHOPPING_FOOD_PRODUCTIVITY_UNUSED`
    - `UNUSED_RESOURCE_292` → `ANIMAL_DECAY_PREVENTION`
    - `UNUSED_RESOURCE_293` → `HERDER_FOOD_PRODUCTIVITY`
    - `UNUSED_RESOURCE_294` → `SHEPHERD_FOOD_PRODUCTIVITY`
  - Introduces new resources:
    - `MAXIMUM_POLEMARCHS = 501`
    - `CHOPPING_FOOD_PRODUCTIVITY = 502`
    - `TRADE_WOOD_PERCENTAGE = 503`
    - `ACHAMENIDS_TOWN_CENTER_UPGRADES = 506`
    - `BUILDING_LOOT_PRODUCTIVITY = 509`
    - `CASTLE_GOLD_PRODUCTIVITY = 521`
    - `UNKNOWN_RESOURCE_550 = 550`
    - `UNIT_LOOT_PRODUCTIVITY = 551`
### Fixes

- Data trigger combination syntax doesn't exclude area/tiles from contributing objects when area/tiles are themselves part of the data — Credits: by [@Alian713] in [#90](https://github.com/KSneijders/AoE2ScenarioParser/pull/90)
- Corrupting scenarios instead of raising an exception when data is `None` but `Retriever.repeat > 0` — Credits: by [@ougidarkness] in [#89](https://github.com/KSneijders/AoE2ScenarioParser/pull/89)

[@ougidarkness]: https://github.com/MegaDusknoir

---

##  0.5.2 - 2025-August-15

### Fixes

- Issue when writing effects when quantity was equal to -1

---

##  0.5.1 - 2025-August-14

### Added

- Support for the `caption_string` in `Unit`s

### Fixes

- Effect/Condition order now updates immediately upon removal
- Issue when writing certain effects when quantity was equal to 0
- Facet2 missing from replace object effect
- Global sound attribute not being presented as bool

---

##  0.5.0 - 2025-August-13

Official support for the new 1.55 scenarios! 

### Added

- Allow for data trigger syntax to combine types using `+` — Credits: by [@Alian713] in [#83](https://github.com/KSneijders/AoE2ScenarioParser/pull/83)
- Support for the Xs-Check `v0.2.12` — View the `v0.2.12` release here: https://github.com/Divy1211/xs-check/releases/tag/v0.2.12

### Fixes

- Flooring `None` value in effects under specific circumstances 
- Reading scenarios with triggers from previous versions
- Writing scenarios multiple times causing issues with locked `Retrievers`

---

##  0.5.0b2 - 2025-August-03

- Applied changes from [`v0.4.7`](#047---2025-august-03)

---

##  0.5.0b1 - 2025-July-23

### Added

- **Support for the new `1.55` scenario file version!**
- Support for the new Effects (and the corresponding new attributes) introduced in the last patch — Credits: by [@mardaravicius] in [#80](https://github.com/KSneijders/AoE2ScenarioParser/pull/80)
  - `trigger.new_effect.add_train_location(...)`
  - `trigger.new_effect.research_local_technology(...)`
  - `trigger.new_effect.modify_attribute_for_class(...)`
  - `trigger.new_effect.modify_object_attribute(...)`
  - `trigger.new_effect.modify_object_attribute_by_variable(...)`
- Support for the new Conditions (and the corresponding new attributes) introduced in the last patch — Credits: by [@mardaravicius] in [#80](https://github.com/KSneijders/AoE2ScenarioParser/pull/80)
  - `trigger.new_condition.local_tech_researched(...)`
- Support for the Xs-Check `v0.2.8` — View the `v0.2.8` release here: https://github.com/Divy1211/xs-check/releases/tag/v0.2.8
- The new `Trigger.execute_on_load` — Credits: by [@mardaravicius] in [#80](https://github.com/KSneijders/AoE2ScenarioParser/pull/80)
- **45** new `ObjectAttribute` entries! ([See them here](https://github.com/KSneijders/AoE2ScenarioParser/commit/420341046a3b3b9b8336ae8f89d324726cdc2dec#diff-1abd345aacaedad23f368a6e2e743ee67587737d8c35eda0562b38fb1b8baac7R753-R798))
- A new dataset `LocalTechnology` for the `local_tech_researched` condition and the `research_local_technology` effect

---

##  0.4.7 - 2025-August-03

### Fixes

- The value of `Effect.item_id` attribute being lost in specific circumstances
- Overwriting source scenario check being inverted and only triggering _when it was supposed to be disabled_.

### Improves

- Performance editing of `Trigger`/`Effect`/`Condition` lists in specific circumstances

---

##  0.4.6 - 2025-July-17

### Fixes

- References to removed triggers in Conditions/Effects not being reset to -1

---

##  0.4.5 - 2025-July-15

### Added 

- Support for the Xs-Check `v0.2.6` — View the `v0.2.6` release here: https://github.com/Divy1211/xs-check/releases/tag/v0.2.6

### Fixes

- "Active Trigger" Conditions' `trigger_id` not being updated when using TriggerManager functions for moving triggers around

---

##  0.4.4 - 2025-June-29

### Added

- New herder villagers to `UnitInfo` — Credits: by [@mardaravicius] in [#73]

### Fixed

- Incorrect `DisableUnitFlag` values — Credits: by [@mardaravicius] in [#73]

[#73]: https://github.com/KSneijders/AoE2ScenarioParser/pull/73

---

##  0.4.3 - 2025-June-27

### Added 

- `AttackPriority` dataset — Credits: by [@mardaravicius] in [#71]
  - Used in the 'Modify Attribute' effect with the 'Attack Priority' attributes
- `DisableUnitFlag` dataset — Credits: by [@mardaravicius] in [#71]
  - Used in the 'Modify Attribute' effect with the 'Disable Unit Flag' attributes
- New attributes to many datasets — Credits: by [@mardaravicius] in [#71]
  - `ObjectAttribute`
  - `CombatAbility`
  - `ChargeType`
  - `BlastLevel`
  - `ObjectClass`
  - `ProjectileVanishMode`

### Fixes

- Incorrect values in datasets from release v0.4.2 — Credits: by [@mardaravicius] in [#71]

### Updated

- Some names in `TerrainId` to reflect the in-game names — Credits: by [@mardaravicius] in [#71]

[#71]: https://github.com/KSneijders/AoE2ScenarioParser/pull/71

---

##  0.4.2 - 2025-June-23

### Added 

- `HeroInfo.trainable_heroes(...)` to retrieve heroes that can be trained in normal games (Shu, Wei & Wu) — Credits: by [@mardaravicius] in [#69](https://github.com/KSneijders/AoE2ScenarioParser/pull/69)

### Updated

There is a possibility that dataset entry names you're using have changed. If that's the case, look at [the diff](https://github.com/KSneijders/AoE2ScenarioParser/pull/70/files)
to figure out what the new names are.

- Updated many datasets to support the new units released since the 3K civs were introduced — Credits: by [@mardaravicius] in [#69](https://github.com/KSneijders/AoE2ScenarioParser/pull/69)
  - `UnitInfo`
  - `OtherInfo`
  - `BuildingInfo`
  - `HeroInfo`
  - `ProjectileInfo`
  - `TerrainId`

---

##  0.4.1 - 2025-June-19

### Added

- Support for the new Effects (and the corresponding new attributes) introduced in the last patch — Credits: by [@mardaravicius] in [#68](https://github.com/KSneijders/AoE2ScenarioParser/pull/68)
  - `trigger.new_effect.create_decision(...)`
  - `trigger.new_effect.disable_unit_attackable(...)`
  - `trigger.new_effect.enable_unit_attackable(...)`
  - `trigger.new_effect.modify_variable_by_variable(...)`
  - `trigger.new_effect.count_units_into_variable(...)`

---

##  0.4.0 - 2025-June-18

### Added

- Support for the new Conditions (and the corresponding new attributes) introduced in the last patch:
  - `trigger.new_condition.decision_triggered(...)`
  - `trigger.new_condition.object_attacked(...)`
  - `trigger.new_condition.hero_power_cast(...)`
  - `trigger.new_condition.compare_variables(...)`
  - `trigger.new_condition.trigger_active(...)`
- A new small dataset: `DecisionOption`
- 13 new `ColorMood` entries -- Credits: Goku2134 @ Discord
- 3 new flags to the OtherInfo dataset

### Dropped support

Due to limitations within the `AoE2ScenarioParser`'s versioning system, scenarios with a `trigger version` older than the 
latest `trigger version` for that `scenario version` will no longer be supported. 

Solutions: Save the scenario in-game to upgrade the scenario, or downgrade `AoE2ScenarioParser`.

**For more context, see [this Discord post](https://discord.com/channels/866955546182942740/877085102201536553/1372708645711777843)**. 

---

##  0.3.6 - 2025-May-15

### Added

- Support for the Xs-Check `v0.2.4` — View the `v0.2.4` release here: https://github.com/Divy1211/xs-check/releases/tag/v0.2.4
- New civilizations to the `Civilization` dataset (Jurchens, Khitans, Shu, Wei & Wu)

### Fixes 

- Too many triggers being selected as Data Triggers  — Credits: by [@Alian713] in [#65](https://github.com/KSneijders/AoE2ScenarioParser/pull/65)
- Incorrect usage of the `--ignores` argument for Xs-Check when using the `xs_check.ignores` set

[@Alian713]: https://github.com/Divy1211

---

##  0.3.5 - 2025-April-13

Was: `0.3.4` but got yanked due to producing corrupt scenarios

### Added

- Support for Trigger Version 4.1 that was (accidentally?) pushed with the new patch
  - (`v0.3.3` added the necessary fixes to triggers and effects... But not conditions)

---

## 0.3.3 - 2025-April-11

### Added

- Support for Trigger Version 4.1 that was (accidentally?) pushed with the new patch

---

## 0.3.2 - 2025-March-29

### Added

- Support for setting ignores on XS-Check
  - `XsManager.xs_check.ignores` is a `set` of warnings that will be ignored when processing
  - `XsManager.xs_check.additional_args` is a `list` of arguments that will be appended to the XS-Check calls
- Support for the Xs-Check `v0.2.3` — View the `v0.2.3` release here: https://github.com/Divy1211/xs-check/releases/tag/v0.2.3
- Updated many datasets to include objects from the Chronicles DLC! — Credits: by [@mardaravicius] in [#57](https://github.com/KSneijders/AoE2ScenarioParser/pull/57) 

[@mardaravicius]: https://github.com/mardaravicius

### Fixed

- Direct function calls in conditions and effects being added to the script provided to XS-Check 

---

## 0.3.1 - 2025-March-01

### Fixed

- The default scenario file not being added into the final package build

---

## 0.3.0 - 2025-March-01

### Added

_Thanks Alian for the wonderful [XS Check] library!_

- [XS Check] integration into AoE2ScenarioParser. 
  - XS Check will automatically verify all XS and show errors without having to launch the scenario! 
  - Check out the **new** [XS Check cheatsheet](https://ksneijders.github.io/AoE2ScenarioParser/cheatsheets/xs_check/) for examples and configurations!
  - Also check out the **new** [XS Check API docs](https://ksneijders.github.io/AoE2ScenarioParser/api_docs/xs/xs_check/) for everything else!
- `from_default` functionality on `AoE2DEScenario` to start working on a scenario without needing a base scenario.
  - Can be used like: `scenario = AoE2DEScenario.from_default()` instead of `scenario = AoE2DEScenario.from_file(...)`

[XS Check]: https://github.com/Divy1211/xs-check

---

## 0.2.15 - 2025-Januari-17

### Updated

- `PanelLocation` attributes updated to be consistent with in-game names
  - `PanelLocation.BETWEEN` → `PanelLocation.MIDDLE`
  - `PanelLocation.CENTER` → `PanelLocation.BOTTOM`

### Fixed

- `MapManager.map_color_mood` causing an error on write in certain conditions

---

## 0.2.14 - 2025-Januari-11

[Datasets documentation](https://ksneijders.github.io/AoE2ScenarioParser/api_docs/datasets/trigger_lists/action_type/) has been improved:

- Ordering of attributes within datasets has been matched to source instead of alphabetically.
  - So (for example) the order of ages is no longer: "Castle Age, Dark Age, Feudal Age, Imperial Age"
- Invalid links from UGC site have been filtered out

### Changed

- `MapManager.map_color_mood` will now return the `ColorMood` enum when possible

---

## 0.2.13 - 2024-December-31

Datasets are now in the API docs! [They should appear here](https://ksneijders.github.io/AoE2ScenarioParser/api_docs/datasets/trigger_lists/action_type/)!  
_(Predicting the URL)_

### Added

- Three new datasets: (For use in a `Modify Attribute` Effect with the corresponding attribute selected)
  - `BlockageClass` dataset 
  - `ObstructionType` dataset
  - `SelectionEffect` dataset

### Renamed

- `unit_action` dataset module to `unit_ai_action` — **NOT** the class itself (Was already `UnitAiAction`)
- `game_variant` dataset module to `scenario_variant` — **NOT** the class itself (Was already `ScenarioVariant`)

### Improved

- Type hinting for unit objects when accessed through `unit_manager.units`

### Fixed

- Copying triggers (using any trigger manager copy function) resulted in missing attributes on triggers / effects
- Creating units with older scenario versions

### Removed

- Legacy `BlastLevel` attributes. For more info, see this [commit description](https://github.com/KSneijders/AoE2ScenarioParser/commit/aaaaec803072f2fed714fbae27a74e8e52c9f137)

---

## 0.2.12 - 2024-November-16

### Added

- Support for the new civilizations -- Credits: [mardaravicius](https://github.com/KSneijders/AoE2ScenarioParser/pull/52)
  - `Civilization.ACHAEMENIDS = 46`
  - `Civilization.ATHENIANS = 47`
  - `Civilization.SPARTANS = 48`
- Support for the new blank technologies -- Credits: [mardaravicius](https://github.com/KSneijders/AoE2ScenarioParser/pull/52)
  - `TechInfo.BLANK_TECHNOLOGY_0` to `TechInfo.BLANK_TECHNOLOGY_19` 
- Support for the new action types -- Credits: [mardaravicius](https://github.com/KSneijders/AoE2ScenarioParser/pull/52)
  - `ActionType.LINE_FORMATION` = 18
  - `ActionType.BOX_FORMATION` = 19
  - `ActionType.STAGGERED_FORMATION` = 20
  - `ActionType.FLANK_FORMATION` = 21

### Improved

- Type hinting for triggers and some other object lists

---

## 0.2.11 - 2024-November-02

### Fixed

- Fixed the same bug corrupting scenarios - missed even more edge cases...

---

## 0.2.10 - 2024-November-02

### Fixed

- Fixed the same bug corrupting scenarios - missed other edge cases

---

## 0.2.9 - 2024-November-02

### Fixed

- Fixed a bug corrupting scenarios

---

## 0.2.8 - 2024-November-01

### Fixed

- Issues with reading older scenarios
- Issue with creating a new effect with specific combination of attributes

---

## 0.2.7 - 2024-November-01

### Added

- Support for 10 new effects:
  - `trigger.new_effect.set_object_cost(...)`
  - `trigger.new_effect.load_key_value(...)`
  - `trigger.new_effect.store_key_value(...)`
  - `trigger.new_effect.delete_key(...)`
  - _Note that the "load", "store" and "delete" key effects are campaign only_.
  - `trigger.new_effect.change_technology_icon(...)`
  - `trigger.new_effect.change_technology_hotkey(...)`
  - `trigger.new_effect.modify_variable_by_resource(...)`
  - `trigger.new_effect.modify_variable_by_attribute(...)`
  - `trigger.new_effect.change_object_caption(...)`
  - `trigger.new_effect.change_player_color(...)`
- Support for setting Player starting views:
  - `moved.player_manager.players[PlayerId.ONE].initial_player_view_x = ...`
  - `moved.player_manager.players[PlayerId.ONE].initial_player_view_y = ...`
- A new function to the `Tile` object: `tile.to_dict()` (Similar to `area.to_dict()`)
  - `Tile(4, 6).to_dict()` would result in: `{'location_x': 4, 'location_y': 6}`
- The `OptionManager` for global options in the scenario:
  - `OptionManager.victory_condition`
  - `OptionManager.victory_score`
  - `OptionManager.victory_years`
  - `OptionManager.victory_custom_conditions_required`
  - `OptionManager.secondary_game_modes`
  - `OptionManager.lock_teams`
  - `OptionManager.random_start_points`
  - `OptionManager.allow_players_choose_teams`
  - `OptionManager.collide_and_correct`
  - `OptionManager.villager_force_drop`
  - `OptionManager.lock_coop_alliances`

### Fixed

- Incorrect IDs for `BuildingInfo`: `YURT_I`, `YURT_J`, `YURT_K`, `YURT_L`

### Changed

- Deprecated two attributes in the MapManager
  - `MapManager.collide_and_correct` moved to `OptionManager.collide_and_correct`
  - `MapManager.villager_force_drop` moved to `OptionManager.villager_force_drop` 

---

## 0.2.6 - 2024-October-24

### Fixed

- Incorrect default for `caption_string_id` in `UnitManager.add_unit(...)` causing crash on scenario load in the editor

---

## 0.2.5 - 2024-October-20

### Fixed

- Error when calling `UnitManager.add_unit(...)` (missing the `caption_string_id` param)

---

## 0.2.4 - 2024-October-17

### Fixed

- Issue while reading older scenarios (pre 1.54)

---

## 0.2.3 - 2024-October-16

### Added

- Support for the **new** `Unit.caption_string_id` attribute
- Support for the 6 **new** `Effect` attributes:
  - `resource_1` & `resource_1_quantity`
  - `resource_2` & `resource_2_quantity`
  - `resource_3` & `resource_3_quantity`
- Support for the **new** `Effect` attributes in the following effects:
  - `change_object_cost`
  - `change_technology_cost`
  - This is reflected in the `trigger.new_effect.<effect>` functions and the `EffectId` documentation.
  - Example:
      ```py
      from AoE2ScenarioParser.datasets.trigger_lists import Attribute
      ...
      trigger.new_effect.change_object_cost(
          resource_1=Attribute.WOOD_STORAGE,
          resource_1_quantity=20,
          resource_2=Attribute.GOLD_STORAGE,
          resource_2_quantity=80,
      )
      ```

### Removed 

> ⚠️ BREAKING CHANGE

- Support for the `wood`, `food`, `gold` and `stone` attributes in the following effects:
  - `change_object_cost`
  - `change_technology_cost`
  - Switch to the new `resource_X` and `resource_X_value` properties
  - This is reflected in the `trigger.new_effect.<effect>` functions and the `EffectId` documentation.

---

## 0.2.2 - 2024-October-16

> _Due to earlier version release testing `0.2.0` and `0.2.1` were pushed to `test.pypi.org` blocking those versions forever... F_

### Added

- **Ability to read the new 1.54 scenarios**
  - This version is available since Update Preview 125283 (October 14, 2024)
  - ⚠️ Very limited implementation - No new features from the update have been implemented yet ⚠️ 

---

## 0.1.74 - 2024-October-10

### Added

- `r3c5` to the `ButtonLocation` dataset (`value = 15`) -- Credits: [mardaravicius](https://github.com/KSneijders/AoE2ScenarioParser/pull/49)
- `dock_page2` to the `ButtonLocation` dataset (`value += 20`) -- Credits: [mardaravicius](https://github.com/KSneijders/AoE2ScenarioParser/pull/49)
  - Example: `ButtonLocation.r1c5.dock_page2  # Result: (5 + 20) = 25`  

---

## 0.1.73 - 2024-October-05

### Added

- Placeholder Technologies to the `TechInfo` dataset -- Credits: [mardaravicius](https://github.com/KSneijders/AoE2ScenarioParser/pull/48)
  - `TechInfo.TECHNOLOGY_PLACEHOLDER_01` (Until 10 (incl))

---

## 0.1.72 - 2024-September-10

### Renamed

- The effect `CHANGE_RESEARCH_LOCATION` to `CHANGE_TECHNOLOGY_LOCATION`
  - Fixes an inconsistency with the in-game name (renamed a while ago)
  - Kept an alias of the old function `change_research_location` with deprecation warning

### Fixed

- `PlayerAttribute.<X>.editor_name` not working
  - Updated the `json` file used by the `editor_name` property to reflect the new in-game names

---

## 0.1.71 - 2024-September-07

### Added

- The `remove_triggers` function to the `TriggerManager`
  - This function doesn't break display order or changes execution order and also keeps all activation effects properly linked

### Fixed

- `scenario.actions.load_data_triggers()` function overwriting the trigger display order 

---

## 0.1.70 - 2024-August-29

### Added

- A new property to the `Area` object: `Area.maximum_coordinate`
  - Mimics the previous behaviour of `Area.map_size` (read fix below)

### Fixed

- The `Area` object returning the wrong `map_size` value (returned `map_size - 1`)
  - This also impacts multiple related functions which used it internally

---

## 0.1.69 - 2024-July-27

Many thanks to `Alian713` for all his dataset work! ❤️

### Fixed

- Outdated datasets (Updated to match UGC Guide)  (Thanks Alian)
- Internal scenario name not matching new filename on writing
  - Affected the names of data files created by XS 

---

## 0.1.68 - 2024-May-25

### Added

- Ability to register functions to run on scenario write for easier 3rd party support
  - Can be used as a `@scenario.on_write` decorator or called directly

---

## 0.1.67 - 2024-May-18

### Fixed

- Effect `change_object_civilization_name` missing the `source_player` attribute

---

## 0.1.66 - 2024-May-02

### Added

- 3 new functions to the `Area` object
  - `move()` move the selection relatively by an x/y offset
  - `move_to()` move the selection to a coordinate from on any corner of the selection
  - `is_within_bounds()` see if the selection is currently within the bounds of a map size
- 1 function to the `UnitManager`
  - `clone_unit()` clone an existing unit and only edit attributes you like to edit

### Fixed

- Missing `TechInfo.SAVAR` entry
- XS code being duplicated if it was added through the `XsManagerDE.add_script(...)` and it was called in between two `XsManagerDE.initialise_xs_trigger()` calls

---

## 0.1.65 - 2024-April-03

### Fixed

- Issue with reading scenarios with AI files

---

## 0.1.64 - 2024-March-13

### Fixed

- Default cliffs missing from `OtherInfo` dataset
  - Unit IDs: 264 to 272

---

## 0.1.63 - 2024-March-12

### Fixed

- Error on reading non-pup scenarios (since `v0.1.62`)

---

## 0.1.62 - 2024-March-06

### Added

- Ability to read the new 1.53 scenarios
  - This version is available since the pup (March 1st)
- The **new** `lock_personality` boolean to a `Player` object

---

## 0.1.61 - 2024-Januari-03

> **Dataset update!**

Many thanks to `Alian713` for all his dataset work! ❤️

### Added

- All missing units to the `UnitInfo` dataset (Centurion, Savar, Dromon etc.)
- All missing technologies to the `TechInfo` dataset (Elite monaspa, Devotion etc.)
- All missing buildings to the `BuildingInfo` dataset (Fortified Church, Mule cart, yurts, bridges etc.)
- All missing heroes to the `HeroInfo` dataset
- All missing miscellaneous objects to the `OtherInfo` dataset (Cliffs, Hunnic Horse etc.)
- All missing projectiles to the `ProjectileInfo` dataset (See changes to this dataset below)
- All missing resources to the `Attribute` dataset
- All missing attributes to the `ObjectAttribute` dataset

### Changed

- The `UnitInfo.CENTURION` (`275`) was renamed to: `UnitInfo.IMPERIAL_CENTURION`
- The `UnitInfo.LEGIONARY` (`1`) was renamed to: `UnitInfo.IMPERIAL_LEGIONARY`
- The `Attribute.EXTRA_ELEPHANT_CONVERT_RESIST` (`262`) was renamed to: `Attribute.CIVILIZATION_NAME_OVERRIDE`
- The `Attribute.UNUSED_RESOURCE_268` (`268`) was renamed to: `Attribute.HUNTER_PRODUCTIVITY`
- The `Attribute.UNUSED_RESOURCE_269` (`269`) was renamed to: `Attribute.TECHNOLOGY_REWARD_EFFECT`
- Updated a couple `ProjectileInfo` values to reflect changes in the game [[See changes](https://github.com/KSneijders/AoE2ScenarioParser/commit/6d414f953fdf72ddead5f4e781fa14408a382c7e#diff-19e7450eb9566b3db73077bd8771635eee40ae61f80f106c2622bb96186dd092)]

---

## 0.1.60 - 2023-December-29

### Fixed

- `MapManager.set_elevation(...)` When inner area is not level to the edge will result in illegal terrain elevation [#44]

[#44]: https://github.com/KSneijders/AoE2ScenarioParser/issues/44

---

## 0.1.59 - 2023-December-12

### Added

- Support for the **five** new effects added in update **99311** (11-Dec):
  - `(75) Train Unit`
  - `(76) Initiate Research`
  - `(77) Create Object Attack`
  - `(78) Create Object Armor`
  - `(79) Modify Attibute By Variable`

---

## 0.1.58 - 2023-November-08

### Fixed

- `MapManager` removing entire map when setting the map size to the same value more than once [#43]

[#43]: https://github.com/KSneijders/AoE2ScenarioParser/issues/43

---

## 0.1.57 - 2023-November-01

### Added

- Ability to read the new 1.51 scenarios (Since update on Oct 31st)
- `Armenians` and `Georgians` to the `Civilization` dataset 

---

## 0.1.56 - 2023-June-30

### Added

- Proper support for `RoR` scenarios. 
  - Scenarios can now easily be converted back and forth by doing:
    - `scenario.variant = ScenarioVariant.AOE2`
    - `scenario.variant = ScenarioVariant.ROR`
  - Note: 'Support' does **not** include any `RoR` datasets.
- Warnings for writing scenarios with an incorrect variant (like legacy variants)
- A setting to disable said warnings: `settings.SHOW_VARIANT_WARNINGS = False`

---

## 0.1.55 - 2023-May-24

### Added

- `version` attribute to the core of AoE2ScenarioParser
  - Can be used like: `from AoE2ScenarioParser import version`

### Fixed

- Issue with indices not being reset when overwriting maps [#42]
  - This issue also occurred when changing map size

### Removed

- Development logging information

[#42]: https://github.com/KSneijders/AoE2ScenarioParser/issues/42

---

## 0.1.54 - 2023-May-18

### Added

- Ability to read the new 1.49 scenarios
- `Romans` to the `Civilization` dataset 

---

## 0.1.53 - 2023-March-25

### Added

- Ability to read the new 1.48 scenarios (No functional changes found (yet))
  - This version is available since the pup released _today_ (March 25th)

---

## 0.1.52 - 2023-March-15

### Fixed

- Issue when updating `TerrainTile` list in the map manager
- Not all player resource names being present in the resource name file

---

## 0.1.51 - 2023-March-05

### Added

- `Attribute.FORAGING_WOOD_PRODUCTIVITY` -- [#40] (Alian)

### Fixed

- Warning showing more bytes were found in scenarios
  - Present since 31st of January console update with '_no functional changes_'.
- Minor docstring copypasta mistake (`VictoryTimerType`)

[#40]: https://github.com/KSneijders/AoE2ScenarioParser/pull/40

---

## 0.1.50 - 2023-January-20

### Added

- New error message for certain type of errors which might help find the cause of the issue faster.
- New unit to the `UnitInfo` dataset, named: `Sogdian Cataphract`.
- **Deprecation** warning to `scenario.remove_store_reference()`, see the docstring for more info.

### Updated

- Scenario store now uses `WeakValueDictionary` instead of normal dictionary.

### Fixed

- Multiple issues when printing an effect with `selected_object_ids` that had invalid references.
- Issue when trying to write a scenario with an effect containing an invalid effect ID.

---

## 0.1.49 - 2023-January-01

### Added

- **[API Docs (Beta)](https://ksneijders.github.io/AoE2ScenarioParser/api_docs/aoe2_scenario/)**!
- `corner1` and `corner2` attributes to the `Area` object.
- The ability to use `Area` objects without linking them to a scenario.
  - Example: `area = Area(x1=0, y1=0, x2=5, y2=5)`.
  - Example: `area = Area(corner1=Tile(0, 0), corner2=Tile(5, 5))`.

### Updated

- Warnings now use the [Python built-in warning system](https://docs.python.org/3/library/warnings.html).

### Fixed

- Issue when copying the entire terrain list to another scenario (`mm2.terrain = mm.terrain`).
- Issue when using UTF-8 characters in fixed length strings.

### Removed

- The `create_hill` function in the map manager. Use `set_elevation` instead.

---

## 0.1.48 - 2022-November-05

### Added

- More ways to get access to scenario object and its managers without having to drag them everywhere.
  - `scenario <object>.get_scenario()` i.e. `scenario = trigger.get_scenario()`
  - `scenario = AoE2DEScenario.get_scenario(obj=trigger)`
  - `scenario = AoE2DEScenario.get_scenario(name="coolname")`
    - You can set the names like this:
      1. Defaults to filename: `AoE2DEScenario.from_file('path/coolname.aoe2scenario')` (name: coolname) 
      2. Explicitely setting the name: `AoE2DEScenario.from_file('path/othername.aoe2scenario', name="myname")` (name: myname)
- Time indicators for status messages and execution time per scenario

### Fixed

- The `EnableTechnologyStacking` effect missing the `quantity` attribute.
- The `item_id` attribute not updating properly for all use cases.
- The `ChangeView` effect missing the recently added (to this effect) `quantity` field.
- An issue that occurred when reading scenarios which had the `civ` field set to `0`.
- An issue with copying `Variable` objects from one scenario to another.
- The ordering of units returned from `object` data triggers not being consistent with the condition/effect input order

---

## 0.1.47 - 2022-September-01

### Fixed

- Issues with reading new 1.47 scenario

---

## 0.1.46 - 2022-September-01

### Removed

- Development logging information

---

## 0.1.45 - 2022-August-31

**Support for the new 66692 update!** (Scenario version 1.47)

---

## 0.1.44 - 2022-August-05

### Added

- String Table ID alternatives to `MessageManager` attributes.
  - `message_manager.instructions_string_table_id = 123`

### Fixed

- `Retriever.commit_callback` wasn't called on commit causing text fields on Effects to corrupt (sometimes)
- `UnitInfo.THIRISADAI` showing as castle unit in `UnitInfo.unique_units()`

---

## 0.1.43 - 2022-August-03

### Added

- The `MessageManager` (`scenario.message_manager`)
  - The ability to change the 6 text fields in the message tab (instructions, hints, victory etc.)
  - `MessageManager` documentation: [link](https://ksneijders.github.io/AoE2ScenarioParser/cheatsheets/message/)
- The `is_dirty` attribute to retrievers to see if they were manually changed (from outside managers)
- A setting that stops managers from overwriting dirty retrievers (on by default)
  - `settings.ALLOW_DIRTY_RETRIEVER_OVERWRITE`

### Changed

- **BackEnd**: Partially rewritten construct & commit logic (slight performance improvement)
- **BackEnd**: Renamed all references to `UUID` named: `host_uuid` to just `uuid`

---

## 0.1.42 - 2022-August-01

### Fixed

- Issue with `Effect.armour_attack_class` attribute not being displayed (correctly) when printing triggers/effects
- Incorrect ID for `EffectId.DISABLE_OBJECT_DELETION`

---

## 0.1.41 - 2022-June-30

### Fixed

- `DifficultyLevel.EXTREME` is now properly available. Representing `-1` `:yFE:`
- The `quantity` field not being shown when printing the `Difficulty level` Condition when the difficulty was set to `EXTREME (-1)`
- `TechInfo.INDIANS` not being renamed to `TechInfo.HINDUSTANIS`

---

## 0.1.40 - 2022-May-18

### Improved

- Docstrings and for the PlayerAttribute (`Attribute`) dataset  (Thanks Alian)

### Fixed

- `TechInfo.unique_techs()` having a typo in `TechInfo.FABRIC_SHIELDS` tech
- `UnitInfo.unique_units()` returning the (`ELITE_`)`SHRIVAMSHA_RIDER` as castle units

---

## 0.1.39 - 2022-May-8

### Added

- **Update 61321**:
  - Techs in `TechInfo`
- Docstrings for all `ObjectAttribute` entries (Directly from the UGC Guide. Credits: Alian)
- These new datasets for the `Modify Attribute` effect:  (**Thanks to Alian, our dataset wizard**)
  - Import like: `from AoE2ScenarioParser.datasets.trigger_lists import <NAME HERE>`
  - `ChargeType`
  - `ChargeEvent`
  - `CombatAbility`
  - `FogVisibility`
  - `GarrisonType`
  - `OcclusionMode`
  - `ProjectileHitMode`
  - `ProjectileVanishMode`
  - `UnitTrait`

### Updated

- **Update 61321**:
  - `TechInfo.SULTANS` to: `TechInfo.GRAND_TRUNK_ROAD`
  - `TechInfo.INDIANS` to: `TechInfo.HINDUSTANIS`
  - Renamed dataset `SmartProjectile` to: `ProjectileSmartMode`
- Dataset documentation: [link](https://ksneijders.github.io/AoE2ScenarioParser/cheatsheets/datasets/)

### Fixed

- Issue reading some older scenarios
- Typo in `TechInfo` dataset:
  - `TechInfo.FABRIC_SHIEDS` to: `TechInfo.FABRIC_SHIELDS`
  - `TechInfo.STONE_SHADT_MINING_GOLD_GENERATION_INCREASE` to: `TechInfo.STONE_SHAFT_MINING_GOLD_GENERATION_INCREASE`
- Typo in `BlastLevel` dataset:
  - `BlastLevel.TWNETY_FIVE_PERCENT` to: `BlastLevel.TWENTY_FIVE_PERCENT`
  
### Changed

- Renamed `SmartProjectile.ENABLED` to: `ProjectileSmartMode.TARGET_FUTURE_LOCATION`
- Renamed a couple techs for consistency (Thanks Alian)
  - `HEAVY_CAV_ARCHER` to: `HEAVY_CAVALRY_ARCHER`
  - `RESOURCES_LAST_LONGER_15` to: `RESOURCES_LAST_15_PERCENT_LONGER`
  - `RESOURCES_LAST_LONGER_30` to: `RESOURCES_LAST_30_PERCENT_LONGER`
  - `RESOURCES_LAST_LONGER_40` to: `RESOURCES_LAST_40_PERCENT_LONGER`
  - `RESOURCES_LAST_LONGER_50` to: `RESOURCES_LAST_50_PERCENT_LONGER`
  - `RESOURCES_LAST_LONGER_75` to: `RESOURCES_LAST_75_PERCENT_LONGER`
  - `RESOURCES_LAST_LONGER_100` to: `RESOURCES_LAST_100_PERCENT_LONGER`
  - `RESOURCES_LAST_LONGER_125` to: `RESOURCES_LAST_125_PERCENT_LONGER`
  - `RESOURCES_LAST_LONGER_150` to: `RESOURCES_LAST_150_PERCENT_LONGER`
  - `RESOURCES_LAST_LONGER_175` to: `RESOURCES_LAST_175_PERCENT_LONGER`
  - `RESOURCES_LAST_LONGER_200` to: `RESOURCES_LAST_200_PERCENT_LONGER`
  - `RESOURCES_LAST_LONGER_300` to: `RESOURCES_LAST_300_PERCENT_LONGER`
  - `FOLWARK_HORSE_COLLAR_EXTRA` to: `HORSE_COLLAR_FOLWARK_BONUS_INCREASE`

---

## 0.1.38 - 2022-May-1

### Fixed

- Issue with reading scenario files when script name field was populated

---

## 0.1.37 - 2022-May-1

**Support for the new 61321 update!** (Scenario version 1.46)

### Added

- **Update 61321**:
  - Support for the new Conditions
    - `BUILDING_IS_TRADING`
    - `DISPLAY_TIMER_TRIGGERED`
    - `VICTORY_TIMER`
    - `AND`
  - Support for the new Effects
    - `ENABLE_OBJECT_DELETION`
    - `DISABLE_OBJECT_DELETION`
  - 19 new entries in `ObjectAttribute`
  - 24 new entries in `Attribute` (aka: 'Player Attribute' or 'Resource')
  - 15 new units to `UnitInfo`
  - 2 new buildings to `BuildingInfo`
  - 8 new heroes to `HeroInfo`
  - 7 new others to `OtherInfo` (Partially from new update)
  - New dataset: `VictoryTimerType`
- [Community documentation page](https://ksneijders.github.io/AoE2ScenarioParser/community/resources/) (WIP)

### Improved

- `UnitManager.change_ownership` now accepts a list of units as well as a single unit
  - Also improved function performance
- **BackEnd**: UnitManager read & writing logic (by a lot)

### Fixed

- Player Count shown in in-game scenario overview now updates to the amount of active players 
  - instead of not updating at all
- Typo in `Attribute` entries: 
  - `CONVERT_RESIST_MIO_ADJUSTMENT (Typo)` => `CONVERT_RESIST_MIN_ADJUSTMENT` (ID: 178)
  - `VILLAGERS_KILLED_BY_AL_PLAYER` => `VILLAGERS_KILLED_BY_AI_PLAYER` (ID: 228)

### Changed

- **Update 61321**:
  - Renamed some `ObjectAttribute` entries:
    - `ENABLE_SMART_PROJECTILES` => `PROJECTILE_SMART_MODE` (ID: 19)
    - `AMOUNT_OF_1ST_RESOURCES` => `AMOUNT_OF_1ST_RESOURCE_STORAGE` (ID: 21)
    - `BONUS_DAMAGE_RESIST` => `BONUS_DAMAGE_RESISTANCE` (ID: 24)
  - Renamed some `Attribute` entries:
    - `UNUSED_RESOURCE_096` => `NO_DROPSITE_FARMERS` (ID: 96)
    - `FEUDAL_TOWN_CENTER_LIMIT` => `EARLY_TOWN_CENTER_LIMIT` (ID: 218)
  - Renamed some `DamageClass` entries:
    - `RAMS` => `RAMS_TREBUCHETS_SIEGE_TOWERS` (ID: 17)
    - `CASTLE` => `CASTLES` (ID: 26)
    - `LEITIS` => `UNUSED_ID31` (ID: 31) -- _behaviour moved to a combat ability_
    - `CONDOTTIERO` => `CONDOTTIERI` (ID: 32)
    - `ORGAN_GUN_BULLET` => `PROJECTILE_GUNPOWDER_SECONDARY` (ID: 33) -- _no longer used by only the organ gun_
    - `FISHING_SHIP` => `FISHING_SHIPS` (ID: 34)
    - `HEROES_AND_KING` => `HEROES_AND_KINGS` (ID: 36)
    - `UNUSED_ID37` => `HUSSITE_WAGONS` (ID: 37)
- Elephant Archer from the `UnitInfo.unique_units()` function

---

## 0.1.36 - 2022-March-15

### Added

- `Attribute.X.editor_name` attribute to get the editor name as string -- [#36] (Alian)
- `scenario.remove_store_reference()` to remove the scenario reference from the store
  - Useful for when you want the scenario to be cleared by garbage collection (You also need to delete all other references to the scenario yourself)

### Fixed

- Issue with printing trigger values that are not in a dataset

### Updated

- `Attribute` dataset names & docstrings updated -- [#36] (Alian).

[#36]: https://github.com/KSneijders/AoE2ScenarioParser/pull/36

---

## 0.1.35 - 2022-March-3

### Fixed

- Issue introduced after the `0.1.33` fix. 
  - `XS Manager` was trying to create a `script call` effect regardless if the scenario supported it or not.

---

## 0.1.34 - 2022-March-1

### Fixed

- Issue with deepcopying `UuidList`s. (Causing issues with trigger importing). 

---

## 0.1.33 - 2022-February-21

### Fixed

- Issue with `XS Manager` not copying the script content to the right trigger object. 

---

## 0.1.32 - 2022-February-04

### Fixed

- Issue with type hinting `trigger.new_effect` and `trigger.new_condition`

---

## 0.1.31 - 2022-February-02

**Support for the new 58259 update!**   

### Added 

- **The new `Data Triggers` functionality!** A powerful tool to communicate information from in-game to the parser!
  - You can find the `Data Triggers` cheatsheet [here](https://ksneijders.github.io/AoE2ScenarioParser/cheatsheets/data_triggers/)!
- `message` field to the `modify_attribute` effect.

### Improved

- `Area.to_chunks()` function is now **A LOT** faster in certain situations (sometimes 40x faster!)

### Fixed

- Issue with reading the new scenario files (since update 58259, 31-Jan-22)
- Issue with imported triggers not being deep-copied and causing reference problems
- Issue with copied triggers not being able to use `new_effect` and `new_condition`
- Issue where `get_unit_in_area` params `x2` and `y2` were considered exclusive 
  - Locations: `(0, 0), (3, 3)` would be considered like: `(0, 0), (2, 2)`

---

## 0.1.30 - 2022-January-04

### Fixed

- Issue with reading older scenarios (older than 1.40)

---

## 0.1.29 - 2022-January-03

**Happy new year!**

### Added

- **The `Area` object! A powerful object for area management!**
  - You can find the `Area` cheatsheet [here](https://ksneijders.github.io/AoE2ScenarioParser/cheatsheets/area/)!
- `tile` parameter to add_unit (Overwrites given x & y values)
- `SectionName` enum for easier access to scenario sections

### Fixed

- Issue with reading armor/attack values in some effects.
- (Possibly) Worked around issue caused by a bug in Python from 3.8.6 to 3.9.1 (Fixed in 3.9.2)
- Renamed `TerrainTile` attribute `index` to `_index` (Index value should be retrieved through the attribute: `i`)
- Issue where `typing_extensions` wasn't downloaded automatically through pypi (pip)
- Final print statement not ending with a newline

### Changed

- `i_to_xy` function returns named tuple. Can now **also** access the coords using `.x` and `.y`
- `Tile` object to be (simple) (x, y) `NamedTuple` instead of an entire object
  - Note: This is not about `TerrainTile` objects from the Map Manager.

---

## 0.1.28 - 2021-November-19

### Added

- Missing `MINUTES_AND_SECONDS` to `TimeUnit`

### Fixed

- Module `typing_extensions` not in requirements.txt

---

## 0.1.27 - 2021-November-19

**Support for the new 56005 update!**   

### Added

- Support for the **1.45** scenario files!
- The **Player Manager**!
  - Allows access to many player related attributes like resources, civ, disables, diplomacy and more!
  - Check the [player manager cheatsheet](https://ksneijders.github.io/AoE2ScenarioParser/cheatsheets/players/) for more info!
- Error when overwriting the source scenario (with a setting to disable this behaviour)
  - `settings.DISABLE_ERROR_ON_OVERWRITING_SOURCE` (`False` by default)
- `map_manager.set_elevation()`
  - A new function which superseeds the `create_hill` function as it can create hills and holes
  - **Note:** `elevation` is now the first argument, instead of the last
  - Deprecation warning to the `create_hill` function
- `map_manager.terrain_2d`
  - A property which returns the map in a 2D list.
  - **Note:** This is calculated for each request so it's recommended to call it once and store it
- `map_manager.get_tile_safe()`
  - Same as `get_tile` except it won't throw an `IndexError` when the tile cannot be found.  
  Instead, it returns `None`
- Datasets from the nitpicked pull: [#18] (newtonerdai).
  - `StartingAge`
  - `Civilization`
- `ColorId` dataset for setting the player color in the player manager
- The palisade gate to the building dataset (`BuildingInfo.PALISADE_GATE`) for disabling the palisade gate

### Improved 

- Datasets printed through a trigger content string can be individually customized

### Fixed

- Swapped incorrect `object_visible_multiplayer` and `object_selected_multiplayer` effect IDs
- Issue with reading legacy scenarios that had units selected in effects 
- `TechInfo.unique_techs` returning an empty list by default

### Changed

- Renamed the `TerrainId.CORRUPTION` to `TerrainId.VERY_EVIL_FOG` to resemble the actual in-game name.
- **BackEnd**: Renamed the retriever: `player_names` to `tribe_names` to resemble the in-game input field label.
- **BackEnd**: UUID functions have been moved to getters and actions modules

### Uncovered structures in the scenario file

- Many structures in the structure files for future use. Nitpicked from pull: [#18] (newtonerdai)
  - `per_player_lock_civilization`
  - `lock_teams`
  - `allow_players_choose_teams`
  - `random_start_points`
  - `max_number_of_teams`
  - `per_player_base_priority`
  - `editor_camera_x & y`
  - `initial_camera_x & y`
- Properly added a new structure from the 1.44 version update
  - `per_player_population_cap`

[#18]: https://github.com/KSneijders/AoE2ScenarioParser/pull/18

---

## 0.1.26 - 2021-October-01

### Fixed

- `effect.selected_object_ids` got reset when using `trigger_manager.get_content_as_string()`

---

## 0.1.25 - 2021-September-29

### Fixed

- Issue with reading certain scenarios which contained legacy bitmap images
- Issue where requesting TriggerManager content string would crash due to an unknown unit

---

## 0.1.24 - 2021-September-25

**Updated the minimum requirements to python 3.8 & Support for the new PUP September Scenarios!!**

### Added

- Support for the new `1.44` scenario version in the current September PUP beta on steam. **(Work in Progress)**
- A cheatsheet for the Map Manager [link](https://ksneijders.github.io/AoE2ScenarioParser/cheatsheets/map/)!
- Scenarios now have a `UUID`. This is used for easy access to information through the entire library.  
This allowed the following:
  - `variable: 0` now shows as: `variable: "NumberOfAttempts" (0)`
  - `trigger_id: 1` now shows as: `trigger_id: "Move units" (1)`
  - `location_object_reference: 222` now shows as:
    ```
    location_object_reference: 1 unit:
        0: Camel Rider [P1, X50.5, Y67.5] (222)
    ```
  - `selected_object_ids: [21, 22]` now shows as: 
    ```
    selected_object_ids: 2 units:
        0: Berserk [P1, X65.5, Y74.5] (21)
        1: Berserk [P1, X66.5, Y75.5] (22)
    ```
- New properties to the `TerrainTile` object
  - `x`:  Get it's X coordinate
  - `y`:  Get it's Y coordinate
  - `xy`:  Get a tuple of it's XY coordinates
  - `i`:  Get it's index
- New functions to the map manager:
  - `get_tile(x=.., y=..)` or `get_tile(i=..)`
  - `get_square_1d(x1, y1, x2, y2)` and `get_square_2d(x1, y1, x2, y2)`  
  Get a square of tiles in a 1D or 2D list.

### Updated

- `unit_manager.get_new_reference_id()` will now pull from a number generator instead of searching the entire unit list.

### Fixed

- Functions `xy_to_i` and `i_to_xy` having the x and y coordinate reversed.
- `bidict` still being imported while not being a dependency anymore
- Changing the map size linked all new terrain tiles to the same object
- Error being raised when importing `ProjectileInfo`
- `TimeUnit` dataset values `Years` and `Seconds` being the wrong way around.

### Removed

- `object_location_reference` attribute from the `patrol` effect as it doesn't work in game.

---

## 0.1.23 - 2021-September-09

### Added

- Warning about python minimum requirement being moved from `3.6` to `3.8`.
- Setting to disable the python minimum requirement warning.

### Fixed

- Issue caused by referencing unit IDs not included in the datasets

---

## 0.1.22 - 2021-September-08

### Added

- The **XS Manager**.
  - Can be used to add XS to a script call effect. This way XS can be transfered between lobbies.
  - Check out the XS cheatsheet [here](https://ksneijders.github.io/AoE2ScenarioParser/cheatsheets/xs/)!
- A **Hello World** example for the parser. You can find it [here](https://ksneijders.github.io/AoE2ScenarioParser/hello_world/).
- `__str__` functions to `TriggerManaer`, `Trigger`, `Effect` and `Condition`
  - You can now do: `print(trigger_manager)` instead of `print(trigger_manager.get_content_as_string())`
- Value representations in `get_content_as_string()`. Shows dataset numerical values as dataset names.
  - `object_list_unit_id: 4` now shows as: `object_list_unit_id: Archer (4)`
  - `technology: 12` now shows as: `technology: Crop Rotation (12)`
  - `operation: 3` now shows as: `operation: Subtract (3)`
- Swapping coords when adding effects/conditions with `x1`>`x2` or `y1`>`y2` + warning about it.
- 5 New functions to `TechInfo` (all with filter params). -- [#31] (Alian713)
  - `blacksmith_techs()`
  - `university_techs()`
  - `monastery_techs()`
  - `town_center_techs()`
  - `eco_techs()`
- `Age` dataset to `trigger_lists`. -- [#31] (Alian713)
- `MAIN_CHARSET` and `FALLBACK_CHARSET` to the settings.
  - Can be used to read scenario text in other charsets than the default `utf-8` and `latin-1` fallback.

[#31]: https://github.com/KSneijders/AoE2ScenarioParser/pull/31

### Fixed

- Typo - `SmartPorjectile` to `SmartProjectile`
- Missing several parameters for specific effects and conditions in `new_effect` and `new_condition`
- Missing several attributes for specific effects and conditions when using `get_content_as_string()`
- `effect.player_color` resulting in the wrong color when assigned using `PlayerId` or `PlayerColorId`
- Functions in `unit_manager` requiring `PlayerId`. Just an `int` is also possible now.
- Issue with resizing the map.
- Issue with importing triggers that had activation effects referencing triggers that were not imported.

### Moved

- The `script_name` (for XS scripts) attribute from the `MapManager` to the `XsManager`

### Removed

- The `BiDict` dependency from the entire project

---

## 0.1.21 - 2021-August-28

Special thanks to **Alian** for his contribution to the datasets! <3

### Added

- Units, Buildings and Techs to the datasets. -- [#30] (Alian713)
- Three new functions (**Which all keep `(de)activate trigger` effects synced!**)
  - `move_triggers(trigger_ids, insert_index)` function to the `Trigger Manager`.
  - `reorder_triggers(new_id_order)` function to the `Trigger Manager`.
  - `import_triggers(triggers, index)` function to the `Trigger Manager`.

### Updated

- Tech & Unit datasets -- [#30] (Alian713)
- Docstrings for all Attribute resources. -- [#30] (Alian713)

### Fixed

- Desync issues with `(de)activate trigger` effects when using any of the following functions:
  - `group_triggers_by` parameter in `copy_trigger_tree_per_player`,
  - `append_after_source` parameter in `copy_trigger`,
  - `remove_trigger` function.

[#30]: https://github.com/KSneijders/AoE2ScenarioParser/pull/30

---

## 0.1.20 - 2021-August-17

### Fixed

-  `GroupBy` mechanics when using `copy_trigger_tree_per_player` function.

---

## 0.1.19 - 2021-August-16

### Added

- The `append_after_source` parameter to the `copy_trigger` function.
- The `add_suffix` parameter to the `copy_trigger` function. Decides if `" (copy)"` is added to the name.
- QOL feature for the creation of `Effects` and `Conditions`.
  - When not using `area_x2` and `area_y2`, they are set to the values of `area_x1` and `area_y1` respectively.
    This makes selecting a single tile a little easier.
- A list functions to the `TerrainId` dataset.
  - `water_terrains()` for all water terrains.
  - `beach_terrains()` for all beach terrains.
  - `tree_terrains()` for all tree terrains.
- A list function to the `OtherInfo` dataset.
  - `OtherInfo.trees()` for all tree objects.

### Updated

- Projectiles dataset with `houfnice` and `hussite wagon` projectiles.

### Fixed

- Multiple new issues with the famous `\x00` (end of line) character.
- The `copy_trigger_per_player` and `copy_trigger_tree_per_player` functions.
- Units and Techs in `UnitInfo` and `TechInfo` dataset.

### Removed

- Type checks from `UnitInfo` and `TechInfo` filter functions.
- The parameter `item_id` from the `new_effect` functions as it's unused in the editor.

---

## 0.1.18 - 2021-August-12

**Support for the new 51737 update!**   
Special thanks to **Alian** for his contribution with the datasets! <3

### Added

- Support for the new `1.43` scenario file version.
- New Units, Buildings, Heroes etc. from the `51737` patch! -- [#28] (Alian713)
- Added `append_after_source` parameter to `copy_trigger` function.

[#28]: https://github.com/KSneijders/AoE2ScenarioParser/pull/28

---

## 0.1.17 - 2021-August-08

### Added

- `filter_units_by_const()` function to the unit_manager. ([check the docs for examples](https://aoe2scenarioparser.readthedocs.io/en/master/cheatsheets/units.html#select-existing-units))
- `PlayerId.all()` function. ([check these docs for examples](https://aoe2scenarioparser.readthedocs.io/en/master/cheatsheets/datasets.html#players))

### Updated

- All `TriggerManager` functions now accept an `int` as well as `TriggerSelect`.
  - `get_trigger(TS.index(i))` is now equal to: `get_trigger(i)`.
- Docs with a link to the newly created Discord server!

### Fixed

- Fixed issue with `remove_effect` and `remove_condition` in display order arrays.
- Fixed issue with specific `modify_attribute` effect combination.

---

## 0.1.16 - 2021-August-06

### Fixed

- Type validation in dataset functions. -- [#25] (Alian713)
- Issue with creating modify_attribute effect.

[#25]: https://github.com/KSneijders/AoE2ScenarioParser/pull/25

---

## 0.1.15 - 2021-August-02

### Added

- **Alian713** as an author! **The dataset wizard!**
- Filters to dataset functions. -- [#22] (Alian713)
- `CORRUPTION` and many `MODDABLE...` to the `TerrainId` dataset. -- [#24] (Alian713)

### Improved

- Doc strings, error messages and type annotations for datasets. -- [#24] (Alian713)

### Fixed

- Issue with order lists updating when directly removing items from the list (using `.pop()` or `.remove()`)
- Issue with reading `1.40` maps.

[#22]: https://github.com/KSneijders/AoE2ScenarioParser/pull/22
[#24]: https://github.com/KSneijders/AoE2ScenarioParser/pull/24

---

## 0.1.14 - 2021-July-26

### Fixed

- Issue with converting `armour_attack_quantity` and `armour_attack_class` inside the parser.
- Some missing attributes for the newly added effect and condition attribute. 

---

## 0.1.13 - 2021-July-17

### Fixed

- Issue with displaying `armour_attack_quantity` and `armour_attack_class` as `None` in `get_content_as_string()`.
- Issue with writing scenarios where `quality` was non truthy but not `None`.

---

## 0.1.12 - 2021-July-16

### Added

- Support for the old `1.36` scenario file version. (Used for many campaign scenarios)
- Colourful print statements!
- Warnings for certain situations.

### Fixed

- Issue with the `quantity` field with the effect `Modify Attribute` when choosing attribute `Attack` or `Armor`.
- Issue in manager construction phase while loading older scenarios.
- Issue with when committing `RetrieverObjectLink` with `support` attribute.

### Reworked (backend)

Only useful if you're working with the 'sections' parts of the parser:

- The `armour_attack_quantity` and `armour_attack_class` fields have been removed from the sections (structure file). 
They are still available in the effect object, and are split using bitwise operations in the `Effect` object itself.

---

## 0.1.11 - 2021-July-08

### Fixed

- Issue with adding effects to any trigger [Issue #21].

[issue #21]: https://github.com/KSneijders/AoE2ScenarioParser/issues/21

---

## 0.1.10 - 2021-July-08

**Support for the new 50292 update!**

### Added 

- Support for the new `1.42` scenario file version.
- The new attribute for conditions: `object_state` (Used in `objects_in_area`)
- The new `ChangeColorMood` effect (`trigger.new_effect.change_color_mood(...)`).
- The `ColorMood` and `ObjectState` dataset. 

---

## 0.1.9 - 2021-June-02

**More datasets! Including some from the newest [47820] update!**

[47820]: https://www.ageofempires.com/news/aoe2de-update-47820/

### Added

- The `HOTKEY_ID` property to the `UnitInfo`, `BuildingInfo`, `HeroInfo` and `TechInfo`.  
  Example: `UnitInfo.ARCHER.HOTKEY_ID`. Or: `UnitInfo.from_hotkey_id(...)`
- The `Hotkey` dataset. These values can be used for static key assignments.
- The `HeroStatusFlag` dataset. Use `HeroStatusFlag.combine(...)` for combinations in the dataset.
- The `BlastLevel` dataset.
- The `DamageClass` dataset. (Credits: Alian713)
- The `ProjectileInfo` dataset. Thanks **[Alian713](https://github.com/KSneijders/AoE2ScenarioParser/pull/16)**!

### Fixed

- Removed `location_object_reference` from the `Change View` effect.
- Trigger docs not updated with the new `UnitInfo` dataset. 
- `Unit.name()` when a unit wasn't present in the datasets. Thanks **[newtonerdai](https://github.com/KSneijders/AoE2ScenarioParser/pull/13)**!
- The ID for `FARMING_GOLD_TRICKLE` from 235 to 236.
- A typo `TechInfo.FELMISH_REVOLUTION` to `TechInfo.FLEMISH_REVOLUTION`

### Changed

- Renamed ObjectAttribute `ICON_GRAPHICS_ANGLE` to `GRAPHICS_ANGLE`.
- Renamed all `area_1_x` attributes to `area_x1`. Same goes for: `area_1_y`, `area_2_x`, `area_2_y`.
- **BACKEND** - retrievers attribute on sections has been swapped out for retriever_map.  
  It's now a `dict` instead of a `list` with the retriever name as keys. Reason: **Improve performance**.

---

## 0.1.8 - 2021-May-01

### Updated

- Several speed improvements

### Fixed

- Hint in exception message when it was clearly not the cause of the error.
- A typo in the condition dataset `OBJECT_IN_AREA` to `OBJECTS_IN_AREA`.
- Unit docs not updated with the new `UnitInfo` dataset - [Issue #12].

[issue #12]: https://github.com/KSneijders/AoE2ScenarioParser/issues/12

---

## 0.1.7 - 2021-April-05

### Added

-   Functions to the `UnitInfo` and `TechInfo` dataset.
    -   `UnitInfo.vils()` for all villagers (Male/Female and all their professions).
    -   `UnitInfo.unique_units()` for all unique units (Both castle and non castle unique units).
    -   `TechInfo.unique_techs()` for all unique technologies.
-   Error messages when accidently setting a value to `UnitInfo.ARCHER` instead of `UnitInfo.ARCHER.ID` (as an example).

### Fixed

-   A recursion issue with the `copy_trigger` related functions - [Issue #10]

[issue #10]: https://github.com/KSneijders/AoE2ScenarioParser/issues/10

---

## 0.1.6 - 2021-April-01

### Fixed

-   An issue which renamed all variables to: "VariableStruct" - [Issue #9]

[issue #9]: https://github.com/KSneijders/AoE2ScenarioParser/issues/9

### Changed

-   The datasets `UnitInfo`, `BuildingInfo`, `HeroInfo`, `TechInfo` and `OtherInfo` replace the following datasets:
    -   UnitId, GaiaUnitId, UnitIcon and GaiaUnitIcon
    -   BuildingId, GaiaBuildingId and BuildingIcon
    -   HeroId, HeroIcon
    -   TechId
    -   UnitOtherId, GaiaUnitOtherId
-   The `ButtonLocation` dataset has changed it's properties.
    -   From: `LOCATION_<C>_<R>` (`<C>` = Column number, `<R>` = Row number)
    -   To: `r<R>c<C>`
    -   Example (Row 1, col 4):
        -   Old: `LOCATION_3_0`. Old numbering started from 0.
        -   New: `r1c4`. New numbering starts from 1.

Please check the [datasets cheatsheet] page or the [readthedocs dataset] page on how to use the new datasets.

[datasets cheatsheet]: https://github.com/KSneijders/AoE2ScenarioParser/blob/master/cheatsheets/DATASETS.md
[readthedocs dataset]: https://aoe2scenarioparser.readthedocs.io/en/master/

---

## 0.1.5 - 2021-March-27

### Fixed

-   An issue with `\x00` suffixes

---

## 0.1.4 - 2021-March-27

### Fixed

-   An issue looking up the `.json` files on non-windows machines.

---

## 0.1.3 - 2021-March-27

### Fixed

-   An issue with relative directories when accessing `.json` structure files.

---

## 0.1.2 - 2021-March-27

### Fixed

-   An issue with pip not uploading non `*.py` files.

---

## 0.1.1 - 2021-March-26

### Fixed

-   Issue with pip not finding the packages due to removing `__init__.py` in `0.1.0`

### Changed

-   Renamed `amount_or_quantity` to `quantity` in conditions for consistentcy with effects.
-   Renamed `resource_type_or_tribute_list` to `attribute` in conditions.
-   Renamed `variable_or_timer` to `timer` in effects because it wasn't used for variables.
-   Renamed `from_variable` to `variable` in effects for consistentcy with conditions.
-   Renamed `enabled_or_victory` to `enabled` in effects.

---

## 0.1.0 - 2021-March-25

**IMPORTANT NOTICE:** A lot about the library has changed internally. Switching from `0.0.20` to `0.1.0` should only require you to implement a [couple of important changes].  
Click the link on the line above to find said changes. If you find any bugs please report them on github.

[couple of important changes]: https://github.com/KSneijders/AoE2ScenarioParser/blob/master/resources/md/update_to_0.1.0.md

**SPEED:** This release _should_ improve average reading and writing speed. Some tested scenarios had a read speed improvement of over 15x when using large AI or other text files. Average reading time will be around 20 to 40 percent faster. Writing time has increased significantly too. Maps with large amount of data have around 700% (7x faster) increase in writing time!

### Other changes:

These changes were in the works for `0.0.21` but got merged into the `0.1.0` relesase.

### Added

-   All villagers to the `Unit` dataset as: `VILLAGER_<SEX>[_<PROFESSION>]`
-   A handful of other units to the `Unit` dataset

### Changed

-   Renamed `FLEMISH_MILITIA_M` and `FLEMISH_MILITIA_F` to `FLEMISH_MILITIA_MALE` and `FLEMISH_MILITIA_FEMALE`

### Removed

-   The old names used for villagers (e.g. `BUILDER` or `HUNTER`). (These were male only)
-   The BiDict variable `unit_names`, because the same effect can be achieved using the `.name` attributes in the dataset.
-   The `scenario.create_default()` function.

---

## 0.0.20 - 2021-February-17

### Fixed

-   Issue with reading a very rare scenario file header. Usage of the difference is unknown.
-   Issue with reading the xs script content that was saved to the scenario.
-   Some small effect fields to no longer be set in a list when they were single ints.

---

## 0.0.19 - 2021-January-31

### Fixed

-   Flemish Militia ID in dataset `Unit` and `UnitIcon`
-   IDE autocomplete finding variables with similar names to the Enums

---

## 0.0.18 - 2021-January-31

### Added

-   Icon datasets for `Units`, `Heroes` and `Buildings` (Credis: Alian713)
-   `TerrainRestrictions` dataset (Used for `ObjectAttribute.TERRAIN_RESTRICTON_ID`, it defines where units can be placed/walk on) (Credis: Alian713)
-   The new `Techs`, `Units` and `Buildings` added in the new [44725] update.

[44725]: https://www.ageofempires.com/news/aoeiide-update-44725/

---

## 0.0.17 - 2021-January-26

**Support for the new update!**

### Added

-   Support for the new version `1.41` (Version `1.40` is still supported)

Please note that work on reading and versions is still being worked on.

---

## 0.0.16 - 2020-December-30

### Fixed

-   Issue with reading bitmap image with certain sizes

---

## 0.0.15 - 2020-December-18

### Added

-   Support for bitmap images (Can't be seen, used (or removed) in DE but crashed the parser if present)
-   Support for legacy codec `latin-1` (Voobly converted maps). Please note that all text will be written back into `utf-8` when writing a new file.
-   Units to the units dataset (Credis: Alian713)

### Updated

-   Many Attribute ID names and their description and usages. (Credits: Alian713)

### Fixed

-   Error while trying to debug a map with non ASCII characters
-   Reading errors with specific uncommon attributes

### Changed

-   Changed parameter `unit_id` to `unit_const` in the `add_unit` function

---

## 0.0.14 - 2020-November-29

### Added

-   Support for AI files. Since the latest update (42848) AI files are (sometimes) stored differently

### Updated

-   [HTML file] with byte structure (Download to view file. Does not contain JS. Just HTML & CSS)

[html file]: https://github.com/KSneijders/AoE2ScenarioParser/blob/master/resources/personal_docs/file_structure.html

### Fixed

-   Issue with rotation on objects. Mostly affecting cliffs, certain tree types and other rotatable objects

---

## 0.0.13 - 2020-November-27

### Fixed

-   Issue introduced in `0.0.12`

---

## 0.0.12 - 2020-November-27

**Support for the new update!**

**Important notice:** This version does not support older versions of the scenario files. This is temporary due to the amount of changes from the newest version (Update: 42848), sorry for the inconvience.  
When loading a map from an older version, instructions will be provided for downgrading this library or updating the scenario to the newest version.

### Added

-   `create_hill` function to the map_manager (Credits: pvallet)
-   **[Update 42848]** `script_name` (xs file) to the MapManager
-   **[Update 42848]** The new effects!!
    -   `Set Building Gather Point`
    -   `Script Call`
    -   `Change Object Player Color`
    -   `Change Object Civilization Name`
    -   `Change Object Player Name`
    -   `Disable Unit Targeting`
    -   `Enable Unit Targeting`
    -   `Change Technology Cost`
    -   `Change Technology Research Time`
    -   `Change Technology Name`
    -   `Change Technology Description`
    -   `Enable Technology Stacking`
    -   `Disable Technology Stacking`
    -   `Acknowledge Multiplayer AI Signal`
    -   `Disable Object Selection`
    -   `Enable Object Selection`
-   **[Update 42848]** The new conditions!!
    -   `Script Call`
    -   `Object Visible (Multiplayer)`
    -   `Object Selected (Multiplayer)`
    -   `Object has Action`
    -   `OR`
    -   `Multiplayer AI Signal`
-   **[Update 42848]** `UnitAIAction` dataset
-   `AttackStance` dataset

### Discovered (in byte structure)

-   **[Update 42848]** The new architecture set feature
-   **[Update 42848]** script (xs) file path at the end of the file

### Improved

-   Defaults for the `create_default()` function when dealing with inconsistent structs

### Fixed

-   Adding a trigger with extra arguments will now work properly (Example: `.add_trigger("name", description="desc")`)
-   Adding a condition with extra arguments will now work properly (Example: `.add_condition(Cond.TIMER, timer=20)`)
-   The 'Fix' in version `0.0.11` for the lazy loading of effect and condition display orders wasn't working properly. Now it is.

### Removed

-   `number_of_units_selected` as an attribute for effects. This is now dealt with internally.

---

## 0.0.11 - 2020-November-15

### Added

-   Optional arguments for `create_trigger` function (all trigger parameters except for it's internal ID)
-   Optional arguments for `add_condition` function (all condition parameters)
-   Optional arguments for `add_effect` function (all effect parameters)

### Improved

-   Performance:
    -   Writing the file, combining strings using `str.join(list)` instead of `str += str`
    -   Reusing structs when reconstructing where possible, instead of overwriting all of them.
    -   Not initialising RetrieverDependencies for every retriever. Using references instead.
    -   Reworked the eval functions to direct code, huge performance boost
    -   Removed unnecessary DependencyAction objects creation (From ~500.000 to ~100)
    -   Changed trigger display order, condition display order, effect display order attribute to lazy load

### Fixed

-   The `AoE2Scenario.create_default()` function. (Incorrect defaults caused the file to corrupt)

---

## 0.0.10 - 2020-November-10

### Changed

-   The effect attribute `selected_object_id` to `selected_object_ids` to indicate the use of a list.

### Discovered (in byte structure)

-   The `location_object_reference` property for effects. Used for targeting an object as location. For example in the `TaskObject` effect.

### Fixed

-   The `AoE2Scenario.create_default()` function. (Defaults from structs weren't actually used in the parent Pieces)

---

## 0.0.9 - 2020-November-09

### Fixed

-   All `copy_trigger` related functions take very long to copy per player.

---

## 0.0.8 - 2020-November-08

**Important notice:** The way you read your main file changed. It is now:

    AoE2Scenario.from_file(filename)  # Just add ".from_file". Nothing else changed :)

Also, there has been a massive change to the 'back' portion of the project. If you used this directly, you might need to change quite some code. Sorry :(. If you've got any questions, feel free to reach out. Also, if you encounter any bugs, especially in the new system, please report them! Thanks in advance! <3

### Added

-   `remove_condition()` and `remove_effect()` to TriggerObject
-   `get_condition()` and `get_effect()` to TriggerObject
-   The index and display index to the `trigger.get_content_as_string()`
-   Four very powerful trigger features! Please check the readthedocs [Documentation API], or the function docstrings for the how-to.
    -   `copy_trigger`
    -   `copy_trigger_per_player`
    -   `copy_trigger_tree`
    -   `copy_trigger_tree_per_player`
    -   `replace_player`
-   `commit()` function to objects. This will commit the changes to the piece structure. This is also done for all objects automatically when writing the file.
-   Every object now has `RetrieverObjectLink` objects to represent how to retrieve and commit their data. (These objects also have a commit function, which are called using the objects commit function)
-   The possibility to create a scenario from SCRATCH due to all pieces having default values now! No need for a 'base' scenario file from the game itself! You can achieve this like so: `AoE2Scenario.create_default()`!
-   A `TriggerSelect` object. Used to identify a trigger in the trigger_manager functions. Alias: `TS`. Use Alias + class methods (factory methods) for ease of access: `TS.index(3)`, `TS.display(1)` and `TS.trigger(trigger)`.
-   A `TriggerCELock` object. Used to define which (or all) conditions and effects should be locked while copying/changing players.
-   A `GroupBy` Enum. For selecting the way triggers are grouped after creating them via `copy_trigger_tree_per_player`. You can choose from `NONE` (default), `TRIGGERS` and `PLAYERS`.
-   **A Very much WIP** [Documentation API]

[documentation api]: https://aoe2scenarioparser.readthedocs.io/en/master/

### Discovered (in byte structure)

-   the `layer` property for terrain tiles. Used for layering terrain types.

### Changed

-   **The way a file is read is now done using:** `AoE2Scenario.from_file(filename)`. Nothing changed - just add "_.from_file_" between the class and the brackets :)
-   Within the library the use of `\x00` character for line endings is no longer a necessity.
    -   This mainly affects checking names: (e.g. `trigger.name == "name\x00"`) (Credits: Alian713)
-   The parameter `trigger_id` has been renamed to `trigger_index` in all functions in TriggersObject (trigger_manager)
-   Renamend `Operator` to `Operation`.
-   Managers can now be accessed directly from the scenario. Eg: `scenario.trigger_manager`.
-   Renamed `player` attribute in the `Condition` object to `source_player`
-   Renamed `player_source` attribute in the `Effect` object to `source_player`
-   Renamed `player_target` attribute in the `Effect` object to `target_player`
-   Renamed `find_retriever` function to `get_retriever_by_name`
-   Renamed all retriever names to be lowercase underscored (Credits: pvallet)
-   Progress print statements now replace their current line. So instead of using 2 lines per piece it's now 1.
-   Most trigger_manager functions now require the new `TriggerSelect` object instead of 3 parameters for trigger selection. Read the docstring for more detail.

### Fixed

-   Bug causing the local `trigger_id` attributes to be out of sync when removing triggers.
-   Bug causing the `ValueError` to not get raised when trying to construct a piece with invalid data length.
-   Bug causing `Conditions` and `Effects` not to show in 'get_as_string' functions when set directly using: `trigger.effects = [...]`
-   Bug causing a crash when `selected_object_id` in `Effects` held a single ID.
-   Bug causing a crash when setting `selected_object_id` to an uniterable object. (Like an int instead of List[int])
-   Bug causing Variables to not show up when no triggers were present when using the `get_summary_as_string` in the trigger_manager.
-   Bug making it impossible to set unit IDs negative. (Supported by the game)
-   Typo in Condition dataset "OWH" to "OWN" in `OWH_FEWER_OBJECTS`.
-   Typo in Terrain dataset "MAGROVE" to "MANGROVE" in `FOREST_MAGROVE`.

### Removed

-   Outdated examples

---

## 0.0.7 - 2019-May-23

### Added

-   The `ai_script_goal` effect.
-   The `difficulty_level` condition.
-   The `new_unit_id_to_place` field in the `DataHeader` is updated in the reconstructing phase.
-   VariableObject: `{id: ..., name: ...}`.
-   Variable info to `get_content_as_string` and `get_summary_as_string` functions from the trigger_manager.
-   `get_variable(id or name)` function to the trigger_manager.
-   Defaults to all `effects` & `conditions`. (In-Game Editor defaults)
-   PlayerColor Enum. `PlayerColor.PURPLE`.
-   The ability to remove units using `unit_mamager.remove_unit(unit=... or reference_id=...)`.
-   The abiltiy to remove a trigger using an object reference: `trigger_manager.remove_trigger(trigger=...)`.
-   `Hero` dataset (Credits to [T-West] for the hero name list)
-   `get_enum_from_unit_const` function
-   `GaiaBuilding` and `GaiaUnit` dataset (Like normal Building and Unit dataset but also includes Gaia only buildings & units)
-   Datasets for (All?) dropdown lists in conditions and effects.
    -   `DiplomacyState`
    -   `Operator`
    -   `ButtonLocation`
    -   `PanelLocation`
    -   `TimeUnit`
    -   `VisibilityState`
    -   `DifficultyLevel`
    -   `TechnologyState`
    -   `Comparison`
    -   `ObjectAttribute`
    -   `Attribute`
-   **Code Block** - Added code block for adding KOTH + Regicide to any map with (exactly) one monument - Using triggers. This code block adds close to 600 triggers for displaying all years, displaying players holding the monument and victory & defeat conditions.

### Changed

-   `ChangedVariableStruct` to `VariableStruct`.
-   UnitObject attribute `unit_id` renamed to `unit_const`. (Credit: [T-West])
-   Effects and Condition constants are now `IntEnum`s. (ie. `Effect.CREATE_OBJECT`)
-   Units, Buildings, Techs and Terrains are now `IntEnum`s. (ie. `Unit.MAN_AT_ARMS`)
-   Renamed `delete_trigger` function to `remove_trigger`.
-   Renamed `trigger_data` attribute to `triggers`
-   Reading and Writing UTF-8 instead of ASCII characters. (The game might not support all characters everywhere)

### Updated

-   `Snow`, `Ice, Navigable`, `Beach, Ice` in Terrain dataset. (Fixed in game)

### Fixed

-   `get_new_reference_id()` returns `highest_id + 1` instead of `highest_id`.
-   Bug removing all `Trigger` names.
-   Bug causing `Trigger display order` to be incorrect. Wasn't breaking scenarios as the in-game editor was able to handle it properly and fixed it when saving from there. Only caused the Parser from being able to read the file.

### Removed

-   The default attributes in `Condition` and `Effect` constructors.
-   The `get_triggers` function. It was redundant as it's equal to the following:
    -   0.0.6: `trigger_manager.trigger_data`
    -   0.0.7: `trigger_manager.triggers`

---

## 0.0.6 - 2019-April-20

### Added

-   UnitsObject and UnitObject reconstruct support (AKA: Made Usable).
    -   Check the cheatsheets on [Github edit Scenario].
-   Player Enum.
-   Tile object.
-   Logging options for Reading, Parsing, Reconstructing and writing.
-   Bidict for units, buildings and techs dataset.
-   `pretty_print_name` to the Helper (Credits: [T-West]).

### Changed

-   `VariableChangeStruct` to `VariableStruct`.
-   The object_manager function `get_x_object` to `x_manager`.
-   Some `__repr__` and `__str__` are now more readable

[keep a changelog]: https://keepachangelog.com/en/1.0.0/
[github edit scenario]: https://github.com/KSneijders/AoE2ScenarioParser#editing-a-scenario
[t-west]: https://github.com/twestura/
