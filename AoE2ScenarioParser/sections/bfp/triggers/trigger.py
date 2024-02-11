from __future__ import annotations

from typing import TYPE_CHECKING

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import Bytes, bool32, bool8, int32, nt_str32, RefList, uint32

from AoE2ScenarioParser.helper.list_functions import update_order_array
from AoE2ScenarioParser.sections.bfp.triggers import ConditionStruct, EffectStruct
from AoE2ScenarioParser.sections.bfp.triggers.trigger_bfp_repr import TriggerBfpRepr

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.data_objects.conditions.condition import Condition
    from AoE2ScenarioParser.objects.data_objects.effects.effect import Effect


class Trigger(TriggerBfpRepr, BaseStruct):

    @staticmethod
    def set_effects_repeat(_, instance: Trigger):
        Retriever.set_repeat(Trigger.effects, instance, instance.num_effects)  # type:ignore

    @staticmethod
    def set_effect_display_orders_repeat(_, instance: Trigger):
        Retriever.set_repeat(Trigger.effect_display_orders, instance, instance.num_effects)  # type:ignore

    @staticmethod
    def set_conditions_repeat(_, instance: Trigger):
        Retriever.set_repeat(Trigger.conditions, instance, instance.num_conditions)  # type:ignore

    @staticmethod
    def set_condition_display_orders_repeat(_, instance: Trigger):
        Retriever.set_repeat(Trigger.condition_display_orders, instance, instance.num_conditions)  # type:ignore

    @staticmethod
    def update_num_effects(_, instance: Trigger):
        instance.num_effects = len(instance.effects)
        update_order_array(instance.effect_display_orders, instance.num_effects)

    @staticmethod
    def update_num_conditions(_, instance: Trigger):
        instance.num_conditions = len(instance.conditions)
        update_order_array(instance.condition_display_orders, instance.num_conditions)

    # @formatter:off
    enabled: bool                          = Retriever(bool32,                                default = True)
    looping: bool                          = Retriever(bool8,                                 default = False)
    description_str_id_id_2_4_1_40: int    = Retriever(int32, max_ver=Version((2, 4, 1, 40)), default = -1)
    description_str_id_id_2_4_1_41: int    = Retriever(int32, min_ver=Version((2, 4, 1, 41)), default = 0)
    display_as_objective: bool             = Retriever(bool8,                                 default = False)
    objective_description_order: int       = Retriever(uint32,                                default = 0)
    make_header: bool                      = Retriever(bool8,                                 default = False)
    short_description_str_id_2_4_1_40: int = Retriever(int32, max_ver=Version((2, 4, 1, 40)), default = -1)
    short_description_str_id_2_4_1_41: int = Retriever(int32, min_ver=Version((2, 4, 1, 41)), default = 0)
    display_on_screen: bool                = Retriever(bool8,                                 default = False)
    unknown: bytes                         = Retriever(Bytes[5],                              default = b"\x00" * 5)
    mute_objectives: bool                  = Retriever(bool8,                                 default = False)
    description: str                       = Retriever(nt_str32,                              default = "")
    name: str                              = Retriever(nt_str32,                              default = "Trigger 0")
    short_description: str                 = Retriever(nt_str32,                              default = "")
    num_effects: int                       = Retriever(uint32,                                default = 0,
                                                       on_set=[set_effects_repeat, set_effect_display_orders_repeat],
                                                       on_write=[update_num_effects])
    effects: list[Effect]                  = Retriever(EffectStruct,                          default_factory = lambda sv, p: EffectStruct(sv, p),   repeat=0)
    effect_display_orders: list[int]       = Retriever(uint32,                                default = 0,              repeat=0)
    num_conditions: int                    = Retriever(uint32,                                default = 0,
                                                       on_set=[set_conditions_repeat, set_condition_display_orders_repeat],
                                                       on_write=[update_num_conditions])
    conditions: list[Condition]            = Retriever(ConditionStruct,                       default_factory = lambda sv, p: ConditionStruct(sv, p),    repeat=0)
    condition_display_orders: list[int]    = Retriever(uint32,                                default = 0,              repeat=0)
    # @formatter:on

    def __init__(
        self, struct_ver: Version = Version((3, 5, 1, 47)), parent: BaseStruct = None, initialise_defaults = True,
        **retriever_inits
    ):
        if 'effects' in retriever_inits:
            retriever_inits['effects'] = RefList(retriever_inits['effects'])
        if 'conditions' in retriever_inits:
            retriever_inits['conditions'] = RefList(retriever_inits['conditions'])

        super().__init__(struct_ver, parent, initialise_defaults = initialise_defaults, **retriever_inits)
