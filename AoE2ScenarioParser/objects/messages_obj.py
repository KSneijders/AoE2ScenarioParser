from AoE2ScenarioParser.objects.aoe2_object import AoE2Object


class MessagesObject(AoE2Object):
    def __init__(self,
                 instructions,
                 hints,
                 victory,
                 loss,
                 history,
                 scouts,
                 ascii_instructions,
                 ascii_hints,
                 ascii_victory,
                 ascii_loss,
                 ascii_history,
                 ascii_scouts,
                 ):

        super().__init__(locals())
