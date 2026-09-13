from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.sections.trigger_data import Effect
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.sections import Unit
from AoE2ScenarioParser.sections.trigger_data.concerns import HasSelectedUnitsAttribute
from AoE2ScenarioParser.concerns import CanHoldUnits
from AoE2ScenarioParser.objects.support import Area, AreaT
from AoE2ScenarioParser.datasets.units import UnitInfo

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ResearchLocalTechnology(Effect, HasSelectedUnitsAttribute, CanHoldUnits):
    """
    This effect can be used to research a local technology for a type of unit.
    """
    EFFECT_ID: int = 103

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    local_technology_id: TechInfo | int = RetrieverRef(Effect._local_technology_id)
    """The local technology to research for the type of unit"""

    source_player: Player | int = RetrieverRef(Effect._source_player)
    """The player for whom the local technology will be researched"""

    @property
    def area(self) -> Area:
        """The area in which units will research the local technology. When not set, units across the entire map research the local technology"""
        return self._area

    @area.setter
    def area(self, value: AreaT) -> None:
        """The area in which units will research the local technology. When not set, units across the entire map research the local technology"""
        self._area = Area.from_value(value)

    object2_id: UnitInfo | int = RetrieverRef(Effect._object2_id)
    """The type of unit to research the local technology in"""

    def __init__(
        self,
        local_technology_id: TechInfo | int = -1,
        source_player: Player | int = -1,
        selected_units: list[Unit] | None = None,
        area: AreaT | None = None,
        object2_id: UnitInfo | int = -1,
    ):
        super().__init__()

        self.local_technology_id: TechInfo | int = local_technology_id
        self.source_player: Player | int = source_player
        self._selected_unit_ref_ids: list[int] = []
        self._selected_units: tuple[Unit, ...] = ()
        self.selected_units: list[Unit] = selected_units or []
        self.area: AreaT = area or Area((-1, -1), (-1, -1))
        self.object2_id: UnitInfo | int = object2_id

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
