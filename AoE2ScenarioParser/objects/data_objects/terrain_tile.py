from typing import Optional, Tuple

from AoE2ScenarioParser.datasets.terrains import TerrainId
from AoE2ScenarioParser.helper.helper import i_to_xy
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.scenarios import scenario_store
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink


class TerrainTile(AoE2Object):
    """Object for handling a tile in the map."""

    _link_list = [
        RetrieverObjectLink("terrain_id", "Map", "terrain_data[__index__].terrain_id"),
        RetrieverObjectLink("elevation", "Map", "terrain_data[__index__].elevation"),
        RetrieverObjectLink("layer", "Map", "terrain_data[__index__].layer"),
        RetrieverObjectLink("index", retrieve_history_number=0),
    ]

    def __init__(self, terrain_id: int = TerrainId.GRASS_1, elevation: int = 0, layer: int = -1, index: int = - 1,
                 **kwargs):
        self.terrain_id = terrain_id
        self.elevation = elevation
        self.layer = layer
        self._index = index
        self._xy: Optional[Tuple[int, int]] = None

        super().__init__(**kwargs)

    @property
    def x(self) -> int:
        return self.xy[0]

    @property
    def y(self) -> int:
        return self.xy[1]

    @property
    def i(self) -> int:
        return self._index

    @property
    def xy(self) -> Tuple[int, int]:
        if not self._xy:
            self._xy = i_to_xy(self._index, scenario_store.get_map_size(self._host_uuid))
        return self._xy


def reset_terrain_index(tile, new_index):
    tile._index = new_index
    tile._xy = None
