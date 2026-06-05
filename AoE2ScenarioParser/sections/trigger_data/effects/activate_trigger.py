from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.sections import Trigger
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ActivateTrigger(Effect):
    """
    This effect can be used to activate a specific trigger.
    """
    EFFECT_ID: int = 8

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    trigger_id: Trigger = RetrieverRef(Effect._trigger_id)
    """The trigger to be activated."""

    def __init__(
        self,
        trigger_id: Trigger | None = None,
    ):
        super().__init__()

        self.trigger_id: Trigger | None = trigger_id

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
