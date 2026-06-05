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


class TeleportObject(Effect):
    """
    This effect can be used to teleport units to the specified tile.
    The game will check for collisions before teleporting, which means it will teleport only a single unit unless the units have no collision.
    """
    EFFECT_ID: int = 35

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
    """The type of unit to teleport"""

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player whose units will be teleported"""

    @property
    def location(self) -> Tile:
        """The tile to teleport units to"""
        return self._location

    @location.setter
    def location(self, value: TileT) -> None:
        """The tile to teleport units to"""
        self._location = value

    @property
    def area(self) -> Area:
        """The area in which units will be teleported. When not set, units across the entire map are teleported"""
        return self._area

    @area.setter
    def area(self, value: AreaT) -> None:
        """The area in which units will be teleported. When not set, units across the entire map are teleported"""
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
        self.area: Area | None = area
        self.object_group: ObjectClass | None = object_group
        self.object_type: ObjectType | None = object_type
        self.selected_unit_ref_ids: list[Unit] | None = selected_unit_ref_ids
        self.max_units_affected: int | None = max_units_affected

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
