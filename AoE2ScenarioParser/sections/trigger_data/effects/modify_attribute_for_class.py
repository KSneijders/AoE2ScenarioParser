from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.datasets.trigger_data.damage_class import DamageClass
from AoE2ScenarioParser.datasets.trigger_data.object_attribute import ObjectAttribute
from AoE2ScenarioParser.datasets.trigger_data.object_class import ObjectClass
from AoE2ScenarioParser.datasets.trigger_data.object_type import ObjectType
from AoE2ScenarioParser.datasets.trigger_data.operation import Operation
from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ModifyAttributeForClass(Effect):
    """
    This effect can be used to modify a specific object attribute for all units matching the specified class and type, globally for the specified player.
    """
    EFFECT_ID: int = 104

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    object2_group: ObjectClass | int = RetrieverRef(Effect._object2_group)
    """The unit class to be affected by this effect"""

    object2_type: ObjectType | int = RetrieverRef(Effect._object2_type)
    """The type of unit to be affected by this effect"""

    source_player: Player | int = RetrieverRef(Effect._source_player)
    """The player whose units will have their attribute modified"""

    object_attribute: ObjectAttribute | int = RetrieverRef(Effect._object_attribute)
    """The object attribute to modify"""

    message: str = RetrieverRef(ret(Effect._message))
    """The string value to use when the selected object attribute accepts a string (e.g. Object Name ID)"""

    operation: Operation | int = RetrieverRef(Effect._operation)
    """The operation to apply to the attribute using the quantity."""

    quantity: int = RetrieverRef(Effect._quantity)
    """The amount to modify the attribute by"""

    quantity_float: float = RetrieverRef(Effect._quantity_float)
    """The (decimal) amount to modify the attribute by"""

    def __init__(
        self,
        object2_group: ObjectClass | int = -1,
        object2_type: ObjectType | int = -1,
        source_player: Player | int = -1,
        object_attribute: ObjectAttribute | int = -1,
        message: str = '',
        operation: Operation | int = -1,
        quantity: int = -1,
        quantity_float: float = -1.0,
    ):
        super().__init__()

        self.object2_group: ObjectClass | int = object2_group
        self.object2_type: ObjectType | int = object2_type
        self.source_player: Player | int = source_player
        self.object_attribute: ObjectAttribute | int = object_attribute
        self.message: str = message
        self.operation: Operation | int = operation
        self.quantity: int = quantity
        self.quantity_float: float = quantity_float

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
