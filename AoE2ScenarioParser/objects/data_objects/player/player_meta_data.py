from AoE2ScenarioParser.datasets.object_support import Civilization
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.data_objects.player.player import Player
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.sections.retrievers.retriever_object_link_group import RetrieverObjectLinkGroup
from AoE2ScenarioParser.sections.retrievers.support import Support


class PlayerMetaData(AoE2Object):

    _link_list = [
        RetrieverObjectLinkGroup("DataHeader", "player_data_1[__index__]", group=[
            RetrieverObjectLink("active"),
            RetrieverObjectLink("human"),
            RetrieverObjectLink("civilization"),
            RetrieverObjectLink("architecture_set", support=Support(since=1.40), destination_object=Player),
        ])
    ]

    def __init__(self, active: int, human: int, civilization: int, architecture_set: int, **kwargs):
        super().__init__(**kwargs)

        self.active: bool = bool(active)
        self.human: bool = bool(human)
        self.civilization: int = civilization
        self.architecture_set: int = architecture_set if architecture_set is not None else None
