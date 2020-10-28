from AoE2ScenarioParser.objects.aoe2_object import AoE2Object


class OptionsObject(AoE2Object):
    def __init__(self,
                 disables,
                 all_techs
                 ):

        self.disables = disables
        self.all_techs = all_techs

        super().__init__()
