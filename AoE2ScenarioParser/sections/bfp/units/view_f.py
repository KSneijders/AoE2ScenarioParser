from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import float32


class ViewF(BaseStruct):
    x: float = Retriever(float32, default = 60.0)
    y: float = Retriever(float32, default = 60.0)

    def __init__(
        self, struct_ver: Version = Version((1, 47)), parent: BaseStruct = None, initialise_defaults = True,
        **retriever_inits
    ):
        super().__init__(struct_ver, parent, initialise_defaults = initialise_defaults, **retriever_inits)
