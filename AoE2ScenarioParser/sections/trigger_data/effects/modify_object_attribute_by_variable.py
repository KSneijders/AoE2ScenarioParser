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
from AoE2ScenarioParser.sections import Variable
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ModifyObjectAttributeByVariable(Effect):
    """
    This effect can be used to modify a specific attribute of units using a variable.
    """
    EFFECT_ID: int = 106

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
    """The type of unit to modify the attribute for"""

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player whose units will have their attribute modified"""

    object_attribute: ObjectAttribute = RetrieverRef(Effect._object_attribute)
    """The object attribute to modify using the variable"""

    selected_unit_ref_ids: list[Unit] = RetrieverRef(ret(Effect._selected_unit_ref_ids))
    """The units to be affected by this effect. When defined, overwrites all other unit filters, like area selection, type of unit, object type etc."""

    @property
    def area(self) -> Area:
        """The area in which units will have their attribute modified. When not set, units across the entire map have their attribute modified"""
        return self._area

    @area.setter
    def area(self, value: AreaT) -> None:
        """The area in which units will have their attribute modified. When not set, units across the entire map have their attribute modified"""
        self._area = value

    operation: Operation = RetrieverRef(Effect._operation)
    """The operation to apply to the attribute using the quantity."""

    message: str = RetrieverRef(ret(Effect._message))
    """The string value to use when the selected object attribute accepts a string (e.g. Object Name ID)"""

    variable1_id: Variable = RetrieverRef(Effect._variable1_id)
    """The variable whose value will be used to modify the attribute"""

    def __init__(
        self,
        object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = None,
        source_player: Player | None = None,
        object_attribute: ObjectAttribute | None = None,
        selected_unit_ref_ids: list[Unit] | None = None,
        area: Area | None = None,
        operation: Operation | None = None,
        message: str | None = None,
        variable1_id: Variable | None = None,
    ):
        super().__init__()

        self.object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = object_id
        self.source_player: Player | None = source_player
        self.object_attribute: ObjectAttribute | None = object_attribute
        self.selected_unit_ref_ids: list[Unit] | None = selected_unit_ref_ids
        self.area: Area | None = area
        self.operation: Operation | None = operation
        self.message: str | None = message
        self.variable1_id: Variable | None = variable1_id

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
