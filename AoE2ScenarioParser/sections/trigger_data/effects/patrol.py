from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.sections.trigger_data import Effect
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.objects.support import Tile, TileT, Area, AreaT
from AoE2ScenarioParser.datasets.trigger_data import ObjectClass, ObjectType
from AoE2ScenarioParser.sections import Unit
from AoE2ScenarioParser.sections.trigger_data.concerns import HasSelectedUnitsAttribute
from AoE2ScenarioParser.concerns import CanHoldUnits

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class Patrol(Effect, HasSelectedUnitsAttribute, CanHoldUnits):
    """
    This effect can be used to patrol units to a specific tile.
    """
    EFFECT_ID: int = 19

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
    """The type of unit to patrol"""

    source_player: Player | int = RetrieverRef(Effect._source_player)
    """The player whose units to patrol"""

    @property
    def location(self) -> Tile:
        """The tile to patrol to"""
        return self._location

    @location.setter
    def location(self, value: TileT) -> None:
        """The tile to patrol to"""
        self._location = Tile.from_value(value)

    @property
    def area(self) -> Area:
        """The area in which units will be patrolled. When not set, units across the entire map are patrolled"""
        return self._area

    @area.setter
    def area(self, value: AreaT) -> None:
        """The area in which units will be patrolled. When not set, units across the entire map are patrolled"""
        self._area = Area.from_value(value)

    object_group: ObjectClass | int = RetrieverRef(Effect._object_group)
    """The units with this class will be affected by this effect"""

    object_type: ObjectType | int = RetrieverRef(Effect._object_type)
    """The units of this type will be affected by this effect"""

    max_units_affected: int = RetrieverRef(Effect._max_units_affected)
    """The maximum number of units affected by this effect"""

    def __init__(
        self,
        object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = -1,
        source_player: Player | int = -1,
        location: TileT | None = None,
        area: AreaT | None = None,
        object_group: ObjectClass | int = -1,
        object_type: ObjectType | int = -1,
        selected_units: list[Unit] | None = None,
        max_units_affected: int = -1,
    ):
        super().__init__()

        self.object_id: BuildingInfo | HeroInfo | OtherInfo | UnitInfo | int = object_id
        self.source_player: Player | int = source_player
        self.location: TileT = location or Tile(-1, -1)
        self.area: AreaT = area or Area((-1, -1), (-1, -1))
        self.object_group: ObjectClass | int = object_group
        self.object_type: ObjectType | int = object_type
        self._selected_unit_ref_ids: list[int] = []
        self._selected_units: tuple[Unit, ...] = ()
        self.selected_units: list[Unit] = selected_units or []
        self.max_units_affected: int = max_units_affected

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
