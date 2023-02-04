from typing import Type, TYPE_CHECKING

from AoE2ScenarioParser.helper.printers import warn

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.data_objects.trigger import Trigger


class TriggerSelect:
    """
    Object used to select a trigger in many trigger related functions. For ease of use, the alias `TS` can be
    called. You can also use those in combination with the class methods (factory methods). Like so:

    Tip: Selecting a trigger by its ID doesn't require this object
        Most functions allow you to just input `4` into the trigger parameter (instead of: `TS.index(4)`)

    Examples:
        `TS.index(4)`  To select the trigger with index 4

        `TS.display(4)`  Trigger with display index 4

        `TS.trigger(trigger)`  Well... The trigger object given...
    """

    _deprecated: str = "The usage of TriggerSelect (TS) object is no longer necessary. \n" \
                       "The class will be removed in the future. \n" \
                       "Using the ID (number: e.g. 34) or the actual trigger by itself is enough. \n" \
                       "Using the display index is discouraged but can be achieved using the following syntax: \n" \
                       "\t`trigger_manager.get_trigger(34, use_display_index=True)`"

    def __init__(self, trigger_index: int = None, display_index: int = None, trigger: 'Trigger' = None, **kwargs):
        """
        Args:
            trigger_index: The index of the trigger. Starting from 0, based on creation time
            display_index: The display index of a trigger. Starting from 0, based on display order in the editor
            trigger: The trigger object itself.
        """
        if 'through_alias' not in kwargs:
            warn(f"{TriggerSelect._deprecated}", DeprecationWarning)

        self.trigger = trigger
        self.display_index = display_index
        self.trigger_index = trigger_index

    @classmethod
    def index(cls, index: int):
        # Using a format string so that PyCharm shows the functions with a strike-through effect.
        # For whatever reason, it doesn't with a variable...
        warn(f"{TriggerSelect._deprecated}", DeprecationWarning)
        return cls(trigger_index=index, through_alias=True)

    @classmethod
    def display(cls, display_index: int):
        # Using a format string so that PyCharm shows the functions with a strike-through effect.
        # For whatever reason, it doesn't with a variable...
        warn(f"{TriggerSelect._deprecated}", DeprecationWarning)
        return cls(display_index=display_index, through_alias=True)

    @classmethod
    def trigger(cls, trigger: 'Trigger'):
        # Using a format string so that PyCharm shows the functions with a strike-through effect.
        # For whatever reason, it doesn't with a variable...
        warn(f"{TriggerSelect._deprecated}", DeprecationWarning)
        return cls(trigger=trigger, through_alias=True)


TS: Type[TriggerSelect] = TriggerSelect
"""Alias for `TriggerSelect`"""
