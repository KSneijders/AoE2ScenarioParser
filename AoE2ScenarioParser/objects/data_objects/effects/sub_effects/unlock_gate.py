from binary_file_parser.retrievers import RetrieverRef

from AoE2ScenarioParser.datasets.triggers import EffectType
from AoE2ScenarioParser.sections.bfp.triggers import EffectStruct

from AoE2ScenarioParser.objects.data_objects.effects.effect import Effect


class UnlockGate(Effect):
    _type_ = EffectType.UNLOCK_GATE

    gates: list[int] = RetrieverRef(EffectStruct._selected_object_ids)  # type:ignore # Todo: [Object vs Int]
    """The gate(s) to unlock"""

    # @overload
    # def __init__(self, gates: list[int]): ...

    # @overload
    # def __init__(self, gates: int): ...

    def __init__(
        self,
        gates: list[int],
        **kwargs,
    ):
        """
        Unlock all selected gates

        Args:
            gates: The gate(s) to unlock
        """
        super().__init__(local_vars = locals(), **kwargs)
