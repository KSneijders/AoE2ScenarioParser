from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import i32

from AoE2ScenarioParser.sections.scx_versions import TRIGGER_LATEST


class Attacker(BaseStruct):
    __default_ver__ = TRIGGER_LATEST

    # @formatter:off
    object_id: int      = Retriever(i32, default = 0)
    object_group: int   = Retriever(i32, default = 0)
    object_type: int    = Retriever(i32, default = 0)
    unit_level: int     = Retriever(i32, default = 0)
    player_id: int      = Retriever(i32, default = 0)
    attack_time: int    = Retriever(i32, default = 0)
    # @formatter:on

