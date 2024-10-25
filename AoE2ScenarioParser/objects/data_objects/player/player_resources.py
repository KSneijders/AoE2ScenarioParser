from AoE2ScenarioParser.datasets.players import ColorId
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.sections.retrievers.retriever_object_link_group import RetrieverObjectLinkGroup


class PlayerResources(AoE2Object):

    _link_list = [
        RetrieverObjectLinkGroup("PlayerDataTwo", "resources[__index__]", group=[
            RetrieverObjectLink("food"),
            RetrieverObjectLink("wood"),
            RetrieverObjectLink("gold"),
            RetrieverObjectLink("stone"),
            RetrieverObjectLink("color", link="player_color"),
        ])
    ]

    def __init__(self, food: int, wood: int, gold: int, stone: int, color: int, **kwargs):
        super().__init__(**kwargs)

        self.food: int = food
        self.wood: int = wood
        self.gold: int = gold
        self.stone: int = stone
        self.color: ColorId = ColorId(color)
