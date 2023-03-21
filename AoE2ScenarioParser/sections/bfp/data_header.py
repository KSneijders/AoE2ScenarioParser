from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import bool32, uint32, float32, FixedLenStr, Bytes, str16


class PlayerData1(BaseStruct):
    # @formatter:off
    active: bool               = Retriever(bool32, default=False)
    human: bool                = Retriever(bool32, default=False)
    civilization_1_36: int     = Retriever(uint32, default=36, min_ver=(1, 36), max_ver=(1, 40))
    civilization_1_41: int     = Retriever(uint32, default=38, min_ver=(1, 41), max_ver=(1, 42))
    civilization_1_43: int     = Retriever(uint32, default=40, min_ver=(1, 43), max_ver=(1, 45))
    civilization_1_46: int     = Retriever(uint32, default=43, min_ver=(1, 46))
    architecture_set_1_40: int = Retriever(uint32, default=36, min_ver=(1, 40), max_ver=(1, 40))
    architecture_set_1_41: int = Retriever(uint32, default=38, min_ver=(1, 41), max_ver=(1, 42))
    architecture_set_1_43: int = Retriever(uint32, default=40, min_ver=(1, 43), max_ver=(1, 45))
    architecture_set_1_46: int = Retriever(uint32, default=43, min_ver=(1, 46))
    cty_mode: int              = Retriever(uint32, default=4)
    # @formatter:on

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)


# Todo: Rename this class (Metadata?) -- Move parts of this to struct for clarity? ->
#  Both: 'tribe_names' and 'player_name_str_ids' should be inside PlayerData1
class DataHeader(BaseStruct):
    # @formatter:off
    next_unit_id: int               = Retriever(uint32,           default=0)
    version: float                  = Retriever(float32,          default=1.47)
    tribe_names: list[str]          = Retriever(FixedLenStr[256], default="0" * 256,     repeat=16)
    player_name_str_ids: list[int]  = Retriever(uint32,           default=4294967294,    repeat=16)
    player_data1: list[PlayerData1] = Retriever(PlayerData1,      default=PlayerData1(), repeat=16)
    lock_civilizations: list[bool]  = Retriever(bool32,           default=False,         repeat=16)
    unknown: bytes                  = Retriever(Bytes[9],         default=b"\x00" + b"\x00" * 8, max_ver=(1, 45))
    unknown_1_46: bytes             = Retriever(Bytes[9],         default=b"\x01" + b"\x00" * 8, min_ver=(1, 46))
    file_name: str                  = Retriever(str16,            default="MadeWithAoE2SP.aoe2scenario")
    # @formatter:on

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)
