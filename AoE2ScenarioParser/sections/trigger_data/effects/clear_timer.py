from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ClearTimer(Effect):
    """
    This effect can be used to clear and hide a previously displayed timer.
    """
    EFFECT_ID: int = 57

    timer_id: int = RetrieverRef(Effect._timer_id)
    """The ID of the timer to clear and hide"""

    def __init__(
        self,
        timer_id: int | None = None,
    ):
        super().__init__()

        self.timer_id: int | None = timer_id

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
