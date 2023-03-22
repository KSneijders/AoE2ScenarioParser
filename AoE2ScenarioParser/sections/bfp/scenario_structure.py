import zlib

from binary_file_parser import Retriever, BaseStruct
from binary_file_parser.types import ByteStream

from AoE2ScenarioParser.sections.bfp.background_image import BackgroundImage
from AoE2ScenarioParser.sections.bfp.cynematics import Cinematics
from AoE2ScenarioParser.sections.bfp.meta_data import MetaData
from AoE2ScenarioParser.sections.bfp.file_header import FileHeader
from AoE2ScenarioParser.sections.bfp.messages import Messages
from AoE2ScenarioParser.sections.bfp.player_data_block_2 import PlayerDataBlock2


class ScenarioStructure(BaseStruct):
    file_header: FileHeader = Retriever(FileHeader, default=FileHeader())
    data_header: MetaData = Retriever(MetaData, default=MetaData(), remaining_compressed=True)
    text_data: Messages = Retriever(Messages, default=Messages())
    cinematics: Cinematics = Retriever(Cinematics, default=Cinematics())
    background_image: BackgroundImage = Retriever(BackgroundImage, default=BackgroundImage())
    player_data2: PlayerDataBlock2 = Retriever(PlayerDataBlock2, default=PlayerDataBlock2())

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
