from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import float32, int32, uint16, uint8


class Unit(BaseStruct):
    # formatter:off
    x: float                        = Retriever(float32, default=0.5)
    y: float                        = Retriever(float32, default=0.5)
    z: float                        = Retriever(float32, default=0)
    reference_id: int               = Retriever(int32, default=0)
    const: int                      = Retriever(uint16, default=4)
    status: int                     = Retriever(uint8, default=2)
    rotation: float                 = Retriever(float32, default=0)
    initial_animation_frame: int    = Retriever(uint16, default=0)
    garrisoned_in_reference_id: int = Retriever(int32, default=-1)
    # formatter:on

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)
