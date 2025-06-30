from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version
from bfp_rs.types.le import nt_str32, u32

from AoE2ScenarioParser.sections.scx_versions import TRIGGER_LATEST


class Variable(BaseStruct):
    # @formatter:off
    id: int   = Retriever(u32,      default = 0)
    name: str = Retriever(nt_str32, default = "_Variable")
    # @formatter:on

    def __new__(cls, ver: Version = TRIGGER_LATEST, init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, init_defaults, **retriever_inits)
