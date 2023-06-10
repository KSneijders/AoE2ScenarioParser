from typing import overload

from binary_file_parser.retrievers import RetrieverRef

from AoE2ScenarioParser.datasets.triggers import EffectType
from AoE2ScenarioParser.helper.list_functions import listify
from AoE2ScenarioParser.objects.data_objects.effects.effect import Effect
from AoE2ScenarioParser.sections.bfp.triggers import EffectStruct


class UnlockGate(Effect):
    gates: list[int] = RetrieverRef(EffectStruct._selected_object_ids)  # type:ignore # Todo: [Object vs Int]
    """The gate(s) to unlock"""

    @overload
    def __init__(self, gates: list[int]): ...

    @overload
    def __init__(self, gates: int): ...

    def __init__(
        self,
        gates: list[int],
        **kwargs,
    ):
        """
        Play a sound for the source_player

        Args:
            gates: The gate(s) to unlock
        """
        gates = listify(gates)

        super().__init__(local_vars = locals(), **kwargs)

    @property
    def type(self) -> EffectType:
        return EffectType.UNLOCK_GATE
