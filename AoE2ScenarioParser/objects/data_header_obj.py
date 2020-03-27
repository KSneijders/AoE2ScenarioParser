from AoE2ScenarioParser.objects.aoe2_object import AoE2Object


class DataHeaderObject(AoE2Object):
    def __init__(self,
                 version,
                 filename,
                 ):

        super().__init__(locals())

    @staticmethod
    def _parse_object(parsed_data, **kwargs):
        pass

    @staticmethod
    def _reconstruct_object(parsed_data, objects, **kwargs):
        pass
