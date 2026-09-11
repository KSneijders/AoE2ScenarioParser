from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.objects.support import Area, AreaT
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.trigger_data.damage_class import DamageClass
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.trigger_data.object_attribute import ObjectAttribute
from AoE2ScenarioParser.datasets.trigger_data.operation import Operation
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.sections import Unit
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ModifyObjectAttribute(Effect):
    """
    This effect can be used to modify a specific attribute of units.
    """
    EFFECT_ID: int = 105

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
    """The type of unit to modify the attribute for"""

    source_player: Player | int = RetrieverRef(Effect._source_player)
    """The player whose units will have their attribute modified"""

    object_attribute: ObjectAttribute | int = RetrieverRef(Effect._object_attribute)
    """The object attribute to modify"""

    selected_unit_ref_ids: list[Unit] | None = RetrieverRef(ret(Effect._selected_unit_ref_ids))
    """The units to be affected by this effect. When defined, overwrites all other unit filters, like area selection, type of unit, object type etc."""

    @property
    def area(self) -> Area:
        """The area in which units will have their attribute modified. When not set, units across the entire map have their attribute modified"""
        return self._area

    @area.setter
    def area(self, value: AreaT) -> None:
        """The area in which units will have their attribute modified. When not set, units across the entire map have their attribute modified"""
        self._area = Area.from_value(value)

    operation: Operation | int = RetrieverRef(Effect._operation)
    """The operation to apply to the attribute using the quantity."""

    message: str = RetrieverRef(ret(Effect._message))
    """The string value to use when the selected object attribute accepts a string (e.g. Object Name ID)"""

    quantity: int = RetrieverRef(Effect._quantity)
    """The amount to modify the attribute by"""

    quantity_float: float = RetrieverRef(Effect._quantity_float)
    """The (decimal) amount to modify the attribute by"""

    def __init__(
        self,
        object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = -1,
        source_player: Player | int = -1,
        object_attribute: ObjectAttribute | int = -1,
        selected_unit_ref_ids: list[Unit] | None = None,
        area: AreaT | None = None,
        operation: Operation | int = -1,
        message: str = '',
        quantity: int = -1,
        quantity_float: float = -1.0,
    ):
        super().__init__()

        self.object_id: BuildingInfo | HeroInfo | OtherInfo | UnitInfo | int = object_id
        self.source_player: Player | int = source_player
        self.object_attribute: ObjectAttribute | int = object_attribute
        self.selected_unit_ref_ids: list[Unit] = selected_unit_ref_ids or []
        self.area: AreaT = area or Area((-1, -1), (-1, -1))
        self.operation: Operation | int = operation
        self.message: str = message
        self.quantity: int = quantity
        self.quantity_float: float = quantity_float

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
