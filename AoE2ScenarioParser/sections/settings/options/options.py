from __future__ import annotations

from bfp_rs import BaseStruct, ret, Retriever, RetrieverCombiner, RetrieverRef, Version
from bfp_rs.types.le import Array, bool32, bool8, i32, StackedArray32, str16, u16, u32, u8

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST
from AoE2ScenarioParser.sections.settings.options.legacy_disables import LegacyDisables
from AoE2ScenarioParser.sections.settings.options.view import View


class Options(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    _legacy_disables: LegacyDisables        = Retriever(LegacyDisables,          min_ver = Version(1,  3), max_ver = Version(1, 26), default_factory = LegacyDisables)
    _disabled_tech_ids: list[list[int]]     = Retriever(StackedArray32[16][u32], min_ver = Version(1, 27),                           default_factory = lambda _: [[] for _ in range(16)])
    _disabled_unit_ids: list[list[int]]     = Retriever(StackedArray32[16][u32], min_ver = Version(1, 27),                           default_factory = lambda _: [[] for _ in range(16)])
    _disabled_building_ids: list[list[int]] = Retriever(StackedArray32[16][u32], min_ver = Version(1, 27),                           default_factory = lambda _: [[] for _ in range(16)])

    combat_mode: bool                       = Retriever(bool32,                  min_ver = Version(1,  5),                           default = False)
    naval_mode: bool                        = Retriever(bool32,                  min_ver = Version(1, 12),                           default = False)
    all_techs: bool                         = Retriever(bool32,                  min_ver = Version(1, 12),                           default = False)
    starting_ages: list[int]                = Retriever(Array[16][u32],          min_ver = Version(1,  6),                           default_factory = lambda _ver: [2]*16)
    separator: int                          = Retriever(i32,                     min_ver = Version(1,  3),                           default = -99)
    editor_camera_position: View            = Retriever(View,                    min_ver = Version(1, 19),                           default_factory = View)
    ai_map_type1: int                       = Retriever(i32,                     min_ver = Version(1, 21),                           default = 2)
    base_priorities: list[int]              = Retriever(Array[16][u8],           min_ver = Version(1, 24),                           default_factory = lambda _ver: [0]*16)
    num_triggers: int                       = Retriever(u32,                     min_ver = Version(1, 35),                           default = 0)

    str_sign1: int                          = Retriever(u16,                     min_ver = Version(1, 30),                           default = 2656)
    water_definition: str                   = Retriever(str16,                   min_ver = Version(1, 30),                           default = "")
    str_sign2: int                          = Retriever(u16,                     min_ver = Version(1, 32),                           default = 2656)
    color_mood: str                         = Retriever(str16,                   min_ver = Version(1, 32),                           default = "Empty")
    str_sign3: int                          = Retriever(u16,                     min_ver = Version(1, 38),                           default = 2656)
    script_name: str                        = Retriever(str16,                   min_ver = Version(1, 38),                           default = "")
    collide_and_correct: bool               = Retriever(bool8,                   min_ver = Version(1, 36),                           default = False)
    villager_force_drop: bool               = Retriever(bool8,                   min_ver = Version(1, 37),                           default = False)
    player_views: list[View]                = Retriever(Array[16][View],         min_ver = Version(1, 39),                           default_factory = lambda ver: [View(ver) for _ in range(16)])
    lock_coop_alliances: bool               = Retriever(bool8,                   min_ver = Version(1, 41),                           default = False)
    ai_map_type2: int                       = Retriever(u32,                     min_ver = Version(1, 42), max_ver = Version(1, 46), default = 0)
    population_caps: list[int]              = Retriever(Array[16][u32],          min_ver = Version(1, 44),                           default_factory = lambda _ver: [0]*16)
    secondary_game_mode                     = Retriever(u32,                     min_ver = Version(1, 45),                           default = 0)

    _legacy_disabled_tech_ids: list[list[int]]     = RetrieverRef(ret(_legacy_disables), ret(LegacyDisables.disabled_tech_ids))
    _legacy_disabled_unit_ids: list[list[int]]     = RetrieverRef(ret(_legacy_disables), ret(LegacyDisables.disabled_unit_ids))
    _legacy_disabled_building_ids: list[list[int]] = RetrieverRef(ret(_legacy_disables), ret(LegacyDisables.disabled_building_ids))

    disabled_tech_ids: list[list[int]]     = RetrieverCombiner(ret(_disabled_tech_ids), ret(_legacy_disabled_tech_ids))
    disabled_unit_ids: list[list[int]]     = RetrieverCombiner(ret(_disabled_unit_ids), ret(_legacy_disabled_unit_ids))
    disabled_building_ids: list[list[int]] = RetrieverCombiner(ret(_disabled_building_ids), ret(_legacy_disabled_building_ids))
    # @formatter:on
