from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.sections.trigger_data import Effect
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.objects.support import Tile, TileT, Area, AreaT
from AoE2ScenarioParser.sections import Unit
from AoE2ScenarioParser.datasets.trigger_data import ObjectClass, ObjectType
from AoE2ScenarioParser.sections.trigger_data.concerns import HasSelectedUnitsAttribute
from AoE2ScenarioParser.concerns import CanHoldUnits

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class Unload(Effect, HasSelectedUnitsAttribute, CanHoldUnits):
    """
    This effect can be used to unload units at a target location.
    """
    EFFECT_ID: int = 17

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
    """The type of unit to unload"""

    source_player: Player | int = RetrieverRef(Effect._source_player)
    """The player whose garrisoned units will be ordered to unload"""

    @property
    def location(self) -> Tile:
        """The tile where garrisoned units will be unloaded"""
        return self._location

    @location.setter
    def location(self, value: TileT) -> None:
        """The tile where garrisoned units will be unloaded"""
        self._location = Tile.from_value(value)

    location_unit_ref: Unit | int = RetrieverRef(Effect._location_unit_ref)
    """The target unit to unload at (as if it was right clicked)"""

    @property
    def area(self) -> Area:
        """The area in which garrisoned units will be ordered to unload. When not set, units across the entire map are ordered to unload"""
        return self._area

    @area.setter
    def area(self, value: AreaT) -> None:
        """The area in which garrisoned units will be ordered to unload. When not set, units across the entire map are ordered to unload"""
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
        location_unit_ref: Unit | int = -1,
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
        self.location_unit_ref: Unit | int = location_unit_ref
        self.area: AreaT = area or Area((-1, -1), (-1, -1))
        self.object_group: ObjectClass | int = object_group
        self.object_type: ObjectType | int = object_type
        self._selected_unit_ref_ids: list[int] = []
        self._selected_units: tuple[Unit, ...] = ()
        self.selected_units: list[Unit] = selected_units or []
        self.max_units_affected: int = max_units_affected

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
