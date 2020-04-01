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

        self.instructions = instructions
        self.hints = hints
        self.victory = victory
        self.loss = loss
        self.history = history
        self.scouts = scouts
        self.ascii_instructions = ascii_instructions
        self.ascii_hints = ascii_hints
        self.ascii_victory = ascii_victory
        self.ascii_loss = ascii_loss
        self.ascii_history = ascii_history
        self.ascii_scouts = ascii_scouts

        super().__init__()

    @staticmethod
    def parse_object(parsed_data, **kwargs):
        pass

    @staticmethod
    def reconstruct_object(parsed_data, objects, **kwargs):
        pass
