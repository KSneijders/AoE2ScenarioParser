from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int16, int8, uint8


class TerrainTile(BaseStruct):
    # @formatter:off
    type: int       = Retriever(uint8,                           default = 0)
    elevation: int  = Retriever(int8,                            default = 0)
    zone: int       = Retriever(int8,                            default = 0)
    """unused?"""
    mask_type: int  = Retriever(int16, min_ver = Version((1, )), default = -1)
    """what does this do?"""
    layer_type: int = Retriever(int16, min_ver = Version((1, )), default = -1)
    # @formatter:on

    def __init__(self, struct_ver: Version = Version((2, )), initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
