from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i32, u8

from AoE2ScenarioParser.sections.scx_versions import TRIGGER_LATEST


class Decision(BaseStruct):
    __default_ver__ = TRIGGER_LATEST

    # @formatter:off
    id: int    = Retriever(i32, default = 0)
    state: int = Retriever(u8,  default = 0)
    # @formatter:on
