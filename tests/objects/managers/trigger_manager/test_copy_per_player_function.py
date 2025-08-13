from unittest import TestCase

from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.objects.managers.de.trigger_manager_de import TriggerManagerDE
from AoE2ScenarioParser.scenarios.aoe2_scenario import _initialise_version_dependencies

_initialise_version_dependencies("DE", "1.55")


class Test(TestCase):
    tm: TriggerManagerDE

    def setUp(self) -> None:
        self.tm = TriggerManagerDE([], [], [])

    def test_copy_trigger_per_player_attributes(self):
        trigger = self.tm.add_trigger("Trigger0")
        trigger.new_effect.create_object(object_list_unit_id=1, source_player=PlayerId.ONE)
        trigger.new_effect.create_object(object_list_unit_id=1, source_player=PlayerId.TWO)

        self.tm.copy_trigger_per_player(from_player=PlayerId.ONE, trigger_select=0)

        self.assertListEqual(
            [t.name for t in self.tm.triggers],
            ["Trigger0 (p1)", "Trigger0 (p2)", "Trigger0 (p3)", "Trigger0 (p4)",
             "Trigger0 (p5)", "Trigger0 (p6)", "Trigger0 (p7)", "Trigger0 (p8)", ]
        )

        for index, player in enumerate(PlayerId.all(exclude_gaia=True)):
            self.assertEqual(self.tm.triggers[index].effects[0].object_list_unit_id, 1)
            self.assertEqual(self.tm.triggers[index].effects[0].source_player, player)

            if index != 0:  # First entry is source trigger. Remains unchanged
                self.assertEqual(self.tm.triggers[index].effects[1].source_player, player)

    def test_copy_trigger_per_player_change_from_player_only(self):
        trigger = self.tm.add_trigger("Trigger0")
        trigger.new_effect.create_object(object_list_unit_id=1, source_player=PlayerId.ONE)
        trigger.new_effect.create_object(object_list_unit_id=1, source_player=PlayerId.TWO)

        self.tm.copy_trigger_per_player(from_player=PlayerId.ONE, trigger_select=0, change_from_player_only=True)

        for index, player in enumerate(PlayerId.all(exclude_gaia=True)):
            self.assertEqual(self.tm.triggers[index].effects[0].object_list_unit_id, 1)
            self.assertEqual(self.tm.triggers[index].effects[0].source_player, player)
            self.assertEqual(self.tm.triggers[index].effects[1].source_player, 2)

    def test_copy_trigger_per_player_include_player_source(self):
        trigger = self.tm.add_trigger("Trigger0")
        trigger.new_effect.change_diplomacy(source_player=PlayerId.ONE, target_player=PlayerId.TWO)

        self.tm.copy_trigger_per_player(from_player=PlayerId.ONE, trigger_select=0, include_player_source=False)

        for index, player in enumerate(PlayerId.all(exclude_gaia=True)):
            self.assertEqual(self.tm.triggers[index].effects[0].source_player, PlayerId.ONE)
            self.assertEqual(self.tm.triggers[index].effects[0].target_player, PlayerId.TWO)

    def test_copy_trigger_per_player_include_player_target(self):
        trigger = self.tm.add_trigger("Trigger0")
        trigger.new_effect.change_diplomacy(source_player=PlayerId.ONE, target_player=PlayerId.TWO)

        self.tm.copy_trigger_per_player(from_player=PlayerId.ONE, trigger_select=0, include_player_target=True)

        for index, player in enumerate(PlayerId.all(exclude_gaia=True)):
            self.assertEqual(self.tm.triggers[index].effects[0].source_player, player)
            if index != 0:  # First entry is source trigger. Remains unchanged
                self.assertEqual(self.tm.triggers[index].effects[0].target_player, player)

    def test_copy_trigger_per_player_include_gaia(self):
        trigger = self.tm.add_trigger("Trigger0")
        trigger.new_effect.change_diplomacy(source_player=PlayerId.ONE, target_player=PlayerId.TWO)

        self.tm.copy_trigger_per_player(from_player=PlayerId.ONE, trigger_select=0, include_gaia=True)

        self.assertListEqual(
            [t.name for t in self.tm.triggers],
            ["Trigger0 (p1)", "Trigger0 (p2)", "Trigger0 (p3)", "Trigger0 (p4)",
             "Trigger0 (p5)", "Trigger0 (p6)", "Trigger0 (p7)", "Trigger0 (p8)", 'Trigger0 (GAIA)']
        )

    def test_copy_trigger_per_player_create_copy_for_players(self):
        trigger = self.tm.add_trigger("Trigger0")
        trigger.new_effect.change_diplomacy(source_player=PlayerId.ONE, target_player=PlayerId.TWO)

        self.tm.copy_trigger_per_player(from_player=PlayerId.ONE, trigger_select=0, create_copy_for_players=[
            PlayerId.THREE, PlayerId.FIVE, PlayerId.SEVEN, PlayerId.EIGHT
        ])

        self.assertListEqual(
            [t.name for t in self.tm.triggers],
            ["Trigger0 (p1)", "Trigger0 (p3)", "Trigger0 (p5)", "Trigger0 (p7)", "Trigger0 (p8)"]
        )
