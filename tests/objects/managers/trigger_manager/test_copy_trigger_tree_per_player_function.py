#
#from AoE2ScenarioParser.datasets.player_data import Player
#from AoE2ScenarioParser.objects.managers.trigger_manager import TriggerManager
#from AoE2ScenarioParser.objects.support.enums.group_by import GroupBy
#from AoE2ScenarioParser.scenarios.aoe2_scenario import _initialise_version_dependencies
#
#_initialise_version_dependencies("DE", "1.55")
#
#
## Todo: REWRITE BEFORE V1 RELEASE!
#
#
#class Test(TestCase):
#    tm: TriggerManager
#
#    def setUp(self) -> None:
#        self.tm = TriggerManager([], [], [])
#
#    def test_copy_trigger_tree_per_player_attributes(self):
#        trigger = self.tm.add_trigger("Trigger0")
#        trigger.new_effect.create_object(object_list_unit_id=1, source_player=Player.ONE)
#        trigger.new_effect.create_object(source_player=Player.TWO)
#
#        self.tm.copy_trigger_tree_per_player(from_player=Player.ONE, trigger=0)
#
#        self.assertListEqual(
#            [t.name for t in self.tm.triggers],
#            ["Trigger0 (p1)", "Trigger0 (p2)", "Trigger0 (p3)", "Trigger0 (p4)",
#             "Trigger0 (p5)", "Trigger0 (p6)", "Trigger0 (p7)", "Trigger0 (p8)", ]
#        )
#
#        for index, player in enumerate(Player.all(exclude_gaia=True)):
#            self.assertEqual(self.tm.triggers[index].effects[0].object_list_unit_id, 1)
#            self.assertEqual(self.tm.triggers[index].effects[0].source_player, player)
#
#            if index != 0:  # First entry is source trigger. Remains unchanged
#                self.assertEqual(self.tm.triggers[index].effects[1].source_player, player)
#
#    def test_copy_trigger_tree_per_player_groupby_none(self):
#        self.tm.add_trigger("Trigger0").new_effect.activate_trigger(trigger_id=1)
#        self.tm.add_trigger("Trigger1")
#        trigger2 = self.tm.add_trigger("Trigger2")
#        trigger2.new_effect.activate_trigger(trigger_id=3)
#        trigger3 = self.tm.add_trigger("Trigger3")
#
#        new_triggers = self.tm.copy_trigger_tree_per_player(from_player=Player.ONE, trigger=0)
#
#        self.assertListEqual(
#            [t.name for t in self.tm.triggers],
#            [
#                "Trigger0 (p1)",
#                "Trigger1 (p1)",
#                "Trigger2",
#                "Trigger3",
#                "Trigger0 (p2)", "Trigger0 (p3)", "Trigger0 (p4)", "Trigger0 (p5)",
#                "Trigger0 (p6)", "Trigger0 (p7)", "Trigger0 (p8)",
#                "Trigger1 (p2)", "Trigger1 (p3)", "Trigger1 (p4)", "Trigger1 (p5)",
#                "Trigger1 (p6)", "Trigger1 (p7)", "Trigger1 (p8)",
#            ]
#        )
#
#        # Verify if triggers still link to their new copy
#        for player, triggers in new_triggers.items():
#            activate_id = triggers[0].effects[0].trigger_id
#
#            self.assertEqual(activate_id, triggers[1].id)
#            self.assertIs(self.tm.triggers[activate_id], triggers[1])
#
#        # Verify activate triggers outside of the tree
#        self.assertEqual(trigger2.effects[0].trigger_id, trigger3.id)
#
#    def test_copy_trigger_tree_per_player_groupby_trigger(self):
#        self.tm.add_trigger("Trigger0")
#        trigger1 = self.tm.add_trigger("Trigger1")
#        trigger1.new_effect.activate_trigger(trigger_id=4)
#        self.tm.add_trigger("Trigger2").new_effect.activate_trigger(trigger_id=3)
#        self.tm.add_trigger("Trigger3").new_effect.activate_trigger(trigger_id=0)
#        trigger4 = self.tm.add_trigger("Trigger4")
#
#        new_triggers = self.tm.copy_trigger_tree_per_player(
#            from_player=Player.ONE, trigger=2, group_triggers_by=GroupBy.TRIGGER
#        )
#
#        self.assertListEqual(
#            [t.name for t in self.tm.triggers],
#            [
#                "Trigger1",
#                "Trigger2 (p1)", "Trigger2 (p2)", "Trigger2 (p3)", "Trigger2 (p4)",
#                "Trigger2 (p5)", "Trigger2 (p6)", "Trigger2 (p7)", "Trigger2 (p8)",
#                "Trigger3 (p1)", "Trigger3 (p2)", "Trigger3 (p3)", "Trigger3 (p4)",
#                "Trigger3 (p5)", "Trigger3 (p6)", "Trigger3 (p7)", "Trigger3 (p8)",
#                "Trigger0 (p1)", "Trigger0 (p2)", "Trigger0 (p3)", "Trigger0 (p4)",
#                "Trigger0 (p5)", "Trigger0 (p6)", "Trigger0 (p7)", "Trigger0 (p8)",
#                "Trigger4",
#            ]
#        )
#
#        # Verify if triggers still link to their new copy
#        for player, triggers in new_triggers.items():
#            activate_id0 = triggers[0].effects[0].trigger_id
#            activate_id1 = triggers[1].effects[0].trigger_id
#
#            self.assertEqual(activate_id0, triggers[1].id)
#            self.assertEqual(activate_id1, triggers[2].id)
#
#            self.assertIs(self.tm.triggers[activate_id0], triggers[1])
#            self.assertIs(self.tm.triggers[activate_id1], triggers[2])
#
#        # Verify activate triggers outside of the tree
#        self.assertEqual(trigger1.effects[0].trigger_id, trigger4.id)
#
#    def test_copy_trigger_tree_per_player_groupby_player(self):
#        self.tm.add_trigger("Trigger0")
#        self.tm.add_trigger("Trigger1").new_effect.activate_trigger(trigger_id=2)
#        self.tm.add_trigger("Trigger2").new_effect.activate_trigger(trigger_id=0)
#        self.tm.add_trigger("Trigger3")
#        trigger4 = self.tm.add_trigger("Trigger4")
#        trigger4.new_effect.activate_trigger(trigger_id=5)
#        trigger5 = self.tm.add_trigger("Trigger5")
#
#        new_triggers = self.tm.copy_trigger_tree_per_player(
#            from_player=Player.ONE, trigger=1, group_triggers_by=GroupBy.PLAYER
#        )
#
#        self.assertListEqual(
#            [t.name for t in self.tm.triggers],
#            [
#                "Trigger1 (p1)", "Trigger2 (p1)", "Trigger0 (p1)",
#                "Trigger1 (p2)", "Trigger2 (p2)", "Trigger0 (p2)",
#                "Trigger1 (p3)", "Trigger2 (p3)", "Trigger0 (p3)",
#                "Trigger1 (p4)", "Trigger2 (p4)", "Trigger0 (p4)",
#                "Trigger1 (p5)", "Trigger2 (p5)", "Trigger0 (p5)",
#                "Trigger1 (p6)", "Trigger2 (p6)", "Trigger0 (p6)",
#                "Trigger1 (p7)", "Trigger2 (p7)", "Trigger0 (p7)",
#                "Trigger1 (p8)", "Trigger2 (p8)", "Trigger0 (p8)",
#                "Trigger3",
#                "Trigger4",
#                "Trigger5"
#            ]
#        )
#
#        # Verify if triggers still link to their new copy
#        for player, triggers in new_triggers.items():
#            activate_id0 = triggers[0].effects[0].trigger_id
#            activate_id1 = triggers[1].effects[0].trigger_id
#
#            self.assertEqual(activate_id0, triggers[1].id)
#            self.assertEqual(activate_id1, triggers[2].id)
#
#            self.assertIs(self.tm.triggers[activate_id0], triggers[1])
#            self.assertIs(self.tm.triggers[activate_id1], triggers[2])
#
#        # Verify activate triggers outside of the tree
#        self.assertEqual(trigger4.effects[0].trigger_id, trigger5.id)
#