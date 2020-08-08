from AoE2ScenarioParser.objects.aoe2_object import AoE2Object


class TerrainObject(AoE2Object):
    def __init__(self,
                 terrain_id,
                 elevation,
                 layer,
                 ):
        self.terrain_id = terrain_id
        self.elevation = elevation
        self.layer = layer

        super().__init__()

    @staticmethod
    def _parse_object(parsed_data, **kwargs):
        pass

    @staticmethod
    def _reconstruct_object(parsed_header, parsed_data, objects, **kwargs):
        pass
