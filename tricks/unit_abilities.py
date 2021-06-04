from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.datasets.trigger_lists import PanelLocation
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

# File & Folder setup
scenario_folder = "C:/Users/Kerwin Sneijders/Games/Age of Empires 2 DE/76561198140740017/resources/_common/scenario/"
read_file = scenario_folder + "unitTest.aoe2scenario"
write_to_file = scenario_folder + "unitTestResult.aoe2scenario"

scenario = AoE2DEScenario.from_file(read_file)

trigger_manager = scenario.trigger_manager
unit_manager = scenario.unit_manager

# Use 9 for projectile.
unit_to_be_garrisoned = UnitInfo.ARCHER.ID
# Anything < 0, but not -1 as that's default
unit_to_be_garrisoned_id = -20

unit_manager.add_unit(PlayerId.ONE, UnitInfo.PALADIN.ID, 20, 5, reference_id=0)

unit_manager.add_unit(PlayerId.ONE, unit_to_be_garrisoned, 0, 0, garrisoned_in_id=0,
                      reference_id=unit_to_be_garrisoned_id)
unit_manager.add_unit(PlayerId.ONE, unit_to_be_garrisoned, 119, 119, garrisoned_in_id=0,
                      reference_id=unit_to_be_garrisoned_id)

trigger = trigger_manager.add_trigger("DetectUnitUngarrisoned", looping=True)

trigger.new_condition.objects_in_area(
    quantity=1,
    object_list=unit_to_be_garrisoned,
    source_player=PlayerId.ONE,
    area_x1=0,
    area_y1=0,
    area_x2=10,
    area_y2=10
)

trigger.new_effect.display_instructions(
    object_list_unit_id=HeroInfo.EMPEROR_IN_A_BARREL.ID,
    source_player=PlayerId.ONE,
    display_time=1,
    instruction_panel_position=PanelLocation.TOP,
    message="DETECTED!",
)

# Works weird (only with units)
trigger.new_effect.teleport_object(
    object_list_unit_id=unit_to_be_garrisoned,
    source_player=PlayerId.ONE,
    location_x=100,
    location_y=100,
    area_x1=0,
    area_y1=0,
    area_x2=10,
    area_y2=10,
)

# Works consistently (also with projectiles)
trigger.new_effect.patrol(
    object_list_unit_id=unit_to_be_garrisoned,
    source_player=PlayerId.ONE,
    location_x=100,
    location_y=100,
    area_x1=0,
    area_y1=0,
    area_x2=10,
    area_y2=10,
)

scenario.write_to_file(write_to_file)
