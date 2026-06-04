from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.objects.support import Tile, TileT
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ChangeView(Effect):
    """
    This effect can be used to move the camera view for the specified player to a specific tile.
    """
    EFFECT_ID: int = 16

    quantity: int = RetrieverRef(Effect._quantity)
    """The time in seconds it takes to scroll to the new camera position"""

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player whose camera view will be moved"""

    @property
    def location(self) -> Tile:
        """The tile to move the camera to"""
        return self._location

    @location.setter
    def location(self, value: TileT) -> None:
        """The tile to move the camera to"""
        self._location = value

    scroll: bool = RetrieverRef(Effect._scroll)
    """When enabled, animate the camera transition. When disabled, the camera snaps to the new position without any animation (ignoring the quantity)"""

    def __init__(
        self,
        quantity: int | None = None,
        source_player: Player | None = None,
        location: Tile | None = None,
        scroll: bool | None = None,
    ):
        super().__init__()

        self.quantity: int | None = quantity
        self.source_player: Player | None = source_player
        self.location: Tile | None = location
        self.scroll: bool | None = scroll

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
