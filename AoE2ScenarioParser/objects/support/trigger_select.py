from AoE2ScenarioParser.objects.data_objects.trigger import Trigger


class TriggerSelect:
    def __init__(self, trigger_index=None, display_index=None, trigger=None):
        """
        Object used to select a trigger in many trigger related functions. For ease of use, the alias `TS` can be
        called. You can also use those in combination with the class methods (factory methods). Like so:

        TS.index(4)    # To select the trigger with index 4

        TS.display(4)  # Trigger with display index 4

        TS.trigger(trigger)  # Well... The trigger object given...

        Args:
            trigger_index (int): The index of the trigger. Starting from 0, based on creation time
            display_index (int): The display index of a trigger. Starting from 0, based on display order in the editor
            trigger (Trigger): The trigger object itself.
        """
        self.trigger = trigger
        self.display_index = display_index
        self.trigger_index = trigger_index

    @classmethod
    def index(cls, index: int):
        return cls(trigger_index=index)

    @classmethod
    def display(cls, display_index: int):
        return cls(display_index=display_index)

    @classmethod
    def trigger(cls, trigger: Trigger):
        return cls(trigger=trigger)


TS = TriggerSelect
