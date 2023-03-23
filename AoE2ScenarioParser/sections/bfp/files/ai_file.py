from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import nt_str32


class AiFile(BaseStruct):
    file_name: str = Retriever(nt_str32, default="")
    per_content: str = Retriever(nt_str32, default="")

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)
