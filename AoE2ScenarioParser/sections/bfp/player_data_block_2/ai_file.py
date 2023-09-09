from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import Bytes, str32


class AiFile(BaseStruct):
    unknown: bytes = Retriever(Bytes[8], default = b"\x00" * 8)
    per_content: list[str] = Retriever(str32, default = "")

    def __init__(
        self, struct_ver: Version = Version((1, 47)), parent: BaseStruct = None, initialise_defaults = True,
        **retriever_inits
    ):
        super().__init__(struct_ver, parent, initialise_defaults = initialise_defaults, **retriever_inits)
