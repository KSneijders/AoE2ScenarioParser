from AoE2ScenarioParser.objects.aoe2_object import AoE2Object


class TerrainObject(AoE2Object):
    def __init__(self,
                 terrain_id,
                 elevation
                 ):

        super().__init__(locals())

    @staticmethod
    def _parse_object(parsed_data, **kwargs):
        pass

    @staticmethod
    def _reconstruct_object(parsed_data, objects, **kwargs):
        pass