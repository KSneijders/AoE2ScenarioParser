from AoE2ScenarioParser.objects.aoe2_object import AoE2Object


class OptionsObject(AoE2Object):
    def __init__(self,
                 disables,
                 all_techs
                 ):

        self.disables = disables
        self.all_techs = all_techs

        super().__init__()

    @staticmethod
    def parse_object(parsed_data, **kwargs):
        pass

    @staticmethod
    def reconstruct_object(parsed_data, objects, **kwargs):
        pass
