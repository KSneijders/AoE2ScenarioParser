from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ResearchTechnology(Effect):
    """
    This effect can be used to automatically research a technology for the specified player.
    """
    EFFECT_ID: int = 2

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    source_player: Player | int = RetrieverRef(Effect._source_player)
    """The player for whom the technology will be researched."""

    technology_id: TechInfo | int = RetrieverRef(Effect._technology_id)
    """The technology which will be researched for the specified player."""

    force_technology: bool = RetrieverRef(Effect._force_technology)
    """When enabled, force the selected technology to be researched, regardless if the civilization has access to it or not."""

    def __init__(
        self,
        source_player: Player | int = -1,
        technology_id: TechInfo | int = -1,
        force_technology: bool = False,
    ):
        super().__init__()

        self.source_player: Player | int = source_player
        self.technology_id: TechInfo | int = technology_id
        self.force_technology: bool = force_technology

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
