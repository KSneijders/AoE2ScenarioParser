from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.sections.trigger_data import Effect
from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.sections import Unit
from AoE2ScenarioParser.sections.trigger_data.concerns import HasSelectedUnitsAttribute
from AoE2ScenarioParser.concerns import CanHoldUnits

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class InitiateResearch(Effect, HasSelectedUnitsAttribute, CanHoldUnits):
    """
    This effect can be used to queue a technology in a building.
    This effect requires the technology to be available and will deduct the cost of the technology from the player's resources
    """
    EFFECT_ID: int = 76

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    source_player: Player | int = RetrieverRef(Effect._source_player)
    """The player who will research the technology"""

    technology_id: TechInfo | int = RetrieverRef(Effect._technology_id)
    """The technology to begin researching"""

    def __init__(
        self,
        source_player: Player | int = -1,
        technology_id: TechInfo | int = -1,
        selected_units: list[Unit] | None = None,
    ):
        super().__init__()

        self.source_player: Player | int = source_player
        self.technology_id: TechInfo | int = technology_id
        self._selected_unit_ref_ids: list[int] = []
        self._selected_units: tuple[Unit, ...] = ()
        self.selected_units: list[Unit] = selected_units or []

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
