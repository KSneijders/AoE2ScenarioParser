from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version
from bfp_rs.types.le import i16

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class ViewI(BaseStruct):
    x: int = Retriever(i16, default = 60)
    y: int = Retriever(i16, default = 60)

    def __new__(cls, ver: Version = DE_LATEST, init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, init_defaults, **retriever_inits)
