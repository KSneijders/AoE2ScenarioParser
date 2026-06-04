from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class DisableTechnologyStacking(Effect):
    """
    This effect can be used to disable stacking for a technology that was previously set to stack.
    """
    EFFECT_ID: int = 68

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player for whom technology stacking will be disabled"""

    technology_id: TechInfo = RetrieverRef(Effect._technology_id)
    """The technology to disable stacking for"""

    def __init__(
        self,
        source_player: Player | None = None,
        technology_id: TechInfo | None = None,
    ):
        super().__init__()

        self.source_player: Player | None = source_player
        self.technology_id: TechInfo | None = technology_id

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
