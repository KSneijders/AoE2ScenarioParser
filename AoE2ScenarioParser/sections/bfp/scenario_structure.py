import zlib

from binary_file_parser import Retriever, BaseStruct
from binary_file_parser.types import ByteStream

from AoE2ScenarioParser.sections.bfp.data_header import DataHeader
from AoE2ScenarioParser.sections.bfp.file_header import FileHeader


class ScenarioStructure(BaseStruct):
    file_header: FileHeader = Retriever(FileHeader, default=FileHeader())
    data_header: DataHeader = Retriever(DataHeader, default=DataHeader(), remaining_compressed=True)

    @classmethod
    def decompress(cls, bytes_: bytes) -> bytes:
        return zlib.decompress(bytes_, -zlib.MAX_WBITS)

    @classmethod
    def compress(cls, bytes_: bytes) -> bytes:
        deflate_obj = zlib.compressobj(9, zlib.DEFLATED, -zlib.MAX_WBITS)
        compressed = deflate_obj.compress(bytes_) + deflate_obj.flush()
        return compressed

    @classmethod
    def get_version(
        cls,
        stream: ByteStream,
        struct_version: tuple[int, ...] = (0,),
        parent: BaseStruct = None,
    ) -> tuple[int, ...]:
        ver_str = stream.peek(4).decode("ASCII")
        return tuple(map(int, ver_str.split(".")))
