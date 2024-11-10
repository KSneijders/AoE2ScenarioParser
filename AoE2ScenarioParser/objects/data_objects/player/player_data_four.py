from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.sections.retrievers.retriever_object_link_group import RetrieverObjectLinkGroup


class PlayerDataFour(AoE2Object):

    _link_list = [
        RetrieverObjectLinkGroup("Units", "player_data_4[__index__]", group=[
            RetrieverObjectLink("population_limit"),
            RetrieverObjectLink("food_duplicate"),
            RetrieverObjectLink("wood_duplicate"),
            RetrieverObjectLink("gold_duplicate"),
            RetrieverObjectLink("stone_duplicate"),
        ])
    ]

    def __init__(
            self,
            population_limit: float,
            food_duplicate: float,
            wood_duplicate: float,
            gold_duplicate: float,
            stone_duplicate: float,
            **kwargs):
        super().__init__(**kwargs)

        self.population_limit: float = population_limit
        self.food_duplicate: float = food_duplicate
        self.wood_duplicate: float = wood_duplicate
        self.gold_duplicate: float = gold_duplicate
        self.stone_duplicate: float = stone_duplicate
