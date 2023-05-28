from binary_file_parser.retrievers import RetrieverRef

from AoE2ScenarioParser.datasets.triggers import EffectType
from AoE2ScenarioParser.objects.data_objects.effects.effect import Effect
from AoE2ScenarioParser.objects.support import Tile
from AoE2ScenarioParser.sections.bfp.triggers import EffectStruct


class PlaySound(Effect):
    source_player = RetrieverRef(EffectStruct._source_player)
    location_x = RetrieverRef(EffectStruct._location_x)
    location_y = RetrieverRef(EffectStruct._location_y)
    location_object_reference = RetrieverRef(EffectStruct._location_object_reference)
    sound_name = RetrieverRef(EffectStruct._sound_name)

    def __init__(
        self,
        source_player,
        tile: Tile,
        location_object_reference,
        sound_name,
        **kwargs,
    ):
        """
        Play a sound for the source_player

        Args:
            source_player: The player to play the sound for
            tile: The location where to play the sound
            location_object_reference: The location where to play the sound based on a unit on the map
            sound_name: The name of the sound to play
        """
        # Todo: Verify location_object_reference is actually an option and how it works
        # Todo: Potentially raise ValueError if both or neither tile & location_object_reference is used

        (
            kwargs['_location_x'],
            kwargs['_location_y']
        ) = Tile
        # Todo: How to deal with Tile(x, y) to _location_x _location_y attributes for Effects etc?

        super().__init__(type=EffectType.SEND_CHAT, local_vars=locals(), **kwargs)
