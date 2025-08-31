from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i16

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class ViewI(BaseStruct):
    __default_ver__ = DE_LATEST

    x: int = Retriever(i16, default = 60)
    y: int = Retriever(i16, default = 60)

