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
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ModifyAttribute(Effect):
    """
    This effect can be used to modify an object attribute for a type of unit belonging to the specified player.
    """
    EFFECT_ID: int = 51

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    quantity: int = RetrieverRef(Effect._quantity)
    """The amount to modify the attribute by"""

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
    """The type of unit whose attribute will be modified"""

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player whose units will have their attribute modified"""

    operation: Operation = RetrieverRef(Effect._operation)
    """The operation to apply to the attribute using the quantity."""

    object_attribute: ObjectAttribute = RetrieverRef(Effect._object_attribute)
    """The unit attribute to modify"""

    message: str = RetrieverRef(ret(Effect._message))
    """The string value to use when the selected object attribute accepts a string (e.g. Object Name ID)"""

    quantity_float: float = RetrieverRef(Effect._quantity_float)
    """The (decimal) amount to modify the attribute by"""

    def __init__(
        self,
        quantity: int | None = None,
        object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = None,
        source_player: Player | None = None,
        operation: Operation | None = None,
        object_attribute: ObjectAttribute | None = None,
        message: str | None = None,
        quantity_float: float | None = None,
    ):
        super().__init__()

        self.quantity: int | None = quantity
        self.object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = object_id
        self.source_player: Player | None = source_player
        self.operation: Operation | None = operation
        self.object_attribute: ObjectAttribute | None = object_attribute
        self.message: str | None = message
        self.quantity_float: float | None = quantity_float

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
