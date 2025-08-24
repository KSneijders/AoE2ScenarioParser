from __future__ import annotations

from contextlib import suppress

from bfp_rs import BaseStruct, ByteStream, Context, Retriever, Version
from bfp_rs.errors import VersionError
from zlib_ng import zlib_ng as zlib

from AoE2ScenarioParser.sections.file_data import FileData
from AoE2ScenarioParser.sections.file_header import FileHeader
from AoE2ScenarioParser.sections.map_data import MapData
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST
from AoE2ScenarioParser.sections.settings import Settings
from AoE2ScenarioParser.sections.trigger_data import TriggerData
from AoE2ScenarioParser.sections.unit_data import UnitData


def sync_script_file_path(scx: ScenarioSections):
    with suppress(VersionError):
        name = scx.settings.options.script_name
        if name:
            scx.file_data.script_file_path = f"{name}.xs"


def sync_num_triggers(scx: ScenarioSections):
    with suppress(VersionError):
        scx.file_header.num_triggers = len(scx.trigger_data.triggers)
    with suppress(VersionError):
        scx.settings.options.num_triggers = len(scx.trigger_data.triggers)


def sync_resources(scx: ScenarioSections):
    for i in range(8):
        world_data = scx.unit_data.world_player_data[i]
        player_resources = scx.settings.player_options.starting_resources[i]

        world_data.food = player_resources.food
        world_data.wood = player_resources.wood
        world_data.stone = player_resources.stone
        world_data.gold = player_resources.gold
        with suppress(VersionError):
            world_data.ore_x = player_resources.ore_x
        with suppress(VersionError):
            world_data.trade_goods = player_resources.trade_goods


class ScenarioSections(BaseStruct):
    # @formatter:off
    file_header: FileHeader   = Retriever(FileHeader,                            default_factory = FileHeader)
    settings: Settings        = Retriever(Settings,                              default_factory = Settings, remaining_compressed = True)
    map_data: MapData         = Retriever(MapData,                               default_factory = MapData)
    unit_data: UnitData       = Retriever(UnitData,                              default_factory = UnitData)
    trigger_data: TriggerData = Retriever(TriggerData, min_ver = Version(1, 14), default_factory = TriggerData)
    file_data: FileData       = Retriever(FileData,    min_ver = Version(1, 17), default_factory = FileData)
    # @formatter:on

    def __new__(cls, ver: Version = DE_LATEST, ctx: Context = Context(), init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, ctx, init_defaults, **retriever_inits)

    @classmethod
    def _decompress(cls, bytes_: bytes) -> bytes:
        return zlib.decompress(bytes_, -zlib.MAX_WBITS)

    @classmethod
    def _compress(cls, bytes_: bytes) -> bytes:
        deflate_obj = zlib.compressobj(9, zlib.DEFLATED, -zlib.MAX_WBITS)
        compressed = deflate_obj.compress(bytes_) + deflate_obj.flush()
        return compressed

    @classmethod
    def _get_version(cls, stream: ByteStream, _ver: Version = Version(0)) -> Version:
        ver_str = stream.peek(4).decode("ASCII")
        return Version(*map(int, ver_str.split(".")))

    def to_bytes(self):
        sync_script_file_path(self)
        sync_num_triggers(self)
        sync_resources(self)
        return super().to_bytes()
