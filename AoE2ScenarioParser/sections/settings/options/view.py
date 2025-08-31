from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i32

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class View(BaseStruct):
    __default_ver__ = DE_LATEST

    x: int = Retriever(i32, default = -1)
    y: int = Retriever(i32, default = -1)
