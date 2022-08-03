# Messages

You can use the message manager to edit the text fields in the `Messages` tab in the in-game editor.

## Editing

Here's an example of how to edit all the fields in the message manager.

```py
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

# File & Folder setup
# Define paths to the scenario folder.
# You can find this folder by opening AoE2:DE and going to scenarios and clicking on 'open folder'
scenario_folder = "your/path/to/the/scenario/folder/"  # <-- Final slash is important
scenario_name = "name_of_your_scenario"

# Define Scenario file
scenario = AoE2DEScenario.from_file(f"{scenario_folder}{scenario_name}.aoe2scenario")

message_manager = scenario.message_manager

message_manager.instructions  = "Do this. Do that... please."
message_manager.hints         = "Don't build 3 Archery Ranges on a neutral island. ¯\_(ツ)_/¯"
message_manager.history       = "* Old man voice * Back in my day we .."
message_manager.loss          = "Better luck next time!"
message_manager.scouts        = "The amount of wood on this map... It's all I can see..."
message_manager.victory       = "VICTORY IS OURS!"

# Write to same folder with name + '_output'
scenario.write_to_file(f"{scenario_folder}{scenario_name}_output.aoe2scenario")
```
