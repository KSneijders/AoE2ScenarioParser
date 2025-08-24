from __future__ import annotations

from bfp_rs import BaseStruct, Context, Retriever, Version
from bfp_rs.types.le import nt_str32

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class AiFile(BaseStruct):
    # @formatter:off
    file_name: str = Retriever(nt_str32, default = "")
    ai_rules: str  = Retriever(nt_str32, default = "")
    """From the .per file of an AI"""
    # @formatter:on

    def __new__(cls, ver: Version = DE_LATEST, ctx: Context = Context(), init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, ctx, init_defaults, **retriever_inits)
