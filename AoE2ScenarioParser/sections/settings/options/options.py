from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, RetrieverCombiner, RetrieverRef, Version
from binary_file_parser.types import bool32, bool8, int32, StackedArray32s, str16, uint16, uint32, uint8

from AoE2ScenarioParser.sections.settings.options.view import View
from AoE2ScenarioParser.sections.settings.options.legacy_disables import LegacyDisables
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class Options(BaseStruct):
    # @formatter:off
    _legacy_disables: LegacyDisables        = Retriever(LegacyDisables,              min_ver = Version((1,  3)), max_ver = Version((1, 27)), default_factory = LegacyDisables)
    _disabled_tech_ids: list[list[int]]     = Retriever(StackedArray32s[uint32, 16], min_ver = Version((1, 28)),                             default_factory = lambda _: [[] for _ in range(16)])
    _disabled_unit_ids: list[list[int]]     = Retriever(StackedArray32s[uint32, 16], min_ver = Version((1, 28)),                             default_factory = lambda _: [[] for _ in range(16)])
    _disabled_building_ids: list[list[int]] = Retriever(StackedArray32s[uint32, 16], min_ver = Version((1, 28)),                             default_factory = lambda _: [[] for _ in range(16)])

    combat_mode: bool                       = Retriever(bool32,                      min_ver = Version((1,  5)),                             default = False)
    naval_mode: bool                        = Retriever(bool32,                      min_ver = Version((1, 12)),                             default = False)
    all_techs: bool                         = Retriever(bool32,                      min_ver = Version((1, 12)),                             default = False)
    starting_ages: list[int]                = Retriever(uint32,                      min_ver = Version((1,  6)),                             default = 2,            repeat = 16)
    separator: bytes                        = Retriever(int32,                       min_ver = Version((1,  2)),                             default = -99)
    editor_camera_position: View            = Retriever(View,                        min_ver = Version((1, 19)),                             default_factory = View)
    ai_map_type1: int                       = Retriever(int32,                       min_ver = Version((1, 21)),                             default = 2)
    base_priorities: list[int]              = Retriever(uint8,                       min_ver = Version((1, 24)),                             default = 0,            repeat = 16)
    num_triggers: int                       = Retriever(uint32,                      min_ver = Version((1, 35)),                             default = 0)

    str_sign1: int                          = Retriever(uint16,                      min_ver = Version((1, 30)),                             default = 2656)
    water_definition: str                   = Retriever(str16,                       min_ver = Version((1, 30)),                             default = "")
    str_sign2: int                          = Retriever(uint16,                      min_ver = Version((1, 32)),                             default = 2656)
    colour_mood: str                        = Retriever(str16,                       min_ver = Version((1, 32)),                             default = "Empty")
    str_sign3: int                          = Retriever(uint16,                      min_ver = Version((1, 40)),                             default = 2656)
    script_name: str                        = Retriever(str16,                       min_ver = Version((1, 40)),                             default = "")
    _lock_coop_alliances1: bool             = Retriever(bool8,                       min_ver = Version((1, 41)), max_ver = Version((1, 41)), default = False)
    collide_and_correct: bool               = Retriever(bool8,                       min_ver = Version((1, 36)),                             default = False)
    villager_force_drop: bool               = Retriever(bool8,                       min_ver = Version((1, 37)),                             default = False)
    player_views: list[View]                = Retriever(View,                        min_ver = Version((1, 40)),                             default_factory = View, repeat = 16)
    _lock_coop_alliances2: bool             = Retriever(bool8,                       min_ver = Version((1, 42)),                             default = False)
    ai_map_type2: int                       = Retriever(uint32,                      min_ver = Version((1, 42)), max_ver = Version((1, 46)), default = 0)
    population_caps: list[int]              = Retriever(uint32,                      min_ver = Version((1, 44)),                             default = 200,          repeat = 16)
    # todo: figure this out
    secondary_game_mode                     = Retriever(uint32,                      min_ver = Version((1, 45)),                             default = 0)

    _legacy_disabled_tech_ids: list[list[int]]     = RetrieverRef(_legacy_disables, LegacyDisables.disabled_tech_ids)
    _legacy_disabled_unit_ids: list[list[int]]     = RetrieverRef(_legacy_disables, LegacyDisables.disabled_unit_ids)
    _legacy_disabled_building_ids: list[list[int]] = RetrieverRef(_legacy_disables, LegacyDisables.disabled_building_ids)

    disabled_tech_ids: list[list[int]]     = RetrieverCombiner(_disabled_tech_ids, _legacy_disabled_tech_ids)
    disabled_unit_ids: list[list[int]]     = RetrieverCombiner(_disabled_unit_ids, _legacy_disabled_unit_ids)
    disabled_building_ids: list[list[int]] = RetrieverCombiner(_disabled_building_ids, _legacy_disabled_building_ids)

    lock_coop_alliances: bool = RetrieverCombiner(_lock_coop_alliances1, _lock_coop_alliances2)
    """This locks diplomatic stances for humans against other humans but not AIs"""
    # @formatter:on

    def __init__(self, struct_ver: Version = DE_LATEST, initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
