# How to create triggers for all players
This is a tutorial on how to create triggers for all players by combining 2 elements: Basic loop iteration from example 1 and `copy_trigger` function from example 2.
## Step by step
```
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.trigger_lists import *

# File & Folder setup - Declare your scenario directory path
scenario_folder = "C:/Users/Admin/Games/Age of Empires 2 DE/76561198148041091/resources/_common/scenario/"

# Source scenario to work with
input_path = scenario_folder + "ScenarioParser - EditTriggers.aoe2scenario"
output_path = scenario_folder + "ScenarioParser - EditTriggersAllPlayers Parser Result.aoe2scenario"

# declare scenario class
source_scenario = AoE2DEScenario.from_file(input_path)

# declare trigger manager to work with variables and triggers
source_trigger_manager = source_scenario.trigger_manager

# Start writing your code here:
# copy the first trigger and edit it
triggerSource = source_trigger_manager.triggers[0]
triggerSource.name = "example "
triggerSource.new_effect.activate_trigger(trigger_id=triggerSource.trigger_id + 1)
for playerId in range (1, 9, 1):
    triggerCopy = source_trigger_manager.copy_trigger(trigger_select=triggerSource.trigger_id + playerId - 1)
    triggerCopy.enabled = False
    triggerCopy.name = triggerSource.name + " P" + str(playerId)
    triggerCopy.get_condition(0).timer = 10
    triggerCopy.get_effect(0).source_player = playerId
    triggerCopy.get_effect(1).message = "An imposter king has arrived!"
    triggerCopy.get_effect(2).source_player = playerId
    triggerCopy.get_effect(3).trigger_id = triggerCopy.trigger_id + 1
    print(triggerCopy.trigger_id)
triggerCopy.remove_effect(3)


# Final step: write a modified scenario class to a new scenario file
source_scenario.write_to_file(output_path)
```
### 1. Create your scenario
Use the scenario provided in the example folder called `ScenarioParser - EditTriggers.aoe2scenario`, or change the `input_path` to your scenario name.
### 2. Manipulate existing triggers and implement looping incremental changes
![image](https://user-images.githubusercontent.com/40296674/150691285-4f219673-786e-4b6c-9779-49f01b6ffe25.png)

From combining elements from Example 1 and Example 2, you can copy any existing triggers and repeating the process, changing its condition and effect attributes value to every players, from 1 to 8!

With a simple example trigger like this, you can copy it's existing data and edit the trigger's data, as well as it's condition and effects. You can also add an `if else` statements to change the text color according to the current player's `playerId` in the loop iteration like so:

```
    if playerId == 1
        triggerCopy.get_effect(1).message = "<BLUE>An imposter king has arrived!"
    elif playerId == 2:
        triggerCopy.get_effect(1).message = "<RED>An imposter king has arrived!"
    # ...
```
You need to use `copy_trigger` function and set the `trigger_select` attribute to be the id of the previous last copied trigger (ex: if the current loop iteration has `playerId` = 3, you need to copy the id of the trigger with `playerId` = 2), because a copied trigger will be added after the copied trigger in the list, but not appending the trigger to the end of the list.

And so, the trigger id the `trigger_select` attribute should take into accounts is the `triggerSource` id, plus `playerId` minus 1.
```
    triggerCopy = source_trigger_manager.copy_trigger(trigger_select=triggerSource.trigger_id + playerId - 1)
```

And finally, write your block of code and replace any attribute with player's number to be `playerId`, and remove an activate trigger effect in the last trigger.

```
for playerId in range (1, 9, 1):
    triggerCopy = source_trigger_manager.copy_trigger(trigger_select=triggerSource.trigger_id + playerId - 1)
    triggerCopy.enabled = False
    triggerCopy.name = triggerSource.name + " P" + str(playerId)
    triggerCopy.get_condition(0).timer = 10
    triggerCopy.get_effect(0).source_player = playerId
    triggerCopy.get_effect(1).message = "An imposter king has arrived!"
    triggerCopy.get_effect(2).source_player = playerId
    triggerCopy.get_effect(3).trigger_id = triggerCopy.trigger_id + 1
    print(triggerCopy.trigger_id)
triggerCopy.remove_effect(3)
```

![image](https://user-images.githubusercontent.com/40296674/150970939-b9258077-47d5-458b-a5c5-80e799724341.png)



There are a lot more examples, and this is just one of them. Check the main library to [learn more](https://github.com/KSneijders/AoE2ScenarioParser)

