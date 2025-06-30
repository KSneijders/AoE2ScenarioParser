from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version
from bfp_rs.types.le import f32, i32, u16, u8, str32

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class Unit(BaseStruct):
    # @formatter:off
    x: float                = Retriever(f32,                             default = 0.5)
    y: float                = Retriever(f32,                             default = 0.5)
    z: float                = Retriever(f32,                             default = 0)
    reference_id: int       = Retriever(i32,                             default = 0)
    type: int               = Retriever(u16,                             default = 4)
    state: int              = Retriever(u8,                              default = 2)
    rotation: float         = Retriever(f32,                             default = 0)
    """in radians"""
    frame: int              = Retriever(u16,   min_ver = Version(1, 15), default = 0)
    garrisoned_in_ref: int  = Retriever(i32,   min_ver = Version(1, 13), default = -1)
    """another object's reference_id. -1 (and 0 for v1.13 to 1.20) mean None"""
    caption_string_id: int  = Retriever(i32,   min_ver = Version(1, 54), default = -1)
    # @formatter:on

    def __new__(cls, ver: Version = DE_LATEST, init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, init_defaults, **retriever_inits)
