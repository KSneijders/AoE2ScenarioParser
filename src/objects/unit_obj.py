from src.objects.aoe2_object import AoE2Object


class UnitObject(AoE2Object):
    def __init__(self,
                 x,
                 y,
                 z,
                 id_on_map,
                 unit_id,
                 status,
                 rotation,
                 animation_frame,
                 garrisoned_in_id
                 ):

        super().__init__(locals())
