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


class ChangeObjectIcon(Effect):
    """
    This effect can be used to change the icon displayed for units.
    """
    EFFECT_ID: int = 42

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
    """The type of unit to change icon"""

    source_player: Player | int = RetrieverRef(Effect._source_player)
    """The player whose units will have their icon changed"""

    @property
    def area(self) -> Area:
        """The area in which units will have their icon changed. When not set, units across the entire map have their icon changed"""
        return self._area

    @area.setter
    def area(self, value: AreaT) -> None:
        """The area in which units will have their icon changed. When not set, units across the entire map have their icon changed"""
        self._area = Area.from_value(value)

    object_group: ObjectClass | int = RetrieverRef(Effect._object_group)
    """The units with this class will be affected by this effect"""

    object_type: ObjectType | int = RetrieverRef(Effect._object_type)
    """The units of this type will be affected by this effect"""

    object2_id: UnitInfo | int = RetrieverRef(Effect._object2_id)
    """The type of unit whose icon will be used for the affected units"""

    selected_unit_ref_ids: list[Unit] | None = RetrieverRef(ret(Effect._selected_unit_ref_ids))
    """The units to be affected by this effect. When defined, overwrites all other unit filters, like area selection, type of unit, object type etc."""

    max_units_affected: int = RetrieverRef(Effect._max_units_affected)
    """The maximum number of units affected by this effect"""

    def __init__(
        self,
        object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = -1,
        source_player: Player | int = -1,
        area: AreaT | None = None,
        object_group: ObjectClass | int = -1,
        object_type: ObjectType | int = -1,
        object2_id: UnitInfo | int = -1,
        selected_unit_ref_ids: list[Unit] | None = None,
        max_units_affected: int = -1,
    ):
        super().__init__()

        self.object_id: BuildingInfo | HeroInfo | OtherInfo | UnitInfo | int = object_id
        self.source_player: Player | int = source_player
        self.area: AreaT = area or Area((-1, -1), (-1, -1))
        self.object_group: ObjectClass | int = object_group
        self.object_type: ObjectType | int = object_type
        self.object2_id: UnitInfo | int = object2_id
        self.selected_unit_ref_ids: list[Unit] = selected_unit_ref_ids or []
        self.max_units_affected: int = max_units_affected

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
