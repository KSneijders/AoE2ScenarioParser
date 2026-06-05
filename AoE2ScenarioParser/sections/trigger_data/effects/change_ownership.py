from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.objects.support import Area, AreaT
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.trigger_data.object_class import ObjectClass
from AoE2ScenarioParser.datasets.trigger_data.object_type import ObjectType
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.sections import Unit
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ChangeOwnership(Effect):
    """
    This effect can be used to change ownership of units from the source player to the target player.
    """
    EFFECT_ID: int = 18

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
    """The type of unit to change ownership"""

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player who currently owns the units"""

    target_player: Player = RetrieverRef(Effect._target_player)
    """The player who will receive ownership of the units"""

    @property
    def area(self) -> Area:
        """The area in which units will have their ownership changed. When not set, units across the entire map have their ownership changed"""
        return self._area

    @area.setter
    def area(self, value: AreaT) -> None:
        """The area in which units will have their ownership changed. When not set, units across the entire map have their ownership changed"""
        self._area = value

    object_group: ObjectClass = RetrieverRef(Effect._object_group)
    """The units with this class will be affected by this effect"""

    object_type: ObjectType = RetrieverRef(Effect._object_type)
    """The units of this type will be affected by this effect"""

    flash_unit: bool = RetrieverRef(Effect._flash_unit)
    """When enabled, flash the affected units when the source and target player are the same"""

    selected_unit_ref_ids: list[Unit] = RetrieverRef(ret(Effect._selected_unit_ref_ids))
    """The units to be affected by this effect. When defined, overwrites all other unit filters, like area selection, type of unit, object type etc."""

    max_units_affected: int = RetrieverRef(Effect._max_units_affected)
    """The maximum number of units affected by this effect"""

    def __init__(
        self,
        object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = None,
        source_player: Player | None = None,
        target_player: Player | None = None,
        area: Area | None = None,
        object_group: ObjectClass | None = None,
        object_type: ObjectType | None = None,
        flash_unit: bool | None = None,
        selected_unit_ref_ids: list[Unit] | None = None,
        max_units_affected: int | None = None,
    ):
        super().__init__()

        self.object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = object_id
        self.source_player: Player | None = source_player
        self.target_player: Player | None = target_player
        self.area: Area | None = area
        self.object_group: ObjectClass | None = object_group
        self.object_type: ObjectType | None = object_type
        self.flash_unit: bool | None = flash_unit
        self.selected_unit_ref_ids: list[Unit] | None = selected_unit_ref_ids
        self.max_units_affected: int | None = max_units_affected

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
