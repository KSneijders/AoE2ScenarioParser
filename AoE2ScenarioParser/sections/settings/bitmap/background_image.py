from __future__ import annotations

from bfp_rs import BaseStruct, Context, ret, Retriever, Version
from bfp_rs.combinators import get, if_, set_repeat
from bfp_rs.types.le import Bytes, i16, i32, str16, u32

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST
from AoE2ScenarioParser.sections.settings.bitmap.bitmap_info_header import BitmapInfoHeader


def info_header_repeat_w():
    return [
        if_(ret(BackgroundImage.width)).eq(0).then(
            set_repeat(ret(BackgroundImage.info_header)).to(-1)
        )
    ]


def info_header_repeat_h():
    return [
        if_(ret(BackgroundImage.height)).eq(0).then(
            set_repeat(ret(BackgroundImage.info_header)).to(-1)
        ),
    ]


def pixel_repeat():
    return [
        set_repeat(ret(BackgroundImage.pixels)).by(
            get(BackgroundImage.height) * ((get(BackgroundImage.width) + 3) & ~3)
        )
    ]


class BackgroundImage(BaseStruct):
    # @formatter:off
    filename: str                        = Retriever(str16,            min_ver = Version(1,  9), default = "")
    version: int                         = Retriever(u32,              min_ver = Version(1, 10), default = 0)
    width: int                           = Retriever(i32,              min_ver = Version(1, 10), default = 0,                        on_read = info_header_repeat_w)
    height: int                          = Retriever(i32,              min_ver = Version(1, 10), default = 0,                        on_read = info_header_repeat_h)
    # """https://en.wikipedia.org/wiki/BMP_file_format#Pixel_storage"""
    orientation: int                     = Retriever(i16,              min_ver = Version(1, 10), default = 1,                        on_read = pixel_repeat)
    info_header: BitmapInfoHeader | None = Retriever(BitmapInfoHeader, min_ver = Version(1, 10), default_factory = lambda _ver: None)
    pixels: list[bytes] | None           = Retriever(Bytes[1],         min_ver = Version(1, 10), default_factory = lambda _ver: None, repeat = -2)
    # @formatter:on

    def __new__(cls, ver: Version = DE_LATEST, ctx: Context = Context(), init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, ctx, init_defaults, **retriever_inits)