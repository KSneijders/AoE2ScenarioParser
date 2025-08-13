from unittest import TestCase

from AoE2ScenarioParser.objects.data_objects.trigger import Trigger
from AoE2ScenarioParser.objects.managers.de.trigger_manager_de import TriggerManagerDE
from AoE2ScenarioParser.scenarios.aoe2_scenario import _initialise_version_dependencies

_initialise_version_dependencies("DE", "1.55")


class Test(TestCase):
    tm: TriggerManagerDE

    def setUp(self) -> None:
        self.tm = TriggerManagerDE([], [], [])

    def test_import_triggers(self):
        self.tm.add_trigger("Trigger0")
        self.tm.add_trigger("Trigger1")
        self.tm.add_trigger("Trigger2")

        new_triggers = [
            Trigger("New Trigger0", trigger_id=0),
            Trigger("New Trigger1", trigger_id=1),
            Trigger("New Trigger2", trigger_id=2)
        ]
        self.tm.import_triggers(new_triggers)
        self.assertListEqual(
            [t.name for t in self.tm.triggers],
            [
                "Trigger0", "Trigger1", "Trigger2",
                "New Trigger0", "New Trigger1", "New Trigger2",
            ]
        )
        self.assertListEqual([t.trigger_id for t in self.tm.triggers], list(range(6)))

    def test_import_triggers_verify_activation_effects(self):
        self.tm.add_trigger("Trigger0")
        self.tm.add_trigger("Trigger1")
        self.tm.add_trigger("Trigger2")

        t0 = Trigger("New Trigger0", trigger_id=0)
        t1 = Trigger("New Trigger1", trigger_id=1)
        t2 = Trigger("New Trigger2", trigger_id=2)
        t0.new_effect.activate_trigger(2)
        t2.new_effect.activate_trigger(1)

        new_triggers = [t0, t1, t2]

        self.tm.import_triggers(new_triggers)
        self.assertListEqual([t.trigger_id for t in self.tm.triggers], list(range(6)))
        self.assertEqual(t0.effects[0].trigger_id, t2.trigger_id)
        self.assertEqual(t2.effects[0].trigger_id, t1.trigger_id)

    def test_import_triggers_verify_activation_effects_twice(self):
        t0 = self.tm.add_trigger("Trigger0")
        t1 = self.tm.add_trigger("Trigger1")
        t2 = self.tm.add_trigger("Trigger2")
        t0.new_effect.activate_trigger(2)
        t2.new_effect.activate_trigger(1)

        new_triggers = [t0, t1, t2]

        for _ in range(2):
            self.tm.import_triggers(new_triggers)
        self.assertListEqual([t.trigger_id for t in self.tm.triggers], list(range(9)))

        for offset in range(0, len(self.tm.triggers), 3):
            self.assertEqual(
                self.tm.triggers[offset].effects[0].trigger_id,
                self.tm.triggers[offset + 2].trigger_id,
            )
            self.assertEqual(
                self.tm.triggers[offset + 2].effects[0].trigger_id,
                self.tm.triggers[offset + 1].trigger_id,
            )

    def test_import_triggers_with_index(self):
        self.tm.add_trigger("Trigger0")
        self.tm.add_trigger("Trigger1")
        self.tm.add_trigger("Trigger2")
        self.tm.add_trigger("Trigger3")

        new_triggers = [
            Trigger("New Trigger0", trigger_id=0),
            Trigger("New Trigger1", trigger_id=1),
            Trigger("New Trigger2", trigger_id=2)
        ]

        self.tm.import_triggers(new_triggers, 2)
        self.assertListEqual([t.trigger_id for t in self.tm.triggers], list(range(7)))
        self.assertListEqual(
            [t.name for t in self.tm.triggers],
            [
                "Trigger0", "Trigger1",
                "New Trigger0", "New Trigger1", "New Trigger2",
                "Trigger2", "Trigger3"
            ]
        )
