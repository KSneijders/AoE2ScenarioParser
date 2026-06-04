from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.datasets.player_data.player_color import PlayerColor
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ChangePlayerColor(Effect):
    """
    This effect can be used to change the color associated with the specified player, affecting all units and buildings.
    """
    EFFECT_ID: int = 89

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player whose color will be changed"""

    player_color: PlayerColor = RetrieverRef(Effect._player_color)
    """The player color to use"""

    def __init__(
        self,
        source_player: Player | None = None,
        player_color: PlayerColor | None = None,
    ):
        super().__init__()

        self.source_player: Player | None = source_player
        self.player_color: PlayerColor | None = player_color

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
