from __future__ import annotations

from time import time

from binary_file_parser import BaseStruct, ByteStream, Retriever, Version
from binary_file_parser.types import bool32, FixedLenStr, int32, nt_str32, uint32
from AoE2ScenarioParser.sections.file_header.dlc_options import DLCOptions


class FileHeader(BaseStruct):
    # @formatter:off
    file_version: str               = Retriever(FixedLenStr[4],                       default = "1.53")
    """unused"""
    size: int                       = Retriever(uint32,                               default = 0)
    """unused"""
    version: int                    = Retriever(int32,                                default = 6)
    timestamp_of_last_save: int     = Retriever(uint32,     min_ver = Version((2, )), default_factory = lambda _: int(time()))
    scenario_instructions: str      = Retriever(nt_str32,                             default = "")
    individual_victories_used: bool = Retriever(bool32,     max_ver = Version((5, )), default = False)
    num_players: int                = Retriever(uint32,                               default = 2)
    dlc_options: DLCOptions         = Retriever(DLCOptions, min_ver = Version((3, )), default_factory = DLCOptions)
    creator: str                    = Retriever(nt_str32,   min_ver = Version((5, )), default = "AoE2SP")
    num_triggers: int               = Retriever(uint32,     min_ver = Version((5, )), default = 0)
    # @formatter:on

    @classmethod
    def _get_version(cls, stream: ByteStream, struct_ver: Version = Version((0, ))) -> Version:
        ver = int32._from_bytes(stream.peek(12)[8:])
        return Version((ver, ))

    def __init__(self, struct_ver: Version = Version((6, )), initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
