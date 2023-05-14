from unittest import TestCase

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.datasets.trigger_data import DiplomacyStance
from AoE2ScenarioParser.objects.managers.trigger_manager import TriggerManager
from AoE2ScenarioParser.scenarios.aoe2_scenario import _initialise_version_dependencies

_initialise_version_dependencies("DE", '1.47')


class Test(TestCase):
    tm: TriggerManager

    def setUp(self) -> None:
        self.tm = TriggerManager([], [], [])

    def test_replace_player_attributes(self):
        trigger = self.tm.add_trigger("Trigger")
        trigger.new_condition.chance(quantity=50)
        trigger.new_condition.objects_in_area(quantity=1, object_list=4, source_player=Player.ONE)
        trigger.new_condition.objects_in_area(quantity=1, object_list=4, source_player=Player.THREE)

        self.tm.replace_player(0, to_player=Player.TWO)

        self.assertEqual(trigger.conditions[0].source_player, -1)
        self.assertEqual(trigger.conditions[1].quantity, 1)
        self.assertEqual(trigger.conditions[1].source_player, Player.TWO)
        self.assertEqual(trigger.conditions[2].source_player, Player.TWO)

    def test_replace_player_only_change_from(self):
        trigger = self.tm.add_trigger("Trigger")
        trigger.new_condition.objects_in_area(quantity=1, object_list=4, source_player=Player.ONE)
        trigger.new_condition.objects_in_area(quantity=1, object_list=4, source_player=Player.THREE)

        self.tm.replace_player(0, to_player=Player.TWO, only_change_from=Player.ONE)

        self.assertEqual(trigger.conditions[0].source_player, Player.TWO)
        self.assertEqual(trigger.conditions[1].source_player, Player.THREE)

    def test_replace_player_include_player_x(self):
        trigger = self.tm.add_trigger("Trigger")
        trigger.new_condition.diplomacy_state(
            quantity=DiplomacyStance.NEUTRAL, source_player=Player.ONE, target_player=Player.THREE
        )

        self.tm.replace_player(0, to_player=Player.TWO, include_player_source=False)
        self.assertEqual(trigger.conditions[0].source_player, Player.ONE)
        self.assertEqual(trigger.conditions[0].target_player, Player.THREE)

        self.tm.replace_player(0, to_player=Player.TWO, include_player_target=True)
        self.assertEqual(trigger.conditions[0].source_player, Player.TWO)
        self.assertEqual(trigger.conditions[0].target_player, Player.TWO)
