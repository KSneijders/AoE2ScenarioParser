from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version, RetrieverRef
from bfp_rs.types.le import Array32, i32, str32

from AoE2ScenarioParser.sections.scx_versions import TRIGGER_LATEST


class Condition(BaseStruct):
    # @formatter:off
    type: int                              = Retriever(i32,          default = 0)
    _properties: list[int]                 = Retriever(Array32[i32], default_factory = lambda _ver: [-1]*27)
    xs_function: str                       = Retriever(str32,        default = "", min_ver = Version(2, 3))

    # todo: subclassing?
    num_properties: int                    = RetrieverRef(_properties, 0)
    quantity: int                          = RetrieverRef(_properties, 1)
    resource: int                          = RetrieverRef(_properties, 2)
    primary_unit_ref: int                  = RetrieverRef(_properties, 3)
    secondary_unit_ref: int                = RetrieverRef(_properties, 4)
    unit_type: int                         = RetrieverRef(_properties, 5)
    source_player: int                     = RetrieverRef(_properties, 6)
    technology: int                        = RetrieverRef(_properties, 7)
    timer: int                             = RetrieverRef(_properties, 8)
    trigger_idx: int                       = RetrieverRef(_properties, 9)

    # todo: use the new area/tiles here
    @property
    def area(self) -> tuple[tuple[int, int], tuple[int, int]]:
        return (self._properties[10], self._properties[11]), (self._properties[12], self._properties[13])

    @area.setter
    def area(self, value: tuple[tuple[int, int], tuple[int, int]]):
        (self._properties[10], self._properties[11]), (self._properties[12], self._properties[13]) = value

    object_group: int                      = RetrieverRef(_properties, 14)
    object_type: int                       = RetrieverRef(_properties, 15)
    ai_signal: int                         = RetrieverRef(_properties, 16)
    inverted: int                          = RetrieverRef(_properties, 17)
    # todo: find out what this is
    unknown2: int                          = RetrieverRef(_properties, 18)
    variable: int                          = RetrieverRef(_properties, 19)
    comparison: int                        = RetrieverRef(_properties, 20)
    target_player: int                     = RetrieverRef(_properties, 21)
    unit_action: int                       = RetrieverRef(_properties, 22)
    # todo: find out what this is
    unknown4: int                          = RetrieverRef(_properties, 23)
    object_state: int                      = RetrieverRef(_properties, 24)
    timer_id: int                          = RetrieverRef(_properties, 25)
    victory_timer_type: int                = RetrieverRef(_properties, 26)
    include_changeable_weapon_objects: int = RetrieverRef(_properties, 27)
    # @formatter:on

    def __new__(cls, ver: Version = TRIGGER_LATEST, init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, init_defaults, **retriever_inits)
