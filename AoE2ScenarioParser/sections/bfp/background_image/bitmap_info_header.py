from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int16, int32, uint32


class BitMapInfoHeader(BaseStruct):
    @staticmethod
    def set_colours_repeat(_, instance: BitMapInfoHeader):
        BitMapInfoHeader.colours.set_repeat(instance, instance.num_colours)

    @staticmethod
    def update_num_colours(_, instance: BitMapInfoHeader):
        instance.num_colours = len(instance.colours)

    # @formatter:off
    header_size: int           = Retriever(int32,  default = 0)
    width: int                 = Retriever(uint32, default = 0)
    height: int                = Retriever(uint32, default = 0)
    planes: int                = Retriever(int16,  default = 0)
    num_bits: int              = Retriever(int16,  default = 0)
    compression: int           = Retriever(uint32, default = 0)
    image_size: int            = Retriever(uint32, default = 0)
    x_pixels_per_meter: int    = Retriever(uint32, default = 0)
    y_pixels_per_meter: int    = Retriever(uint32, default = 0)
    num_colours: int           = Retriever(uint32, default = 0, on_set=[set_colours_repeat], on_write=[update_num_colours])
    num_important_colours: int = Retriever(uint32, default = 0)
    colours: list[int]         = Retriever(uint32, default = 0, repeat=0)
    # @formatter:on

    def __init__(
        self, struct_ver: Version = Version((1, 47)), parent: BaseStruct = None, initialise_defaults = True,
        **retriever_inits
    ):
        super().__init__(struct_ver, parent, initialise_defaults = initialise_defaults, **retriever_inits)
