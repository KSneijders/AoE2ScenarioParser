from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.datasets.trigger_data.diplomacy_stance import DiplomacyStance
from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ChangeDiplomacy(Effect):
    """
    This effect can be used to change the diplomacy stance of the source players with the target player.
    It does NOT change the stance both ways.
    """
    EFFECT_ID: int = 1

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    diplomacy_state: DiplomacyStance = RetrieverRef(Effect._diplomacy_state)
    """The diplomacy stance to set."""

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player for whom the stance will be changed."""

    target_player: Player = RetrieverRef(Effect._target_player)
    """The target player whose diplomacy stance will be changed for the source player."""

    def __init__(
        self,
        diplomacy_state: DiplomacyStance | None = None,
        source_player: Player | None = None,
        target_player: Player | None = None,
    ):
        super().__init__()

        self.diplomacy_state: DiplomacyStance | None = diplomacy_state
        self.source_player: Player | None = source_player
        self.target_player: Player | None = target_player

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
