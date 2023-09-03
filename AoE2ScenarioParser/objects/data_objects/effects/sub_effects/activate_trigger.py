from binary_file_parser.retrievers import RetrieverRef

from AoE2ScenarioParser.objects.data_objects.effects.effect import Effect
from AoE2ScenarioParser.sections.bfp.triggers import EffectStruct


class ActivateTrigger(Effect):
    trigger: int = RetrieverRef(EffectStruct._trigger_id)  # type:ignore # Todo: [Object vs Int]
    """The trigger to activate"""

    # @overload
    # def __init__(self, trigger: int): ...
    
    def __init__(
        self,
        _trigger: list[int],
        **kwargs,
    ):
        """
        Activate a trigger

        Args:
            _trigger: The trigger to activate
        """
        super().__init__(local_vars = locals(), **kwargs)
