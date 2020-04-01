from AoE2ScenarioParser.objects.aoe2_object import AoE2Object


class DiplomacyObject(AoE2Object):
    def __init__(self,
                 player_stances
                 ):

        self.player_stances = player_stances

        super().__init__()

    @staticmethod
    def parse_object(parsed_data, **kwargs):
        pass

    @staticmethod
    def reconstruct_object(parsed_data, objects, **kwargs):
        pass
