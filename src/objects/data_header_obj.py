from src.objects.aoe2_object import AoE2Object


class DataHeaderObject(AoE2Object):
    def __init__(self,
                 version,
                 filename,
                 ):

        super().__init__(locals())