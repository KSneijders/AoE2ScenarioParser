from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int32, str32

from AoE2ScenarioParser.objects.support import Area


class ConditionStruct(BaseStruct):
    # def map(self) -> BaseStruct:
    #     from AoE2ScenarioParser.objects.data_objects.conditions.condition import Condition
    #     return Condition._make_condition(self)

    # Todo: use datasets for type hinting and do on_read and on_write conversions
    # Todo: override list with ref-list in retriever
    # @formatter:off
    _type: int                              = Retriever(int32,                                                 default = 0)
    _static_value_2_4_1_36: int             = Retriever(int32,                 max_ver=Version((2, 2, 1, 37)), default = 21)
    _static_value_2_4_1_40: int             = Retriever(int32, Version((2, 4, 1, 40)), Version((2, 4, 1, 41)), default = 24)
    _static_value_2_4_1_42: int             = Retriever(int32, Version((2, 4, 1, 42)), Version((2, 5, 1, 45)), default = 25)
    _static_value_3_0_1_46: int             = Retriever(int32, Version((3, 0, 1, 46)),                         default = 28)
    _quantity: int                          = Retriever(int32,                                                 default = -1)
    _attribute: int                         = Retriever(int32,                                                 default = -1)
    _unit_object: int                       = Retriever(int32,                                                 default = -1)
    _next_object: int                       = Retriever(int32,                                                 default = -1)
    _object_list: int                       = Retriever(int32,                                                 default = -1)
    _source_player: int                     = Retriever(int32,                                                 default = -1)
    _technology: int                        = Retriever(int32,                                                 default = -1)
    _timer: int                             = Retriever(int32,                                                 default = -1)
    _unknown1: int                          = Retriever(int32,                                                 default = -1)
    _area: Area                             = Retriever(Area,                                                  default_factory=lambda _, __: Area((-1, -1)))
    _object_group: int                      = Retriever(int32,                                                 default = -1)
    _object_type: int                       = Retriever(int32,                                                 default = -1)
    _ai_signal: int                         = Retriever(int32,                                                 default = -1)
    _inverted: int                          = Retriever(int32,                                                 default = -1)
    _unknown2: int                          = Retriever(int32,                                                 default = -1)
    _variable: int                          = Retriever(int32,                                                 default = -1)
    _comparison: int                        = Retriever(int32,                                                 default = -1)
    _target_player: int                     = Retriever(int32,                                                 default = -1)
    _unit_ai_action: int                    = Retriever(int32, Version((2, 4, 1, 40)),                         default = -1)
    _unknown4: int                          = Retriever(int32, Version((2, 4, 1, 40)),                         default = -1)
    _object_state: int                      = Retriever(int32, Version((2, 4, 1, 42)),                         default = -1)
    _timer_id: int                          = Retriever(int32, Version((3, 0, 1, 46)),                         default = -1)
    _victory_timer_type: int                = Retriever(int32, Version((3, 0, 1, 46)),                         default = -1)
    _include_changeable_weapon_objects: int = Retriever(int32, Version((3, 0, 1, 46)),                         default = -1)
    _xs_function: str                       = Retriever(str32, Version((2, 4, 1, 40)),                         default = "")
    # @formatter:on

    def __init__(
        self, struct_ver: Version = Version((3, 5, 1, 47)), parent: BaseStruct = None, initialise_defaults = True,
        **retriever_inits
    ):
        super().__init__(struct_ver, parent, initialise_defaults = initialise_defaults, **retriever_inits)
