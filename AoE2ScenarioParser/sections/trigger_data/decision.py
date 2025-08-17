from __future__ import annotations

from AoE2ScenarioParser.sections.scx_versions import TRIGGER_LATEST

from bfp_rs import BaseStruct, Retriever, Version
from bfp_rs.types.le import i32, u8


class Decision(BaseStruct):
    # @formatter:off
    id: int    = Retriever(i32, default = 0)
    state: int = Retriever(u8,  default = 0)
    # @formatter:on

    def __new__(cls, ver: Version = TRIGGER_LATEST, init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, init_defaults, **retriever_inits)
