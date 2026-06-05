from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class CreateDecision(Effect):
    """
    This effect can be used to display a decision dialog with two choices, storing the choice in the decision ID.
    """
    EFFECT_ID: int = 90

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    decision_id: int = RetrieverRef(Effect._decision_id)
    """The decision ID to use"""

    str_id: int = RetrieverRef(Effect._str_id)
    """The string ID to use as the decision prompt"""

    message: str = RetrieverRef(ret(Effect._message))
    """The prompt to display in the decision dialog"""

    decision_option1_str_id: int = RetrieverRef(Effect._decision_option1_str_id)
    """The string ID to use for the first decision option"""

    message_option1: str = RetrieverRef(ret(Effect._message_option1))
    """The message to use for the first decision option. Ignored when the string ID is set."""

    decision_option2_str_id: int = RetrieverRef(Effect._decision_option2_str_id)
    """The string ID to use for the second decision option"""

    message_option2: str = RetrieverRef(ret(Effect._message_option2))
    """The message to use for the second decision option. Ignored when the string ID is set."""

    def __init__(
        self,
        decision_id: int | None = None,
        str_id: int | None = None,
        message: str | None = None,
        decision_option1_str_id: int | None = None,
        message_option1: str | None = None,
        decision_option2_str_id: int | None = None,
        message_option2: str | None = None,
    ):
        super().__init__()

        self.decision_id: int | None = decision_id
        self.str_id: int | None = str_id
        self.message: str | None = message
        self.decision_option1_str_id: int | None = decision_option1_str_id
        self.message_option1: str | None = message_option1
        self.decision_option2_str_id: int | None = decision_option2_str_id
        self.message_option2: str | None = message_option2

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
