from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.sections.trigger_data import Effect
from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.objects.support import Area, AreaT
from AoE2ScenarioParser.datasets.trigger_data import VisibilityState
from AoE2ScenarioParser.sections import Unit
from AoE2ScenarioParser.sections.trigger_data.concerns import HasSelectedUnitsAttribute
from AoE2ScenarioParser.concerns import CanHoldUnits

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ChangeObjectVisibility(Effect, HasSelectedUnitsAttribute, CanHoldUnits):
    """
    This effect can be used to change the visibility state of units for a specific player.
    """
    EFFECT_ID: int = 107

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    source_player: Player | int = RetrieverRef(Effect._source_player)
    """The player whose units' visibility will be changed for the target player"""

    target_player: Player | int = RetrieverRef(Effect._target_player)
    """The player for whom the unit visibility will change"""

    @property
    def area(self) -> Area:
        """The area in which units will have their visibility changed. When not set, units across the entire map have their visibility changed"""
        return self._area

    @area.setter
    def area(self, value: AreaT) -> None:
        """The area in which units will have their visibility changed. When not set, units across the entire map have their visibility changed"""
        self._area = Area.from_value(value)

    visibility_state: VisibilityState | int = RetrieverRef(Effect._visibility_state)
    """The visibility state to use"""

    max_units_affected: int = RetrieverRef(Effect._max_units_affected)
    """The maximum number of units affected by this effect"""

    def __init__(
        self,
        source_player: Player | int = -1,
        target_player: Player | int = -1,
        area: AreaT | None = None,
        visibility_state: VisibilityState | int = -1,
        max_units_affected: int = -1,
        selected_units: list[Unit] | None = None,
    ):
        super().__init__()

        self.source_player: Player | int = source_player
        self.target_player: Player | int = target_player
        self.area: AreaT = area or Area((-1, -1), (-1, -1))
        self.visibility_state: VisibilityState | int = visibility_state
        self.max_units_affected: int = max_units_affected
        self._selected_unit_ref_ids: list[int] = []
        self._selected_units: tuple[Unit, ...] = ()
        self.selected_units: list[Unit] = selected_units or []

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
