from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import float32


class ViewF(BaseStruct):
    x: float = Retriever(float32, default=60.0)
    y: float = Retriever(float32, default=60.0)

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)
