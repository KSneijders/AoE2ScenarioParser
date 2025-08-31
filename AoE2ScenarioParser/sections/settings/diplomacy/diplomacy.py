from bfp_rs import BaseStruct, ret, Retriever, RetrieverCombiner, Version
from bfp_rs.types.le import Array, bool32, bool8, i32, i8, u32

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST
from AoE2ScenarioParser.sections.settings.diplomacy.legacy_victory_info import LegacyVictoryInfo


class Diplomacy(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    player_stances: list[list[int]]                    = Retriever(Array[16][Array[16][u32]],                                    default_factory = lambda _ver: [[3]*16 for _ in range(16)])
    legacy_victory_info: list[list[LegacyVictoryInfo]] = Retriever(Array[16][Array[12][LegacyVictoryInfo]],                      default_factory = lambda ver: [[LegacyVictoryInfo(ver) for _ in range(12)] for _ in range(16)])
    """used in aoe1"""
    separator: int                                     = Retriever(i32,      min_ver = Version(1,  3),                           default = -99)
    # in < 1.02 this is a nested Array[16]
    allied_victories: list[bool]                       = Retriever(Array[16][bool32],                                            default_factory = lambda _ver: [False]*16)
    _lock_teams_in_game_old: bool                      = Retriever(bool32,   min_ver = Version(1, 23), max_ver = Version(1, 23), default = False)
    _lock_teams_in_game: bool                          = Retriever(bool8,    min_ver = Version(1, 24),                           default = False)
    lock_teams_in_lobby: bool                          = Retriever(bool8,    min_ver = Version(1, 24),                           default = False)
    random_start_points: bool                          = Retriever(bool8,    min_ver = Version(1, 24),                           default = False)
    max_num_teams: int                                 = Retriever(i8,       min_ver = Version(1, 24),                           default = 4)
    # @formatter:on

    lock_teams_in_game: bool = RetrieverCombiner(ret(_lock_teams_in_game_old), ret(_lock_teams_in_game))
