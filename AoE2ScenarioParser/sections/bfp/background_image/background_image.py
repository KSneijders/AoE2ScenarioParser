from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import Bytes, uint32, int16, int32, str16

from AoE2ScenarioParser.sections.bfp.background_image.bitmap_info_header import BitMapInfoHeader


class BackgroundImage(BaseStruct):
    @staticmethod
    def set_img_repeat(_, instance: BackgroundImage):
        BackgroundImage.data.set_repeat(instance, instance.width * instance.height)

    @staticmethod
    def set_bmp_header_repeat(_, instance: BackgroundImage):
        BackgroundImage.info_header.set_repeat(instance, 1 if instance.width != 0 != instance.height else -1)

    # formatter:off
    file_name: str                 = Retriever(str16,            default="")
    version: int                   = Retriever(uint32,           default=3)
    width: int                     = Retriever(uint32,           default=0, on_set=[set_bmp_header_repeat, set_img_repeat])
    height: int                    = Retriever(int32,            default=0, on_set=[set_bmp_header_repeat, set_img_repeat])
    orientation: int               = Retriever(int16,            default=1)
    info_header: BitMapInfoHeader  = Retriever(BitMapInfoHeader, default=BitMapInfoHeader())
    data: list[bytes]              = Retriever(Bytes[1],         default=b"\x00")
    # formatter:on

    def __init__(self, struct_ver: Version = Version((1, 47)), parent: BaseStruct = None, initialise_defaults=True, **retriever_inits):
        super().__init__(struct_ver, parent, initialise_defaults=initialise_defaults, **retriever_inits)
