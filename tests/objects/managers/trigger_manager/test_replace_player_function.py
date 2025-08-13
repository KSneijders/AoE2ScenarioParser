from unittest import TestCase

from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.datasets.trigger_lists import DiplomacyState
from AoE2ScenarioParser.objects.managers.de.trigger_manager_de import TriggerManagerDE
from AoE2ScenarioParser.scenarios.aoe2_scenario import _initialise_version_dependencies

_initialise_version_dependencies("DE", "1.55")


class Test(TestCase):
    tm: TriggerManagerDE

    def setUp(self) -> None:
        self.tm = TriggerManagerDE([], [], [])

    def test_replace_player_attributes(self):
        trigger = self.tm.add_trigger("Trigger")
        trigger.new_condition.chance(quantity=50)
        trigger.new_condition.objects_in_area(quantity=1, object_list=4, source_player=PlayerId.ONE)
        trigger.new_condition.objects_in_area(quantity=1, object_list=4, source_player=PlayerId.THREE)

        self.tm.replace_player(0, to_player=PlayerId.TWO)

        self.assertEqual(trigger.conditions[0].source_player, -1)
        self.assertEqual(trigger.conditions[1].quantity, 1)
        self.assertEqual(trigger.conditions[1].source_player, PlayerId.TWO)
        self.assertEqual(trigger.conditions[2].source_player, PlayerId.TWO)

    def test_replace_player_only_change_from(self):
        trigger = self.tm.add_trigger("Trigger")
        trigger.new_condition.objects_in_area(quantity=1, object_list=4, source_player=PlayerId.ONE)
        trigger.new_condition.objects_in_area(quantity=1, object_list=4, source_player=PlayerId.THREE)

        self.tm.replace_player(0, to_player=PlayerId.TWO, only_change_from=PlayerId.ONE)

        self.assertEqual(trigger.conditions[0].source_player, PlayerId.TWO)
        self.assertEqual(trigger.conditions[1].source_player, PlayerId.THREE)

    def test_replace_player_include_player_x(self):
        trigger = self.tm.add_trigger("Trigger")
        trigger.new_condition.diplomacy_state(
            quantity=DiplomacyState.NEUTRAL, source_player=PlayerId.ONE, target_player=PlayerId.THREE
        )

        self.tm.replace_player(0, to_player=PlayerId.TWO, include_player_source=False)
        self.assertEqual(trigger.conditions[0].source_player, PlayerId.ONE)
        self.assertEqual(trigger.conditions[0].target_player, PlayerId.THREE)

        self.tm.replace_player(0, to_player=PlayerId.TWO, include_player_target=True)
        self.assertEqual(trigger.conditions[0].source_player, PlayerId.TWO)
        self.assertEqual(trigger.conditions[0].target_player, PlayerId.TWO)
