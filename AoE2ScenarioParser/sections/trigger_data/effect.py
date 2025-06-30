from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version, RetrieverRef, ret
from bfp_rs.types.le import Array32, i32, nt_str32
from bfp_rs.combinators import set_repeat

from AoE2ScenarioParser.sections.scx_versions import TRIGGER_LATEST

def selected_unit_ids():
    return [
        set_repeat(ret(Effect.selected_unit_ids)).from_(ret(Effect._properties), 4)
    ]

class Effect(BaseStruct):
    # @formatter:off
    type: int                       = Retriever(i32,          default = -1)
    _properties: list[int]          = Retriever(Array32[i32], default_factory = lambda _ver: [-1]*58, on_read = selected_unit_ids)
    message: str                    = Retriever(nt_str32,     default = "")
    sound_name: str                 = Retriever(nt_str32,     default = "")
    # this list starts in 1.20, previous versions use the _properties[4] as the singular selected unit ID
    selected_unit_ids: list[int]    = Retriever(i32,          default = -1, repeat = 0)
    unused_string1: str             = Retriever(nt_str32,     default = "", min_ver = Version(3, 9))
    unused_string2: str             = Retriever(nt_str32,     default = "", min_ver = Version(3, 9))

    # todo: subclassing?
    ai_script_goal: int             = RetrieverRef(_properties, 0)
    quantity: int                   = RetrieverRef(_properties, 1)
    resource: int                   = RetrieverRef(_properties, 2)
    diplomacy: int                  = RetrieverRef(_properties, 3)
    num_objects_selected: int       = RetrieverRef(_properties, 4)
    legacy_location_object_ref: int = RetrieverRef(_properties, 5)
    unit_type1: int                 = RetrieverRef(_properties, 6)
    source_player: int              = RetrieverRef(_properties, 7)
    target_player: int              = RetrieverRef(_properties, 8)
    technology: int                 = RetrieverRef(_properties, 9)
    string_id: int                  = RetrieverRef(_properties, 10)
    sound_id: int                   = RetrieverRef(_properties, 11)
    instruction_display_time: int   = RetrieverRef(_properties, 12)
    trigger_idx: int                = RetrieverRef(_properties, 13)

    # todo: use the new area/tiles here
    @property
    def location(self):
        return self._properties[14], self._properties[15]

    @location.setter
    def location(self, value: tuple[int, int]):
        self._properties[14], self._properties[15] = value

    @property
    def area(self) -> tuple[tuple[int, int], tuple[int, int]]:
        return (self._properties[16], self._properties[17]), (self._properties[18], self._properties[19])

    @area.setter
    def area(self, value: tuple[tuple[int, int], tuple[int, int]]):
        (self._properties[16], self._properties[17]), (self._properties[18], self._properties[19]) = value

    object_group: int               = RetrieverRef(_properties, 20)
    object_type: int                = RetrieverRef(_properties, 21)
    instruction_panel_position: int = RetrieverRef(_properties, 22)
    attack_stance: int              = RetrieverRef(_properties, 23)
    time_unit: int                  = RetrieverRef(_properties, 24)
    enabled: int                    = RetrieverRef(_properties, 25)
    food: int                       = RetrieverRef(_properties, 26)
    wood: int                       = RetrieverRef(_properties, 27)
    stone: int                      = RetrieverRef(_properties, 28)
    gold: int                       = RetrieverRef(_properties, 29)
    item_id: int                    = RetrieverRef(_properties, 30)
    flash_object: int               = RetrieverRef(_properties, 31)
    force_research_technology: int  = RetrieverRef(_properties, 32)
    visibility_state: int           = RetrieverRef(_properties, 33)
    scroll: int                     = RetrieverRef(_properties, 34)
    operation: int                  = RetrieverRef(_properties, 35)
    unit_type2: int                 = RetrieverRef(_properties, 36)
    button_location: int            = RetrieverRef(_properties, 37)
    ai_signal_value: int            = RetrieverRef(_properties, 38)
    # todo: what's this
    unknown3: int                   = RetrieverRef(_properties, 39)
    object_attributes: int          = RetrieverRef(_properties, 40)
    variable: int                   = RetrieverRef(_properties, 41)
    timer: int                      = RetrieverRef(_properties, 42)
    facet: int                      = RetrieverRef(_properties, 43)
    location_object_reference: int  = RetrieverRef(_properties, 44)
    play_sound: int                 = RetrieverRef(_properties, 45)
    colour: int                     = RetrieverRef(_properties, 46)
    # todo: what's this
    unknown4: int                   = RetrieverRef(_properties, 47)
    colour_mood: int                = RetrieverRef(_properties, 48)
    reset_timer: int                = RetrieverRef(_properties, 49)
    object_state: int               = RetrieverRef(_properties, 50)
    action_type: int                = RetrieverRef(_properties, 51)
    resource1: int                  = RetrieverRef(_properties, 52)
    resource1_quantity: int         = RetrieverRef(_properties, 53)
    resource2: int                  = RetrieverRef(_properties, 54)
    resource2_quantity: int         = RetrieverRef(_properties, 55)
    resource3: int                  = RetrieverRef(_properties, 56)
    resource3_quantity: int         = RetrieverRef(_properties, 57)
    # @formatter:on

    # def map(self) -> BaseStruct:
    #     from testing.sections.effects import Effect as EffectCls
    #     return EffectCls._make_effect(self)

    def __new__(cls, ver: Version = TRIGGER_LATEST, init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, init_defaults, **retriever_inits)
