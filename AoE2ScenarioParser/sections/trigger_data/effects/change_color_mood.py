from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.datasets.trigger_data.color_mood import ColorMood
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ChangeColorMood(Effect):
    """
    This effect can be used to change the overall color atmosphere of the map.
    """
    EFFECT_ID: int = 72

    quantity: int = RetrieverRef(Effect._quantity)
    """The time in seconds to fade to the new color mood"""

    color_mood: ColorMood = RetrieverRef(Effect._color_mood)
    """The color mood to set"""

    def __init__(
        self,
        quantity: int | None = None,
        color_mood: ColorMood | None = None,
    ):
        super().__init__()

        self.quantity: int | None = quantity
        self.color_mood: ColorMood | None = color_mood

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
