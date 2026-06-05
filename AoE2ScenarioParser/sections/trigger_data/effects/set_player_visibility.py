from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.datasets.trigger_data.visibility_state import VisibilityState
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class SetPlayerVisibility(Effect):
    """
    This effect can be used to change the visibility relationship between two players, controlling what the source player can see of the target player.
    """
    EFFECT_ID: int = 41

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player for whom the visibility will be changed."""

    target_player: Player = RetrieverRef(Effect._target_player)
    """The target player whose visibility will be changed for the source player."""

    visibility_state: VisibilityState = RetrieverRef(Effect._visibility_state)
    """The visibility state to use"""

    def __init__(
        self,
        source_player: Player | None = None,
        target_player: Player | None = None,
        visibility_state: VisibilityState | None = None,
    ):
        super().__init__()

        self.source_player: Player | None = source_player
        self.target_player: Player | None = target_player
        self.visibility_state: VisibilityState | None = visibility_state

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
