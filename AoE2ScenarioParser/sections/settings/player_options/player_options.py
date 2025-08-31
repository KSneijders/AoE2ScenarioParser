from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version
from bfp_rs.types.le import Array, i32, NtStr, str16, u8

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST
from AoE2ScenarioParser.sections.settings.data_header import PlayerBaseOptions, Resources
from AoE2ScenarioParser.sections.settings.player_options.legacy_ai_file import LegacyAiFile


class PlayerOptions(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    build_lists: list[str]                       = Retriever(Array[16][str16],                                       default_factory = lambda _ver: [""]*16)
    """unused?"""
    city_plans: list[str]                        = Retriever(Array[16][str16],                                       default_factory = lambda _ver: [""]*16)
    """unused?"""
    ai_names: list[str]                          = Retriever(Array[16][str16],             min_ver = Version(1,  8), default_factory = lambda _ver: [""]*16)
    legacy_ai_files: list[LegacyAiFile]          = Retriever(Array[16][LegacyAiFile],                                default_factory = lambda ver: [LegacyAiFile(ver) for _ in range(16)])
    ai_types: list[int]                          = Retriever(Array[16][u8],                min_ver = Version(1, 20), default_factory = lambda _ver: [1]*16)
    separator1: int                              = Retriever(i32,                          min_ver = Version(1,  3), default = -99)
    tribe_names: list[str]                       = Retriever(Array[16][NtStr[256]],        max_ver = Version(1, 13), default_factory = lambda _ver: [""]*16)
    starting_resources: list[Resources]          = Retriever(Array[16][Resources],         min_ver = Version(1, 14), default_factory = lambda ver: [Resources(ver) for _ in range(16)])
    player_base_options: list[PlayerBaseOptions] = Retriever(Array[16][PlayerBaseOptions], max_ver = Version(1, 13), default_factory = lambda ver: [PlayerBaseOptions(ver) for _ in range(16)])
    separator2: int                              = Retriever(i32,                          min_ver = Version(1,  3), default = -99)
    # @formatter:on
