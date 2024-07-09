from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import (
    Array32, ByteStream, float64, int8, uint32,
)
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST, TRIGGER_LATEST
from AoE2ScenarioParser.sections.trigger_data.trigger import Trigger
from AoE2ScenarioParser.sections.trigger_data.variable_data import VariableData


class TriggerData(BaseStruct):
    @staticmethod
    def set_disp_ords_repeat(_, instance: TriggerData):
        TriggerData.trigger_display_orders.set_repeat(instance, len(instance.triggers))

    @staticmethod
    def sync_disp_ords(_, instance: TriggerData):
        num_triggers = len(instance.triggers)
        if (
            len(instance.trigger_display_orders) != num_triggers
            or len(set(instance.trigger_display_orders)) != num_triggers
            or any(map(lambda id_: id_ >= num_triggers, instance.trigger_display_orders))
        ):
            instance.trigger_display_orders = list(range(num_triggers))

    # @formatter:off
    version: float                     = Retriever(float64,                                              default = 3.6)
    objectives_state: int              = Retriever(int8,                      min_ver = Version((1, 5)), default = 0)
    triggers: list[Trigger]            = Retriever(Array32[Trigger],                                     default_factory = lambda _: [],             on_read = [set_disp_ords_repeat])
    trigger_display_orders: list[int]  = Retriever(uint32,                    min_ver = Version((1, 4)), default = 0,                    repeat = 0, on_write = [sync_disp_ords])
    variable_data: VariableData        = Retriever(VariableData,              min_ver = Version((2, 2)), default_factory = VariableData)
    # @formatter:on

    @classmethod
    def _get_version(
        cls,
        stream: ByteStream,
        struct_ver: Version = Version((0,)),
    ) -> Version:
        ver_str = str(float64._from_bytes(stream.peek(8)))
        return Version(map(int, ver_str.split(".")))

    def __init__(self, struct_ver: Version = TRIGGER_LATEST, initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
