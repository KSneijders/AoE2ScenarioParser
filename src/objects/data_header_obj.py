from src.objects.aoe2_object import AoE2Object


class DataHeaderObject(AoE2Object):
    def __init__(self,
                 version,
                 filename,
                 ):

        super().__init__(locals())

    @staticmethod
    def parse_object(parsed_data, **kwargs):
        pass

    @staticmethod
    def reconstruct_object(parsed_data, objects, **kwargs):
        pass
