from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ChangeTechnologyDescription(Effect):
    """
    This effect can be used to change the description of a specific technology for the specified player.
    """
    EFFECT_ID: int = 66

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    source_player: Player | int = RetrieverRef(Effect._source_player)
    """The player for whom the technology description will be changed"""

    technology_id: TechInfo | int = RetrieverRef(Effect._technology_id)
    """The technology whose description will be changed"""

    str_id: int = RetrieverRef(Effect._str_id)
    """The string ID to use as the new technology description"""

    message: str = RetrieverRef(ret(Effect._message))
    """The new description for the technology"""

    def __init__(
        self,
        source_player: Player | int = -1,
        technology_id: TechInfo | int = -1,
        str_id: int = -1,
        message: str = '',
    ):
        super().__init__()

        self.source_player: Player | int = source_player
        self.technology_id: TechInfo | int = technology_id
        self.str_id: int = str_id
        self.message: str = message

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
