from typing import overload

from AoE2ScenarioParser.objects.data_objects.conditions.condition import Condition


class NoneCondition(Condition):

    @overload
    def __init__(self): ...

    def __init__(self, **kwargs):
        """
        A blank effect. In the game this effect is just called 'None'.
        It doesn't do anything at all, not even 'splash'...
        """
        super().__init__(local_vars = locals(), **kwargs)
