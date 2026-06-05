from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.objects.support import Area, AreaT
from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.sections import Unit
from AoE2ScenarioParser.datasets.trigger_data.visibility_state import VisibilityState
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ChangeObjectVisibility(Effect):
    """
    This effect can be used to change the visibility state of units for a specific player.
    """
    EFFECT_ID: int = 107

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player whose units' visibility will be changed for the target player"""

    target_player: Player = RetrieverRef(Effect._target_player)
    """The player for whom the unit visibility will change"""

    @property
    def area(self) -> Area:
        """The area in which units will have their visibility changed. When not set, units across the entire map have their visibility changed"""
        return self._area

    @area.setter
    def area(self, value: AreaT) -> None:
        """The area in which units will have their visibility changed. When not set, units across the entire map have their visibility changed"""
        self._area = value

    visibility_state: VisibilityState = RetrieverRef(Effect._visibility_state)
    """The visibility state to use"""

    max_units_affected: int = RetrieverRef(Effect._max_units_affected)
    """The maximum number of units affected by this effect"""

    selected_unit_ref_ids: list[Unit] = RetrieverRef(ret(Effect._selected_unit_ref_ids))
    """The units to be affected by this effect. When defined, overwrites all other unit filters, like area selection, type of unit, object type etc."""

    def __init__(
        self,
        source_player: Player | None = None,
        target_player: Player | None = None,
        area: Area | None = None,
        visibility_state: VisibilityState | None = None,
        max_units_affected: int | None = None,
        selected_unit_ref_ids: list[Unit] | None = None,
    ):
        super().__init__()

        self.source_player: Player | None = source_player
        self.target_player: Player | None = target_player
        self.area: Area | None = area
        self.visibility_state: VisibilityState | None = visibility_state
        self.max_units_affected: int | None = max_units_affected
        self.selected_unit_ref_ids: list[Unit] | None = selected_unit_ref_ids

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
