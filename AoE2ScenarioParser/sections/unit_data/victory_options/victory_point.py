from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import float32, int32, int8, uint8


class VictoryPoint(BaseStruct):
    # @formatter:off
    type: int = Retriever(uint8, default = 0)
    """
    - 0 Capture,
    - 1 Create,
    - 2 Destroy,
    - 3 DestroyMultiple,
    - 4 BringToArea,
    - 5 BringToObject,
    - 6 Attribute,
    - 7 Explore,
    - 8 CreateInArea,
    - 9 DestroyAll,
    - 10 DestroyPlayer,
    - 11 Points,
    """
    state: int = Retriever(uint8, default = 0)
    """
    - 0: Not achieved
    - 1: Failed
    - 2: Achieved
    - 3: Disabled
    """
    attribute1: int                    = Retriever(int32,                             default = 0)
    quantity: int                      = Retriever(int32,                             default = 0)
    points: int                        = Retriever(int32,                             default = 0)
    current_points: int                = Retriever(int32,                             default = 0)
    id: int                            = Retriever(int8,                              default = 0)
    group: int                         = Retriever(int8,                              default = 0)
    current_attribute1_quantity: float = Retriever(float32,                           default = 0)
    attribute2: int                    = Retriever(int32,   min_ver = Version((2, )), default = 0)
    current_attribute2_quantity: float = Retriever(float32, min_ver = Version((2, )), default = 0)
    # @formatter:on

    def __init__(self, struct_ver: Version = Version((2, )), initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
