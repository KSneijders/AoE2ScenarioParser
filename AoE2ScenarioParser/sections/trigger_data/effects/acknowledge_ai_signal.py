from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class AcknowledgeAiSignal(Effect):
    """
    This effect can be used to acknowledge a pending AI signal.
    """
    EFFECT_ID: int = 50

    ai_signal: int = RetrieverRef(Effect._ai_signal)
    """The AI Signal ID to acknowledge"""

    def __init__(
        self,
        ai_signal: int | None = None,
    ):
        super().__init__()

        self.ai_signal: int | None = ai_signal

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
