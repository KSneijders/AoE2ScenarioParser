from typing import List

from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink


class PlayerDiplomacy(AoE2Object):

    _link_list = [
        RetrieverObjectLink("diplomacy_stance", "Diplomacy", "per_player_diplomacy[__index__].stance_with_each_player"),
    ]

    def __init__(self, diplomacy_stance: List[int], **kwargs):
        super().__init__(**kwargs)

        self.diplomacy_stance: List[int] = diplomacy_stance
