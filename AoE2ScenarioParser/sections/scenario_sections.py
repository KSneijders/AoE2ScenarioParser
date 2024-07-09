from __future__ import annotations

import zlib
from contextlib import suppress
from os import path

from binary_file_parser import BaseStruct, ByteStream, Retriever, Version, VersionError

from AoE2ScenarioParser.sections import FileData
from AoE2ScenarioParser.sections.file_header import FileHeader
from AoE2ScenarioParser.sections.map_data import MapData
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST
from AoE2ScenarioParser.sections.settings import Settings
from AoE2ScenarioParser.sections.trigger_data import TriggerData
from AoE2ScenarioParser.sections.unit_data import UnitData


class ScenarioSections(BaseStruct):
    @staticmethod
    def sync_script_file_path(_, instance: ScenarioSections):
        with suppress(VersionError):
            instance.file_data.script_file_path = (
                instance.settings.options.script_name + ".xs" if instance.settings.options.script_name else ""
            )

    @staticmethod
    def sync_num_triggers(_, instance: ScenarioSections):
        with suppress(VersionError):
            instance.file_header.num_triggers = len(instance.trigger_data.triggers)
        with suppress(VersionError):
            instance.settings.options.num_triggers = len(instance.trigger_data.triggers)

    @staticmethod
    def sync_resources(_, instance: ScenarioSections):
        with suppress(VersionError):
            for i in range(8):
                world_data = instance.unit_data.world_player_data[i]
                player_resources = instance.settings.player_options.starting_resources[i]

                world_data.food = player_resources.food
                world_data.wood = player_resources.wood
                world_data.stone = player_resources.stone
                world_data.gold = player_resources.gold
                world_data.ore_x = player_resources.ore_x
                world_data.trade_goods = player_resources.trade_goods

    # @formatter:off
    file_header: FileHeader   = Retriever(FileHeader,                                  default_factory = FileHeader, on_write = [sync_num_triggers])
    settings: Settings        = Retriever(Settings,                                    default_factory = Settings,   remaining_compressed = True)
    map_data: MapData         = Retriever(MapData,                                     default_factory = MapData)
    unit_data: UnitData       = Retriever(UnitData,                                    default_factory = UnitData,   on_write = [sync_resources])
    trigger_data: TriggerData = Retriever(TriggerData,     min_ver = Version((1, 14)), default_factory = TriggerData)
    file_data: FileData       = Retriever(FileData,        min_ver = Version((1, 17)), default_factory = FileData,   on_write = [sync_script_file_path])
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
    def _get_version(
        cls,
        stream: ByteStream,
        struct_ver: Version = Version((0,)),
    ) -> Version:
        ver_str = stream.peek(4).decode("ASCII")
        return Version(map(int, ver_str.split(".")))

    @classmethod
    def from_file(cls, file_name: str, *, file_version: Version = Version((0,)), strict = True) -> ScenarioSections:
        return cls._from_file(file_name, file_version=file_version, strict=strict)

    def to_file(self, file_name: str, overwrite_original_file_name = True):
        if overwrite_original_file_name:
            self.settings.data_header.file_name = path.basename(file_name)
        super()._to_file(file_name)

    def __init__(self, struct_ver: Version = DE_LATEST, initialise_defaults = True, **retriever_inits):
        # todo: correctly initialise struct_ver `from_default` for all self versioned structs
        #  for default values that are different across different versions, use default_factory
        super().__init__(struct_ver, initialise_defaults=initialise_defaults, **retriever_inits)
