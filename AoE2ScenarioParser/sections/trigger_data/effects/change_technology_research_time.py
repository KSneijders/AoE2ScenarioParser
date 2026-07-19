from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ChangeTechnologyResearchTime(Effect):
    """
    This effect can be used to change the research time of a specific technology.
    """
    EFFECT_ID: int = 64

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    quantity: int = RetrieverRef(Effect._quantity)
    """The new research time to set"""

    source_player: Player | int = RetrieverRef(Effect._source_player)
    """The player for whom the research time will be changed"""

    technology_id: TechInfo | int = RetrieverRef(Effect._technology_id)
    """The technology whose research time will be changed"""

    def __init__(
        self,
        quantity: int = -1,
        source_player: Player | int = -1,
        technology_id: TechInfo | int = -1,
    ):
        super().__init__()

        self.quantity: int = quantity
        self.source_player: Player | int = source_player
        self.technology_id: TechInfo | int = technology_id

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
