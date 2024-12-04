from binary_file_parser.retrievers import RetrieverRef

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.datasets.triggers import EffectType
from AoE2ScenarioParser.sections.bfp.triggers import EffectStruct

from AoE2ScenarioParser.objects.data_objects.effects.effect import Effect


class SendChat(Effect):
    _type_ = EffectType.SEND_CHAT

    source_player: Player = RetrieverRef(EffectStruct._source_player)  # type: ignore
    """The player to send the message to"""
    message: str = RetrieverRef(EffectStruct._message)  # type: ignore
    """The message to send. If left empty, a message sound is still produced"""
    string_id: int = RetrieverRef(EffectStruct._string_id)  # type: ignore
    """The string ID of the message. Using this will override the message text"""
    sound_name: str = RetrieverRef(EffectStruct._sound_name)  # type: ignore
    """The name of the sound to play with the message"""

    # @overload
    # def __init__(self, source_player: Player, message: str): ...

    # @overload
    # def __init__(self, source_player: Player, message: str, sound_name: str): ...

    # @overload
    # def __init__(self, source_player: Player, string_id: int): ...

    # @overload
    # def __init__(self, source_player: Player, string_id: int, sound_name: str): ...

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
            message: The message to send. If left empty, a message sound is still produced
            string_id: The string ID of the message. Using this will override the message text
            sound_name: The name of the sound to play with the message
        """
        super().__init__(local_vars = locals(), **kwargs)