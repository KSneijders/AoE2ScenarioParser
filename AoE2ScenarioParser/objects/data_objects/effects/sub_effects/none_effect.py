from typing import overload

from AoE2ScenarioParser.datasets.triggers import EffectType

from AoE2ScenarioParser.objects.data_objects.effects.effect import Effect


class NoneEffect(Effect):

    @overload
    def __init__(self): ...

    def __init__(self, **kwargs):
        """
        A blank effect. In the game this effect is just called 'None'.
        It doesn't do anything at all, not even 'splash'...
        """
        kwargs["type"] = EffectType.NONE
        super().__init__(local_vars=locals(), **kwargs)