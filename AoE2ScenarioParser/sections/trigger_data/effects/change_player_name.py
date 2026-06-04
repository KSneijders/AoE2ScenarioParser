from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ChangePlayerName(Effect):
    """
    This effect can be used to change the name displayed for the specified player.
    """
    EFFECT_ID: int = 45

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player whose name will be changed"""

    str_id: int = RetrieverRef(Effect._str_id)
    """The string ID to use as the new player name"""

    message: str = RetrieverRef(ret(Effect._message))
    """The new player name to display"""

    def __init__(
        self,
        source_player: Player | None = None,
        str_id: int | None = None,
        message: str | None = None,
    ):
        super().__init__()

        self.source_player: Player | None = source_player
        self.str_id: int | None = str_id
        self.message: str | None = message

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
