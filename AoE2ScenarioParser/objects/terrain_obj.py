from AoE2ScenarioParser.helper.retriever import RetrieverObjectLink
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object


class TerrainObject(AoE2Object):
    """Object for handling a tile in the map."""

    # List of attributes
    terrain_id: int
    elevation: int
    layer: int

    _link_list = [
        RetrieverObjectLink("terrain_id", "MapPiece.terrain_data[__index__].terrain_id"),
        RetrieverObjectLink("elevation", "MapPiece.terrain_data[__index__].elevation"),
        RetrieverObjectLink("layer", "MapPiece.terrain_data[__index__].layer"),
    ]

    def __init__(self, pieces=None, instance_number: int = -1):
        super().__init__(pieces, instance_number)
