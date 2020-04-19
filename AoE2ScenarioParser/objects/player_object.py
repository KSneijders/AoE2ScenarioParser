from AoE2ScenarioParser.objects.aoe2_object import AoE2Object


class PlayerObject(AoE2Object):
    def __init__(self,
                 player_number,
                 active,
                 human,
                 civilization,
                 gold,
                 wood,
                 food,
                 stone,
                 color,
                 starting_age,
                 pop_limit
                 ):

        self.player_number = player_number
        self.active = active
        self.human = human
        self.civilization = civilization
        self.gold = gold
        self.wood = wood
        self.food = food
        self.stone = stone
        self.color = color
        self.starting_age = starting_age
        self.pop_limit = pop_limit

        super().__init__()

    @staticmethod
    def _parse_object(parsed_data, **kwargs):
        pass

    @staticmethod
    def _reconstruct_object(parsed_data, objects, **kwargs):
        pass
