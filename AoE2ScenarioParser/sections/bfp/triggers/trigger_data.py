from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import (
    ByteStream, Bytes, int8, uint32, float64, Array32,
)

from AoE2ScenarioParser.sections.bfp.triggers.trigger import Trigger
from AoE2ScenarioParser.sections.bfp.triggers.variable import Variable


class TriggerData(BaseStruct):
    @staticmethod
    def set_triggers_repeat(_, instance: TriggerData):
        Retriever.set_repeat(TriggerData.triggers, instance, instance.num_triggers)

    @staticmethod
    def set_display_orders_repeat(_, instance: TriggerData):
        Retriever.set_repeat(TriggerData.trigger_display_orders, instance, instance.num_triggers)

    @staticmethod
    def update_num_triggers(_, instance: TriggerData):
        instance.num_triggers = len(instance.triggers)

        if len(instance.trigger_display_orders) != instance.num_triggers:
            highest_display_order = max(instance.trigger_display_orders)
            if highest_display_order != instance.num_triggers - 1:
                raise ValueError("trigger display order array out of sync")
            instance.trigger_display_orders.extend(range(highest_display_order + 1, instance.num_triggers))

    # formatter:off
    trigger_version: float            = Retriever(float64,                          default=3.5)
    trigger_instruction_start: int    = Retriever(int8,                             default=0)
    num_triggers: int                 = Retriever(uint32,                           default=0,
                                                  on_set=[set_triggers_repeat, set_display_orders_repeat],
                                                  on_write=[update_num_triggers])
    triggers: list[Trigger]           = Retriever(Trigger,                          default_factory = lambda sv, p: Trigger(sv, p), repeat=0)
    trigger_display_orders: list[int] = Retriever(uint32,                           default=0, repeat=0)
    unknown: bytes                    = Retriever(Bytes[1028],                      default=b"\x00" * 1028)
    variables: list[Variable]         = Retriever(Array32[Variable],                default_factory= lambda _, __: [])
    unused: bytes                     = Retriever(Bytes[9], Version((3, 0, 1, 46)), default=b"\x00" * 9)
    unknown2: bytes                   = Retriever(Bytes[8], Version((3, 5, 1, 47)), default=b"\x00" * 8)
    # formatter:on

    @classmethod
    def get_version(
            cls,
            stream: ByteStream,
            struct_ver: Version = Version((0,)),
            parent: BaseStruct = None,
    ) -> Version:
        ver_str = str(float64.from_bytes(stream.peek(8)))
        return Version(tuple(map(int, ver_str.split(".")))) + struct_ver

    def __init__(self, struct_ver: Version = Version((3, 5, 1, 47)), parent: BaseStruct = None, initialise_defaults=True, **retriever_inits):
        super().__init__(struct_ver, parent, initialise_defaults=initialise_defaults, **retriever_inits)
