from AoE2ScenarioParser.aoe2_scenario import AoE2Scenario
from AoE2ScenarioParser.datasets.conditions import Condition
from AoE2ScenarioParser.datasets.effects import Effect
from AoE2ScenarioParser.datasets.heroes import Hero
from AoE2ScenarioParser.datasets.players import Player
from AoE2ScenarioParser.datasets.trigger_lists import PanelLocation
from AoE2ScenarioParser.datasets.units import Unit


# File & Folder setup
scenario_folder = "C:/Users/Kerwin Sneijders/Games/Age of Empires 2 DE/76561198140740017/resources/_common/scenario/"
read_file = scenario_folder + "unitTest.aoe2scenario"
write_to_file = scenario_folder + "unitTestResult.aoe2scenario"

scenario = AoE2Scenario(read_file)

trigger_manager = scenario.trigger_manager
unit_manager = scenario.unit_manager

# Use 9 for projectile.
unit_to_be_garrisoned = Unit.ARCHER
# Anything < 0, but not -1 as that's default
unit_to_be_garrisoned_id = -20

unit_manager.add_unit(Player.ONE, Unit.PALADIN, 20, 5, reference_id=0)

unit_manager.add_unit(Player.ONE, unit_to_be_garrisoned, 0, 0, garrisoned_in_id=0,
                      reference_id=unit_to_be_garrisoned_id)
unit_manager.add_unit(Player.ONE, unit_to_be_garrisoned, 119, 119, garrisoned_in_id=0,
                      reference_id=unit_to_be_garrisoned_id)

# trigger = trigger_manager.add_trigger("ChangeGraphic")
# effect = trigger.add_effect(Effect.CHANGE_OBJECT_ICON)
# effect.object_list_unit_id_2 = Hero.EMPEROR_IN_A_BARREL
# effect.selected_object_id = unit_to_be_garrisoned_id

trigger = trigger_manager.add_trigger("DetectUnitUngarrisoned")
trigger.looping = True

condition = trigger.add_condition(Condition.OBJECT_IN_AREA)
condition.amount_or_quantity = 1
condition.object_list = unit_to_be_garrisoned
condition.source_player = Player.ONE
condition.area_1_x = 0
condition.area_1_y = 0
condition.area_2_x = 10
condition.area_2_y = 10

effect = trigger.add_effect(Effect.DISPLAY_INSTRUCTIONS)
effect.object_list_unit_id = Hero.EMPEROR_IN_A_BARREL
effect.source_player = Player.ONE
effect.display_time = 1
effect.instruction_panel_position = PanelLocation.TOP
effect.message = "DETECTED!"

# Works weird (only with units)
effect = trigger.add_effect(Effect.TELEPORT_OBJECT)
effect.object_list_unit_id = unit_to_be_garrisoned
effect.source_player = Player.ONE
effect.location_x = 100
effect.location_y = 100
effect.area_1_x = 0
effect.area_1_y = 0
effect.area_2_x = 10
effect.area_2_y = 10

# Works consistently (also with projectiles)
effect = trigger.add_effect(Effect.PATROL)
effect.object_list_unit_id = unit_to_be_garrisoned
effect.source_player = Player.ONE
effect.location_x = 100
effect.location_y = 100
effect.area_1_x = 0
effect.area_1_y = 0
effect.area_2_x = 10
effect.area_2_y = 10

scenario.write_to_file(write_to_file, log_reconstructing=True)
