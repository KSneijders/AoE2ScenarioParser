from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.datasets.trigger_data.panel_location import PanelLocation
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ClearInstructions(Effect):
    """
    This effect can be used to clear the message from an instruction panel.
    """
    EFFECT_ID: int = 21

    instruction_panel_position: PanelLocation = RetrieverRef(Effect._instruction_panel_position)
    """The position of the instruction panel to clear"""

    def __init__(
        self,
        instruction_panel_position: PanelLocation | None = None,
    ):
        super().__init__()

        self.instruction_panel_position: PanelLocation | None = instruction_panel_position

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
