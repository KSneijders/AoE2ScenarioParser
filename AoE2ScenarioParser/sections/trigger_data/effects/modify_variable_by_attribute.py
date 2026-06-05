from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.trigger_data.damage_class import DamageClass
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.trigger_data.object_attribute import ObjectAttribute
from AoE2ScenarioParser.datasets.trigger_data.operation import Operation
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.sections import Variable
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ModifyVariableByAttribute(Effect):
    """
    This effect can be used to modify a variable using the value of a specific unit attribute.
    """
    EFFECT_ID: int = 87

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
    """The type of unit to read the attribute value from"""

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player whose unit's attribute value will be used"""

    operation: Operation = RetrieverRef(Effect._operation)
    """The operation to apply to the variable using the attribute's value."""

    object_attribute: ObjectAttribute = RetrieverRef(Effect._object_attribute)
    """The unit attribute whose value will be used to modify the variable"""

    variable1_id: Variable = RetrieverRef(Effect._variable1_id)
    """The variable that will be modified"""

    message: str = RetrieverRef(ret(Effect._message))
    """Unused - ThxDE"""

    def __init__(
        self,
        object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = None,
        source_player: Player | None = None,
        operation: Operation | None = None,
        object_attribute: ObjectAttribute | None = None,
        variable1_id: Variable | None = None,
        message: str | None = None,
    ):
        super().__init__()

        self.object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = object_id
        self.source_player: Player | None = source_player
        self.operation: Operation | None = operation
        self.object_attribute: ObjectAttribute | None = object_attribute
        self.variable1_id: Variable | None = variable1_id
        self.message: str | None = message

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
