from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version
from bfp_rs.types.le import i16, i8, u8

from AoE2ScenarioParser.objects.support import Tile
from AoE2ScenarioParser.sections.scx_versions import MAP_LATEST


class TerrainTile(BaseStruct):
    __default_ver__ = MAP_LATEST

    _tile = None

    # @formatter:off
    type: int       = Retriever(u8,                        default = 0)
    elevation: int  = Retriever(i8,                        default = 0)
    zone: int       = Retriever(i8,                        default = 0)
    """unused?"""
    mask_type: int  = Retriever(i16, min_ver = Version(1), default = -1)
    """what does this do?"""
    layer_type: int = Retriever(i16, min_ver = Version(1), default = -1)
    # @formatter:on

    @property
    def tile(self) -> Tile:
        """
        The location of the TerrainTile on the map. CANNOT be changed directly, should be done through MapManager.

        Returns:
            The tile representing where this TerrainTile is on the map
        """
        return self._tile
