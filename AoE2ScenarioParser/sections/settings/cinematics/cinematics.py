from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import str16

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class Cinematics(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    pregame: str = Retriever(str16, default = "")
    victory: str = Retriever(str16, default = "")
    loss: str    = Retriever(str16, default = "")
    # @formatter:on
