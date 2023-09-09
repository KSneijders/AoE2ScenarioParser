from binary_file_parser.retrievers import RetrieverRef

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.objects.data_objects.effects.effect import Effect
from AoE2ScenarioParser.objects.support import Tile, TileT
from AoE2ScenarioParser.sections.bfp.triggers import EffectStruct


class PlaySound(Effect):
    source_player: Player = RetrieverRef(EffectStruct._source_player)  # type: ignore
    """The player to play the sound for"""
    sound_name: str = RetrieverRef(EffectStruct._sound_name)  # type: ignore
    """The name of the sound file to play. The wem extension is not required"""
    location: Tile = RetrieverRef(EffectStruct._location)  # type: ignore
    """The location to play the sound at. If left empty, plays globally"""

    # @overload
    # def __init__(self, source_player: Player, sound_name: str): ...

    # @overload
    # def __init__(self, source_player: Player, sound_name: str, location: TileT): ...

    def __init__(
        self,
        source_player: Player,
        sound_name: str,
        location: TileT = Tile(-1, -1),
        **kwargs,
    ):
        """
        Play a sound for the source_player

        Args:
            source_player: The player to play the sound for
            sound_name: The name of the sound file to play. The wem extension is not required
            location: The location to play the sound at. If left empty, plays globally
        """
        if location:
            location = Tile.from_value(location)

        super().__init__(local_vars = locals(), **kwargs)
