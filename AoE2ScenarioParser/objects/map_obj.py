from AoE2ScenarioParser.objects.aoe2_object import AoE2Object


class MapObject(AoE2Object):
    def __init__(self,
                 map_color_mood,
                 collide_and_correct,
                 map_width,
                 map_height,
                 terrain
                 ):

        super().__init__(locals())
