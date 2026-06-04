from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class DeclareVictory(Effect):
    """
    This effect can be used to declare victory or defeat for the specified player.
    """
    EFFECT_ID: int = 13

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player for whom victory or defeat will be declared"""

    enabled: bool = RetrieverRef(Effect._enabled)
    """When enabled, victory is declared for the player. When disabled, defeat is declared"""

    def __init__(
        self,
        source_player: Player | None = None,
        enabled: bool | None = None,
    ):
        super().__init__()

        self.source_player: Player | None = source_player
        self.enabled: bool | None = enabled

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
