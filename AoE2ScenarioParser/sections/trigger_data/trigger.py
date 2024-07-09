from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import Array32, bool32, bool8, Bytes, int32, nt_str32, uint32, uint8
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST, TRIGGER_LATEST
from AoE2ScenarioParser.sections.trigger_data.condition import Condition
from AoE2ScenarioParser.sections.trigger_data.effect import Effect


class Trigger(BaseStruct):
    @staticmethod
    def set_eff_disp_ords_repeat(_, instance: Trigger):
        Trigger.effect_display_orders.set_repeat(instance, len(instance.effects))

    @staticmethod
    def sync_eff_disp_ords(_, instance: Trigger):
        num_effects = len(instance.effects)
        if (
            len(instance.effect_display_orders) != num_effects
            or len(set(instance.effect_display_orders)) != num_effects
            or any(map(lambda id_: id_ >= num_effects, instance.effect_display_orders))
        ):
            instance.effect_display_orders = list(range(num_effects))

    @staticmethod
    def set_con_disp_ords_repeat(_, instance: Trigger):
        Trigger.condition_display_orders.set_repeat(instance, len(instance.conditions))

    @staticmethod
    def sync_con_disp_ords(_, instance: Trigger):
        num_conditions = len(instance.conditions)
        if (
            len(instance.condition_display_orders) != num_conditions
            or len(set(instance.condition_display_orders)) != num_conditions
            or any(map(lambda id_: id_ >= num_conditions, instance.condition_display_orders))
        ):
            instance.condition_display_orders = list(range(num_conditions))

    # @formatter:off
    enabled: bool                          = Retriever(bool32,                                        default = True)
    looping: bool                          = Retriever(bool8,                                         default = False)
    description_str_id: int                = Retriever(int32,                                         default = 0)
    display_as_objective: bool             = Retriever(bool8,                                         default = False)
    objective_order: int                   = Retriever(uint32,                                        default = 0)
    make_header: bool                      = Retriever(bool8,              min_ver = Version((1, 8)), default = False)
    short_description_str_id: int          = Retriever(int32,              min_ver = Version((1, 8)), default = 0)
    display_on_screen: bool                = Retriever(bool8,              min_ver = Version((1, 8)), default = False)
    short_description_state: int           = Retriever(uint8,              min_ver = Version((1, 8)), default = 0)
    start_time: int                        = Retriever(uint32,                                        default = 0)
    mute_objectives: bool                  = Retriever(bool8,              min_ver = Version((1, 8)), default = False)
    description: str                       = Retriever(nt_str32,                                      default = "")
    name: str                              = Retriever(nt_str32,                                      default = "Trigger 0")
    short_description: str                 = Retriever(nt_str32,           min_ver = Version((1, 8)), default = "")
    effects: list[Effect]                  = Retriever(Array32[Effect],                               default_factory = lambda _: [], on_read = [set_eff_disp_ords_repeat])
    effect_display_orders: list[int]       = Retriever(uint32,                                        default = 0, repeat = 0,        on_write = [sync_eff_disp_ords])
    conditions: list[Condition]            = Retriever(Array32[Condition],                            default_factory = lambda _: [], on_read = [set_con_disp_ords_repeat])
    condition_display_orders: list[int]    = Retriever(uint32,                                        default = 0, repeat = 0,        on_write = [sync_con_disp_ords])
    # @formatter:on

    def __init__(self, struct_ver: Version = TRIGGER_LATEST, initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
