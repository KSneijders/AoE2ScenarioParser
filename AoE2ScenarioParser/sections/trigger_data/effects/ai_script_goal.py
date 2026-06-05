from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class AiScriptGoal(Effect):
    """
    This effect can be used to communicate with an AI player by setting an AI Trigger number.
    The AI Trigger number can be detected inside an AI script using: `event-detected trigger NUMBER`
    """
    EFFECT_ID: int = 10

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    ai_script_goal: int = RetrieverRef(Effect._ai_script_goal)
    """The AI Trigger number to set"""

    def __init__(
        self,
        ai_script_goal: int | None = None,
    ):
        super().__init__()

        self.ai_script_goal: int | None = ai_script_goal

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
