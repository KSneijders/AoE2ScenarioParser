from __future__ import annotations

from binary_file_parser import BaseStruct, ByteStream, Retriever, Version
from binary_file_parser.types import bool8, uint32

from AoE2ScenarioParser.sections.map_data.terrain_tile import TerrainTile


class MapData(BaseStruct):
    @staticmethod
    def set_terrain_data_repeat(_, instance: MapData):
        MapData.terrain_tiles.set_repeat(instance, instance.width * instance.height)

    @staticmethod
    def update_width_height(_, instance: MapData):
        instance.width = instance.height = int(len(instance.terrain_tiles) ** 0.5)

    # @formatter:off
    dead_food: int                   = Retriever(uint32, min_ver = Version((1, )), default = 0xDEAD_F00D) # yES
    version                          = Retriever(uint32, min_ver = Version((1, )), default = 2)
    no_waves_on_shore: bool          = Retriever(bool8,  min_ver = Version((2, )), default = False)
    width: int                       = Retriever(uint32,                           default = 144, on_set = [set_terrain_data_repeat], on_write = [update_width_height])
    height: int                      = Retriever(uint32,                           default = 144, on_set = [set_terrain_data_repeat])
    terrain_tiles: list[TerrainTile] = Retriever(TerrainTile,                      default_factory = TerrainTile, repeat = 144**2)
    # @formatter:on

    @classmethod
    def _get_version(cls, stream: ByteStream, struct_ver: Version = Version((0,))) -> Version:
        dead_food = uint32._from_bytes(stream.peek(4))
        if dead_food != 0xDEAD_F00D: # yES
            return Version((0, ))
        ver = uint32._from_bytes(stream.peek(8)[:4])
        return Version((ver, ))

    def __init__(self, struct_ver: Version = Version((2, )), initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
