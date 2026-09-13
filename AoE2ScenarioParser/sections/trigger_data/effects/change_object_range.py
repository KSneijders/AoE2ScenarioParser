from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.sections.trigger_data import Effect
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.objects.support import Area, AreaT
from AoE2ScenarioParser.datasets.trigger_data import ObjectClass, ObjectType, Operation
from AoE2ScenarioParser.sections import Unit
from AoE2ScenarioParser.sections.trigger_data.concerns import HasSelectedUnitsAttribute
from AoE2ScenarioParser.concerns import CanHoldUnits

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ChangeObjectRange(Effect, HasSelectedUnitsAttribute, CanHoldUnits):
    """
    This effect can be used to modify the attack range of units.
    """
    EFFECT_ID: int = 32

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    quantity: int = RetrieverRef(Effect._quantity)
    """The amount to change the attack range by"""

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
    """The type of unit to change range"""

    source_player: Player | int = RetrieverRef(Effect._source_player)
    """The player whose units will have their range changed"""

    @property
    def area(self) -> Area:
        """The area in which units will have their range changed. When not set, units across the entire map have their range changed"""
        return self._area

    @area.setter
    def area(self, value: AreaT) -> None:
        """The area in which units will have their range changed. When not set, units across the entire map have their range changed"""
        self._area = Area.from_value(value)

    object_group: ObjectClass | int = RetrieverRef(Effect._object_group)
    """The units with this class will be affected by this effect"""

    object_type: ObjectType | int = RetrieverRef(Effect._object_type)
    """The units of this type will be affected by this effect"""

    operation: Operation | int = RetrieverRef(Effect._operation)
    """The operation to apply to the attribute using the quantity."""

    max_units_affected: int = RetrieverRef(Effect._max_units_affected)
    """The maximum number of units affected by this effect"""

    def __init__(
        self,
        quantity: int = -1,
        object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = -1,
        source_player: Player | int = -1,
        area: AreaT | None = None,
        object_group: ObjectClass | int = -1,
        object_type: ObjectType | int = -1,
        operation: Operation | int = -1,
        selected_units: list[Unit] | None = None,
        max_units_affected: int = -1,
    ):
        super().__init__()

        self.quantity: int = quantity
        self.object_id: BuildingInfo | HeroInfo | OtherInfo | UnitInfo | int = object_id
        self.source_player: Player | int = source_player
        self.area: AreaT = area or Area((-1, -1), (-1, -1))
        self.object_group: ObjectClass | int = object_group
        self.object_type: ObjectType | int = object_type
        self.operation: Operation | int = operation
        self._selected_unit_ref_ids: list[int] = []
        self._selected_units: tuple[Unit, ...] = ()
        self.selected_units: list[Unit] = selected_units or []
        self.max_units_affected: int = max_units_affected

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
