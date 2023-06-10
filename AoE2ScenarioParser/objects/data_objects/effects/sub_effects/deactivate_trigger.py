from typing import overload

from binary_file_parser.retrievers import RetrieverRef

from AoE2ScenarioParser.datasets.triggers import EffectType
from AoE2ScenarioParser.objects.data_objects.effects.effect import Effect
from AoE2ScenarioParser.sections.bfp.triggers import EffectStruct


class DeactivateTrigger(Effect):
    trigger: int = RetrieverRef(EffectStruct._trigger_id)  # type:ignore # Todo: [Object vs Int]
    """The trigger to deactivate"""

    # @overload
    # def __init__(self, trigger: int): ...

    def __init__(
        self,
        trigger: list[int],
        **kwargs,
    ):
        """
        Deactivate a trigger

        Args:
            trigger: The trigger to deactivate
        """
        super().__init__(local_vars = locals(), **kwargs)

    @property
    def type(self) -> EffectType:
        return EffectType.DEACTIVATE_TRIGGER
