from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.datasets.trigger_data.player_attribute import PlayerAttribute
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class Tribute(Effect):
    """
    This effect can be used to send resources from one player to another.
    """
    EFFECT_ID: int = 5

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    quantity: int = RetrieverRef(Effect._quantity)
    """The amount of the specified resource to send."""

    resource: PlayerAttribute = RetrieverRef(Effect._resource)
    """The resource that will be sent."""

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player who will be sending the resources."""

    target_player: Player = RetrieverRef(Effect._target_player)
    """The player who will receive the resources."""

    def __init__(
        self,
        quantity: int | None = None,
        resource: PlayerAttribute | None = None,
        source_player: Player | None = None,
        target_player: Player | None = None,
    ):
        super().__init__()

        self.quantity: int | None = quantity
        self.resource: PlayerAttribute | None = resource
        self.source_player: Player | None = source_player
        self.target_player: Player | None = target_player

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
