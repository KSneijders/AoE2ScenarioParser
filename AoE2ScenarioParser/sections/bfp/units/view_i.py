from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int16


class ViewI(BaseStruct):
    x: int = Retriever(int16, default=60)
    y: int = Retriever(int16, default=60)

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)
