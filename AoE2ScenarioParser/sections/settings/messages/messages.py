from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int32, str16
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class Messages(BaseStruct):
    # @formatter:off
    instructions_str_id: int = Retriever(int32,  min_ver = Version((1, 16)), default = -2)
    hints_str_id: int        = Retriever(int32,  min_ver = Version((1, 16)), default = -2)
    victory_str_id: int      = Retriever(int32,  min_ver = Version((1, 16)), default = -2)
    loss_str_id: int         = Retriever(int32,  min_ver = Version((1, 16)), default = -2)
    history_str_id: int      = Retriever(int32,  min_ver = Version((1, 16)), default = -2)
    scouts_str_id: int       = Retriever(int32,  min_ver = Version((1, 22)), default = -2)
    instructions: str        = Retriever(str16,                              default = "")
    hints: str               = Retriever(str16,  min_ver = Version((1, 11)), default = "")
    victory: str             = Retriever(str16,  min_ver = Version((1, 11)), default = "This scenario was created using AoE2ScenarioParser! Hopefully you enjoyed!")
    loss: str                = Retriever(str16,  min_ver = Version((1, 11)), default = "This scenario was created using AoE2ScenarioParser! Hopefully you enjoyed!")
    history: str             = Retriever(str16,  min_ver = Version((1, 11)), default = "")
    scouts: str              = Retriever(str16,  min_ver = Version((1, 22)), default = "")
    # @formatter:on

    def __init__(self, struct_ver: Version = DE_LATEST, initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
