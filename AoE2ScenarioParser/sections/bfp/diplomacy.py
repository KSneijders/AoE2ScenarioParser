from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import Bytes, FixedLenArray, bool32, bool8, int8, uint32


class Diplomacy(BaseStruct):
    # @formatter:off
    player_stances: list[list[int]] = Retriever(FixedLenArray[uint32, 16], default_factory=lambda _, __: [3] * 16, repeat=16)
    individual_victories: bytes     = Retriever(Bytes[11520], default = b"\x00" * 11520)
    """unused (?)"""
    separator: int                  = Retriever(uint32, default = 4294967197)
    allied_victories: list[bool]    = Retriever(bool32, default = False, repeat=16)
    lock_teams_in_game: bool        = Retriever(bool8, default = False)
    lock_teams_in_lobby: bool       = Retriever(bool8, default = False)
    random_start_points: bool       = Retriever(bool8, default = False)
    max_num_teams: int              = Retriever(int8, default = 4)
    # @formatter:on

    def __init__(
        self, struct_ver: Version = Version((1, 47)), parent: BaseStruct = None, initialise_defaults = True,
        **retriever_inits
    ):
        super().__init__(struct_ver, parent, initialise_defaults = initialise_defaults, **retriever_inits)
