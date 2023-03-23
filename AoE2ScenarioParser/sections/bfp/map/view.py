from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int32


class View(BaseStruct):
    x: int = Retriever(int32, default=-1)
    y: int = Retriever(int32, default=-1)

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)
