from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.sections.retrievers.retriever_object_link_group import RetrieverObjectLinkGroup


class PlayerAiFile(AoE2Object):

    _link_list = [
        RetrieverObjectLinkGroup("PlayerDataTwo", "ai_files[__index__]", group=[
            RetrieverObjectLink("ai_per_file_text"),
        ])
    ]

    def __init__(self, ai_per_file_text: str = "", **kwargs):
        super().__init__(**kwargs)

        self.ai_per_file_text: str = ai_per_file_text
