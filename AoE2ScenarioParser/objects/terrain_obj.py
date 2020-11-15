from AoE2ScenarioParser.helper.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object


class TerrainObject(AoE2Object):
    """Object for handling a tile in the map."""

    _link_list = [
        RetrieverObjectLink("terrain_id", "MapPiece", "terrain_data[__index__].terrain_id"),
        RetrieverObjectLink("elevation", "MapPiece", "terrain_data[__index__].elevation"),
        RetrieverObjectLink("layer", "MapPiece", "terrain_data[__index__].layer"),
    ]

    def __init__(self, terrain_id: int, elevation: int, layer: int):
        self.terrain_id = terrain_id
        self.elevation = elevation
        self.layer = layer

        super().__init__()
