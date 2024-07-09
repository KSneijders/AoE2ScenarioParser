from binary_file_parser import BaseStruct, ByteStream, Retriever, Version
from binary_file_parser.types import Array32, uint32


class DLCOptions(BaseStruct):
    # @formatter:off
    version: int             = Retriever(uint32, min_ver = Version((1000, )), default = 1000)
    game_dataset: int        = Retriever(uint32,                              default = 1)
    """
    - 0: AoC
    - 1: HD+
    """
    # todo: update this list with proper default versioning
    required_dlcs: list[int] = Retriever(Array32[uint32], min_ver = Version((1000, )), default_factory = lambda _: [2, 3, 4, 5, 6, 7])
    """
    - 2: AoK
    - 3: AoC
    - 4: FE
    - 5: AK
    - 6: RoR
    - 7: TLK
    - 8: LotW
    - 9: DotD
    - 10: DI
    - 11: RoR
    - 12: TMR
    """
    # @formatter:on

    @classmethod
    def _get_version(cls, stream: ByteStream, struct_ver: Version = Version((0,))) -> Version:
        ver = uint32._from_bytes(stream.peek(4))
        return Version((ver, ))

    def __init__(self, struct_ver: Version = Version((1000, )), initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
