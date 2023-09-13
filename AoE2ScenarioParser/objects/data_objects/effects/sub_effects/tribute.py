from binary_file_parser.retrievers import RetrieverRef

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.datasets.trigger_data import PlayerAttribute
from AoE2ScenarioParser.datasets.triggers import EffectType
from AoE2ScenarioParser.sections.bfp.triggers import EffectStruct

from AoE2ScenarioParser.objects.data_objects.effects.effect import Effect

class Tribute(Effect):
    _type_ = EffectType.TRIBUTE

    source_player: Player = RetrieverRef(EffectStruct._source_player)  # type: ignore
    """The player to tribute the resources away from"""
    target_player: Player = RetrieverRef(EffectStruct._target_player)  # type: ignore
    """The player to tribute the resources to"""
    attribute: PlayerAttribute = RetrieverRef(EffectStruct._tribute_list)  # type: ignore
    """The player attribute type to tribute"""
    quantity: int = RetrieverRef(EffectStruct._quantity)  # type: ignore
    """The amount of the chosen player attribute to tribute. Every value (positive & negative) is allowed except for -1."""

    # @overload
    # def __init__(self,
    #     source_player: Player,
    #     target_player: Player,
    #     attribute: PlayerAttribute,
    #     quantity: RetrieverRef
    # ): ...

    def __init__(
        self,
        source_player: Player,
        target_player: Player,
        attribute: PlayerAttribute,
        quantity: RetrieverRef,
        **kwargs,
    ):
        """
        Tribute player resources from source_player to target_player. Notifications are always shown to the
        target_player even if the quantity is negative.

        When positive:

        - Respects the amount of resources of the source_player meaning: it doesn't send more than they have

        When negative:

        - Sends resources from the target_player to the source_player
        - Does not respect the amount of resources on the target_player, meaning they can go into negative resources

        Tricks:

        - Set target_player to `Player.GAIA` and set quantity to any negative quantity to send resources silently to the source_player

        Args:
            source_player: The player to tribute the resources away from
            target_player: The player to tribute the resources to
            attribute: The player attribute type to tribute
            quantity: The amount of the chosen player attribute to tribute. Every value (positive & negative) is allowed except for -1.
        """
        super().__init__(local_vars = locals(), **kwargs)
