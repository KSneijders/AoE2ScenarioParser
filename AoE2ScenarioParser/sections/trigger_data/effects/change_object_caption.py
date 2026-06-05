from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.objects.support import Area, AreaT
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.sections import Unit
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ChangeObjectCaption(Effect):
    """
    This effect can be used to change the caption displayed above units.
    """
    EFFECT_ID: int = 88

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
    """The type of unit to change the caption for"""

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player whose units will have their caption changed"""

    str_id: int = RetrieverRef(Effect._str_id)
    """The string ID to use as the new caption for the affected units"""

    message: str = RetrieverRef(ret(Effect._message))
    """The new caption to display for the affected units"""

    @property
    def area(self) -> Area:
        """The area in which units will have their caption changed. When not set, units across the entire map have their caption changed"""
        return self._area

    @area.setter
    def area(self, value: AreaT) -> None:
        """The area in which units will have their caption changed. When not set, units across the entire map have their caption changed"""
        self._area = value

    selected_unit_ref_ids: list[Unit] = RetrieverRef(ret(Effect._selected_unit_ref_ids))
    """The units to be affected by this effect. When defined, overwrites all other unit filters, like area selection, type of unit, object type etc."""

    def __init__(
        self,
        object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = None,
        source_player: Player | None = None,
        str_id: int | None = None,
        message: str | None = None,
        area: Area | None = None,
        selected_unit_ref_ids: list[Unit] | None = None,
    ):
        super().__init__()

        self.object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = object_id
        self.source_player: Player | None = source_player
        self.str_id: int | None = str_id
        self.message: str | None = message
        self.area: Area | None = area
        self.selected_unit_ref_ids: list[Unit] | None = selected_unit_ref_ids

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
