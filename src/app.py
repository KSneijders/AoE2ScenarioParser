import resources.settings as settings
from src.aoe2_scenario import AoE2Scenario
from src.datasets import effect as effects
from src.datasets import condition as conditions

# for x in condition.parameters[condition.chance]:
#     print(condition.naming_conversion[x])
#
# exit()

scenario = AoE2Scenario(settings.file.get("name"))
triggers = scenario.object_manager.get_triggers()

trigger = triggers.add_trigger("Test1")
trigger.set_description("This is a great description!")

condition = trigger.add_condition(conditions.chance)
condition.data_dict['amount_or_quantity'] = 25

effect = trigger.add_effect(effects.display_instructions)
effect.data_dict['player_source'] = 1
effect.data_dict['display_time'] = 10
effect.data_dict['message'] = "This message was set using python parsing!"

scenario.object_manager.reconstruct()
scenario.write_to_file(settings.file.get("output"))
