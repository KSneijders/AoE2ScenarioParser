from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import uint8, Bytes, int16


class Terrain(BaseStruct):
    terrain_id: int = Retriever(uint8, default=0)
    elevation: int = Retriever(uint8, default=0)
    unused: bytes = Retriever(Bytes[3], default=b"\x00\xff\xff")
    layer: int = Retriever(int16, default=-1)

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)
