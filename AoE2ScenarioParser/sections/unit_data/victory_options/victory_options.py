from __future__ import annotations

from binary_file_parser import BaseStruct, ByteStream, Retriever, Version
from binary_file_parser.types import float32, int32, uint8
from AoE2ScenarioParser.sections.unit_data.victory_options.victory_condition import VictoryCondition
from AoE2ScenarioParser.sections.unit_data.victory_options.victory_point import VictoryPoint


class VictoryOptions(BaseStruct):
    @staticmethod
    def set_conditions_repeat(_, instance: VictoryOptions):
        VictoryOptions.victory_conditions.set_repeat(instance, instance._num_conditions)

    @staticmethod
    def sync_num_conditions(_, instance: VictoryOptions):
        instance._num_conditions = len(instance.victory_conditions)

    @staticmethod
    def set_points_repeat(_, instance: VictoryOptions):
        VictoryOptions.victory_points.set_repeat(instance, instance._num_points)

    @staticmethod
    def sync_num_points(_, instance: VictoryOptions):
        instance._num_points = len(instance.victory_points)

    # @formatter:off
    version: float       = Retriever(float32, min_ver = Version((1, 0)), default = 2.1)
    _num_conditions: int = Retriever(int32,                              default = 0, on_set = [set_conditions_repeat], on_write = [sync_num_conditions])
    victory_state: int   = Retriever(uint8,                              default = 0)
    """
    - 0: Not achieved
    - 1: Failed
    - 2: Achieved
    - 3: Disabled
    """
    victory_conditions: list[VictoryCondition] = Retriever(VictoryCondition,                            default_factory = VictoryCondition, repeat = 0)
    total_points: int                          = Retriever(int32,            min_ver = Version((1, 0)), default = 0)
    _num_points: int                           = Retriever(int32,            min_ver = Version((1, 0)), default = 0, on_set = [set_points_repeat], on_write = [sync_num_points])
    starting_points: int                       = Retriever(int32,            min_ver = Version((2, 0)), default = 0)
    starting_group: int                        = Retriever(int32,            min_ver = Version((2, 0)), default = 0)
    victory_points: list[VictoryPoint]         = Retriever(VictoryPoint,     min_ver = Version((1, 0)), default_factory = VictoryPoint,     repeat = 0)
    # @formatter:on

    @classmethod
    def _get_version(cls, stream: ByteStream, struct_ver: Version = Version((0,))) -> Version:
        if struct_ver >= Version((1, 9)):
            ver_str = str(float32._from_bytes(stream.peek(4)))
            return Version(map(int, ver_str.split(".")))
        return Version((0, 0))

    def __init__(self, struct_ver: Version = Version((2, )), initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
