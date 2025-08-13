from unittest import TestCase

from AoE2ScenarioParser.objects.managers.de.trigger_manager_de import TriggerManagerDE
from AoE2ScenarioParser.scenarios.aoe2_scenario import _initialise_version_dependencies

_initialise_version_dependencies("DE", "1.55")


class Test(TestCase):
    tm: TriggerManagerDE

    def setUp(self) -> None:
        self.tm = TriggerManagerDE([], [], [])

    def test_copy_trigger_tree_attributes(self):
        self.tm.add_trigger("Trigger0").new_effect.activate_trigger(trigger_id=1)
        self.tm.add_trigger("Trigger1")

        self.tm.copy_trigger_tree(0)

        self.assertListEqual(
            [t.name for t in self.tm.triggers],
            ["Trigger0", "Trigger1", "Trigger0 (copy)", "Trigger1 (copy)"]
        )
        self.assertEqual(self.tm.triggers[2].effects[0].trigger_id, 3)

    def test_copy_trigger_tree_attributes_surrounded_triggers(self):
        self.tm.add_trigger("Trigger0")
        self.tm.add_trigger("Trigger1").new_effect.activate_trigger(trigger_id=5)
        self.tm.add_trigger("Trigger2").new_effect.activate_trigger(trigger_id=1)
        self.tm.add_trigger("Trigger3")
        self.tm.add_trigger("Trigger4")
        self.tm.add_trigger("Trigger5")

        self.tm.copy_trigger_tree(2)

        self.assertListEqual(
            [t.name for t in self.tm.triggers],
            ["Trigger0", "Trigger1", "Trigger2", "Trigger3", "Trigger4", "Trigger5",
             "Trigger2 (copy)", "Trigger1 (copy)", "Trigger5 (copy)"]
        )
        self.assertEqual(self.tm.triggers[6].effects[0].trigger_id, 7)
        self.assertEqual(self.tm.triggers[7].effects[0].trigger_id, 8)

    def test_copy_trigger_tree_inf_loop(self):
        self.tm.add_trigger("Trigger0").new_effect.activate_trigger(trigger_id=3)
        self.tm.add_trigger("Trigger1").new_effect.activate_trigger(trigger_id=0)
        self.tm.add_trigger("Trigger2").new_effect.activate_trigger(trigger_id=1)
        self.tm.add_trigger("Trigger3").new_effect.activate_trigger(trigger_id=4)
        self.tm.add_trigger("Trigger4").new_effect.activate_trigger(trigger_id=2)

        self.tm.copy_trigger_tree(0)

        self.assertListEqual(
            [t.name for t in self.tm.triggers],
            ["Trigger0", "Trigger1", "Trigger2", "Trigger3", "Trigger4",
             "Trigger0 (copy)", "Trigger3 (copy)", "Trigger4 (copy)", "Trigger2 (copy)", "Trigger1 (copy)"]
        )
