from __future__ import annotations

from bfp_rs import ret, RetrieverRef

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


class ChangeObjectDescription(Effect):
    """
    This effect can be used to change the description of a specific type of unit for the specified player.
    """
    EFFECT_ID: int = 44

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
    """The type of unit whose description will be changed"""

    source_player: Player | int = RetrieverRef(Effect._source_player)
    """The player for whom the unit description will be changed"""

    str_id: int = RetrieverRef(Effect._str_id)
    """The string ID to use as the new description for the type of unit"""

    message: str = RetrieverRef(ret(Effect._message))
    """The new description for the type of unit"""

    def __init__(
        self,
        object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = -1,
        source_player: Player | int = -1,
        str_id: int = -1,
        message: str = '',
    ):
        super().__init__()

        self.object_id: BuildingInfo | HeroInfo | OtherInfo | UnitInfo | int = object_id
        self.source_player: Player | int = source_player
        self.str_id: int = str_id
        self.message: str = message

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
