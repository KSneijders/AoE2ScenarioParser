from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class EnableDisableTechnology(Effect):
    """
    This effect can be used to enable or disable technologies.
    """
    EFFECT_ID: int = 39

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player for whom the technology will be enabled or disabled"""

    technology_id: TechInfo = RetrieverRef(Effect._technology_id)
    """The technology to enable or disable"""

    enabled: bool = RetrieverRef(Effect._enabled)
    """When enabled, the technology is available. When disabled, the technology is not available"""

    def __init__(
        self,
        source_player: Player | None = None,
        technology_id: TechInfo | None = None,
        enabled: bool | None = None,
    ):
        super().__init__()

        self.source_player: Player | None = source_player
        self.technology_id: TechInfo | None = technology_id
        self.enabled: bool | None = enabled

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
