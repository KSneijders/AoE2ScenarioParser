from AoE2ScenarioParser.datasets.triggers import EffectType
from AoE2ScenarioParser.objects.data_objects.effects.effect import Effect


class NoneEffect(Effect):
    def __init__(self, **kwargs):
        """
        A blank effect. In the game this effect is just called 'None'.
        It doesn't do anything at all, not even 'splash'...
        """
        super().__init__(type=EffectType.NONE, local_vars=locals(), **kwargs)
