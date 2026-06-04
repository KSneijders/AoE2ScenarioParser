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


class ChangeObjectCost(Effect):
    """
    This effect can be used to change the cost of a specific type of unit.
    """
    EFFECT_ID: int = 40

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
    """The type of unit to change cost"""

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player for whom the cost will be changed"""

    resource1: PlayerAttribute = RetrieverRef(Effect._resource1)
    """The type of resource for the first cost"""

    resource1_quantity: int = RetrieverRef(Effect._resource1_quantity)
    """The quantity for the first cost"""

    resource2: PlayerAttribute = RetrieverRef(Effect._resource2)
    """The type of resource for the second cost"""

    resource2_quantity: int = RetrieverRef(Effect._resource2_quantity)
    """The quantity for the second cost"""

    resource3: PlayerAttribute = RetrieverRef(Effect._resource3)
    """The type of resource for the third cost"""

    resource3_quantity: int = RetrieverRef(Effect._resource3_quantity)
    """The quantity for the third cost"""

    def __init__(
        self,
        object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = None,
        source_player: Player | None = None,
        resource1: PlayerAttribute | None = None,
        resource1_quantity: int | None = None,
        resource2: PlayerAttribute | None = None,
        resource2_quantity: int | None = None,
        resource3: PlayerAttribute | None = None,
        resource3_quantity: int | None = None,
    ):
        super().__init__()

        self.object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = object_id
        self.source_player: Player | None = source_player
        self.resource1: PlayerAttribute | None = resource1
        self.resource1_quantity: int | None = resource1_quantity
        self.resource2: PlayerAttribute | None = resource2
        self.resource2_quantity: int | None = resource2_quantity
        self.resource3: PlayerAttribute | None = resource3
        self.resource3_quantity: int | None = resource3_quantity

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
