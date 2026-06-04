from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.objects.support import Tile, TileT
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class PlaceFoundation(Effect):
    """
    This effect can be used to place a building foundation for the specified player at the specified location.
    """
    EFFECT_ID: int = 25

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
    """The building foundation to place"""

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player for whom the foundation will be placed"""

    @property
    def location(self) -> Tile:
        """The tile where the building foundation will be placed"""
        return self._location

    @location.setter
    def location(self, value: TileT) -> None:
        """The tile where the building foundation will be placed"""
        self._location = value

    def __init__(
        self,
        object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = None,
        source_player: Player | None = None,
        location: Tile | None = None,
    ):
        super().__init__()

        self.object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = object_id
        self.source_player: Player | None = source_player
        self.location: Tile | None = location

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
