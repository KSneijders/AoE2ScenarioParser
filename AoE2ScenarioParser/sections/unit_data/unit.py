from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import float32, int32, uint16, uint8
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class Unit(BaseStruct):
    # @formatter:off
    x: float               = Retriever(float32, default = 0.5)
    y: float               = Retriever(float32, default = 0.5)
    z: float               = Retriever(float32, default = 0)
    reference_id: int      = Retriever(int32,   default = 0)
    type: int              = Retriever(uint16,  default = 4)
    state: int             = Retriever(uint8,   default = 2)
    rotation: float        = Retriever(float32, default = 0)
    """in radians"""
    frame: int             = Retriever(uint16, min_ver = Version((1, 15)), default = 0)
    garrisoned_in_ref: int = Retriever(int32,  min_ver = Version((1, 13)), default = -1)
    """another object's reference_id. -1 (and 0 for v1.12+) mean None"""
    # @formatter:on

    def __init__(self, struct_ver: Version = DE_LATEST, initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
