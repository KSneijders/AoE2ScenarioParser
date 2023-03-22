from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import bool32, uint32, float32, FixedLenStr, Bytes, str16


class PlayerDataBlock1(BaseStruct):
    # @formatter:off
    active: bool               = Retriever(bool32,                   default=False)
    human: bool                = Retriever(bool32,                   default=False)
    civilization_1_36: int     = Retriever(uint32, (1, 36), (1, 40), default=36)
    civilization_1_41: int     = Retriever(uint32, (1, 41), (1, 42), default=38)
    civilization_1_43: int     = Retriever(uint32, (1, 43), (1, 45), default=40)
    civilization_1_46: int     = Retriever(uint32, (1, 46),          default=43)
    architecture_set_1_40: int = Retriever(uint32, (1, 40), (1, 40), default=36)
    architecture_set_1_41: int = Retriever(uint32, (1, 41), (1, 42), default=38)
    architecture_set_1_43: int = Retriever(uint32, (1, 43), (1, 45), default=40)
    architecture_set_1_46: int = Retriever(uint32, (1, 46),          default=43)
    cty_mode: int              = Retriever(uint32,                   default=4)
    # @formatter:on

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)


class MetaData(BaseStruct):
    # @formatter:off
    next_unit_id: int                    = Retriever(uint32,                    default=0)
    version: float                       = Retriever(float32,                   default=1.47)
    tribe_names: list[str]               = Retriever(FixedLenStr[256],          default="0" * 256,          repeat=16)
    player_name_str_ids: list[int]       = Retriever(uint32,                    default=4294967294,         repeat=16)
    player_data1: list[PlayerDataBlock1] = Retriever(PlayerDataBlock1,          default=PlayerDataBlock1(), repeat=16)
    lock_civilizations: list[bool]       = Retriever(bool32,                    default=False,              repeat=16)
    unknown_1_45: bytes                  = Retriever(Bytes[1], max_ver=(1, 45), default=b"\x00")
    unknown_1_46: bytes                  = Retriever(Bytes[1], min_ver=(1, 46), default=b"\x01")
    unknown2: bytes                      = Retriever(Bytes[8],                  default=b"\x00" * 8)
    file_name: str                       = Retriever(str16,                     default="MadeWithAoE2SP.aoe2scenario")
    # @formatter:on

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)
