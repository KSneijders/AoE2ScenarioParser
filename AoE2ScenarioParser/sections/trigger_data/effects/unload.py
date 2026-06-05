from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.objects.support import Area, AreaT
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.trigger_data.object_class import ObjectClass
from AoE2ScenarioParser.datasets.trigger_data.object_type import ObjectType
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


class Unload(Effect):
    """
    This effect can be used to unload units at a target location.
    """
    EFFECT_ID: int = 17

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
    """The type of unit to unload"""

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player whose garrisoned units will be ordered to unload"""

    @property
    def location(self) -> Tile:
        """The tile where garrisoned units will be unloaded"""
        return self._location

    @location.setter
    def location(self, value: TileT) -> None:
        """The tile where garrisoned units will be unloaded"""
        self._location = value

    location_unit_ref: Unit = RetrieverRef(Effect._location_unit_ref)
    """The target unit to unload at (as if it was right clicked)"""

    @property
    def area(self) -> Area:
        """The area in which garrisoned units will be ordered to unload. When not set, units across the entire map are ordered to unload"""
        return self._area

    @area.setter
    def area(self, value: AreaT) -> None:
        """The area in which garrisoned units will be ordered to unload. When not set, units across the entire map are ordered to unload"""
        self._area = value

    object_group: ObjectClass = RetrieverRef(Effect._object_group)
    """The units with this class will be affected by this effect"""

    object_type: ObjectType = RetrieverRef(Effect._object_type)
    """The units of this type will be affected by this effect"""

    selected_unit_ref_ids: list[Unit] = RetrieverRef(ret(Effect._selected_unit_ref_ids))
    """The units to be affected by this effect. When defined, overwrites all other unit filters, like area selection, type of unit, object type etc."""

    max_units_affected: int = RetrieverRef(Effect._max_units_affected)
    """The maximum number of units affected by this effect"""

    def __init__(
        self,
        object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = None,
        source_player: Player | None = None,
        location: Tile | None = None,
        location_unit_ref: Unit | None = None,
        area: Area | None = None,
        object_group: ObjectClass | None = None,
        object_type: ObjectType | None = None,
        selected_unit_ref_ids: list[Unit] | None = None,
        max_units_affected: int | None = None,
    ):
        super().__init__()

        self.object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = object_id
        self.source_player: Player | None = source_player
        self.location: Tile | None = location
        self.location_unit_ref: Unit | None = location_unit_ref
        self.area: Area | None = area
        self.object_group: ObjectClass | None = object_group
        self.object_type: ObjectType | None = object_type
        self.selected_unit_ref_ids: list[Unit] | None = selected_unit_ref_ids
        self.max_units_affected: int | None = max_units_affected

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
