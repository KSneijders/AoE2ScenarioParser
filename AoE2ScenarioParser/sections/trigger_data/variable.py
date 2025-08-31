from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import nt_str32, u32

from AoE2ScenarioParser.sections.scx_versions import TRIGGER_LATEST


class Variable(BaseStruct):
    __default_ver__ = TRIGGER_LATEST

    # @formatter:off
    id: int   = Retriever(u32,      default = 0)
    name: str = Retriever(nt_str32, default = "_Variable")
    # @formatter:on
