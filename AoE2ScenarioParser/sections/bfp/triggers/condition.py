from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int32, str32


class Condition(BaseStruct):
    # formatter:off
    condition_type: int                    = Retriever(int32,                               default=0)
    static_value_2_4_1_36: int             = Retriever(int32,        max_ver=(2, 2, 1, 37), default=21)
    static_value_2_4_1_40: int             = Retriever(int32, (2, 4, 1, 40), (2, 4, 1, 41), default=24)
    static_value_2_4_1_42: int             = Retriever(int32, (2, 4, 1, 42), (2, 5, 1, 45), default=25)
    static_value_3_0_1_46: int             = Retriever(int32, (3, 0, 1, 46),                default=28)
    quantity: int                          = Retriever(int32,                               default=-1)
    attribute: int                         = Retriever(int32,                               default=-1)
    unit_object: int                       = Retriever(int32,                               default=-1)
    next_object: int                       = Retriever(int32,                               default=-1)
    object_list: int                       = Retriever(int32,                               default=-1)
    source_player: int                     = Retriever(int32,                               default=-1)
    technology: int                        = Retriever(int32,                               default=-1)
    timer: int                             = Retriever(int32,                               default=-1)
    unknown1: int                          = Retriever(int32,                               default=-1)
    area_x1: int                           = Retriever(int32,                               default=-1)
    area_y1: int                           = Retriever(int32,                               default=-1)
    area_x2: int                           = Retriever(int32,                               default=-1)
    area_y2: int                           = Retriever(int32,                               default=-1)
    object_group: int                      = Retriever(int32,                               default=-1)
    object_type: int                       = Retriever(int32,                               default=-1)
    ai_signal: int                         = Retriever(int32,                               default=-1)
    inverted: int                          = Retriever(int32,                               default=-1)
    unknown2: int                          = Retriever(int32,                               default=-1)
    variable: int                          = Retriever(int32,                               default=-1)
    comparison: int                        = Retriever(int32,                               default=-1)
    target_player: int                     = Retriever(int32,                               default=-1)
    unit_ai_action: int                    = Retriever(int32, (2, 4, 1, 40),                default=-1)
    unknown4: int                          = Retriever(int32, (2, 4, 1, 40),                default=-1)
    object_state: int                      = Retriever(int32, (2, 4, 1, 42),                default=-1)
    timer_id: int                          = Retriever(int32, (3, 0, 1, 46),                default=-1)
    victory_timer_type: int                = Retriever(int32, (3, 0, 1, 46),                default=-1)
    include_changeable_weapon_objects: int = Retriever(int32, (3, 0, 1, 46),                default=-1)
    xs_function: str                       = Retriever(str32, (2, 4, 1, 40),                default="")
    # formatter:on

    def __init__(self, struct_version: tuple[int, ...] = (3, 5, 1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)
