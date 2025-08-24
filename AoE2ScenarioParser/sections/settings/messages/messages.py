from __future__ import annotations

from bfp_rs import BaseStruct, Context, Retriever, Version
from bfp_rs.types.le import i32, str16

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class Messages(BaseStruct):
    # @formatter:off
    instructions_str_id: int = Retriever(i32,    min_ver = Version(1, 16), default = -2)
    hints_str_id: int        = Retriever(i32,    min_ver = Version(1, 16), default = -2)
    victory_str_id: int      = Retriever(i32,    min_ver = Version(1, 16), default = -2)
    loss_str_id: int         = Retriever(i32,    min_ver = Version(1, 16), default = -2)
    history_str_id: int      = Retriever(i32,    min_ver = Version(1, 16), default = -2)
    scouts_str_id: int       = Retriever(i32,    min_ver = Version(1, 22), default = -2)
    instructions: str        = Retriever(str16,                            default = "")
    hints: str               = Retriever(str16,  min_ver = Version(1, 11), default = "")
    victory: str             = Retriever(str16,  min_ver = Version(1, 11), default = "This scenario was created using AoE2ScenarioParser! Hopefully you enjoyed!")
    loss: str                = Retriever(str16,  min_ver = Version(1, 11), default = "This scenario was created using AoE2ScenarioParser! Hopefully you enjoyed!")
    history: str             = Retriever(str16,  min_ver = Version(1, 11), default = "")
    scouts: str              = Retriever(str16,  min_ver = Version(1, 22), default = "")
    # @formatter:on

    def __new__(cls, ver: Version = DE_LATEST, ctx: Context = Context(), init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, ctx, init_defaults, **retriever_inits)