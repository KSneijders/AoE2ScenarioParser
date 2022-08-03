from __future__ import annotations

from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.sections.retrievers.retriever_object_link_group import RetrieverObjectLinkGroup


class MessageManager(AoE2Object):
    """Manager of the everything message tab related."""

    _link_list = [
        RetrieverObjectLinkGroup("Messages", group=[
            RetrieverObjectLink("instructions", "ascii_instructions"),
            RetrieverObjectLink("hints", "ascii_hints"),
            RetrieverObjectLink("victory", "ascii_victory"),
            RetrieverObjectLink("loss", "ascii_loss"),
            RetrieverObjectLink("history", "ascii_history"),
            RetrieverObjectLink("scouts", "ascii_scouts"),
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
