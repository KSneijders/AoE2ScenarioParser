from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, RetrieverRef, Version
from binary_file_parser.types import Array32, int32, nt_str32
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST, TRIGGER_LATEST


class Effect(BaseStruct):
    @staticmethod
    def set_sel_obj_ids_repeat(_, instance: Effect):
        if instance.num_objects_selected > 0:
            Effect.selected_object_ids.set_repeat(instance, instance.num_objects_selected)

    @staticmethod
    def sync_num_obj_sel(_, instance: Effect):
        instance.num_objects_selected = len(instance.selected_object_ids)

    @staticmethod
    def s1(_, instance: Effect):
        if instance._properties[4] > 0:
            Effect.selected_object_ids.set_repeat(instance, instance._properties[4])

    @staticmethod
    def s2(_, instance: Effect):
        instance._properties[4] = len(instance.selected_object_ids)

    # @formatter:off
    type: int                       = Retriever(int32,          default = -1)
    _properties: list[int]          = Retriever(Array32[int32], default_factory = lambda _: [-1]*52, on_set = [s1], on_write = [s2])
    message: str                    = Retriever(nt_str32,       default = "")
    sound_name: str                 = Retriever(nt_str32,       default = "")
    selected_object_ids: list[int]  = Retriever(int32,          default = -1, repeat = 0)

    # refs
    # todo: move these into their own effects in subclasses
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
    # @formatter:on

    # def map(self) -> BaseStruct:
    #     from testing.sections.effects import Effect as EffectCls
    #     return EffectCls._make_effect(self)

    def __init__(self, struct_ver: Version = TRIGGER_LATEST, initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
