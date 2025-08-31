from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import f32

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class ViewF(BaseStruct):
    __default_ver__ = DE_LATEST

    x: float = Retriever(f32, default = 60.0)
    y: float = Retriever(f32, default = 60.0)

