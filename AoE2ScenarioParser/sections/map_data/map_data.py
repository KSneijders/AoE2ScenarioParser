from __future__ import annotations

from bfp_rs import BaseStruct, ByteStream, Context, ret, Retriever, Version
from bfp_rs.combinators import get, set_repeat
from bfp_rs.types.le import bool8, u32

from AoE2ScenarioParser.sections.map_data.terrain_tile import TerrainTile
from AoE2ScenarioParser.sections.scx_versions import MAP_LATEST


def terrain_tiles_repeat():
    return [
        set_repeat(ret(MapData.terrain_tiles)).by(get(MapData.height) * get(MapData.width))
    ]


class MapData(BaseStruct):
    # @formatter:off
    dead_food: int                   = Retriever(u32,    min_ver = Version(1), default = 0xDEAD_F00D) # yES
    version                          = Retriever(u32,    min_ver = Version(1), default = 2)
    no_waves_on_shore: bool          = Retriever(bool8,  min_ver = Version(2), default = False)
    width: int                       = Retriever(u32,                          default = 144)
    height: int                      = Retriever(u32,                          default = 144, on_read = terrain_tiles_repeat)
    terrain_tiles: list[TerrainTile] = Retriever(TerrainTile,                  default_factory = TerrainTile, repeat = 144**2)
    # @formatter:on

    @classmethod
    def _get_version(cls, stream: ByteStream, _ver: Version = Version(0)) -> Version:
        dead_food = u32.from_bytes(stream.peek(4))
        if dead_food != 0xDEAD_F00D:  # yES
            return Version(0)
        ver = u32.from_bytes(stream.peek(8)[4:])
        return Version(ver)

    def __new__(cls, ver: Version = MAP_LATEST, ctx: Context = Context(), init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, ctx, init_defaults, **retriever_inits)
