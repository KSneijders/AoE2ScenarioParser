from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class UseAdvancedButtons(Effect):
    """
    This effect is used to toggle the advanced buttons in the minimap interface.
    """
    EFFECT_ID: int = 23

    def __init__(
        self,
    ):
        super().__init__()


    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
