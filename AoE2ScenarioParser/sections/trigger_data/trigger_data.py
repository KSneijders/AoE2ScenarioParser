from __future__ import annotations

from bfp_rs import BaseStruct, ByteStream, ret, Retriever, Version
from bfp_rs.combinators import set_repeat
from bfp_rs.types.le import (Array32, Array64, bool8, f64, i8, u32, u64)

from AoE2ScenarioParser.sections.scx_versions import TRIGGER_LATEST
from AoE2ScenarioParser.sections.trigger_data.attacker import Attacker
from AoE2ScenarioParser.sections.trigger_data.decision import Decision
from AoE2ScenarioParser.sections.trigger_data.trigger import Trigger
from AoE2ScenarioParser.sections.trigger_data.variable_data import VariableData


def trigger_display_orders_repeat():
    return [
        set_repeat(ret(TriggerData.trigger_display_orders)).from_len(ret(TriggerData.triggers))
    ]


class TriggerData(BaseStruct):
    # @formatter:off
    version: float                    = Retriever(f64,                                       default = 3.6)
    objectives_state: int             = Retriever(i8,               min_ver = Version(1, 5), default = 0)
    triggers: list[Trigger]           = Retriever(Array32[Trigger],                          default_factory = lambda _: [], on_read = trigger_display_orders_repeat)
    trigger_display_orders: list[int] = Retriever(u32,              min_ver = Version(1, 4), default = 0,                    repeat = 0)
    variable_data: VariableData       = Retriever(VariableData,     min_ver = Version(1, 9), default_factory = VariableData)
    unused1: int                      = Retriever(u32,              min_ver = Version(2, 4), default = 0)
    unused2: int                      = Retriever(u32,              min_ver = Version(2, 7), default = 0)
    unused3: int                      = Retriever(bool8,            min_ver = Version(2, 7), default = False)
    unused4: bytes                    = Retriever(u64,              min_ver = Version(3, 5), default = 0)
    decisions: Decision                = Retriever(Array64[Decision],         min_ver = Version(4, 0), default_factory = lambda _: [])
    attackers: Attacker                = Retriever(Array64[Attacker],         min_ver = Version(4, 1), default_factory = lambda _: [])
    is_legacy_execution_order: bool    = Retriever(bool8,                     min_ver = Version(4, 5), default = False)
    # @formatter:on

    @classmethod
    def _get_version(
        cls,
        stream: ByteStream,
        _ver: Version = Version(0),
    ) -> Version:
        ver_str = str(f64.from_bytes(stream.peek(8)))
        return Version(*map(int, ver_str.split(".")))

    def __new__(cls, ver: Version = TRIGGER_LATEST, init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, init_defaults, **retriever_inits)
