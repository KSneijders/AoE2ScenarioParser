from AoE2ScenarioParser.aoe2_scenario import AoE2Scenario
from AoE2ScenarioParser.datasets.effects import Effect

scenario_folder = "folder_path"

filename2 = filename = "trigger_with_effect"

scenario = AoE2Scenario.from_file(f'{scenario_folder}{filename}.aoe2scenario')
timestamp = scenario._parsed_header['FileHeaderPiece'].timestamp_of_last_save
scenario._debug_write_from_source(filename, "hd", write_bytes=False)
scenario._debug_byte_structure_to_file("_structure")

filename = "no_effect_or_trigger"
scenario = AoE2Scenario.from_file(f'{scenario_folder}{filename}.aoe2scenario')

scenario._parsed_header['FileHeaderPiece'].timestamp_of_last_save = timestamp
scenario._parsed_data['DataHeaderPiece'].filename = f"{filename2}.aoe2scenario"

trigger_manager = scenario.trigger_manager
trigger = trigger_manager.add_trigger("Trigger 0")
trigger.add_effect(Effect.DISPLAY_INSTRUCTIONS, message="ABC")
scenario.write_to_file(f'{scenario_folder}{filename}___.aoe2scenario')

scenario = AoE2Scenario.from_file(f'{scenario_folder}{filename}___.aoe2scenario')
scenario._debug_write_from_source(filename, "hd", write_bytes=False)
scenario._debug_byte_structure_to_file("_structure2")
