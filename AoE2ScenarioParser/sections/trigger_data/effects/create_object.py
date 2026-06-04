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


class CreateObject(Effect):
    """
    This effect can be used to create a unit (including buildings, heroes etc.) for the specified player
    """
    EFFECT_ID: int = 11

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
    """The type of unit to be created."""

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player whose unit will be created"""

    @property
    def location(self) -> Tile:
        """The tile where the unit will be created"""
        return self._location

    @location.setter
    def location(self, value: TileT) -> None:
        """The tile where the unit will be created"""
        self._location = value

    facet: int = RetrieverRef(Effect._facet)
    """The rotation of the created unit. This can be any integer between 0 and 15, with 0 looking towards the right of the screen and 8 looking towards the left of the screen. With increasing values moving counter clockwise."""

    disable_sound: bool = RetrieverRef(Effect._disable_sound)
    """When enabled, disable the creation sound of the object"""

    def __init__(
        self,
        object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = None,
        source_player: Player | None = None,
        location: Tile | None = None,
        facet: int | None = None,
        disable_sound: bool | None = None,
    ):
        super().__init__()

        self.object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = object_id
        self.source_player: Player | None = source_player
        self.location: Tile | None = location
        self.facet: int | None = facet
        self.disable_sound: bool | None = disable_sound

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
