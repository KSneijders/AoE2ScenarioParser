from __future__ import annotations

from bfp_rs import BaseStruct, ret, Retriever, Version
from bfp_rs.combinators import set_repeat
from bfp_rs.types.le import Array32, bool32, bool8, i32, nt_str32, u32, u8

from AoE2ScenarioParser.sections.scx_versions import TRIGGER_LATEST
from AoE2ScenarioParser.sections.trigger_data.condition import Condition
from AoE2ScenarioParser.sections.trigger_data.effect import Effect


def effect_display_orders_repeat():
    return [
        set_repeat(ret(Trigger.effect_display_orders)).from_len(ret(Trigger.effects))
    ]


def condition_display_orders_repeat():
    return [
        set_repeat(ret(Trigger.condition_display_orders)).from_len(ret(Trigger.conditions))
    ]


class Trigger(BaseStruct):
    # @formatter:off
    enabled: bool                       = Retriever(bool32,                                      default = True)
    looping: bool                       = Retriever(bool8,                                       default = False)
    description_str_id: int             = Retriever(i32,                                         default = 0)
    display_as_objective: bool          = Retriever(bool8,                                       default = False)
    objective_order: int                = Retriever(u32,                                         default = 0)
    make_header: bool                   = Retriever(bool8,              min_ver = Version(1, 7), default = False)
    short_description_str_id: int       = Retriever(i32,                min_ver = Version(1, 8), default = 0)
    display_on_screen: bool             = Retriever(bool8,              min_ver = Version(1, 8), default = False)
    short_description_state: int        = Retriever(u8,                 min_ver = Version(1, 8), default = 0)
    start_time: int                     = Retriever(u32,                min_ver = Version(1, 6), default = 0)
    mute_objectives: bool               = Retriever(bool8,              min_ver = Version(2, 0), default = False)
    description: str                    = Retriever(nt_str32,                                    default = "")
    name: str                           = Retriever(nt_str32,                                    default = "Trigger 0")
    short_description: str              = Retriever(nt_str32,           min_ver = Version(1, 8), default = "")
    effects: list[Effect]               = Retriever(Array32[Effect],                             default_factory = lambda _: [], on_read = effect_display_orders_repeat)
    effect_display_orders: list[int]    = Retriever(u32,                                         default = 0, repeat = 0)
    conditions: list[Condition]         = Retriever(Array32[Condition],                          default_factory = lambda _: [], on_read = condition_display_orders_repeat)
    condition_display_orders: list[int] = Retriever(u32,                                         default = 0, repeat = 0)
    # @formatter:on

    def __new__(cls, ver: Version = TRIGGER_LATEST, init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, init_defaults, **retriever_inits)
