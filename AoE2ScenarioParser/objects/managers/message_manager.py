from __future__ import annotations

from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.sections.retrievers.retriever_object_link_group import RetrieverObjectLinkGroup


class MessageManager(AoE2Object):
    """Manager of the everything message tab related."""

    _link_list = [
        RetrieverObjectLinkGroup("Messages", group=[
            RetrieverObjectLink("instructions", link="ascii_instructions"),
            RetrieverObjectLink("hints", link="ascii_hints"),
            RetrieverObjectLink("victory", link="ascii_victory"),
            RetrieverObjectLink("loss", link="ascii_loss"),
            RetrieverObjectLink("history", link="ascii_history"),
            RetrieverObjectLink("scouts", link="ascii_scouts"),
        ]),
    ]

    def __init__(self,
                 instructions: str,
                 hints: str,
                 victory: str,
                 loss: str,
                 history: str,
                 scouts: str,
                 **kwargs
                 ):
        super().__init__(**kwargs)

        self.instructions = instructions
        self.hints = hints
        self.victory = victory
        self.loss = loss
        self.history = history
        self.scouts = scouts
