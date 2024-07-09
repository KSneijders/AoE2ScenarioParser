from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import bool32, bool8, FixedLenArray, int32, int8, uint32
from AoE2ScenarioParser.sections.settings.diplomacy.legacy_victory_info import LegacyVictoryInfo
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class Diplomacy(BaseStruct):
    # @formatter:off
    player_stances: list[list[int]]                    = Retriever(FixedLenArray[uint32, 16],            default_factory = lambda _: [3]*16,                                      repeat = 16)
    legacy_victory_info: list[list[LegacyVictoryInfo]] = Retriever(FixedLenArray[LegacyVictoryInfo, 12], default_factory = lambda sv: [LegacyVictoryInfo(sv) for _ in range(12)], repeat = 16)
    """used in aoe1"""
    separator: int                                     = Retriever(int32,  min_ver = Version((1,  2)),   default = -99)
    allied_victories: list[bool]                       = Retriever(bool32,                               default = False,                                                         repeat = 16)
    lock_teams_in_game: bool                           = Retriever(bool8,  min_ver = Version((1, 23)),   default = False)
    lock_teams_in_lobby: bool                          = Retriever(bool8,  min_ver = Version((1, 24)),   default = False)
    random_start_points: bool                          = Retriever(bool8,  min_ver = Version((1, 24)),   default = False)
    max_num_teams: int                                 = Retriever(int8,   min_ver = Version((1, 24)),   default = 4)
    # @formatter:on

    def __init__(self, struct_ver: Version = DE_LATEST, initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
