from __future__ import annotations

from bfp_rs import BaseStruct, Context, Retriever, Version
from bfp_rs.types.le import i32

from AoE2ScenarioParser.sections.scx_versions import TRIGGER_LATEST


class Attacker(BaseStruct):
    # @formatter:off
    object_id: int      = Retriever(i32, default = 0)
    object_group: int   = Retriever(i32, default = 0)
    object_type: int    = Retriever(i32, default = 0)
    unit_level: int     = Retriever(i32, default = 0)
    player_id: int      = Retriever(i32, default = 0)
    attack_time: int    = Retriever(i32, default = 0)
    # @formatter:on

    def __new__(cls, ver: Version = TRIGGER_LATEST, ctx: Context = Context(), init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, ctx, init_defaults, **retriever_inits)
