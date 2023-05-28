from binary_file_parser.retrievers import RetrieverRef

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.datasets.triggers import EffectType
from AoE2ScenarioParser.objects.data_objects.effects.effect import Effect
from AoE2ScenarioParser.sections.bfp.triggers import EffectStruct


class SendChat(Effect):
    source_player = RetrieverRef(EffectStruct._source_player)
    message = RetrieverRef(EffectStruct._message)
    string_id = RetrieverRef(EffectStruct._string_id)
    sound_name = RetrieverRef(EffectStruct._sound_name)

    def __init__(
        self,
        source_player: Player,
        message: str = '',
        string_id: int = -1,
        sound_name: str = '',
        **kwargs,
    ):
        """
        Send a chat message to the source_player

        Args:
            source_player: The player to send the message to
            message: The message to send
            string_id: The string ID of the message
            sound_name: The name of the sound to play with the message
        """
        # Todo: Verify if 'message' can actually be left blank
        # Todo: If 'message' can be left blank, raise an exception (ValueError for invalid effect)
        super().__init__(type=EffectType.SEND_CHAT, local_vars=locals(), **kwargs)
