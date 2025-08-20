from __future__ import annotations

from bfp_rs import BaseStruct, ret, Retriever, RetrieverRef, Version
from bfp_rs.combinators import set_repeat
from bfp_rs.types.le import Array32, i32, nt_str32

from AoE2ScenarioParser.objects.support import Area, AreaT, Tile, TileT
from AoE2ScenarioParser.sections.scx_versions import TRIGGER_LATEST


def selected_unit_ids():
    return [
        set_repeat(ret(Effect.selected_unit_ids)).from_(ret(Effect._properties), 4)
    ]


class Effect(BaseStruct):
    # @formatter:off
    type: int                       = Retriever(i32,          default = -1)
    _properties: list[int]          = Retriever(Array32[i32], default_factory = lambda _ver: [-1]*62, on_read = selected_unit_ids)
    message: str                    = Retriever(nt_str32,     default = "")
    sound_name: str                 = Retriever(nt_str32,     default = "")
    # this list starts in 1.20, previous versions use the _properties[4] as the singular selected unit ID
    selected_unit_ids: list[int]    = Retriever(i32,          default = -1, repeat = 0)
    message_option1: str            = Retriever(nt_str32,     default = "", min_ver = Version(3, 9))
    message_option2: str            = Retriever(nt_str32,     default = "", min_ver = Version(3, 9))

    ai_script_goal: int             = RetrieverRef(ret(_properties),  0)
    quantity: int                   = RetrieverRef(ret(_properties),  1)
    resource: int                   = RetrieverRef(ret(_properties),  2)
    diplomacy: int                  = RetrieverRef(ret(_properties),  3)
    num_objects_selected: int       = RetrieverRef(ret(_properties),  4)
    legacy_location_object_ref: int = RetrieverRef(ret(_properties),  5)
    unit_type1: int                 = RetrieverRef(ret(_properties),  6)
    source_player: int              = RetrieverRef(ret(_properties),  7)
    target_player: int              = RetrieverRef(ret(_properties),  8)
    technology: int                 = RetrieverRef(ret(_properties),  9)
    string_id: int                  = RetrieverRef(ret(_properties), 10)
    sound_id: int                   = RetrieverRef(ret(_properties), 11)
    instruction_display_time: int   = RetrieverRef(ret(_properties), 12)
    trigger_idx: int                = RetrieverRef(ret(_properties), 13)

    @property
    def location(self) -> Tile:
        return Tile((self._properties[14], self._properties[15]))

    @location.setter
    def location(self, value: TileT) -> None:
        self._properties[14], self._properties[15] = Tile.from_value(value)

    @property
    def area(self) -> Area:
        return Area((self._properties[16], self._properties[17]), (self._properties[18], self._properties[19]))

    @area.setter
    def area(self, value: AreaT) -> None:
        (
            (self._properties[16], self._properties[17]),
            (self._properties[18], self._properties[19])
        ) = Area.from_value(value)

    object_group: int               = RetrieverRef(ret(_properties), 20)
    object_type: int                = RetrieverRef(ret(_properties), 21)
    instruction_panel_position: int = RetrieverRef(ret(_properties), 22)
    attack_stance: int              = RetrieverRef(ret(_properties), 23)
    time_unit: int                  = RetrieverRef(ret(_properties), 24)
    enabled: int                    = RetrieverRef(ret(_properties), 25)
    food: int                       = RetrieverRef(ret(_properties), 26)
    wood: int                       = RetrieverRef(ret(_properties), 27)
    stone: int                      = RetrieverRef(ret(_properties), 28)
    gold: int                       = RetrieverRef(ret(_properties), 29)
    item_id: int                    = RetrieverRef(ret(_properties), 30)
    flash_object: int               = RetrieverRef(ret(_properties), 31)
    force_research_technology: int  = RetrieverRef(ret(_properties), 32)
    visibility_state: int           = RetrieverRef(ret(_properties), 33)
    scroll: int                     = RetrieverRef(ret(_properties), 34)
    operation: int                  = RetrieverRef(ret(_properties), 35)
    unit_type2: int                 = RetrieverRef(ret(_properties), 36)
    button_location: int            = RetrieverRef(ret(_properties), 37)
    ai_signal_value: int            = RetrieverRef(ret(_properties), 38)
    unknown3: int                   = RetrieverRef(ret(_properties), 39)
    object_attributes: int          = RetrieverRef(ret(_properties), 40)
    variable: int                   = RetrieverRef(ret(_properties), 41)
    timer: int                      = RetrieverRef(ret(_properties), 42)
    facet: int                      = RetrieverRef(ret(_properties), 43)
    location_object_reference: int  = RetrieverRef(ret(_properties), 44)
    play_sound: int                 = RetrieverRef(ret(_properties), 45)
    color: int                      = RetrieverRef(ret(_properties), 46)
    unknown4: int                   = RetrieverRef(ret(_properties), 47)
    color_mood: int                 = RetrieverRef(ret(_properties), 48)
    reset_timer: int                = RetrieverRef(ret(_properties), 49)
    object_state: int               = RetrieverRef(ret(_properties), 50)
    action_type: int                = RetrieverRef(ret(_properties), 51)
    resource1: int                  = RetrieverRef(ret(_properties), 52)
    resource1_quantity: int         = RetrieverRef(ret(_properties), 53)
    resource2: int                  = RetrieverRef(ret(_properties), 54)
    resource2_quantity: int         = RetrieverRef(ret(_properties), 55)
    resource3: int                  = RetrieverRef(ret(_properties), 56)
    resource3_quantity: int         = RetrieverRef(ret(_properties), 57)
    decision_id: int                = RetrieverRef(ret(_properties), 58)
    string_id_option1: int          = RetrieverRef(ret(_properties), 59)
    string_id_option2: int          = RetrieverRef(ret(_properties), 60)
    variable2: int                  = RetrieverRef(ret(_properties), 61)
    # @formatter:on

    def __new__(cls, ver: Version = TRIGGER_LATEST, init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, init_defaults, **retriever_inits)
