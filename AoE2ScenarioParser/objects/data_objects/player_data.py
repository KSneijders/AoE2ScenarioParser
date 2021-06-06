from __future__ import annotations

from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.sections.retrievers.support import Support


class PlayerFeature(AoE2Object):

    _link_list = [
        RetrieverObjectLink("active", "DataHeader", "player_data_1[__index__].active"),
        RetrieverObjectLink("human", "DataHeader", "player_data_1[__index__].human"),
        RetrieverObjectLink("civilization", "DataHeader", "player_data_1[__index__].civilization"),
        RetrieverObjectLink("architecture_set", "DataHeader", "player_data_1[__index__].architecture_set", Support(since=1.40)),
        RetrieverObjectLink("cty_mode", "DataHeader", "player_data_1[__index__].cty_mode")
    ]

    def __init__(self,
                 active: int,
                 human: int,
                 civilization: int,
                 architecture_set: int,
                 cty_mode: int
                 ):

        self.active = active
        self.human = human
        self.civilization = civilization
        self.architecture_set = architecture_set
        self.cty_mode = cty_mode

        super().__init__()


class PlayerResourcesColor(AoE2Object):

    _link_list = [
        RetrieverObjectLink("gold", "PlayerDataTwo", "resources[__index__].gold"),
        RetrieverObjectLink("wood", "PlayerDataTwo", "resources[__index__].wood"),
        RetrieverObjectLink("food", "PlayerDataTwo", "resources[__index__].food"),
        RetrieverObjectLink("stone", "PlayerDataTwo", "resources[__index__].stone"),
        RetrieverObjectLink("ore_x_unused", "PlayerDataTwo", "resources[__index__].ore_x_unused"),
        RetrieverObjectLink("trade_goods", "PlayerDataTwo", "resources[__index__].trade_goods"),
        RetrieverObjectLink("player_color", "PlayerDataTwo", "resources[__index__].player_color")
    ]

    def __init__(self,
                 gold: int,
                 wood: int,
                 food: int,
                 stone: int,
                 ore_x_unused: int,
                 trade_goods: int,
                 player_color: int
                 ):

        self.gold = gold
        self.wood = wood
        self.food = food
        self.stone = stone
        self.ore_x_unused = ore_x_unused
        self.trade_goods = trade_goods
        self.player_color = player_color

        super().__init__()


class PlayerAiFileText(AoE2Object):

    _link_list = [
        RetrieverObjectLink("ai_per_file_text", "PlayerDataTwo", "ai_files[__index__].ai_per_file_text"),
    ]

    def __init__(self, ai_per_file_text: str):
        self.ai_per_file_text = ai_per_file_text
        super().__init__()


class PlayerMiscSettings(AoE2Object):

    _link_list = [
        RetrieverObjectLink("constant_name", "Units", "player_data_3[__index__].constant_name"),
        RetrieverObjectLink("initial_camera_x", "Units", "player_data_3[__index__].initial_camera_x"),
        RetrieverObjectLink("initial_camera_y", "Units", "player_data_3[__index__].initial_camera_y"),
        RetrieverObjectLink("unknown_similar_to_camera_x", "Units", "player_data_3[__index__].unknown_similar_to_camera_x"),
        RetrieverObjectLink("unknown_similar_to_camera_y", "Units", "player_data_3[__index__].unknown_similar_to_camera_y"),
        RetrieverObjectLink("aok_allied_victory", "Units", "player_data_3[__index__].aok_allied_victory"),
        RetrieverObjectLink("player_count_for_diplomacy", "Units", "player_data_3[__index__].player_count_for_diplomacy"),
        RetrieverObjectLink("diplomacy_for_interaction", "Units", "player_data_3[__index__].diplomacy_for_interaction"),
        RetrieverObjectLink("diplomacy_for_ai_system", "Units", "player_data_3[__index__].diplomacy_for_ai_system"),
        RetrieverObjectLink("color_duplicate", "Units", "player_data_3[__index__].color"),
        RetrieverObjectLink("victory_version", "Units", "player_data_3[__index__].victory_version"),
    ]

    def __init__(self,
                 constant_name: str,
                 initial_camera_x: float,
                 initial_camera_y: float,
                 unknown_similar_to_camera_x: int,
                 unknown_similar_to_camera_y: int,
                 aok_allied_victory: int,
                 player_count_for_diplomacy: int,
                 diplomacy_for_interaction: int,
                 diplomacy_for_ai_system: int,
                 color_duplicate: int,
                 victory_version: float,
                 ):

        self.constant_name = constant_name
        self.initial_camera_x = initial_camera_x
        self.initial_camera_y = initial_camera_y
        self.unknown_similar_to_camera_x = unknown_similar_to_camera_x
        self.unknown_similar_to_camera_y = unknown_similar_to_camera_y
        self.aok_allied_victory = aok_allied_victory
        self.player_count_for_diplomacy = player_count_for_diplomacy
        self.diplomacy_for_interaction = diplomacy_for_interaction
        self.diplomacy_for_ai_system = diplomacy_for_ai_system
        self.color_duplicate = color_duplicate
        self.victory_version = victory_version

        super().__init__()


class PlayerResourcesPopulation(AoE2Object):

    _link_list = [
        RetrieverObjectLink("gold_duplicate", "Units", "player_data_4[__index__].gold_duplicate"),
        RetrieverObjectLink("wood_duplicate", "Units", "player_data_4[__index__].wood_duplicate"),
        RetrieverObjectLink("food_duplicate", "Units", "player_data_4[__index__].food_duplicate"),
        RetrieverObjectLink("stone_duplicate", "Units", "player_data_4[__index__].stone_duplicate"),
        RetrieverObjectLink("ore_x_duplicate", "Units", "player_data_4[__index__].ore_x_duplicate"),
        RetrieverObjectLink("trade_goods_duplicate", "Units", "player_data_4[__index__].trade_goods_duplicate"),
        RetrieverObjectLink("population_limit", "Units", "player_data_4[__index__].population_limit")
    ]

    def __init__(self,
                 gold_duplicate: float,
                 wood_duplicate: float,
                 food_duplicate: float,
                 stone_duplicate: float,
                 ore_x_duplicate: float,
                 trade_goods_duplicate: float,
                 population_limit: float
                 ):

        self.gold_duplicate = gold_duplicate
        self.wood_duplicate = wood_duplicate
        self.food_duplicate = food_duplicate
        self.stone_duplicate = stone_duplicate
        self.ore_x_duplicate = ore_x_duplicate
        self.trade_goods_duplicate = trade_goods_duplicate
        self.population_limit = population_limit

        super().__init__()


class PlayerDiplomacy(AoE2Object):

    _link_list = [
        RetrieverObjectLink("stance_with_each_player", "Diplomacy",
                            "per_player_diplomacy[__index__].stance_with_each_player")
    ]

    def __init__(self, stance_with_each_player: int):
        self.stance_with_each_player = stance_with_each_player
        super().__init__()

