from typing import List

from AoE2ScenarioParser.datasets.players import ColorId
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.sections.retrievers.retriever_object_link_group import RetrieverObjectLinkGroup


class PlayerDataThree(AoE2Object):

    _link_list = [
        RetrieverObjectLinkGroup("Units", "player_data_3[__index__]", group=[
            RetrieverObjectLink("initial_camera_x"),
            RetrieverObjectLink("initial_camera_y"),
            # Sort of duplicates. Values gets overridden by other diplomacy values, these just get changed based on that
            RetrieverObjectLink("diplomacy_for_interaction"),
            RetrieverObjectLink("diplomacy_for_ai_system"),
            # Duplicates, only here so they're replaced in the scenario file. In case it impacts gameplay
            RetrieverObjectLink("aok_allied_victory"),
            RetrieverObjectLink("color"),
            # AFAIK - These are stored but have no impact on the game, last camera xy position with player selected
            # RetrieverObjectLink("editor_camera_x"),
            # RetrieverObjectLink("editor_camera_y"),
        ]),
    ]

    def __init__(
            self,
            initial_camera_x: int,
            initial_camera_y: int,
            aok_allied_victory: int,
            diplomacy_for_interaction: List[int],
            diplomacy_for_ai_system: List[int],
            color: int,
            **kwargs):
        super().__init__(**kwargs)

        self.initial_camera_x = initial_camera_x
        self.initial_camera_y = initial_camera_y
        self.aok_allied_victory = aok_allied_victory
        self.diplomacy_for_interaction = diplomacy_for_interaction
        self.diplomacy_for_ai_system = diplomacy_for_ai_system
        self.color: ColorId = ColorId(color)
