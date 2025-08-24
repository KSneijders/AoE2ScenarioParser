from __future__ import annotations

from bfp_rs import BaseStruct, Context, ret, Retriever, RetrieverRef, Version
from bfp_rs.types.le import Array32, i32, str32

from AoE2ScenarioParser.objects.support import Area, AreaT
from AoE2ScenarioParser.sections.scx_versions import TRIGGER_LATEST


class Condition(BaseStruct):
    # @formatter:off
    type: int                              = Retriever(i32,          default = 0)
    _properties: list[int]                 = Retriever(Array32[i32], default_factory = lambda _ver: [-1]*30)
    xs_function: str                       = Retriever(str32,        default = "", min_ver = Version(2, 3))

    quantity: int                          = RetrieverRef(ret(_properties),  0)
    resource: int                          = RetrieverRef(ret(_properties),  1)
    primary_unit_ref: int                  = RetrieverRef(ret(_properties),  2)
    secondary_unit_ref: int                = RetrieverRef(ret(_properties),  3)
    unit_type: int                         = RetrieverRef(ret(_properties),  4)
    source_player: int                     = RetrieverRef(ret(_properties),  5)
    technology: int                        = RetrieverRef(ret(_properties),  6)
    timer: int                             = RetrieverRef(ret(_properties),  7)
    trigger_idx: int                       = RetrieverRef(ret(_properties),  8)

    @property
    def area(self) -> Area:
        return Area((self._properties[9], self._properties[10]), (self._properties[11], self._properties[12]))

    @area.setter
    def area(self, value: AreaT) -> None:
        (
            (self._properties[9], self._properties[10]),
            (self._properties[11], self._properties[12])
        ) = Area.from_value(value)

    object_group: int                      = RetrieverRef(ret(_properties), 13)
    object_type: int                       = RetrieverRef(ret(_properties), 14)
    ai_signal: int                         = RetrieverRef(ret(_properties), 15)
    inverted: int                          = RetrieverRef(ret(_properties), 16)
    unknown2: int                          = RetrieverRef(ret(_properties), 17)
    variable: int                          = RetrieverRef(ret(_properties), 18)
    comparison: int                        = RetrieverRef(ret(_properties), 19)
    target_player: int                     = RetrieverRef(ret(_properties), 20)
    unit_action: int                       = RetrieverRef(ret(_properties), 21)
    unknown4: int                          = RetrieverRef(ret(_properties), 22)
    object_state: int                      = RetrieverRef(ret(_properties), 23)
    timer_id: int                          = RetrieverRef(ret(_properties), 24)
    victory_timer_type: int                = RetrieverRef(ret(_properties), 25)
    include_changeable_weapon_objects: int = RetrieverRef(ret(_properties), 26)
    decision_id: int                       = RetrieverRef(ret(_properties), 27)
    decision_option: int                   = RetrieverRef(ret(_properties), 28)
    variable2: int                         = RetrieverRef(ret(_properties), 29)
    # @formatter:on

    def __new__(cls, ver: Version = TRIGGER_LATEST, ctx: Context = Context(), init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, ctx, init_defaults, **retriever_inits)
