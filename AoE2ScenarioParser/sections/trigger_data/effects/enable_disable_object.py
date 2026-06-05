from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class EnableDisableObject(Effect):
    """
    This effect can be used to enable or disable units.
    """
    EFFECT_ID: int = 38

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
    """The unit to enable or disable"""

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player for whom the unit will be enabled or disabled"""

    enabled: bool = RetrieverRef(Effect._enabled)
    """When enabled, the unit is available. When disabled, the unit is not available"""

    def __init__(
        self,
        object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = None,
        source_player: Player | None = None,
        enabled: bool | None = None,
    ):
        super().__init__()

        self.object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = object_id
        self.source_player: Player | None = source_player
        self.enabled: bool | None = enabled

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
