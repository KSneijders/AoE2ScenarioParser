from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import Bytes, int16, int32, str16, uint32

from AoE2ScenarioParser.sections.settings.bitmap.bitmap_info_header import BitmapInfoHeader
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class BackgroundImage(BaseStruct):
    @staticmethod
    def set_img_repeat(_, instance: BackgroundImage):
        """https://en.wikipedia.org/wiki/BMP_file_format#Pixel_storage"""
        BackgroundImage.pixels.set_repeat(instance, instance.height * ((instance.width + 3) & ~3))

    @staticmethod
    def set_bmp_header_repeat(_, instance: BackgroundImage):
        if instance.width == 0 or instance.height == 0:
            BackgroundImage.info_header.set_repeat(instance, -1)

    # @formatter:off
    background_image_filename: str = Retriever(str16,                                        default = "")
    # todo: does size needs to be set correctly? testing needed
    size: int                      = Retriever(uint32,           min_ver = Version((1, 10)), default = 0)
    width: int                     = Retriever(uint32,           min_ver = Version((1, 10)), default = 0)
    height: int                    = Retriever(int32,            min_ver = Version((1, 10)), default = 0,                        on_read = [set_bmp_header_repeat, set_img_repeat], on_write = [set_bmp_header_repeat])
    orientation: int               = Retriever(int16,            min_ver = Version((1, 10)), default = 1)
    info_header: BitmapInfoHeader  = Retriever(BitmapInfoHeader, min_ver = Version((1, 10)), default_factory = BitmapInfoHeader)
    pixels: list[bytes]            = Retriever(Bytes[1],         min_ver = Version((1, 10)), default = b"\x00",                  repeat = -1)
    # @formatter:on

    def __init__(self, struct_ver: Version = DE_LATEST, initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
