from __future__ import annotations

from bfp_rs import BaseStruct, ret, Retriever, RetrieverRef, Version
from bfp_rs.combinators import set_repeat
from bfp_rs.types.le import Array32, i32, nt_str32

from AoE2ScenarioParser.objects.support import Area, AreaT, Tile, TileT
from AoE2ScenarioParser.sections.scx_versions import TRIGGER_LATEST


def selected_unit_ids():
    return [
        set_repeat(ret(Effect._selected_objects)).from_(ret(Effect._properties), 4)
    ]


class Effect(BaseStruct):
    __default_ver__ = TRIGGER_LATEST

    # @formatter:off
    _type: int                       = Retriever(i32,          default = -1)
    _properties: list[int]           = Retriever(Array32[i32], default_factory = lambda _ver: [-1]*81, on_read = selected_unit_ids)
    _message: str                    = Retriever(nt_str32,     default = "")
    _sound_name: str                 = Retriever(nt_str32,     default = "")
    # this list starts in 1.20, previous versions use the _properties[4] as the singular selected unit ID
    _selected_objects: list[int]     = Retriever(i32,          default = -1, repeat = 0)
    _message_option1: str            = Retriever(nt_str32,     default = "", min_ver = Version(3, 9))
    _message_option2: str            = Retriever(nt_str32,     default = "", min_ver = Version(3, 9))

    _ai_script_goal: int             = RetrieverRef(ret(_properties),  0)
    _quantity: int                   = RetrieverRef(ret(_properties),  1)
    _resource: int                   = RetrieverRef(ret(_properties),  2)
    _diplomacy_state: int            = RetrieverRef(ret(_properties),  3)
    _num_objects_selected: int       = RetrieverRef(ret(_properties),  4)
    _legacy_location_object_ref: int = RetrieverRef(ret(_properties),  5)
    _object_unit_id: int             = RetrieverRef(ret(_properties),  6)
    _source_player: int              = RetrieverRef(ret(_properties),  7)
    _target_player: int              = RetrieverRef(ret(_properties),  8)
    _technology_id: int              = RetrieverRef(ret(_properties),  9)
    _str_id: int                     = RetrieverRef(ret(_properties), 10)
    _sound_id: int                   = RetrieverRef(ret(_properties), 11)
    _display_time: int               = RetrieverRef(ret(_properties), 12)
    _trigger: int                    = RetrieverRef(ret(_properties), 13)

    @property
    def _location(self) -> Tile:
        return Tile((self._properties[14], self._properties[15]))

    @_location.setter
    def _location(self, value: TileT) -> None:
        self._properties[14], self._properties[15] = Tile.from_value(value)

    @property
    def _area(self) -> Area:
        return Area((self._properties[16], self._properties[17]), (self._properties[18], self._properties[19]))

    @_area.setter
    def _area(self, value: AreaT) -> None:
        (
            (self._properties[16], self._properties[17]),
            (self._properties[18], self._properties[19])
        ) = Area.from_value(value)

    _object_group: int                     = RetrieverRef(ret(_properties), 20)
    _object_type: int                      = RetrieverRef(ret(_properties), 21)
    _instruction_panel_position: int       = RetrieverRef(ret(_properties), 22)
    _attack_stance: int                    = RetrieverRef(ret(_properties), 23)
    _time_unit: int                        = RetrieverRef(ret(_properties), 24)
    _enabled: int                          = RetrieverRef(ret(_properties), 25)
    _food: int                             = RetrieverRef(ret(_properties), 26)
    _wood: int                             = RetrieverRef(ret(_properties), 27)
    _stone: int                            = RetrieverRef(ret(_properties), 28)
    _gold: int                             = RetrieverRef(ret(_properties), 29)
    _item_id: int                          = RetrieverRef(ret(_properties), 30)
    _flash_object: int                     = RetrieverRef(ret(_properties), 31)
    _force_technology: int                 = RetrieverRef(ret(_properties), 32)
    _visibility_state: int                 = RetrieverRef(ret(_properties), 33)
    _scroll: int                           = RetrieverRef(ret(_properties), 34)
    _operation: int                        = RetrieverRef(ret(_properties), 35)
    _object_unit_id2: int                  = RetrieverRef(ret(_properties), 36)
    _button_location: int                  = RetrieverRef(ret(_properties), 37)
    _ai_signal_value: int                  = RetrieverRef(ret(_properties), 38)
    _unknown3: int                         = RetrieverRef(ret(_properties), 39)
    _object_attributes: int                = RetrieverRef(ret(_properties), 40)
    _variable: int                         = RetrieverRef(ret(_properties), 41)
    _timer_id: int                         = RetrieverRef(ret(_properties), 42)
    _facet: int                            = RetrieverRef(ret(_properties), 43)
    _location_object_ref: int              = RetrieverRef(ret(_properties), 44)
    _play_sound: int                       = RetrieverRef(ret(_properties), 45)
    _player_color: int                     = RetrieverRef(ret(_properties), 46)
    _unknown4: int                         = RetrieverRef(ret(_properties), 47)
    _color_mood: int                       = RetrieverRef(ret(_properties), 48)
    _reset_timer: int                      = RetrieverRef(ret(_properties), 49)
    _object_state: int                     = RetrieverRef(ret(_properties), 50)
    _action_type: int                      = RetrieverRef(ret(_properties), 51)
    _resource1: int                        = RetrieverRef(ret(_properties), 52)
    _resource1_quantity: int               = RetrieverRef(ret(_properties), 53)
    _resource2: int                        = RetrieverRef(ret(_properties), 54)
    _resource2_quantity: int               = RetrieverRef(ret(_properties), 55)
    _resource3: int                        = RetrieverRef(ret(_properties), 56)
    _resource3_quantity: int               = RetrieverRef(ret(_properties), 57)
    _decision_id: int                      = RetrieverRef(ret(_properties), 58)
    _decision_option1_str_id: int          = RetrieverRef(ret(_properties), 59)
    _decision_option2_str_id: int          = RetrieverRef(ret(_properties), 60)
    _variable2: int                        = RetrieverRef(ret(_properties), 61)
    _max_units_affected: int               = RetrieverRef(ret(_properties), 62)
    _disable_garrison_unload_sound: int    = RetrieverRef(ret(_properties), 63)
    _hotkey: int                           = RetrieverRef(ret(_properties), 64)
    _train_time: int                       = RetrieverRef(ret(_properties), 65)
    _local_technology_id: int              = RetrieverRef(ret(_properties), 66)
    _disable_sound: int                    = RetrieverRef(ret(_properties), 67)
    _object_group2: int                    = RetrieverRef(ret(_properties), 68)
    _object_type2: int                     = RetrieverRef(ret(_properties), 69)
    _quantity_float: int                   = RetrieverRef(ret(_properties), 70)
    _facet2: int                           = RetrieverRef(ret(_properties), 71)
    _global_sound: int                     = RetrieverRef(ret(_properties), 72)
    _issue_group_command: int              = RetrieverRef(ret(_properties), 73)
    _queue_action: int                     = RetrieverRef(ret(_properties), 74)
    _mutual_diplomacy: int                 = RetrieverRef(ret(_properties), 75)
    _building_list: int                    = RetrieverRef(ret(_properties), 76)
    _wall_x1: int                          = RetrieverRef(ret(_properties), 77)
    _wall_y1: int                          = RetrieverRef(ret(_properties), 78)
    _wall_x2: int                          = RetrieverRef(ret(_properties), 79)
    _wall_y2: int                          = RetrieverRef(ret(_properties), 80)
    # @formatter:on
