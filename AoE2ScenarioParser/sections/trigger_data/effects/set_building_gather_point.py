from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.objects.support import Area, AreaT
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.objects.support import Tile, TileT
from AoE2ScenarioParser.sections import Unit
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class SetBuildingGatherPoint(Effect):
    """
    This effect can be used to set the gather point (rally point) for buildings.
    """
    EFFECT_ID: int = 54

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
    """The type of building to set the gather point for"""

    source_player: Player | int = RetrieverRef(Effect._source_player)
    """The player whose buildings will have their gather point set"""

    @property
    def location(self) -> Tile:
        """The tile to set the gather point at"""
        return self._location

    @location.setter
    def location(self, value: TileT) -> None:
        """The tile to set the gather point at"""
        self._location = Tile.from_value(value)

    @property
    def area(self) -> Area:
        """The area in which buildings will have their gather point set. When not set, buildings across the entire map are affected"""
        return self._area

    @area.setter
    def area(self, value: AreaT) -> None:
        """The area in which buildings will have their gather point set. When not set, buildings across the entire map are affected"""
        self._area = Area.from_value(value)

    selected_unit_ref_ids: list[Unit] | None = RetrieverRef(ret(Effect._selected_unit_ref_ids))
    """The units to be affected by this effect. When defined, overwrites all other unit filters, like area selection, type of unit, object type etc."""

    max_units_affected: int = RetrieverRef(Effect._max_units_affected)
    """The maximum number of units affected by this effect"""

    def __init__(
        self,
        object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = -1,
        source_player: Player | int = -1,
        location: TileT | None = None,
        area: AreaT | None = None,
        selected_unit_ref_ids: list[Unit] | None = None,
        max_units_affected: int = -1,
    ):
        super().__init__()

        self.object_id: BuildingInfo | HeroInfo | OtherInfo | UnitInfo | int = object_id
        self.source_player: Player | int = source_player
        self.location: TileT = location or Tile(-1, -1)
        self.area: AreaT = area or Area((-1, -1), (-1, -1))
        self.selected_unit_ref_ids: list[Unit] = selected_unit_ref_ids or []
        self.max_units_affected: int = max_units_affected

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
