from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, RetrieverRef, Version
from binary_file_parser.types import Array32, int32, str32
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST, TRIGGER_LATEST


class Condition(BaseStruct):
    # @formatter:off
    type: int                              = Retriever(int32, default = 0)
    _properties: list[int]                 = Retriever(Array32[int32], default_factory = lambda _: [-1]*27)
    xs_function: str                       = Retriever(str32, default = "", min_ver = Version((2, 4)))

    # refs
    # todo: move these into their own conditions in subclasses
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

    # area_x1: int                           = RetrieverRef(_properties, 10)
    # area_y1: int                           = RetrieverRef(_properties, 11)
    # area_x2: int                           = RetrieverRef(_properties, 12)
    # area_y2: int                           = RetrieverRef(_properties, 13)
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

    def __init__(self, struct_ver: Version = TRIGGER_LATEST, initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
