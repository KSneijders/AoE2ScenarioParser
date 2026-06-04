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


class ModifyAttributeByVariable(Effect):
    """
    This effect can be used to modify an object attribute for a type of unit belonging to the specified player using the value stored in a variable.
    """
    EFFECT_ID: int = 79

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
    """The type of unit whose attribute will be modified"""

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player whose units will have their attribute modified"""

    operation: Operation = RetrieverRef(Effect._operation)
    """The operation to apply to the attribute using the variable."""

    object_attribute: ObjectAttribute = RetrieverRef(Effect._object_attribute)
    """The unit attribute to modify using the variable"""

    variable1_id: Variable | int = RetrieverRef(Effect._variable1_id)
    """The variable whose value will be used to modify the attribute"""

    message: str = RetrieverRef(ret(Effect._message))
    """The string value to use when the selected object attribute accepts a string (e.g. Object Name ID)"""

    armour_attack_class: DamageClass = RetrieverRef(Effect._armour_attack_class)
    """The armor or attack class to modify"""

    def __init__(
        self,
        object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = None,
        source_player: Player | None = None,
        operation: Operation | None = None,
        object_attribute: ObjectAttribute | None = None,
        variable1_id: Variable | int | None = None,
        message: str | None = None,
        armour_attack_class: DamageClass | None = None,
    ):
        super().__init__()

        self.object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = object_id
        self.source_player: Player | None = source_player
        self.operation: Operation | None = operation
        self.object_attribute: ObjectAttribute | None = object_attribute
        self.variable1_id: Variable | int | None = variable1_id
        self.message: str | None = message
        self.armour_attack_class: DamageClass | None = armour_attack_class

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
