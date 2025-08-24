from __future__ import annotations

from bfp_rs import BaseStruct, ByteStream, Context, ret, Retriever, Version
from bfp_rs.combinators import set_, set_repeat
from bfp_rs.types.le import f32, i32, u8

from AoE2ScenarioParser.sections.unit_data.victory_options.victory_condition import VictoryCondition
from AoE2ScenarioParser.sections.unit_data.victory_options.victory_point import VictoryPoint


def victory_conditions_repeat():
    return [
        set_repeat(ret(VictoryOptions.victory_conditions)).from_(ret(VictoryOptions._num_conditions))
    ]


def sync_num_victory_conditions():
    return [
        set_(ret(VictoryOptions._num_conditions)).from_len(ret(VictoryOptions.victory_conditions))
    ]


def victory_points_repeat():
    return [
        set_repeat(ret(VictoryOptions.victory_points)).from_(ret(VictoryOptions._num_points))
    ]


def sync_num_victory_points():
    return [
        set_(ret(VictoryOptions._num_points)).from_len(ret(VictoryOptions.victory_points))
    ]


class VictoryOptions(BaseStruct):
    # @formatter:off
    version: float       = Retriever(f32, min_ver = Version(1, 0), default = 2.1)
    _num_conditions: int = Retriever(i32,                          default = 0, on_read = victory_conditions_repeat, on_write = sync_num_victory_conditions)
    victory_state: int   = Retriever(u8,                           default = 0)
    """
    - 0: Not achieved
    - 1: Failed
    - 2: Achieved
    - 3: Disabled
    """
    victory_conditions: list[VictoryCondition] = Retriever(VictoryCondition,                          default_factory = VictoryCondition, repeat = 0)
    total_points: int                          = Retriever(i32,              min_ver = Version(1, 0), default = 0)
    _num_points: int                           = Retriever(i32,              min_ver = Version(1, 0), default = 0, on_read = victory_points_repeat, on_write = sync_num_victory_points)
    starting_points: int                       = Retriever(i32,              min_ver = Version(2, 0), default = 0)
    starting_group: int                        = Retriever(i32,              min_ver = Version(2, 0), default = 0)
    victory_points: list[VictoryPoint]         = Retriever(VictoryPoint,     min_ver = Version(1, 0), default_factory = VictoryPoint,     repeat = 0)
    # @formatter:on

    @classmethod
    def _get_version(cls, stream: ByteStream, ver: Version = Version(0)) -> Version:
        if ver >= Version(1, 9):
            ver_str = str(f32.from_bytes(stream.peek(4)))
            return Version(*map(int, ver_str.split(".")))
        return Version(0, 0)

    def __new__(cls, ver: Version = Version(2, 0), ctx: Context = Context(), init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, ctx, init_defaults, **retriever_inits)
