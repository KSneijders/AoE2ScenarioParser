from unittest import TestCase

from AoE2ScenarioParser.objects.managers.de.trigger_manager_de import TriggerManagerDE
from AoE2ScenarioParser.scenarios.aoe2_scenario import _initialise_version_dependencies

_initialise_version_dependencies("DE", "1.55")


class Test(TestCase):
    tm: TriggerManagerDE

    def setUp(self) -> None:
        self.tm = TriggerManagerDE([], [], [])

    def test_reorder_triggers(self):
        for i in range(10):
            self.tm.add_trigger(f"Trigger{i}")

        self.tm.reorder_triggers(list(reversed(range(10))))
        self.assertListEqual(
            [t.name for t in self.tm.triggers],
            [f"Trigger{i}" for i in [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]
        )

    def test_reorder_triggers_verify_activation_effects(self):
        t0 = self.tm.add_trigger("Trigger0")
        t0.new_effect.activate_trigger(2)
        self.tm.add_trigger("Trigger1")
        t2 = self.tm.add_trigger("Trigger2")
        t2.new_effect.activate_trigger(4)
        self.tm.add_trigger("Trigger3")
        t4 = self.tm.add_trigger("Trigger4")

        self.tm.reorder_triggers([3, 0, 1, 4, 2])
        self.assertListEqual(
            [t.name for t in self.tm.triggers],
            [f"Trigger{i}" for i in [3, 0, 1, 4, 2]]
        )

        self.assertEqual(t0.effects[0].trigger_id, t2.trigger_id)
        self.assertEqual(t2.effects[0].trigger_id, t4.trigger_id)

    def test_reorder_triggers_verify_conditions(self):
        t0 = self.tm.add_trigger("Trigger0")
        t0.new_condition.trigger_active(2)
        self.tm.add_trigger("Trigger1")
        t2 = self.tm.add_trigger("Trigger2")
        t2.new_condition.trigger_active(4)
        self.tm.add_trigger("Trigger3")
        t4 = self.tm.add_trigger("Trigger4")

        self.tm.reorder_triggers([3, 0, 1, 4, 2])
        self.assertListEqual(
            [t.name for t in self.tm.triggers],
            [f"Trigger{i}" for i in [3, 0, 1, 4, 2]]
        )

        self.assertEqual(t0.conditions[0].trigger_id, t2.trigger_id)
        self.assertEqual(t2.conditions[0].trigger_id, t4.trigger_id)
