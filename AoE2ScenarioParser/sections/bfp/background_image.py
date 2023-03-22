from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct
from binary_file_parser.types import Bytes, uint32, int16, int32, str16


class BitMapInfoHeader(BaseStruct):
    @staticmethod
    def set_colours_repeat(_, instance: BitMapInfoHeader):
        BitMapInfoHeader.colours.set_repeat(instance, instance.num_colours)

    @staticmethod
    def update_num_colours(_, instance: BitMapInfoHeader):
        instance.num_colours = len(instance.colours)

    header_size: int           = Retriever(int32,  default=0)
    width: int                 = Retriever(uint32, default=0)
    height: int                = Retriever(uint32, default=0)
    planes: int                = Retriever(int16,  default=0)
    num_bits: int              = Retriever(int16,  default=0)
    compression: int           = Retriever(uint32, default=0)
    image_size: int            = Retriever(uint32, default=0)
    x_pixels_per_meter: int    = Retriever(uint32, default=0)
    y_pixels_per_meter: int    = Retriever(uint32, default=0)
    num_colours: int           = Retriever(uint32, default=0, on_set=[set_colours_repeat], on_write=[update_num_colours])
    num_important_colours: int = Retriever(uint32, default=0)
    colours: list[int]         = Retriever(uint32, default=0, repeat=0)

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)


class BackgroundImage(BaseStruct):
    @staticmethod
    def set_img_repeat(_, instance: BackgroundImage):
        BackgroundImage.data.set_repeat(instance, instance.width * instance.height)

    @staticmethod
    def set_bmp_header_repeat(_, instance: BackgroundImage):
        BackgroundImage.info_header.set_repeat(instance, 1 if instance.width != 0 != instance.height else -1)

    file_name: str                 = Retriever(str16,            default="")
    version: int                   = Retriever(uint32,           default=3)
    width: int                     = Retriever(uint32,           default=0, on_set=[set_bmp_header_repeat, set_img_repeat])
    height: int                    = Retriever(int32,            default=0, on_set=[set_bmp_header_repeat, set_img_repeat])
    orientation: int               = Retriever(int16,            default=1)
    info_header: BitMapInfoHeader  = Retriever(BitMapInfoHeader, default=BitMapInfoHeader())
    data: list[bytes]              = Retriever(Bytes[1],         default=b"\x00")

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)
