from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import Array32, bool32, str16, str32
from AoE2ScenarioParser.sections.file_data.ai_error import AiError
from AoE2ScenarioParser.sections.file_data.ai_file import AiFile
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class FileData(BaseStruct):
    @staticmethod
    def set_ai_files_repeat(_, instance: FileData):
        if not instance.has_ai_files:
            FileData.ai_files.set_repeat(instance, 0)

    @staticmethod
    def sync_has_ai_files(_, instance: FileData):
        instance.has_ai_files = len(instance.ai_files) > 0

    @staticmethod
    def set_ai_errors_repeat(_, instance: FileData):
        if not instance.has_ai_errors:
            FileData.ai_errors.set_repeat(instance, 0)

    @staticmethod
    def sync_has_ai_errors(_, instance: FileData):
        instance.has_ai_errors = len(instance.ai_errors) > 0

    # @formatter:off
    has_script_files: bool   = Retriever(bool32,           min_ver = Version((1, 40)), max_ver = Version((1, 45)), default = False)
    script_file_path: str    = Retriever(str16,            min_ver = Version((1, 40)),                             default = "")
    script: str              = Retriever(str32,            min_ver = Version((1, 40)),                             default = "")
    has_ai_files: bool       = Retriever(bool32,                                                                   default = False, on_set = [set_ai_files_repeat], on_write = [sync_has_ai_files])
    has_ai_errors: bool      = Retriever(bool32,                                                                   default = False, on_set = [set_ai_errors_repeat], on_write = [sync_has_ai_errors])
    ai_errors: list[AiError] = Retriever(Array32[AiError],                                                         default_factory = AiError)
    ai_files: list[AiFile]   = Retriever(Array32[AiFile],                                                          default_factory = AiFile)
    # @formatter:on

    def __init__(self, struct_ver: Version = DE_LATEST, initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
