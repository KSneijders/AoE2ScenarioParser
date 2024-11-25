from __future__ import annotations

from typing import Any

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int16, int8, uint8

from AoE2ScenarioParser.objects.support import Tile
from AoE2ScenarioParser.sections.scx_versions import MAP_LATEST


class TerrainTile(BaseStruct):
    # @formatter:off
    type: int       = Retriever(uint8,                           default = 0)
    elevation: int  = Retriever(int8,                            default = 0)
    zone: int       = Retriever(int8,                            default = 0)
    mask_type: int  = Retriever(int16, min_ver = Version((1, )), default = -1)
    layer_type: int = Retriever(int16, min_ver = Version((1, )), default = -1)
    # @formatter:on

    _tile: Tile

    # Todo: Move to general class (struct_ver as param?)
    def merge_init_kwargs(self, locals_: dict[str, Any]):
        kwargs = locals_.get('kwargs', {})
        keys = (r.p_name for r in self._retrievers)

        return {
            'struct_ver': MAP_LATEST,
            'initialise_defaults': True,
            **{key: locals_[key] for key in keys if key in locals_},
            **kwargs,
        }

    # noinspection PyShadowingBuiltins
    def __init__(
        self,
        type: int = 0,
        elevation: int = 0,
        zone: int = 0,
        mask_type: int = -1,
        layer_type: int = -1,
        **kwargs
    ):
        values = self.merge_init_kwargs(locals())

        super().__init__(**values)

        self._tile = Tile(0, 0)  # To be overridden when added to a scenario using the MapManager

    @property
    def tile(self) -> Tile:
        """
        The location of the TerrainTile on the map. CANNOT be changed directly, should be done through MapManager.

        Returns:
            The tile representing where this TerrainTile is on the map
        """
        return self._tile
