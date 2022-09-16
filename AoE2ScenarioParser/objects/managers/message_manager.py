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

            RetrieverObjectLink("instructions_string_table_id", link="instructions"),
            RetrieverObjectLink("hints_string_table_id", link="hints"),
            RetrieverObjectLink("victory_string_table_id", link="victory"),
            RetrieverObjectLink("loss_string_table_id", link="loss"),
            RetrieverObjectLink("history_string_table_id", link="history"),
            RetrieverObjectLink("scouts_string_table_id", link="scouts"),
        ]),
    ]

    def __init__(self,
                 instructions: str,
                 hints: str,
                 victory: str,
                 loss: str,
                 history: str,
                 scouts: str,
                 instructions_string_table_id: int,
                 hints_string_table_id: int,
                 victory_string_table_id: int,
                 loss_string_table_id: int,
                 history_string_table_id: int,
                 scouts_string_table_id: int,
                 **kwargs
                 ):
        super().__init__(**kwargs)

        self.instructions: str = instructions
        self.hints: str = hints
        self.victory: str = victory
        self.loss: str = loss
        self.history: str = history
        self.scouts: str = scouts
        self.instructions_string_table_id: int = instructions_string_table_id
        self.hints_string_table_id: int = hints_string_table_id
        self.victory_string_table_id: int = victory_string_table_id
        self.loss_string_table_id: int = loss_string_table_id
        self.history_string_table_id: int = history_string_table_id
        self.scouts_string_table_id: int = scouts_string_table_id
