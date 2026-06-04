from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.sections import Trigger
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class DeactivateTrigger(Effect):
    """
    This effect can be used to deactivate a specific trigger.
    """
    EFFECT_ID: int = 9

    trigger_id: Trigger = RetrieverRef(Effect._trigger_id)
    """The trigger to be deactivated."""

    def __init__(
        self,
        trigger_id: Trigger | None = None,
    ):
        super().__init__()

        self.trigger_id: Trigger | None = trigger_id

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
