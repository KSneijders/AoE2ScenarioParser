from __future__ import annotations

from bfp_rs import BaseStruct, Context, Retriever, Version
from bfp_rs.types.le import i32

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class View(BaseStruct):
    x: int = Retriever(i32, default = -1)
    y: int = Retriever(i32, default = -1)

    def __new__(cls, ver: Version = DE_LATEST, ctx: Context = Context(), init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, ctx, init_defaults, **retriever_inits)