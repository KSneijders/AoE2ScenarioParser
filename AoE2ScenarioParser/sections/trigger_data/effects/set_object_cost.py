from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.datasets.trigger_data.player_attribute import PlayerAttribute
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class SetObjectCost(Effect):
    """
    This effect can be used to set the cost for a specific type of unit.
    """
    EFFECT_ID: int = 80

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
    """The type of unit to set cost"""

    source_player: Player | int = RetrieverRef(Effect._source_player)
    """The player for whom the cost will be set"""

    quantity: int = RetrieverRef(Effect._quantity)
    """The amount to set as the cost"""

    resource: PlayerAttribute | int = RetrieverRef(Effect._resource)
    """The type of resource for the cost"""

    def __init__(
        self,
        object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = -1,
        source_player: Player | int = -1,
        quantity: int = -1,
        resource: PlayerAttribute | int = -1,
    ):
        super().__init__()

        self.object_id: BuildingInfo | HeroInfo | OtherInfo | UnitInfo | int = object_id
        self.source_player: Player | int = source_player
        self.quantity: int = quantity
        self.resource: PlayerAttribute | int = resource

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
