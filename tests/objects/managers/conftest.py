from __future__ import annotations

from contextlib import suppress

import pytest
from bfp_rs import BaseStruct, ByteStream, ret, Retriever, Version
from bfp_rs.combinators import get, set_repeat
from bfp_rs.errors import VersionError
from bfp_rs.types.le import bool8, u32
from zlib_ng import zlib_ng as zlib

from AoE2ScenarioParser.managers import MapManager, UnitManager
from AoE2ScenarioParser.sections.file_data import FileData
from AoE2ScenarioParser.sections.file_header import FileHeader
from AoE2ScenarioParser.sections.map_data import MapData
from AoE2ScenarioParser.sections.map_data.terrain_tile import TerrainTile
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST, MAP_LATEST
from AoE2ScenarioParser.sections.settings import Settings
from AoE2ScenarioParser.sections.trigger_data import TriggerData
from AoE2ScenarioParser.sections.unit_data import UnitData


def terrain_tiles_repeat():
    return [
        set_repeat(ret(MapData.terrain_tiles)).by(get(MapData.height) * get(MapData.width))
    ]


class MapData2(BaseStruct):
    __default_ver__ = MAP_LATEST

    # @formatter:off
    dead_food: int                   = Retriever(u32,    min_ver = Version(1), default = 0xDEAD_F00D) # yES
    version                          = Retriever(u32,    min_ver = Version(1), default = 2)
    no_waves_on_shore: bool          = Retriever(bool8,  min_ver = Version(2), default = False)
    width: int                       = Retriever(u32,                          default = 5)
    height: int                      = Retriever(u32,                          default = 5, on_read = terrain_tiles_repeat)
    terrain_tiles: list[TerrainTile] = Retriever(TerrainTile,                  default_factory = TerrainTile, repeat = 5**2)
    # @formatter:on

    @classmethod
    def _get_version(cls, stream: ByteStream, _ver: Version = Version(0)) -> Version:
        dead_food = u32.from_bytes(stream.peek(4))
        if dead_food != 0xDEAD_F00D:  # yES
            return Version(0)
        ver = u32.from_bytes(stream.peek(8)[4:])
        return Version(ver)


def sync_script_file_path(scx: ScenarioSections2):
    with suppress(VersionError):
        name = scx.settings.options.script_name
        if name:
            scx.file_data.script_file_path = f"{name}.xs"


def sync_num_triggers(scx: ScenarioSections2):
    with suppress(VersionError):
        scx.file_header.num_triggers = len(scx.trigger_data.triggers)
    with suppress(VersionError):
        scx.settings.options.num_triggers = len(scx.trigger_data.triggers)


def sync_resources(scx: ScenarioSections2):
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


class ScenarioSections2(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    file_header: FileHeader   = Retriever(FileHeader,                            default_factory = FileHeader)
    settings: Settings        = Retriever(Settings,                              default_factory = Settings, remaining_compressed = True)
    map_data: MapData2         = Retriever(MapData2,                               default_factory = MapData2)
    unit_data: UnitData       = Retriever(UnitData,                              default_factory = UnitData)
    trigger_data: TriggerData = Retriever(TriggerData, min_ver = Version(1, 14), default_factory = TriggerData)
    file_data: FileData       = Retriever(FileData,    min_ver = Version(1, 17), default_factory = FileData)
    # @formatter:on

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


@pytest.fixture
def um():
    sections = ScenarioSections2()

    um = UnitManager(sections)
    um._initialize_properties()

    return um


@pytest.fixture
def mm():
    sections = ScenarioSections2()

    mm = MapManager(sections)
    mm._initialize_properties()
    mm.map_size = 5

    return mm
