from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import Bytes, str32


class AiFile(BaseStruct):
    unknown: bytes = Retriever(Bytes[8], default=b"\x00" * 8)
    per_content: list[str] = Retriever(str32, default="")

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)
