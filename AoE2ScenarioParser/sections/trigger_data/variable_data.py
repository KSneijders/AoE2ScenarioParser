from __future__ import annotations

from bfp_rs import BaseStruct, Context, Retriever, Version
from bfp_rs.types.le import Array, Array32, i32

from AoE2ScenarioParser.sections.scx_versions import TRIGGER_LATEST
from AoE2ScenarioParser.sections.trigger_data.variable import Variable


class VariableData(BaseStruct):
    # @formatter:off
    variable_initial_values: list[int] = Retriever(Array[256][i32],                            default_factory = lambda _ver: [0]*256)
    enabled_techs: list[int]           = Retriever(Array32[i32],      min_ver = Version(2, 1), default_factory = lambda _ver: [])
    """probably unused?"""
    variables: list[Variable]          = Retriever(Array32[Variable], min_ver = Version(2, 2), default_factory = lambda _ver: [])
    # @formatter:on

    def __new__(cls, ver: Version = TRIGGER_LATEST, ctx: Context = Context(), init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, ctx, init_defaults, **retriever_inits)
