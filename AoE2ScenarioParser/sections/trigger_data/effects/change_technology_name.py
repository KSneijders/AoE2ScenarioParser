from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ChangeTechnologyName(Effect):
    """
    This effect can be used to change the display name of a specific technology for the specified player.
    """
    EFFECT_ID: int = 65

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player for whom the technology name will be changed"""

    technology_id: TechInfo = RetrieverRef(Effect._technology_id)
    """The technology whose name will be changed"""

    str_id: int = RetrieverRef(Effect._str_id)
    """The string ID to use as the new technology name"""

    message: str = RetrieverRef(ret(Effect._message))
    """The new name to display for the technology"""

    def __init__(
        self,
        source_player: Player | None = None,
        technology_id: TechInfo | None = None,
        str_id: int | None = None,
        message: str | None = None,
    ):
        super().__init__()

        self.source_player: Player | None = source_player
        self.technology_id: TechInfo | None = technology_id
        self.str_id: int | None = str_id
        self.message: str | None = message

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
