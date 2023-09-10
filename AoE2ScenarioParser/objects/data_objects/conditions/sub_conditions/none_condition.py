from typing import overload

from AoE2ScenarioParser.datasets.triggers.condition_type import ConditionType
from AoE2ScenarioParser.objects.data_objects.conditions.condition import Condition


class NoneCondition(Condition):
    _type_ = ConditionType.NONE

    @overload
    def __init__(self): ...

    def __init__(self, **kwargs):
        """
        A blank condition. In the game this condition is just called 'None'
        """
        super().__init__(local_vars = locals(), **kwargs)
