from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version
from bfp_rs.types.le import (Array, bool32, bool8, f32, i32, NtStr, str16, u16, u32)

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST
from AoE2ScenarioParser.sections.settings.data_header.player_base_options import PlayerBaseOptions


class DataHeader(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    next_unit_ref: int                           = Retriever(u32,                                                    default = 0)
    version: float                               = Retriever(f32,                                                    default = 1.54)
    num_max_players: int                         = Retriever(i32,                          min_ver = Version(1, 52), default = 0)
    gaia_player_idx: int                         = Retriever(i32,                          min_ver = Version(1, 52), default = 8)
    tribe_names: list[str]                       = Retriever(Array[16][NtStr[256]],        min_ver = Version(1, 13), default_factory = lambda _ver: [""]*16)
    player_name_str_ids: list[int]               = Retriever(Array[16][i32],               min_ver = Version(1, 16), default_factory = lambda _ver: [-2]*16)
    player_base_options: list[PlayerBaseOptions] = Retriever(Array[16][PlayerBaseOptions], min_ver = Version(1, 14), default_factory = lambda ver: [PlayerBaseOptions(ver) for _ in range(16)])
    lock_civilizations: list[bool]               = Retriever(Array[16][bool32],            min_ver = Version(1, 28), default_factory = lambda _ver: [False]*16)
    lock_ai_personality: list[bool]              = Retriever(Array[16][bool32],            min_ver = Version(1, 53), default_factory = lambda _ver: [False]*16)
    victory_conquest: bool                       = Retriever(bool8,                        min_ver = Version(1,  7), default = True)
    timeline_count: int                          = Retriever(u16,                                          default = 0)
    """unused, must always be 0"""
    timeline_available: int                      = Retriever(u16,                                          default = 0)
    """unused"""
    old_timeline: float                          = Retriever(f32,                                          default = 0)
    """unused"""
    file_name: str                               = Retriever(str16,                                        default = "MadeWithAoE2SP.aoe2scenario")
    # @formatter:on
