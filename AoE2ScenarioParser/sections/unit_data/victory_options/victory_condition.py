from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import float32, int32, int8


class VictoryCondition(BaseStruct):
    # @formatter:off
    type: int = Retriever(int8, default = 0)
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
    object_type: int   = Retriever(int32,   default = 0)
    player_id: int     = Retriever(int32,   default = 0)
    area_x1: float     = Retriever(float32, default = 0)
    area_y1: float     = Retriever(float32, default = 0)
    area_x2: float     = Retriever(float32, default = 0)
    area_y2: float     = Retriever(float32, default = 0)
    number: int        = Retriever(int32,   default = 0)
    count: int         = Retriever(int32,   default = 0)
    source_object: int = Retriever(int32,   default = 0)
    target_object: int = Retriever(int32,   default = 0)
    victory_group: int = Retriever(int8,    default = 0)
    ally_flag: int     = Retriever(int8,    default = 0)
    state: int         = Retriever(int8,    default = 0)
    """
    - 0: Not achieved
    - 1: Failed
    - 2: Achieved
    - 3: Disabled
    """
    # @formatter:on

    def __init__(self, struct_ver: Version = Version((2, )), initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
