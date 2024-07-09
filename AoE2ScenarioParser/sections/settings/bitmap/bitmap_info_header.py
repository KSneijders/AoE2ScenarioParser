from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int32, uint16, uint32
from AoE2ScenarioParser.sections.settings.bitmap.colour import Colour
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class BitmapInfoHeader(BaseStruct):
    """https://en.wikipedia.org/wiki/BMP_file_format#DIB_header_(bitmap_information_header)"""

    @staticmethod
    def set_colours_repeat(_, instance: BitmapInfoHeader):
        BitmapInfoHeader.colours.set_repeat(instance, instance.num_colours)

    @staticmethod
    def update_num_colours(_, instance: BitmapInfoHeader):
        instance.num_colours = len(instance.colours)

    # @formatter:off
    # todo: this should be set from the # of bytes in this header, is it unused?
    size: int                  = Retriever(uint32, default = 40)
    width: int                 = Retriever(int32,  default = 0)
    height: int                = Retriever(int32,  default = 0)
    num_planes: int            = Retriever(uint16, default = 1)
    num_bits_per_pixel: int    = Retriever(uint16, default = 1)
    compression: int           = Retriever(uint32, default = 0)
    image_size: int            = Retriever(uint32, default = 0)
    x_pixels_per_meter: int    = Retriever(int32,  default = 0)
    y_pixels_per_meter: int    = Retriever(int32,  default = 0)
    num_colours: int           = Retriever(uint32, default = 0, on_read = [set_colours_repeat], on_write = [update_num_colours])
    num_important_colours: int = Retriever(uint32, default = 0)
    colours: list[Colour]      = Retriever(Colour, default_factory = Colour, repeat = 0)
    # @formatter:on

    def __init__(self, struct_ver: Version = DE_LATEST, initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
