from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ChangeTechnologyHotkey(Effect):
    """
    This effect can be used to change the hotkey of a specific technology.
    """
    EFFECT_ID: int = 85

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    technology_id: TechInfo = RetrieverRef(Effect._technology_id)
    """The technology whose hotkey will be changed"""

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player for whom the technology hotkey will be changed"""

    quantity: int = RetrieverRef(Effect._quantity)
    """The hotkey ID to assign to the technology"""

    def __init__(
        self,
        technology_id: TechInfo | None = None,
        source_player: Player | None = None,
        quantity: int | None = None,
    ):
        super().__init__()

        self.technology_id: TechInfo | None = technology_id
        self.source_player: Player | None = source_player
        self.quantity: int | None = quantity

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
