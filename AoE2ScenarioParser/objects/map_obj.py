from AoE2ScenarioParser.helper.retriever import find_retriever
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.terrain_obj import TerrainObject


class MapObject(AoE2Object):
    def __init__(self,
                 map_color_mood,
                 collide_and_correct,
                 map_width,
                 map_height,
                 terrain
                 ):

        self.map_color_mood = map_color_mood
        self.collide_and_correct = collide_and_correct
        self.map_width = map_width
        self.map_height = map_height
        self.terrain = terrain

        super().__init__()

    def get_raw_terrain(self):
        """
        returns terrain_id and elevation values concatenated in a single list
        """
        return [value for tile in self.terrain for value in [tile.terrain_id, tile.elevation]]

    @staticmethod
    def _parse_object(parsed_data, **kwargs):
        object_piece = parsed_data['MapPiece']
        map_width = find_retriever(object_piece.retrievers, "Map Width").data
        map_height = find_retriever(object_piece.retrievers, "Map Height").data
        terrain_list = find_retriever(object_piece.retrievers, "Terrain data").data
        # AoE2 in Game map: Left to top = X. Left to bottom = Y. Tiny map top = [X:199,Y:0]
        terrain = []

        for i in range(0, map_width * map_height):
            to = TerrainObject(
                terrain_id=find_retriever(terrain_list[i].retrievers, "Terrain ID").data,
                elevation=find_retriever(terrain_list[i].retrievers, "Elevation").data
            )
            
            terrain.append(to)

        return MapObject(
            map_color_mood=find_retriever(object_piece.retrievers, "Map color mood").data,
            collide_and_correct=find_retriever(object_piece.retrievers, "Collide and Correcting").data,
            map_width=map_width,
            map_height=map_height,
            terrain=terrain,
        )

    @staticmethod
    def _reconstruct_object(parsed_header, parsed_data, objects, **kwargs):
        pass

