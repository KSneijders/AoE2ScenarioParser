from __future__ import annotations

from time import time

from bfp_rs import BaseStruct, ByteStream, Retriever, Version
from bfp_rs.types.le import bool32, i32, nt_str32, Str, u32

from AoE2ScenarioParser.sections.file_header.dlc_options import DLCOptions


class FileHeader(BaseStruct):
    __default_ver__ = Version(6)

    # @formatter:off
    file_version: str               = Retriever(Str[4],                           default = "1.54")
    """unused"""
    size: int                       = Retriever(u32,                              default = 0)
    """unused"""
    version: int                    = Retriever(i32,                              default = 6)
    timestamp_of_last_save: int     = Retriever(u32,        min_ver = Version(2), default_factory = lambda _: int(time()))
    scenario_instructions: str      = Retriever(nt_str32,                         default = "")
    individual_victories_used: bool = Retriever(bool32,     max_ver = Version(5), default = False)
    num_players: int                = Retriever(u32,                              default = 2)
    dlc_options: DLCOptions         = Retriever(DLCOptions, min_ver = Version(3), default_factory = lambda _ver: DLCOptions())
    creator: str                    = Retriever(nt_str32,   min_ver = Version(4), default = "AoE2SP")
    num_triggers: int               = Retriever(u32,        min_ver = Version(5), default = 0)
    # @formatter:on

    @classmethod
    def _get_version(cls, stream: ByteStream, _ver: Version = Version(0)) -> Version:
        ver = i32.from_bytes(stream.peek(12)[8:])
        return Version(ver)
