from binary_file_parser.retrievers import RetrieverRef

from AoE2ScenarioParser.datasets.triggers import EffectType
from AoE2ScenarioParser.sections.bfp.triggers import EffectStruct

from AoE2ScenarioParser.objects.data_objects.effects.effect import Effect


class AiScriptGoal(Effect):
    _type_ = EffectType.AI_SCRIPT_GOAL

    ai_trigger_id: int = RetrieverRef(EffectStruct._ai_script_goal)  # type:ignore
    """The AI Trigger ID to trigger"""

    # @overload
    # def __init__(self, ai_trigger_id: int): ...

    def __init__(
        self,
        ai_trigger_id: int,
        **kwargs,
    ):
        """
        Used to communicate with an AI.
        Calling this effect with ai_trigger_id set to (for example) 4 can be detected in an AI script
        using ``event-detected trigger 4``.

        Args:
            ai_trigger_id: The AI Trigger ID to trigger
        """
        super().__init__(local_vars = locals(), **kwargs)
