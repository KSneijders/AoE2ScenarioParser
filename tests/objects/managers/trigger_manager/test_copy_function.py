from unittest import TestCase

from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.objects.managers.de.trigger_manager_de import TriggerManagerDE
from AoE2ScenarioParser.scenarios.aoe2_scenario import initialise_version_dependencies

initialise_version_dependencies("DE", 1.43)


class Test(TestCase):
    tm: TriggerManagerDE

    def setUp(self) -> None:
        self.tm = TriggerManagerDE([], [], [])

    def test_copy_trigger_trigger_attributes(self):
        trigger = self.tm.add_trigger("Trigger", description="Description")

        copy = self.tm.copy_trigger(0)
        self.assertEqual(copy.name, trigger.name + " (copy)")

        copy = self.tm.copy_trigger(0, add_suffix=False)
        self.assertEqual(copy.name, trigger.name)
        self.assertEqual(copy.description, trigger.description)
        self.assertEqual(copy.description_stid, trigger.description_stid)
        self.assertEqual(copy.display_as_objective, trigger.display_as_objective)
        self.assertEqual(copy.short_description, trigger.short_description)
        self.assertEqual(copy.short_description_stid, trigger.short_description_stid)
        self.assertEqual(copy.display_on_screen, trigger.display_on_screen)
        self.assertEqual(copy.description_order, trigger.description_order)
        self.assertEqual(copy.enabled, trigger.enabled)
        self.assertEqual(copy.looping, trigger.looping)
        self.assertEqual(copy.header, trigger.header)
        self.assertEqual(copy.mute_objectives, trigger.mute_objectives)

    def test_copy_trigger_append_after_source(self):
        self.tm.add_trigger("Trigger1")
        self.tm.add_trigger("Trigger2")
        self.tm.add_trigger("Trigger3")

        self.tm.copy_trigger(0, append_after_source=True)
        self.assertListEqual(
            [t.name for t in self.tm.triggers],
            ["Trigger1", "Trigger1 (copy)", "Trigger2", "Trigger3"]
        )

        self.tm.copy_trigger(0, append_after_source=False)
        self.assertListEqual(
            [t.name for t in self.tm.triggers],
            ["Trigger1", "Trigger1 (copy)", "Trigger2", "Trigger3", "Trigger1 (copy)"]
        )

    def test_copy_trigger_ce(self):
        trigger = self.tm.add_trigger("50% Create object")
        trigger.new_condition.chance(50)
        trigger.new_effect.create_object(4, PlayerId.ONE, 3, 4)

        copy = self.tm.copy_trigger(0)

        tc0, cc0 = trigger.conditions[0], copy.conditions[0]

        self.assertEqual(tc0.condition_type, cc0.condition_type)
        self.assertEqual(tc0.quantity, cc0.quantity)
        self.assertEqual(tc0.area_x1, cc0.area_x1)  # Random value

        te0, ce0 = trigger.effects[0], copy.effects[0]

        self.assertEqual(te0.effect_type, ce0.effect_type)
        self.assertEqual(te0.source_player, ce0.source_player)
        self.assertEqual(te0.location_x, ce0.location_x)
        self.assertEqual(te0.location_y, ce0.location_y)
        self.assertEqual(te0.area_x2, ce0.area_x2)  # Random value
