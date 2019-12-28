from src.objects.aoe2_object import AoE2Object


class DiplomacyObject(AoE2Object):
    def __init__(self,
                 stance_per_player
                 ):

        super().__init__(locals())

# For when turning it back into bytes:
# import time
# timestamp = int(time.time()) <-- for seconds since epoch
