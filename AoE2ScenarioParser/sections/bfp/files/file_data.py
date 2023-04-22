from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import bool32, Bytes, str32, str16, Array32

from AoE2ScenarioParser.sections.bfp.files.ai_file import AiFile


class FileData(BaseStruct):
    @staticmethod
    def set_ai_files_repeat(_, instance: FileData):
        if not instance.ai_files_present:
            Retriever.set_repeat(FileData.ai_files, instance, 0)

    @staticmethod
    def update_ai_files_present(_, instance: FileData):
        instance.ai_files_present = len(instance.ai_files) > 0

    # formatter:off
    unknown2: bytes          = Retriever(Bytes[4], max_ver=Version((1, 45)), default=b"\x00" * 4)
    script_file_path: str    = Retriever(str16,                              default="")
    script_file_content: str = Retriever(str32,                              default="")
    ai_files_present: bool   = Retriever(bool32,                             default=False, on_set=[set_ai_files_repeat], on_write=[update_ai_files_present])
    unknown4: bytes          = Retriever(Bytes[4],                           default=b"\x00" * 4)
    ai_files: list[AiFile]   = Retriever(Array32[AiFile],                    default=[], repeat=0)
    # formatter:on

    def __init__(self, struct_ver: Version = Version((1, 47)), parent: BaseStruct = None, initialise_defaults=True, **retriever_inits):
        super().__init__(struct_ver, parent, initialise_defaults=initialise_defaults, **retriever_inits)
