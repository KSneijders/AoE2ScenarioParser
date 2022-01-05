from uuid import UUID

from AoE2ScenarioParser.scenarios.support.trigger_markings import TriggerMarkings


class ScenarioActions:
    def __init__(self, uuid: UUID) -> None:
        super().__init__()

        self._uuid = uuid

    def discover_trigger_markings(self, remove_template_triggers=True) -> TriggerMarkings:
        trigger_markings = TriggerMarkings(self._uuid)
        trigger_markings.discover(remove_template_triggers)

        return trigger_markings
