from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.objects.support import Area, AreaT
from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.sections import Unit
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ResearchLocalTechnology(Effect):
    """
    This effect can be used to research a local technology for a type of unit.
    """
    EFFECT_ID: int = 103

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    local_technology_id: TechInfo = RetrieverRef(Effect._local_technology_id)
    """The local technology to research for the type of unit"""

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player for whom the local technology will be researched"""

    selected_unit_ref_ids: list[Unit] = RetrieverRef(ret(Effect._selected_unit_ref_ids))
    """The units to be affected by this effect. When defined, overwrites all other unit filters, like area selection, type of unit, object type etc."""

    @property
    def area(self) -> Area:
        """The area in which units will research the local technology. When not set, units across the entire map research the local technology"""
        return self._area

    @area.setter
    def area(self, value: AreaT) -> None:
        """The area in which units will research the local technology. When not set, units across the entire map research the local technology"""
        self._area = value

    object2_id: UnitInfo = RetrieverRef(Effect._object2_id)
    """The type of unit to research the local technology in"""

    def __init__(
        self,
        local_technology_id: TechInfo | None = None,
        source_player: Player | None = None,
        selected_unit_ref_ids: list[Unit] | None = None,
        area: Area | None = None,
        object2_id: UnitInfo | None = None,
    ):
        super().__init__()

        self.local_technology_id: TechInfo | None = local_technology_id
        self.source_player: Player | None = source_player
        self.selected_unit_ref_ids: list[Unit] | None = selected_unit_ref_ids
        self.area: Area | None = area
        self.object2_id: UnitInfo | None = object2_id

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
