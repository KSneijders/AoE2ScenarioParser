from AoE2ScenarioParser.datasets.terrains import TerrainId

from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink


class TerrainTile(AoE2Object):
    """Object for handling a tile in the map."""

    _link_list = [
        RetrieverObjectLink("terrain_id", "Map", "terrain_data[__index__].terrain_id"),
        RetrieverObjectLink("elevation", "Map", "terrain_data[__index__].elevation"),
        RetrieverObjectLink("layer", "Map", "terrain_data[__index__].layer"),
    ]

    def __init__(self, terrain_id: int = TerrainId.GRASS_1, elevation: int = 0, layer: int = -1):
        self.terrain_id = terrain_id
        self.elevation = elevation
        self.layer = layer

        super().__init__()
