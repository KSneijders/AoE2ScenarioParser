from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.objects.support import Tile, TileT
from AoE2ScenarioParser.sections import Unit
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class PlaySound(Effect):
    """
    This effect can be used to play a sound at a specific location or globally for the specified player.
    """
    EFFECT_ID: int = 4

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player who will hear the sound effect."""

    @property
    def location(self) -> Tile:
        """The tile to play the sound at. When not set, the sound will be played globally."""
        return self._location

    @location.setter
    def location(self, value: TileT) -> None:
        """The tile to play the sound at. When not set, the sound will be played globally."""
        self._location = value

    location_unit_ref: Unit = RetrieverRef(Effect._location_unit_ref)
    """The unit whose position and rotation will be used to play the sound at. When not set, the sound will be played globally."""

    global_sound: bool = RetrieverRef(Effect._global_sound)
    """When enabled, the sound will be played regardless if the target is on screen. This is useful for existing game sounds that are considered '3D'. '3D' sounds are game sounds based on coordinates. '2D' sounds are sounds like GUI, button click or notification sounds."""

    sound_name: str = RetrieverRef(ret(Effect._sound_name))
    """The name of the sound to play."""

    def __init__(
        self,
        source_player: Player | None = None,
        location: Tile | None = None,
        location_unit_ref: Unit | None = None,
        global_sound: bool | None = None,
        sound_name: str | None = None,
    ):
        super().__init__()

        self.source_player: Player | None = source_player
        self.location: Tile | None = location
        self.location_unit_ref: Unit | None = location_unit_ref
        self.global_sound: bool | None = global_sound
        self.sound_name: str | None = sound_name

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
