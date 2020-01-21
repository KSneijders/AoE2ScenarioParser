from AoE2ScenarioParser.aoe2_scenario import AoE2Scenario
from AoE2ScenarioParser.datasets import effects
from AoE2ScenarioParser.datasets import conditions

input_path = "C:\\Users\\Kerwin Sneijders\\Games\\Age of Empires 2 DE\\" \
             "76561198140740017\\resources\\_common\\scenario\\Tiny Arabia.aoe2scenario"
output_path = "C:\\Users\\Kerwin Sneijders\\Games\\Age of Empires 2 DE\\" \
              "76561198140740017\\resources\\_common\\scenario\\generated_from_parsed.aoe2scenario"

scenario = AoE2Scenario(input_path)
triggers = scenario.object_manager.get_triggers()

trigger = triggers.add_trigger("Trigger :)")
trigger.set_description("This is a great description!")

condition = trigger.add_condition(conditions.chance)
condition.set_amount_or_quantity(25)

effect = trigger.add_effect(effects.display_instructions)
effect.set_player_source(1)
effect.set_display_time(11)
effect.set_message("This message was set using python parsing!")

scenario.write_to_file(output_path)
