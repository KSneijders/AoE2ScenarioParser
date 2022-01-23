# How to add triggers
This is a tutorial on how to add triggers using the Parser. Simply use the template python script or use your own script once you got your scenario file set up.
## Step by step
```
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.trigger_lists import *


# File & Folder setup - Declare your scenario directory path
scenario_folder = "C:/Users/Admin/Games/Age of Empires 2 DE/76561198148041091/resources/_common/scenario/"

# Source scenario to work with
input_path = scenario_folder + "ScenarioParser - AddTriggers.aoe2scenario"
output_path = scenario_folder + "ScenarioParser - AddTriggers Parser Result.aoe2scenario"

# declare scenario class
source_scenario = AoE2DEScenario.from_file(input_path)

# declare trigger manager to work with variables and triggers
source_trigger_manager = source_scenario.trigger_manager

# Start writing your code here:
# a loop iteration: triggerId will start from 0, each iteration increase triggerId by 1, until triggerId reached 9999
for triggerId in range(0, 9999, 1):
    trigger1 = source_trigger_manager.add_trigger("Trigger #" + str(triggerId), enabled=True, looping=False)
    trigger1.new_condition.none()
    trigger1.new_effect.none()

# Final step: write a modified scenario class to a new scenario file
source_scenario.write_to_file(output_path)
```
### 1. Create your scenario
Create an empty scenario in the editor and save it as "ScenarioParser - AddTriggers", or change the `input_path` to your scenario name.
### 2. Create mass triggers
In python, you can create a loop iteration to run lines of code on loop for `n` amount of times. This is one of many different examples.

There are many other function (such as switch case to check if multiple conditions matches something, if else statements, etc...)

From the code writing section, add a loop iteration like so:
```
# a loop iteration: triggerId will start from 0, each iteration increase triggerId by 1, until triggerId reached 9999
amountOfLoop = 9999
for triggerId in range(0, amountOfLoop, 1):
  # your running code
```
The first number inside the brackets will be the loop starting index, which is `triggerId = 0`. After a loop, `triggerId` will be incremented by 1. This process will repeat itself until `triggerId` value reached 9999.

Inside the iteration loop, you can start writing functions to create your own trigger:
```
# a loop iteration: triggerId will start from 0, each iteration increase triggerId by 1, until triggerId reached 9999
amountOfLoop = 9999
for triggerId in range(0, amountOfLoop, 1):
    trigger0 = source_trigger_manager.add_trigger("----Trigger block" + str(triggerId) + "----", enabled=False,
                                                  looping=False)
    trigger1 = source_trigger_manager.add_trigger("Trigger #" + str(trigger0.trigger_id + 1), enabled=True,
                                                  looping=False)
    trigger1.new_condition.none()
    trigger1.new_effect.none()
    trigger2 = source_trigger_manager.add_trigger("Trigger #" + str(trigger0.trigger_id + 2), enabled=True,
                                                  looping=False)
    trigger2.new_condition.own_objects(object_type=ObjectClass.CIVILIAN,
                                       quantity=1, source_player=1)
    trigger2.new_effect.send_chat(message="test string #" + str(triggerId))
```
![image](https://user-images.githubusercontent.com/40296674/150690801-c9850853-e1d0-497d-bd23-e40006d9fa87.png)

In this example, every loop will create a block of triggers. To add a trigger, refer to your `source_trigger_manager` object and use the `add_trigger` function. The first `trigger0` in the block is just for labeling.

The second `trigger1` create a test trigger, and the trigger name will be its trigger id. You can add new effect or condition by using the respective `new_effect` and `new_condition` function.

The third `trigger2` create another trigger, and the trigger name will be its trigger id. Additionally, 2 new condition and effect has been added, this trigger will send a chat to player 1 if they have one villager in the map!

The process will be repeated 9999 times. As you can see, this can cause heavy burden on your CPU. But this is just a fun example!

![image](https://user-images.githubusercontent.com/40296674/150690999-849f6f44-43af-4a25-af1c-a3adbcc36cda.png)




There are a lot more examples, and this is just one of them. Check the main library to [learn more](https://github.com/KSneijders/AoE2ScenarioParser)

