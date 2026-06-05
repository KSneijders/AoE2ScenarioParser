from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class SendChat(Effect):
    """
    This effect can be used to send a chat message to the specified player.
    """
    EFFECT_ID: int = 3

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player who will be receiving the message."""

    str_id: int = RetrieverRef(Effect._str_id)
    """The string ID to use instead of the message."""

    message: str = RetrieverRef(ret(Effect._message))
    """The message to send to the player."""

    sound_name: str = RetrieverRef(ret(Effect._sound_name))
    """The name of the sound to play when the message is sent."""

    def __init__(
        self,
        source_player: Player | None = None,
        str_id: int | None = None,
        message: str | None = None,
        sound_name: str | None = None,
    ):
        super().__init__()

        self.source_player: Player | None = source_player
        self.str_id: int | None = str_id
        self.message: str | None = message
        self.sound_name: str | None = sound_name

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
