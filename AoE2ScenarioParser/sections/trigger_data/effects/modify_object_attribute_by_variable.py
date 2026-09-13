from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.sections.trigger_data import Effect
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.datasets.trigger_data import ObjectAttribute, Operation, DamageClass
from AoE2ScenarioParser.sections import Unit, Variable
from AoE2ScenarioParser.sections.trigger_data.concerns import HasSelectedUnitsAttribute
from AoE2ScenarioParser.concerns import CanHoldUnits
from AoE2ScenarioParser.objects.support import Area, AreaT

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ModifyObjectAttributeByVariable(Effect, HasSelectedUnitsAttribute, CanHoldUnits):
    """
    This effect can be used to modify a specific attribute of units using a variable.
    """
    EFFECT_ID: int = 106

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
    """The type of unit to modify the attribute for"""

    source_player: Player | int = RetrieverRef(Effect._source_player)
    """The player whose units will have their attribute modified"""

    object_attribute: ObjectAttribute | int = RetrieverRef(Effect._object_attribute)
    """The object attribute to modify using the variable"""

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

    variable1_id: Variable | int = RetrieverRef(Effect._variable1_id)
    """The variable whose value will be used to modify the attribute"""

    def __init__(
        self,
        object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = -1,
        source_player: Player | int = -1,
        object_attribute: ObjectAttribute | int = -1,
        selected_units: list[Unit] | None = None,
        area: AreaT | None = None,
        operation: Operation | int = -1,
        message: str = '',
        variable1_id: Variable | int = -1,
    ):
        super().__init__()

        self.object_id: BuildingInfo | HeroInfo | OtherInfo | UnitInfo | int = object_id
        self.source_player: Player | int = source_player
        self.object_attribute: ObjectAttribute | int = object_attribute
        self._selected_unit_ref_ids: list[int] = []
        self._selected_units: tuple[Unit, ...] = ()
        self.selected_units: list[Unit] = selected_units or []
        self.area: AreaT = area or Area((-1, -1), (-1, -1))
        self.operation: Operation | int = operation
        self.message: str = message
        self.variable1_id: Variable | int = variable1_id

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
