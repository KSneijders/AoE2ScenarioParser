from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.sections import Unit
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class InitiateResearch(Effect):
    """
    This effect can be used to queue a technology in a building.
    This effect requires the technology to be available and will deduct the cost of the technology from the player's resources
    """
    EFFECT_ID: int = 76

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player who will research the technology"""

    technology_id: TechInfo = RetrieverRef(Effect._technology_id)
    """The technology to begin researching"""

    selected_unit_ref_ids: list[Unit] = RetrieverRef(ret(Effect._selected_unit_ref_ids))
    """The building to be affected by this effect."""

    def __init__(
        self,
        source_player: Player | None = None,
        technology_id: TechInfo | None = None,
        selected_unit_ref_ids: list[Unit] | None = None,
    ):
        super().__init__()

        self.source_player: Player | None = source_player
        self.technology_id: TechInfo | None = technology_id
        self.selected_unit_ref_ids: list[Unit] | None = selected_unit_ref_ids

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
