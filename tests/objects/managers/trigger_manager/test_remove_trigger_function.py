from unittest import TestCase

from AoE2ScenarioParser.objects.managers.trigger_manager import TriggerManager
from AoE2ScenarioParser.scenarios.aoe2_scenario import _initialise_version_dependencies

_initialise_version_dependencies("DE", '1.47')


class Test(TestCase):
    tm: TriggerManager

    def setUp(self) -> None:
        self.tm = TriggerManager([], [], [])

    def test_remove_trigger(self):
        self.tm.add_trigger("Trigger0")
        self.tm.add_trigger("Trigger1")
        self.tm.add_trigger("Trigger2")

        self.tm.remove_trigger(1)
        self.assertListEqual([t.name for t in self.tm.triggers], ["Trigger0", "Trigger2"])

        self.tm.remove_trigger(1)
        self.assertEqual(self.tm.triggers[0].name, "Trigger0")

    def test_remove_trigger_verify_activation_effects(self):
        t0 = self.tm.add_trigger("Trigger0")
        t0.new_effect.activate_trigger(2)
        self.tm.add_trigger("Trigger1")
        t2 = self.tm.add_trigger("Trigger2")

        self.tm.remove_trigger(1)
        self.assertEqual(t0.effects[0].trigger_id, t2.trigger_id)
