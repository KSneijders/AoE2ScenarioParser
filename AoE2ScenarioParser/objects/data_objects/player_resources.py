from AoE2ScenarioParser.datasets.players import ColorId
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink


class PlayerResources(AoE2Object):
    """Object for handling a tile in the map."""

    _link_list = [
        RetrieverObjectLink("food", "PlayerDataTwo", "resources[__index__].food"),
        RetrieverObjectLink("wood", "PlayerDataTwo", "resources[__index__].wood"),
        RetrieverObjectLink("gold", "PlayerDataTwo", "resources[__index__].gold"),
        RetrieverObjectLink("stone", "PlayerDataTwo", "resources[__index__].stone"),
        RetrieverObjectLink("color", "PlayerDataTwo", "resources[__index__].player_color"),
    ]

    def __init__(self, food: int, wood: int, gold: int, stone: int, color: int, **kwargs):
        super().__init__(**kwargs)

        self.food: int = food
        self.wood: int = wood
        self.gold: int = gold
        self.stone: int = stone
        self.color: ColorId = ColorId(color)
