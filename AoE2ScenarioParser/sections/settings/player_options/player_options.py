from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import FixedLenNTStr, int32, str16, uint8
from AoE2ScenarioParser.sections.settings.data_header import PlayerBaseOptions, Resources
from AoE2ScenarioParser.sections.settings.player_options.legacy_ai_file import LegacyAiFile
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class PlayerOptions(BaseStruct):
    # @formatter:off
    build_lists: list[str]                       = Retriever(str16,                                          default = "",                        repeat = 16)
    """unused?"""
    city_plans: list[str]                        = Retriever(str16,                                          default = "",                        repeat = 16)
    """unused?"""
    ai_names: list[str]                          = Retriever(str16,              min_ver = Version((1,  8)), default = "",                        repeat = 16)
    legacy_ai_files: list[LegacyAiFile]          = Retriever(LegacyAiFile,                                   default_factory = LegacyAiFile,      repeat = 16)
    ai_types: list[int]                          = Retriever(uint8,              min_ver = Version((1, 20)), default = 1,                         repeat = 16)
    separator1: int                              = Retriever(int32,              min_ver = Version((1,  2)), default = -99)
    starting_resources: list[Resources]          = Retriever(Resources,          min_ver = Version((1, 14)), default_factory = Resources,         repeat = 16)
    tribe_names: list[str]                       = Retriever(FixedLenNTStr[256], max_ver = Version((1, 13)), default = "",                        repeat = 16)
    player_base_options: list[PlayerBaseOptions] = Retriever(PlayerBaseOptions,  max_ver = Version((1, 13)), default_factory = PlayerBaseOptions, repeat = 16)
    separator2: int                              = Retriever(int32,              min_ver = Version((1,  2)), default = -99)
    # @formatter:on

    def __init__(self, struct_ver: Version = DE_LATEST, initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
