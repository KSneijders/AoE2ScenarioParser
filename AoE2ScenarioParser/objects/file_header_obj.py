from AoE2ScenarioParser.objects.aoe2_object import AoE2Object


class FileHeaderObject(AoE2Object):
    def __init__(self,
                 version,
                 timestamp,
                 instructions,
                 player_count,
                 # Unknown data 36 bytes
                 creator_name,
                 # Unknown data 4 bytes
                 ):

        super().__init__(locals())

# For when turning it back into bytes:
# import time
# timestamp = int(time.time()) <-- for seconds since epoch
