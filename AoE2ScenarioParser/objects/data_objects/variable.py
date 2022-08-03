from __future__ import annotations

from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.sections.retrievers.retriever_object_link_group import RetrieverObjectLinkGroup


class Variable(AoE2Object):
    """Object for handling a variable."""

    _link_list = [
        RetrieverObjectLinkGroup("Triggers", "variable_data[__index__]", group=[
            RetrieverObjectLink("variable_id"),
            RetrieverObjectLink("name", link="variable_name"),
        ])
    ]

    def __init__(self, variable_id: int, name: str, **kwargs):
        self.variable_id = variable_id
        self.name = name

        super().__init__(**kwargs)
