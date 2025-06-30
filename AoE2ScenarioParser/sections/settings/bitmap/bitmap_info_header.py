from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version
from bfp_rs.types.le import i32, u16, u32, Array

from AoE2ScenarioParser.sections.settings.bitmap.colour import Colour
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class BitmapInfoHeader(BaseStruct):
    """https://en.wikipedia.org/wiki/BMP_file_format#DIB_header_(bitmap_information_header)"""
    # @formatter:off
    size: int                  = Retriever(u32,                default = 40)
    width: int                 = Retriever(i32,                default = 0)
    height: int                = Retriever(i32,                default = 0)
    num_planes: int            = Retriever(u16,                default = 1)
    num_bits_per_pixel: int    = Retriever(u16,                default = 1)
    compression: int           = Retriever(u32,                default = 0)
    image_size: int            = Retriever(u32,                default = 0)
    x_pixels_per_meter: int    = Retriever(i32,                default = 0)
    y_pixels_per_meter: int    = Retriever(i32,                default = 0)
    num_colours: int           = Retriever(u32,                default = 0)
    num_important_colours: int = Retriever(u32,                default = 0)
    colours: list[Colour]      = Retriever(Array[256][Colour], default_factory = lambda _ver: [Colour() for _ in range(256)])
    # @formatter:on

    def __new__(cls, ver: Version = DE_LATEST, init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, init_defaults, **retriever_inits)
