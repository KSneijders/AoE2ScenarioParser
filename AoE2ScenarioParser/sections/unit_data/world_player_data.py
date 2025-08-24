from __future__ import annotations

from bfp_rs import BaseStruct, Context, Retriever, Version
from bfp_rs.types.le import f32

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class WorldPlayerData(BaseStruct):
    """All data here is duplicated except pop limit"""

    # @formatter:off
    food: float             = Retriever(f32,                           default = 200)
    wood: float             = Retriever(f32,                           default = 200)
    gold: float             = Retriever(f32,                           default = 200)
    stone: float            = Retriever(f32,                           default = 200)
    ore_x: float            = Retriever(f32, min_ver = Version(1, 14), default = 100)
    trade_goods: float      = Retriever(f32, min_ver = Version(1, 14), default = 0.0)
    population_limit: float = Retriever(f32, min_ver = Version(1, 20), default = 200.0)
    # @formatter:on

    def __new__(cls, ver: Version = DE_LATEST, ctx: Context = Context(), init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, ctx, init_defaults, **retriever_inits)