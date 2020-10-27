from AoE2ScenarioParser.objects.aoe2_object import AoE2Object


class FileHeaderObject(AoE2Object):
    def __init__(self,
                 version,
                 timestamp,
                 instructions,
                 player_count,
                 creator_name,
                 ):

        self.version = version
        self.timestamp = timestamp
        self.instructions = instructions
        self.player_count = player_count
        self.creator_name = creator_name

        super().__init__()



# For when turning it back into bytes:
# import time
# timestamp = int(time.time()) <-- for seconds since epoch
