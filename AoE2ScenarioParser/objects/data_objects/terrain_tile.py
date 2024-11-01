from typing import Optional, Tuple

from AoE2ScenarioParser.datasets.terrains import TerrainId
from AoE2ScenarioParser.helper.helper import i_to_xy
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.scenarios.scenario_store import getters
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.sections.retrievers.retriever_object_link_group import RetrieverObjectLinkGroup


class TerrainTile(AoE2Object):

    _link_list = [
        RetrieverObjectLinkGroup("Map", "terrain_data[__index__]", group=[
            RetrieverObjectLink("terrain_id"),
            RetrieverObjectLink("elevation"),
            RetrieverObjectLink("layer"),
        ]),
        RetrieverObjectLink("_index", retrieve_history_number=0),
    ]

    def __init__(self, terrain_id: int = TerrainId.GRASS_1, elevation: int = 0, layer: int = -1, _index: int = - 1,
                 **kwargs):
        self.terrain_id: int = terrain_id
        self.elevation: int = elevation
        self.layer: int = layer
        self._index: int = _index
        self._xy: Optional[Tuple[int, int]] = None

        super().__init__(**kwargs)

    @property
    def x(self) -> int:
        """The X coordinate of this tile on the map"""
        return self.xy[0]

    @property
    def y(self) -> int:
        """The Y coordinate of this tile on the map"""
        return self.xy[1]

    @property
    def i(self) -> int:
        """The index of this tile on the map"""
        return self._index

    @property
    def xy(self) -> Tuple[int, int]:
        """
        The X,Y coordinate of this tile on the map

        Returns:
            A tuple containing two integers representing the XY coordinates
        """
        if not self._xy:
            self._xy = i_to_xy(self._index, getters.get_map_size(self._uuid))
        return self._xy

    def _reset_terrain_index(self, new_index: int):
        """Reset the current terrain index"""
        self._index = new_index
        self._xy = None
