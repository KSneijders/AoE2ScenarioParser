from uuid import UUID

from AoE2ScenarioParser.scenarios.support.data_triggers import DataTriggers


class ScenarioActions:
    def __init__(self, uuid: UUID) -> None:
        super().__init__()

        self._uuid = uuid

    def load_data_triggers(self, remove_template_triggers=True) -> DataTriggers:
        data_triggers = DataTriggers(self._uuid)
        data_triggers.discover(remove_template_triggers)

        return data_triggers
