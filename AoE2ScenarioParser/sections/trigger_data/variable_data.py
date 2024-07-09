from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import Array32, Bytes, FixedLenArray, int32
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST, TRIGGER_LATEST
from AoE2ScenarioParser.sections.trigger_data.variable import Variable


class VariableData(BaseStruct):
    # @formatter:off
    variable_initial_values: list[int] = Retriever(FixedLenArray[int32, 256], min_ver = Version((2, 2)), default_factory = lambda _: [0]*256)
    enabled_techs: list[int]           = Retriever(Array32[int32],            min_ver = Version((2, 2)), default_factory = lambda _: [])
    """probably unused?"""
    variables: list[Variable]          = Retriever(Array32[Variable],                                     default_factory = Variable)
    unused: bytes                      = Retriever(Bytes[9],                  min_ver = Version((3, 0)),  default = b"\x00"*9)
    """known to be unused"""
    unknown: bytes                     = Retriever(Bytes[8],                  min_ver = Version((3, 5)),  default = b"\x00"*8)
    # @formatter:on

    def __init__(self, struct_ver: Version = TRIGGER_LATEST, initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
