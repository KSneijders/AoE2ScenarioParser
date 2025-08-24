from bfp_rs import BaseStruct, Context, Retriever, Version
from bfp_rs.types.le import bool32, u32

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class GlobalVictory(BaseStruct):
    # @formatter:off
    conquest: bool                       = Retriever(bool32, default = True)
    capture_min_monuments: int           = Retriever(u32,    default = 0)
    """Ruins in aoe1"""
    collect_min_relics: int              = Retriever(u32,    default = 0)
    """Artifacts in aoe1"""
    make_min_remarkable_discoveries: int = Retriever(u32,    default = 0)
    """Only in aoe1"""
    explore_map_percent: int             = Retriever(u32,    default = 0)
    collect_gold: int                    = Retriever(u32,    default = 0)
    meet_all_conditions: bool            = Retriever(bool32, default = False)
    victory_type: int                    = Retriever(u32,    default = 4,    min_ver = Version(1, 13))
    min_score: int                       = Retriever(u32,    default = 900,  min_ver = Version(1, 13))
    time_limit: int                      = Retriever(u32,    default = 9000, min_ver = Version(1, 13))
    """in 10ths of a year"""
    # @formatter:on

    def __new__(cls, ver: Version = DE_LATEST, ctx: Context = Context(), init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, ctx, init_defaults, **retriever_inits)