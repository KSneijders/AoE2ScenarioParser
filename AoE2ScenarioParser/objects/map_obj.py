from AoE2ScenarioParser.objects.aoe2_object import AoE2Object


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

    @staticmethod
    def _parse_object(parsed_data, **kwargs):
        pass

    @staticmethod
    def _reconstruct_object(parsed_header, parsed_data, objects, **kwargs):
        pass

