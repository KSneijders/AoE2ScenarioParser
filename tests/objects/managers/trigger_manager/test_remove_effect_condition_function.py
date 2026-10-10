from unittest import TestCase

from AoE2ScenarioParser.objects.managers.trigger_manager import TriggerManager
from AoE2ScenarioParser.scenarios.aoe2_scenario import _initialise_version_dependencies

_initialise_version_dependencies("DE", "1.55")


class Test(TestCase):
    tm: TriggerManager

    def setUp(self) -> None:
        self.tm = TriggerManager([], [], [])

    def test_remove_effect_keeps_order(self):
        trigger = self.tm.add_trigger("Trigger0")
        for i in range(4):
            trigger.new_effect.send_chat(message=f"E{i}")
        trigger.effect_order = [0, 3, 1, 2]

        trigger.remove_effect(effect_index=0)
        self.assertListEqual([2, 0, 1], trigger.effect_order)
        self.assertListEqual(["E3", "E1", "E2"], [trigger.effects[i].message for i in trigger.effect_order])

        trigger.remove_effect(display_index=1)
        self.assertListEqual([1, 0], trigger.effect_order)
        self.assertListEqual(["E3", "E2"], [trigger.effects[i].message for i in trigger.effect_order])

    def test_remove_condition_keeps_order(self):
        trigger = self.tm.add_trigger("Trigger0")
        for i in range(4):
            trigger.new_condition.timer(timer=i)
        trigger.condition_order = [0, 3, 1, 2]

        trigger.remove_condition(condition_index=0)
        self.assertListEqual([2, 0, 1], trigger.condition_order)
        self.assertListEqual([3, 1, 2], [trigger.conditions[i].timer for i in trigger.condition_order])

        trigger.remove_condition(condition=trigger.conditions[2])
        self.assertListEqual([0, 1], trigger.condition_order)
        self.assertListEqual([1, 2], [trigger.conditions[i].timer for i in trigger.condition_order])
