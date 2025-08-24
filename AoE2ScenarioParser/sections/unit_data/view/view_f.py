from __future__ import annotations

from bfp_rs import BaseStruct, Context, Retriever, Version
from bfp_rs.types.le import f32

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class ViewF(BaseStruct):
    x: float = Retriever(f32, default = 60.0)
    y: float = Retriever(f32, default = 60.0)

    def __new__(cls, ver: Version = DE_LATEST, ctx: Context = Context(), init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, ctx, init_defaults, **retriever_inits)