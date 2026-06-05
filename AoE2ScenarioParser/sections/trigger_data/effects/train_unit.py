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


class TrainUnit(Effect):
    """
    This effect can be used to queue specific units in a building.
    This effect requires the unit to be available and will deduct the cost of the unit from the player's resources
    """
    EFFECT_ID: int = 75

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    quantity: int = RetrieverRef(Effect._quantity)
    """The number of units to queue for training"""

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
    """The type of unit to train"""

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player who will train the unit"""

    @property
    def location(self) -> Tile:
        """The tile to set the gather point at"""
        return self._location

    @location.setter
    def location(self, value: TileT) -> None:
        """The tile to set the gather point at"""
        self._location = value

    @property
    def area(self) -> Area:
        """The area in which buildings will queue the unit. When not set, buildings across the entire map are affected"""
        return self._area

    @area.setter
    def area(self, value: AreaT) -> None:
        """The area in which buildings will queue the unit. When not set, buildings across the entire map are affected"""
        self._area = value

    selected_unit_ref_ids: list[Unit] = RetrieverRef(ret(Effect._selected_unit_ref_ids))
    """The units to be affected by this effect. When defined, overwrites all other unit filters, like area selection, type of unit, object type etc."""

    max_units_affected: int = RetrieverRef(Effect._max_units_affected)
    """The maximum number of units affected by this effect"""

    def __init__(
        self,
        quantity: int | None = None,
        object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = None,
        source_player: Player | None = None,
        location: Tile | None = None,
        area: Area | None = None,
        selected_unit_ref_ids: list[Unit] | None = None,
        max_units_affected: int | None = None,
    ):
        super().__init__()

        self.quantity: int | None = quantity
        self.object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = object_id
        self.source_player: Player | None = source_player
        self.location: Tile | None = location
        self.area: Area | None = area
        self.selected_unit_ref_ids: list[Unit] | None = selected_unit_ref_ids
        self.max_units_affected: int | None = max_units_affected

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
