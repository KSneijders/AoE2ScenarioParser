from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version
from bfp_rs.types.le import f32, i32, i8, u8


class VictoryPoint(BaseStruct):
    __default_ver__ = Version(2)

    # @formatter:off
    type: int = Retriever(u8, default = 0)
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
    state: int = Retriever(u8, default = 0)
    """
    - 0: Not achieved
    - 1: Failed
    - 2: Achieved
    - 3: Disabled
    """
    attribute1: int                    = Retriever(i32,                          default = 0)
    quantity: int                      = Retriever(i32,                          default = 0)
    points: int                        = Retriever(i32,                          default = 0)
    current_points: int                = Retriever(i32,                          default = 0)
    id: int                            = Retriever(i8,                           default = 0)
    group: int                         = Retriever(i8,                           default = 0)
    current_attribute1_quantity: float = Retriever(f32,                          default = 0)
    attribute2: int                    = Retriever(i32, min_ver = Version(2, 0), default = 0)
    current_attribute2_quantity: float = Retriever(f32, min_ver = Version(2, 0), default = 0)
    # @formatter:on
