from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int32, str32


attr_usage_ids = {
    "message": {3, 20, 26, 37, 44, 45, 48, 51, 55, 56, 59, 60, 65, 66},
    "sound_name": {3, 4, 20},
}


class Effect(BaseStruct):
    @staticmethod
    def set_sel_obj_ids_repeat(_, instance: Effect):
        repeat = 0 if instance.num_objects_selected == -1 else instance.num_objects_selected
        Retriever.set_repeat(Effect.selected_object_ids, instance, repeat)

    @staticmethod
    def remove_null_term(retriever: Retriever, instance: Effect):
        setattr(instance, retriever.s_name, getattr(instance, retriever.s_name).removesuffix("\x00"))

    @staticmethod
    def append_null_term_if_used(retriever: Retriever, instance: Effect):
        if instance.type in attr_usage_ids[retriever.p_name]:
            val = getattr(instance, retriever.s_name)
            if len(val) > 0 and val[-1] != "\x00":
                setattr(instance, retriever.s_name, val + "\x00")

    @staticmethod
    def update_num_obj_sel(_, instance: Effect):
        instance.num_objects_selected = len(instance.selected_object_ids)

    # formatter:off
    type: int                             = Retriever(int32,                                                 default=-1)
    static_value_2_2_1_36: int            = Retriever(int32,                 max_ver=Version((2, 2, 1, 37)), default=46)
    static_value_2_4_1_40: int            = Retriever(int32, Version((2, 4, 1, 40)), Version((2, 4, 1, 41)), default=48)
    static_value_2_4_1_42: int            = Retriever(int32, Version((2, 4, 1, 42)), Version((2, 4, 1, 43)), default=49)
    static_value_2_4_1_44: int            = Retriever(int32, Version((2, 4, 1, 44)),                         default=52)
    ai_script_goal: int                   = Retriever(int32,                                                 default=-1)
    quantity: int                         = Retriever(int32,                                                 default=-1)
    tribute_list: int                     = Retriever(int32,                                                 default=-1)
    diplomacy: int                        = Retriever(int32,                                                 default=-1)
    num_objects_selected: int             = Retriever(int32,                                                 default=-1, on_set=[set_sel_obj_ids_repeat], on_write=[update_num_obj_sel])
    legacy_location_object_reference: int = Retriever(int32,                                                 default=-1)
    object_list_unit_id: int              = Retriever(int32,                                                 default=-1)
    source_player: int                    = Retriever(int32,                                                 default=-1)
    target_player: int                    = Retriever(int32,                                                 default=-1)
    technology: int                       = Retriever(int32,                                                 default=-1)
    string_id: int                        = Retriever(int32,                                                 default=-1)
    unknown2: int                         = Retriever(int32,                                                 default=-1)
    display_time: int                     = Retriever(int32,                                                 default=-1)
    trigger_id: int                       = Retriever(int32,                                                 default=-1)
    location_x: int                       = Retriever(int32,                                                 default=-1)
    location_y: int                       = Retriever(int32,                                                 default=-1)
    area_x1: int                          = Retriever(int32,                                                 default=-1)
    area_y1: int                          = Retriever(int32,                                                 default=-1)
    area_x2: int                          = Retriever(int32,                                                 default=-1)
    area_y2: int                          = Retriever(int32,                                                 default=-1)
    object_group: int                     = Retriever(int32,                                                 default=-1)
    object_type: int                      = Retriever(int32,                                                 default=-1)
    instruction_panel_position: int       = Retriever(int32,                                                 default=-1)
    attack_stance: int                    = Retriever(int32,                                                 default=-1)
    time_unit: int                        = Retriever(int32,                                                 default=-1)
    enabled: int                          = Retriever(int32,                                                 default=-1)
    food: int                             = Retriever(int32,                                                 default=-1)
    wood: int                             = Retriever(int32,                                                 default=-1)
    stone: int                            = Retriever(int32,                                                 default=-1)
    gold: int                             = Retriever(int32,                                                 default=-1)
    item_id: int                          = Retriever(int32,                                                 default=-1)
    flash_object: int                     = Retriever(int32,                                                 default=-1)
    force_research_technology: int        = Retriever(int32,                                                 default=-1)
    visibility_state: int                 = Retriever(int32,                                                 default=-1)
    scroll: int                           = Retriever(int32,                                                 default=-1)
    operation: int                        = Retriever(int32,                                                 default=-1)
    object_list_unit_id2: int             = Retriever(int32,                                                 default=-1)
    button_location: int                  = Retriever(int32,                                                 default=-1)
    ai_signal_value: int                  = Retriever(int32,                                                 default=-1)
    unknown3: int                         = Retriever(int32,                                                 default=-1)
    object_attributes: int                = Retriever(int32,                                                 default=-1)
    variable: int                         = Retriever(int32,                                                 default=-1)
    timer: int                            = Retriever(int32,                                                 default=-1)
    facet: int                            = Retriever(int32,                                                 default=-1)
    location_object_reference: int        = Retriever(int32,                                                 default=-1)
    play_sound: int                       = Retriever(int32,                                                 default=-1)
    player_colour: int                    = Retriever(int32, Version((2, 4, 1, 40)),                         default=-1)
    unknown4: int                         = Retriever(int32, Version((2, 4, 1, 40)),                         default=-1)
    colour_mood: int                      = Retriever(int32, Version((2, 4, 1, 42)),                         default=-1)
    reset_timer: int                      = Retriever(int32, Version((2, 4, 1, 44)),                         default=-1)
    object_state: int                     = Retriever(int32, Version((2, 4, 1, 44)),                         default=-1)
    action_type: int                      = Retriever(int32, Version((2, 4, 1, 44)),                         default=-1)
    message: str                          = Retriever(str32,                                                 default="", on_read=[remove_null_term], on_write=[append_null_term_if_used])
    sound_name: str                       = Retriever(str32,                                                 default="", on_read=[remove_null_term], on_write=[append_null_term_if_used])
    selected_object_ids: list[int]        = Retriever(int32,                                                 default=-1, repeat=0)
    # formatter:on

    def __init__(self, struct_ver: Version = Version((3, 5, 1, 47)), parent: BaseStruct = None, initialise_defaults=True, **retriever_inits):
        super().__init__(struct_ver, parent, initialise_defaults=initialise_defaults, **retriever_inits)
