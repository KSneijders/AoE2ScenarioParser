from bfp_rs import BaseStruct, ByteStream, Retriever, Version
from bfp_rs.types.le import f32

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST
from AoE2ScenarioParser.sections.settings.bitmap import BackgroundImage
from AoE2ScenarioParser.sections.settings.cinematics import Cinematics
from AoE2ScenarioParser.sections.settings.data_header import DataHeader
from AoE2ScenarioParser.sections.settings.diplomacy import Diplomacy
from AoE2ScenarioParser.sections.settings.global_victory import GlobalVictory
from AoE2ScenarioParser.sections.settings.messages import Messages
from AoE2ScenarioParser.sections.settings.options import Options
from AoE2ScenarioParser.sections.settings.player_options import PlayerOptions


class Settings(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    data_header: DataHeader           = Retriever(DataHeader,                               default_factory = DataHeader)
    messages: Messages                = Retriever(Messages,                                 default_factory = Messages)
    cinematics: Cinematics            = Retriever(Cinematics,                               default_factory = Cinematics)
    background_image: BackgroundImage = Retriever(BackgroundImage, min_ver = Version(1, 9), default_factory = BackgroundImage)
    player_options: PlayerOptions     = Retriever(PlayerOptions,                            default_factory = PlayerOptions)
    global_victory: GlobalVictory     = Retriever(GlobalVictory,                            default_factory = GlobalVictory)
    diplomacy: Diplomacy              = Retriever(Diplomacy,                                default_factory = Diplomacy)
    options: Options                  = Retriever(Options,                                  default_factory = Options)
    # @formatter:on

    @classmethod
    def _get_version(cls, stream: ByteStream, _ver: Version = Version(0)) -> Version:
        # this should be identical to the file version, but just in case it's possible for it to be different... yES
        ver_str = f"{f32.from_bytes(stream.peek(8)[4:]):.2f}"
        return Version(*map(int, ver_str.split(".")))
