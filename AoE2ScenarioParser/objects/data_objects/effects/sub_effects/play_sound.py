from typing import overload

from binary_file_parser.retrievers import RetrieverRef

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.datasets.triggers import EffectType
from AoE2ScenarioParser.objects.data_objects.effects.effect import Effect
from AoE2ScenarioParser.objects.support import Tile
from AoE2ScenarioParser.sections.bfp.triggers import EffectStruct


class PlaySound(Effect):
    source_player: Player = RetrieverRef(EffectStruct._source_player)
    """The player to play the sound for"""
    sound_name: str = RetrieverRef(EffectStruct._sound_name)
    """The name of the sound file to play. The wem extension is not required"""
    location_x: int = RetrieverRef(EffectStruct._location_x)
    """The location to play the sound at"""
    location_y: int = RetrieverRef(EffectStruct._location_y)
    """The location to play the sound at"""

    @overload
    def __init__(self, source_player: Player, sound_name: str): ...
    @overload
    def __init__(self, source_player: Player, sound_name: str, location: Tile): ...

    def __init__(
        self,
        source_player: Player,
        sound_name: str,
        location: Tile = Tile(-1, -1),
        **kwargs,
    ):
        """
        Play a sound for the source_player

        Args:
            source_player: The player to play the sound for
            sound_name: The name of the sound file to play. The wem extension is not required
            location: The location to play the sound at
        """

        (
            kwargs['_location_x'],
            kwargs['_location_y']
        ) = Tile
        # Todo: How to deal with Tile(x, y) to _location_x _location_y attributes for Effects etc?

        kwargs["type"] = EffectType.PLAY_SOUND
        super().__init__(local_vars=locals(), **kwargs)
