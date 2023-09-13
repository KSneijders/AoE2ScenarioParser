from binary_file_parser.retrievers import RetrieverRef

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.datasets.triggers import EffectType
from AoE2ScenarioParser.objects.support import Tile
from AoE2ScenarioParser.sections.bfp.triggers import EffectStruct

from AoE2ScenarioParser.objects.data_objects.effects.effect import Effect

class ChangeView(Effect):
    _type_ = EffectType.CHANGE_VIEW

    source_player: Player = RetrieverRef(EffectStruct._source_player)  # type:ignore
    """The player to be affected by the effect"""
    location: Tile = RetrieverRef(EffectStruct._location)  # type:ignore
    """The location to scroll to"""
    scroll: bool = RetrieverRef(EffectStruct._scroll)  # type:ignore
    """If the view change should scroll to the given tile or teleport and ignore the given scroll time"""
    seconds: int = RetrieverRef(EffectStruct._quantity)  # type:ignore
    """The amount of seconds the scroll will take before landing on the specified location"""

    def __init__(
        self,
        source_player: Player = Player.ONE,
        location: Tile = Tile(),
        scroll: bool = True,
        seconds: int = -1,
        **kwargs,
    ):
        """
        Change the view for a specific player by scrolling or teleporting it

        Args:
            source_player: The player to be affected by the effect.
            location: The location to scroll the player view to.
            scroll: If the view change should scroll to the given tile or teleport and ignore the given scroll time.
            seconds: The amount of seconds the scroll will take before landing on the specified location.
        """
        super().__init__(local_vars = locals(), **kwargs)
