from src.objects.aoe2_object import AoE2Object


class DiplomacyObject(AoE2Object):
    def __init__(self,
                 player_number,
                 stance_per_player
                 ):

        super().__init__(locals())

