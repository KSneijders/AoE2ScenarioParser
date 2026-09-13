from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.sections.trigger_data import Effect
from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.objects.support import Area, AreaT
from AoE2ScenarioParser.sections import Unit
from AoE2ScenarioParser.sections.trigger_data.concerns import HasSelectedUnitsAttribute
from AoE2ScenarioParser.concerns import CanHoldUnits

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ChangeObjectCivilizationName(Effect, HasSelectedUnitsAttribute, CanHoldUnits):
    """
    This effect can be used to change the civilization name displayed for units.
    """
    EFFECT_ID: int = 59

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    source_player: Player | int = RetrieverRef(Effect._source_player)
    """The player whose units will have their civilization name changed"""

    str_id: int = RetrieverRef(Effect._str_id)
    """The string ID to use as the new civilization name for the affected units"""

    @property
    def area(self) -> Area:
        """The area in which units will have their civilization name changed. When not set, units across the entire map have their civilization name changed"""
        return self._area

    @area.setter
    def area(self, value: AreaT) -> None:
        """The area in which units will have their civilization name changed. When not set, units across the entire map have their civilization name changed"""
        self._area = Area.from_value(value)

    message: str = RetrieverRef(ret(Effect._message))
    """The civilization name to display for the affected units"""

    max_units_affected: int = RetrieverRef(Effect._max_units_affected)
    """The maximum number of units affected by this effect"""

    def __init__(
        self,
        source_player: Player | int = -1,
        str_id: int = -1,
        area: AreaT | None = None,
        message: str = '',
        selected_units: list[Unit] | None = None,
        max_units_affected: int = -1,
    ):
        super().__init__()

        self.source_player: Player | int = source_player
        self.str_id: int = str_id
        self.area: AreaT = area or Area((-1, -1), (-1, -1))
        self.message: str = message
        self._selected_unit_ref_ids: list[int] = []
        self._selected_units: tuple[Unit, ...] = ()
        self.selected_units: list[Unit] = selected_units or []
        self.max_units_affected: int = max_units_affected

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
