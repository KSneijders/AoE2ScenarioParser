from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int32, str32

from AoE2ScenarioParser.datasets.triggers import EffectType
from AoE2ScenarioParser.objects.support import Tile, Area

attr_usage_ids = {
    "_message": {
        EffectType.SEND_CHAT,
        EffectType.DISPLAY_INSTRUCTIONS,
        EffectType.CHANGE_OBJECT_NAME,
        EffectType.DISPLAY_TIMER,
        EffectType.CHANGE_OBJECT_DESCRIPTION,
        EffectType.CHANGE_PLAYER_NAME,
        EffectType.CHANGE_CIVILIZATION_NAME,
        EffectType.MODIFY_ATTRIBUTE,
        EffectType.SCRIPT_CALL,
        EffectType.CHANGE_VARIABLE,
        EffectType.CHANGE_OBJECT_CIVILIZATION_NAME,
        EffectType.CHANGE_OBJECT_PLAYER_NAME,
        EffectType.CHANGE_TECHNOLOGY_NAME,
        EffectType.CHANGE_TECHNOLOGY_DESCRIPTION,
    },
    "_sound_name": {
        EffectType.SEND_CHAT,
        EffectType.PLAY_SOUND,
        EffectType.DISPLAY_INSTRUCTIONS,
    },
}


class EffectStruct(BaseStruct):
    @staticmethod
    def set_sel_obj_ids_repeat(_, instance: EffectStruct):
        repeat = 0 if instance._num_objects_selected == -1 else instance._num_objects_selected
        Retriever.set_repeat(instance._selected_object_ids, instance, repeat)

    @staticmethod
    def remove_null_term(retriever: Retriever, instance: EffectStruct):
        setattr(instance, retriever.s_name, getattr(instance, retriever.s_name).removesuffix("\x00"))

    @staticmethod
    def append_null_term_if_used(retriever: Retriever, instance: EffectStruct):
        if instance._type in attr_usage_ids[retriever.p_name]:
            val = getattr(instance, retriever.s_name)
            if len(val) > 0 and val[-1] != "\x00":
                setattr(instance, retriever.s_name, val + "\x00")

    @staticmethod
    def update_num_obj_sel(_, instance: EffectStruct):
        instance._num_objects_selected = len(instance._selected_object_ids)

    # Todo: use datasets for type hinting and do on_read and on_write conversions
    # Todo: override list with ref-list in retriever
    # formatter:off
    _type: int                             = Retriever(int32,                                                 default=-1)
    _static_value_2_2_1_36: int            = Retriever(int32,                 max_ver=Version((2, 2, 1, 37)), default=46)
    _static_value_2_4_1_40: int            = Retriever(int32, Version((2, 4, 1, 40)), Version((2, 4, 1, 41)), default=48)
    _static_value_2_4_1_42: int            = Retriever(int32, Version((2, 4, 1, 42)), Version((2, 4, 1, 43)), default=49)
    _static_value_2_4_1_44: int            = Retriever(int32, Version((2, 4, 1, 44)),                         default=52)
    _ai_script_goal: int                   = Retriever(int32,                                                 default=-1)
    _quantity: int                         = Retriever(int32,                                                 default=-1)
    _tribute_list: int                     = Retriever(int32,                                                 default=-1)
    _diplomacy: int                        = Retriever(int32,                                                 default=-1)
    _num_objects_selected: int             = Retriever(int32,                                                 default=-1, on_set=[set_sel_obj_ids_repeat], on_write=[update_num_obj_sel])
    _legacy_location_object_reference: int = Retriever(int32,                                                 default=-1)
    _object_list_unit_id: int              = Retriever(int32,                                                 default=-1)
    _source_player: int                    = Retriever(int32,                                                 default=-1)
    _target_player: int                    = Retriever(int32,                                                 default=-1)
    _technology: int                       = Retriever(int32,                                                 default=-1)
    _string_id: int                        = Retriever(int32,                                                 default=-1)
    _unknown2: int                         = Retriever(int32,                                                 default=-1)
    _display_time: int                     = Retriever(int32,                                                 default=-1)
    _trigger_id: int                       = Retriever(int32,                                                 default=-1)
    _location: Tile                        = Retriever(Tile,                                                  default=Tile(-1, -1))
    _area: Area                            = Retriever(Area,                                                  default=Area((-1, -1)))
    _object_group: int                     = Retriever(int32,                                                 default=-1)
    _object_type: int                      = Retriever(int32,                                                 default=-1)
    _instruction_panel_position: int       = Retriever(int32,                                                 default=-1)
    _attack_stance: int                    = Retriever(int32,                                                 default=-1)
    _time_unit: int                        = Retriever(int32,                                                 default=-1)
    _enabled: int                          = Retriever(int32,                                                 default=-1)
    _food: int                             = Retriever(int32,                                                 default=-1)
    _wood: int                             = Retriever(int32,                                                 default=-1)
    _stone: int                            = Retriever(int32,                                                 default=-1)
    _gold: int                             = Retriever(int32,                                                 default=-1)
    _item_id: int                          = Retriever(int32,                                                 default=-1)
    _flash_object: int                     = Retriever(int32,                                                 default=-1)
    _force_research_technology: int        = Retriever(int32,                                                 default=-1)
    _visibility_state: int                 = Retriever(int32,                                                 default=-1)
    _scroll: int                           = Retriever(int32,                                                 default=-1)
    _operation: int                        = Retriever(int32,                                                 default=-1)
    _object_list_unit_id2: int             = Retriever(int32,                                                 default=-1)
    _button_location: int                  = Retriever(int32,                                                 default=-1)
    _ai_signal_value: int                  = Retriever(int32,                                                 default=-1)
    _unknown3: int                         = Retriever(int32,                                                 default=-1)
    _object_attributes: int                = Retriever(int32,                                                 default=-1)
    _variable: int                         = Retriever(int32,                                                 default=-1)
    _timer: int                            = Retriever(int32,                                                 default=-1)
    _facet: int                            = Retriever(int32,                                                 default=-1)
    _location_object_reference: int        = Retriever(int32,                                                 default=-1)
    _play_sound: int                       = Retriever(int32,                                                 default=-1)
    _player_colour: int                    = Retriever(int32, Version((2, 4, 1, 40)),                         default=-1)
    _unknown4: int                         = Retriever(int32, Version((2, 4, 1, 40)),                         default=-1)
    _colour_mood: int                      = Retriever(int32, Version((2, 4, 1, 42)),                         default=-1)
    _reset_timer: int                      = Retriever(int32, Version((2, 4, 1, 44)),                         default=-1)
    _object_state: int                     = Retriever(int32, Version((2, 4, 1, 44)),                         default=-1)
    _action_type: int                      = Retriever(int32, Version((2, 4, 1, 44)),                         default=-1)
    _message: str                          = Retriever(str32,                                                 default="", on_read=[remove_null_term], on_write=[append_null_term_if_used])
    _sound_name: str                       = Retriever(str32,                                                 default="", on_read=[remove_null_term], on_write=[append_null_term_if_used])
    _selected_object_ids: list[int]        = Retriever(int32,                                                 default=-1, repeat=0)
    # formatter:on

    def __init__(self, struct_ver: Version = Version((3, 5, 1, 47)), parent: BaseStruct = None, initialise_defaults=True, **retriever_inits):
        super().__init__(struct_ver, parent, initialise_defaults=initialise_defaults, **retriever_inits)
