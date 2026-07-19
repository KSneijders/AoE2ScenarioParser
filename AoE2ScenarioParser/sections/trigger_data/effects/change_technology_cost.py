from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.datasets.trigger_data.player_attribute import PlayerAttribute
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ChangeTechnologyCost(Effect):
    """
    This effect can be used to change the cost of a specific technology.
    """
    EFFECT_ID: int = 63

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    source_player: Player | int = RetrieverRef(Effect._source_player)
    """The player for whom the cost will be changed"""

    technology_id: TechInfo | int = RetrieverRef(Effect._technology_id)
    """The technology to change cost"""

    resource1: PlayerAttribute | int = RetrieverRef(Effect._resource1)
    """The type of resource for the first cost"""

    resource1_quantity: int = RetrieverRef(Effect._resource1_quantity)
    """The quantity for the first cost"""

    resource2: PlayerAttribute | int = RetrieverRef(Effect._resource2)
    """The type of resource for the second cost"""

    resource2_quantity: int = RetrieverRef(Effect._resource2_quantity)
    """The quantity for the second cost"""

    resource3: PlayerAttribute | int = RetrieverRef(Effect._resource3)
    """The type of resource for the third cost"""

    resource3_quantity: int = RetrieverRef(Effect._resource3_quantity)
    """The quantity for the third cost"""

    def __init__(
        self,
        source_player: Player | int = -1,
        technology_id: TechInfo | int = -1,
        resource1: PlayerAttribute | int = -1,
        resource1_quantity: int = -1,
        resource2: PlayerAttribute | int = -1,
        resource2_quantity: int = -1,
        resource3: PlayerAttribute | int = -1,
        resource3_quantity: int = -1,
    ):
        super().__init__()

        self.source_player: Player | int = source_player
        self.technology_id: TechInfo | int = technology_id
        self.resource1: PlayerAttribute | int = resource1
        self.resource1_quantity: int = resource1_quantity
        self.resource2: PlayerAttribute | int = resource2
        self.resource2_quantity: int = resource2_quantity
        self.resource3: PlayerAttribute | int = resource3
        self.resource3_quantity: int = resource3_quantity

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
