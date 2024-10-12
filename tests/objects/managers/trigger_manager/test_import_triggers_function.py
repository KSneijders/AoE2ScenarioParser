from unittest import TestCase

from AoE2ScenarioParser.objects.data_objects.trigger import Trigger
from AoE2ScenarioParser.objects.managers.trigger_manager import TriggerManager
from AoE2ScenarioParser.scenarios.aoe2_scenario import _initialise_version_dependencies

_initialise_version_dependencies("DE", '1.47')


# Todo: REWRITE BEFORE V1 RELEASE!


class Test(TestCase):
    tm: TriggerManager

    def setUp(self) -> None:
        self.tm = TriggerManager([], [], [])

    def test_import_triggers(self):
        self.tm.add_trigger("Trigger0")
        self.tm.add_trigger("Trigger1")
        self.tm.add_trigger("Trigger2")

        new_triggers = [
            Trigger("New Trigger0", id=0),
            Trigger("New Trigger1", id=1),
            Trigger("New Trigger2", id=2)
        ]
        self.tm.import_triggers(new_triggers)
        self.assertListEqual(
            [t.name for t in self.tm.triggers],
            [
                "Trigger0", "Trigger1", "Trigger2",
                "New Trigger0", "New Trigger1", "New Trigger2",
            ]
        )
        self.assertListEqual([t.id for t in self.tm.triggers], list(range(6)))

    def test_import_triggers_verify_activation_effects(self):
        self.tm.add_trigger("Trigger0")
        self.tm.add_trigger("Trigger1")
        self.tm.add_trigger("Trigger2")

        t0 = Trigger("New Trigger0", id=0)
        t1 = Trigger("New Trigger1", id=1)
        t2 = Trigger("New Trigger2", id=2)
        t0.new_effect.activate_trigger(2)
        t2.new_effect.activate_trigger(1)

        new_triggers = [t0, t1, t2]

        self.tm.import_triggers(new_triggers)
        self.assertListEqual([t.id for t in self.tm.triggers], list(range(6)))
        self.assertEqual(t0.effects[0].trigger_id, t2.id)
        self.assertEqual(t2.effects[0].trigger_id, t1.id)

    def test_import_triggers_verify_activation_effects_twice(self):
        t0 = self.tm.add_trigger("Trigger0")
        t1 = self.tm.add_trigger("Trigger1")
        t2 = self.tm.add_trigger("Trigger2")
        t0.new_effect.activate_trigger(2)
        t2.new_effect.activate_trigger(1)

        new_triggers = [t0, t1, t2]

        for _ in range(2):
            self.tm.import_triggers(new_triggers)
        self.assertListEqual([t.id for t in self.tm.triggers], list(range(9)))

        for offset in range(0, len(self.tm.triggers), 3):
            self.assertEqual(
                self.tm.triggers[offset].effects[0].trigger_id,
                self.tm.triggers[offset + 2].id,
            )
            self.assertEqual(
                self.tm.triggers[offset + 2].effects[0].trigger_id,
                self.tm.triggers[offset + 1].id,
            )

    def test_import_triggers_with_index(self):
        self.tm.add_trigger("Trigger0")
        self.tm.add_trigger("Trigger1")
        self.tm.add_trigger("Trigger2")
        self.tm.add_trigger("Trigger3")

        new_triggers = [
            Trigger("New Trigger0", id=0),
            Trigger("New Trigger1", id=1),
            Trigger("New Trigger2", id=2)
        ]

        self.tm.import_triggers(new_triggers, 2)
        self.assertListEqual([t.id for t in self.tm.triggers], list(range(7)))
        self.assertListEqual(
            [t.name for t in self.tm.triggers],
            [
                "Trigger0", "Trigger1",
                "New Trigger0", "New Trigger1", "New Trigger2",
                "Trigger2", "Trigger3"
            ]
        )
