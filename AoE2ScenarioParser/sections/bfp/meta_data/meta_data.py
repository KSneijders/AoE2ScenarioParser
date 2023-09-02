from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import bool32, uint32, float32, FixedLenStr, Bytes, str16

from AoE2ScenarioParser.sections.bfp.meta_data.player_data_block_1 import PlayerDataBlock1


class MetaData(BaseStruct):
    # @formatter:off
    next_unit_id: int                    = Retriever(uint32,                             default=0)
    version: float                       = Retriever(float32,                            default=1.47)
    tribe_names: list[str]               = Retriever(FixedLenStr[256],                   default="0" * 256,          repeat=16)
    player_name_str_ids: list[int]       = Retriever(uint32,                             default=4294967294,         repeat=16)
    player_data1: list[PlayerDataBlock1] = Retriever(PlayerDataBlock1,                   default_factory = lambda sv, p: PlayerDataBlock1(sv, p), repeat=16)
    lock_civilizations: list[bool]       = Retriever(bool32,                             default=False,              repeat=16)
    unknown_1_45: bytes                  = Retriever(Bytes[1], max_ver=Version((1, 45)), default=b"\x00")
    unknown_1_46: bytes                  = Retriever(Bytes[1], min_ver=Version((1, 46)), default=b"\x01")
    unknown2: bytes                      = Retriever(Bytes[8],                           default=b"\x00" * 8)
    file_name: str                       = Retriever(str16,                              default="MadeWithAoE2SP.aoe2scenario")
    # @formatter:on

    def __init__(self, struct_ver: Version = Version((1, 47)), parent: BaseStruct = None, initialise_defaults=True, **retriever_inits):
        super().__init__(struct_ver, parent, initialise_defaults=initialise_defaults, **retriever_inits)
