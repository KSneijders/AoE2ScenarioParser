from __future__ import annotations

from typing import Iterable, TYPE_CHECKING

from bfp_rs import BaseStruct, borrow_mut, ret, Retriever, Version
from bfp_rs.combinators import set_repeat
from bfp_rs.types.le import Array32, bool32, bool8, i32, nt_str32, u32, u8

from AoE2ScenarioParser.concerns import CanBeLinked, CanHoldUnits
from AoE2ScenarioParser.sections.scx_versions import TRIGGER_LATEST
from AoE2ScenarioParser.sections.trigger_data.condition import Condition
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if TYPE_CHECKING:
    from AoE2ScenarioParser.sections import Unit


def effect_display_orders_repeat():
    return [
        set_repeat(ret(Trigger.effect_display_orders)).from_len(ret(Trigger.effects))
    ]


def condition_display_orders_repeat():
    return [
        set_repeat(ret(Trigger.condition_display_orders)).from_len(ret(Trigger.conditions))
    ]


class Trigger(BaseStruct, CanHoldUnits, CanBeLinked):

    __default_ver__ = TRIGGER_LATEST

    # @formatter:off
    enabled: bool                       = Retriever(bool32,                                      default = True)
    looping: bool                       = Retriever(bool8,                                       default = False)
    execute_on_load: bool               = Retriever(bool8,              min_ver = Version(4, 3), default = False)
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

    def __init__(
        self,
        name: str = '',
        enabled: bool = True,
        looping: bool = False,
        execute_on_load: bool = False,
        description_str_id: int = 0,
        display_as_objective: bool = False,
        objective_order: int = 0,
        make_header: bool = False,
        short_description_str_id: int = 0,
        display_on_screen: bool = False,
        short_description_state: int = 0,  # Todo: Remove?
        start_time: int = 0,  # Todo: Remove?
        mute_objectives: bool = False,
        description: str = '',
        short_description: str = '',
        effects: list[Effect] | None = None,
        effect_display_orders: list[int] | None = None,  # Todo: Remove?
        conditions: list[Condition] | None = None,
        condition_display_orders: list[int] | None = None,  # Todo: Remove?
    ):
        super().__init__()

        self.name: str = name
        self.enabled: bool = enabled
        self.looping: bool = looping
        self.execute_on_load: bool = execute_on_load
        self.description_str_id: int = description_str_id
        self.display_as_objective: bool = display_as_objective
        self.objective_order: int = objective_order
        self.make_header: bool = make_header
        self.short_description_str_id: int = short_description_str_id
        self.display_on_screen: bool = display_on_screen
        self.short_description_state: int = short_description_state
        self.start_time: int = start_time
        self.mute_objectives: bool = mute_objectives
        self.description: str = description
        self.short_description: str = short_description
        self.effects: list[Effect] = effects if effects is not None else []
        self.effect_display_orders: list[int] = effect_display_orders if effect_display_orders is not None else []
        self.conditions: list[Condition] = conditions if conditions is not None else []
        self.condition_display_orders: list[int] = condition_display_orders if condition_display_orders is not None else []

    def add_effect(self, effect: Effect) -> Effect:
        """
        Adds an effect to this trigger.

        Args:
            effect: The effect to add

        Returns:
            The added effect
        """
        with borrow_mut(self.effects):
            self.effects.append(effect)

        self.effect_display_orders.append(len(self.effects) - 1)
        return effect

    def add_effects(self, effects: Iterable[Effect]) -> list[Effect]:
        """
        Adds effects to this trigger.

        Args:
            effects: The effects to add

        Returns:
            The added effects
        """
        return [self.add_effect(effect) for effect in effects]

    def _get_unit_references(self, key: str = '') -> tuple['Unit', ...]:
        pass

    def _remove_unit_reference(self, unit: 'Unit', key: str = '') -> None:
        pass

    def _add_unit_reference(self, unit: 'Unit', key: str = '') -> None:
        pass
