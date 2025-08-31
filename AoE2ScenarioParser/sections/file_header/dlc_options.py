from bfp_rs import BaseStruct, ByteStream, Retriever, Version
from bfp_rs.types.le import Array32, u32


class DLCOptions(BaseStruct):
    __default_ver__ = Version(1000)

    # @formatter:off
    version: int             = Retriever(u32, min_ver = Version(1000), default = 1000)
    game_dataset: int        = Retriever(u32,                          default = 1)
    """
    - 0: AoC
    - 1: HD+
    """
    # todo: update this list with proper default versioning
    required_dlcs: list[int] = Retriever(Array32[u32], min_ver = Version(1000), default_factory = lambda _ver: [2, 3, 4, 5, 6, 7])
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
    - 11: RoR dataset
    - 12: Romans
    - 13: TMR
    - 14: VnV
    - 15: Chronicles
    """
    # @formatter:on

    @classmethod
    def _get_version(cls, stream: ByteStream, _ver: Version = Version(0)) -> Version:
        ver = u32.from_bytes(stream.peek(4))
        return Version(ver)
