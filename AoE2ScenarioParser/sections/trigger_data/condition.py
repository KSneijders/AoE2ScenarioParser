from __future__ import annotations

from bfp_rs import BaseStruct, ret, Retriever, RetrieverRef, Version
from bfp_rs.types.le import Array32, i32, str32

from AoE2ScenarioParser.objects.support import Area, AreaT
from AoE2ScenarioParser.sections.scx_versions import TRIGGER_LATEST


class Condition(BaseStruct):
    __default_ver__ = TRIGGER_LATEST

    # @formatter:off
    _type: int                               = Retriever(i32,          default = 0)
    _properties: list[int]                   = Retriever(Array32[i32], default_factory = lambda _ver: [-1]*33)
    _xs_function: str                        = Retriever(str32,        default = "", min_ver = Version(2, 3))

    _quantity: int                           = RetrieverRef(ret(_properties),  0)
    _resource: int                           = RetrieverRef(ret(_properties),  1)
    _primary_unit_ref: int                   = RetrieverRef(ret(_properties),  2)
    _secondary_unit_ref: int                 = RetrieverRef(ret(_properties),  3)
    _unit_type: int                          = RetrieverRef(ret(_properties),  4)
    _source_player: int                      = RetrieverRef(ret(_properties),  5)
    _technology: int                         = RetrieverRef(ret(_properties),  6)
    _timer: int                              = RetrieverRef(ret(_properties),  7)
    _trigger_idx: int                        = RetrieverRef(ret(_properties),  8)

    @property
    def _area(self) -> Area:
        return Area((self._properties[9], self._properties[10]), (self._properties[11], self._properties[12]))

    @_area.setter
    def _area(self, value: AreaT) -> None:
        (
            (self._properties[9], self._properties[10]),
            (self._properties[11], self._properties[12])
        ) = Area.from_value(value)

    _object_group: int                      = RetrieverRef(ret(_properties), 13)
    _object_type: int                       = RetrieverRef(ret(_properties), 14)
    _ai_signal: int                         = RetrieverRef(ret(_properties), 15)
    _inverted: int                          = RetrieverRef(ret(_properties), 16)
    _unknown2: int                          = RetrieverRef(ret(_properties), 17)
    _variable: int                          = RetrieverRef(ret(_properties), 18)
    _comparison: int                        = RetrieverRef(ret(_properties), 19)
    _target_player: int                     = RetrieverRef(ret(_properties), 20)
    _unit_action: int                       = RetrieverRef(ret(_properties), 21)
    _unknown4: int                          = RetrieverRef(ret(_properties), 22)
    _object_state: int                      = RetrieverRef(ret(_properties), 23)
    _timer_id: int                          = RetrieverRef(ret(_properties), 24)
    _victory_timer_type: int                = RetrieverRef(ret(_properties), 25)
    _include_changeable_weapon_objects: int = RetrieverRef(ret(_properties), 26)
    _decision_id: int                       = RetrieverRef(ret(_properties), 27)
    _decision_option: int                   = RetrieverRef(ret(_properties), 28)
    _variable2: int                         = RetrieverRef(ret(_properties), 29)
    _local_technology: int                  = RetrieverRef(ret(_properties), 30)
    _object_group2: int                     = RetrieverRef(ret(_properties), 31)
    _object_type2: int                      = RetrieverRef(ret(_properties), 32)
    # @formatter:on
