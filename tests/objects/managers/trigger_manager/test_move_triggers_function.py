from unittest import TestCase

from AoE2ScenarioParser.objects.managers.de.trigger_manager_de import TriggerManagerDE
from AoE2ScenarioParser.scenarios.aoe2_scenario import _initialise_version_dependencies

_initialise_version_dependencies("DE", "1.55")


class Test(TestCase):
    tm: TriggerManagerDE

    def setUp(self) -> None:
        self.tm = TriggerManagerDE([], [], [])

    def test_move_triggers(self):
        for i in range(10):
            self.tm.add_trigger(f"Trigger{i}")

        self.tm.move_triggers([3, 4, 5], 0)
        self.assertListEqual(
            [t.name for t in self.tm.triggers],
            [f"Trigger{i}" for i in [3, 4, 5, 0, 1, 2, 6, 7, 8, 9]]
        )

        self.tm.move_triggers([0, 9, 6], 5)  # Triggers: 3, 9 & 6
        self.assertListEqual(
            [t.name for t in self.tm.triggers],
            [f"Trigger{i}" for i in [4, 5, 0, 1, 3, 9, 6, 2, 7, 8]]
        )

    def test_move_triggers_index_over_len(self):
        for i in range(5):
            self.tm.add_trigger(f"Trigger{i}")

        self.tm.move_triggers([1, 4], 99)
        self.assertListEqual(
            [t.name for t in self.tm.triggers],
            [f"Trigger{i}" for i in [0, 2, 3, 1, 4]]
        )
