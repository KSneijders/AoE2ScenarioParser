import zlib

from binary_file_parser import Retriever, BaseStruct
from binary_file_parser.types import ByteStream

from AoE2ScenarioParser.sections.bfp.background_image.background_image import BackgroundImage
from AoE2ScenarioParser.sections.bfp.cynematics import Cinematics
from AoE2ScenarioParser.sections.bfp.diplomacy import Diplomacy
from AoE2ScenarioParser.sections.bfp.files.file_data import FileData
from AoE2ScenarioParser.sections.bfp.global_victory import GlobalVictory
from AoE2ScenarioParser.sections.bfp.map.map_data import MapData
from AoE2ScenarioParser.sections.bfp.meta_data.meta_data import MetaData
from AoE2ScenarioParser.sections.bfp.file_header import FileHeader
from AoE2ScenarioParser.sections.bfp.messages import Messages
from AoE2ScenarioParser.sections.bfp.options import Options
from AoE2ScenarioParser.sections.bfp.player_data_block_2.player_data_block_2 import PlayerDataBlock2
from AoE2ScenarioParser.sections.bfp.triggers.trigger_data import TriggerData
from AoE2ScenarioParser.sections.bfp.units.unit_data import UnitData


class ScenarioStructure(BaseStruct):
    file_header: FileHeader = Retriever(FileHeader, default=FileHeader())
    data_header: MetaData = Retriever(MetaData, default=MetaData(), remaining_compressed=True)
    text_data: Messages = Retriever(Messages, default=Messages())
    cinematics: Cinematics = Retriever(Cinematics, default=Cinematics())
    background_image: BackgroundImage = Retriever(BackgroundImage, default=BackgroundImage())
    player_data2: PlayerDataBlock2 = Retriever(PlayerDataBlock2, default=PlayerDataBlock2())
    global_victory: GlobalVictory = Retriever(GlobalVictory, default=GlobalVictory())
    diplomacy: Diplomacy = Retriever(Diplomacy, default=Diplomacy())
    options: Options = Retriever(Options, default=Options())
    map_data: MapData = Retriever(MapData, default=MapData())
    unit_data: UnitData = Retriever(UnitData, default=UnitData())
    trigger_data: TriggerData = Retriever(TriggerData, default=TriggerData())
    file_data: FileData = Retriever(FileData, default=FileData(), min_ver=(1, 40))

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
