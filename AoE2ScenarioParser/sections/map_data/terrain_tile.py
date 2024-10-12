from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int16, int8, uint8

from AoE2ScenarioParser.objects.support import Tile


class TerrainTile(BaseStruct):
    # @formatter:off
    type: int       = Retriever(uint8,                           default = 0)
    elevation: int  = Retriever(int8,                            default = 0)
    zone: int       = Retriever(int8,                            default = 0)
    mask_type: int  = Retriever(int16, min_ver = Version((1, )), default = -1)
    layer_type: int = Retriever(int16, min_ver = Version((1, )), default = -1)
    # @formatter:on

    _tile: Tile

    def __init__(self, struct_ver: Version = Version((2,)), initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)

        self._tile = Tile(0, 0)

    @property
    def tile(self) -> Tile:
        """
        The location of the TerrainTile on the map. CANNOT be changed directly, should be done through MapManager.

        Returns:
            The tile representing where this TerrainTile is on the map
        """
        return self._tile
