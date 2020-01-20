import resources.settings as settings
from src.aoe2_scenario import AoE2Scenario
from src.datasets import effect as effects
from src.datasets import condition as conditions

scenario = AoE2Scenario(settings.file.get("name"))
triggers = scenario.object_manager.get_triggers()

trigger = triggers.add_trigger("Trigger :)")
trigger.set_description("This is a great description!")

condition = trigger.add_condition(conditions.chance)
condition.set_amount_or_quantity(25)

effect = trigger.add_effect(effects.display_instructions)
effect.set_player_source(1)
effect.set_display_time(11)
effect.set_message("This message was set using python parsing!")

scenario.write_to_file(settings.file.get("output"))
