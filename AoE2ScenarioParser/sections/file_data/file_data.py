from __future__ import annotations

from bfp_rs import BaseStruct, Context, ret, Retriever, Version
from bfp_rs.combinators import if_not, set_, set_repeat
from bfp_rs.types.le import Array32, bool32, Option32, str16, str32

from AoE2ScenarioParser.sections.file_data.ai_error import AiError
from AoE2ScenarioParser.sections.file_data.ai_file import AiFile
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


def ai_files_repeat():
    return [
        if_not(ret(FileData.has_ai_files)).then(set_repeat(ret(FileData.ai_files)).to(-1))
    ]


def sync_has_ai_files():
    return [
        if_not(ret(FileData.ai_files)).is_none().then(set_(ret(FileData.has_ai_files)).to(True))
    ]


class FileData(BaseStruct):
    # @formatter:off
    script_file_path: str         = Retriever(str16, min_ver = Version(1, 40), default = "")
    script: str                   = Retriever(str32, min_ver = Version(1, 40), default = "")
    has_ai_files: bool            = Retriever(bool32,                          default = False, on_read = ai_files_repeat, on_write = sync_has_ai_files)
    ai_error: AiError | None      = Retriever(Option32[AiError],               default_factory = lambda _ver: None)
    ai_files: list[AiFile] | None = Retriever(Array32[AiFile],                 default_factory = lambda _ver: None)
    # @formatter:on

    def __new__(cls, ver: Version = DE_LATEST, ctx: Context = Context(), init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, ctx, init_defaults, **retriever_inits)