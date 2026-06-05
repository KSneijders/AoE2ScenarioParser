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

    object2_group: ObjectClass = RetrieverRef(Effect._object2_group)
    """The unit class to be affected by this effect"""

    object2_type: ObjectType = RetrieverRef(Effect._object2_type)
    """The type of unit to be affected by this effect"""

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player whose units will have their attribute modified"""

    object_attribute: ObjectAttribute = RetrieverRef(Effect._object_attribute)
    """The object attribute to modify"""

    message: str = RetrieverRef(ret(Effect._message))
    """The string value to use when the selected object attribute accepts a string (e.g. Object Name ID)"""

    operation: Operation = RetrieverRef(Effect._operation)
    """The operation to apply to the attribute using the quantity."""

    quantity: int = RetrieverRef(Effect._quantity)
    """The amount to modify the attribute by"""

    quantity_float: float = RetrieverRef(Effect._quantity_float)
    """The (decimal) amount to modify the attribute by"""

    def __init__(
        self,
        object2_group: ObjectClass | None = None,
        object2_type: ObjectType | None = None,
        source_player: Player | None = None,
        object_attribute: ObjectAttribute | None = None,
        message: str | None = None,
        operation: Operation | None = None,
        quantity: int | None = None,
        quantity_float: float | None = None,
    ):
        super().__init__()

        self.object2_group: ObjectClass | None = object2_group
        self.object2_type: ObjectType | None = object2_type
        self.source_player: Player | None = source_player
        self.object_attribute: ObjectAttribute | None = object_attribute
        self.message: str | None = message
        self.operation: Operation | None = operation
        self.quantity: int | None = quantity
        self.quantity_float: float | None = quantity_float

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
