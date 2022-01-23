# How to copy / edit triggers
This is a tutorial on how to manipulate existing triggers using `copy_trigger`, `get_condition` and `get_effect`.
## Step by step
```
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.trigger_lists import *

# File & Folder setup - Declare your scenario directory path
scenario_folder = "C:/Users/Admin/Games/Age of Empires 2 DE/76561198148041091/resources/_common/scenario/"

# Source scenario to work with
input_path = scenario_folder + "ScenarioParser - EditTriggers.aoe2scenario"
output_path = scenario_folder + "ScenarioParser - EditTriggers Parser Result.aoe2scenario"

# declare scenario class
source_scenario = AoE2DEScenario.from_file(input_path)

# declare trigger manager to work with variables and triggers
source_trigger_manager = source_scenario.trigger_manager

# Start writing your code here:
# copy the first trigger and edit it
triggerSource = source_trigger_manager.triggers[0]
triggerSource.new_effect.activate_trigger(trigger_id=triggerSource.trigger_id + 1)
triggerCopy = source_trigger_manager.copy_trigger(trigger_select=triggerSource.trigger_id)
triggerCopy.enabled = False
triggerCopy.get_condition(0).timer = 10
triggerCopy.get_effect(0).source_player = 2
triggerCopy.get_effect(1).message = "<RED> An imposter king has arrived!"
triggerCopy.get_effect(2).source_player = 2
triggerCopy.remove_effect(3)

# Final step: write a modified scenario class to a new scenario file
source_scenario.write_to_file(output_path)

```
### 1. Create your scenario
Create an empty scenario in the editor and save it as "ScenarioParser - EditTriggers", or change the `input_path` to your scenario name.
### 2. Manipulate existing triggers
![image](https://user-images.githubusercontent.com/40296674/150691285-4f219673-786e-4b6c-9779-49f01b6ffe25.png)

This is a fun example, the source trigger will create a fat king and announce his presence, and then move him to a degsinated area.

With a simple example trigger like this, you can copy it's existing data and edit the trigger's data, as well as it's condition and effect.

In Python and many programming language, the first object of any list has an index of 0, so you can take the first trigger out of the trigger list like so:
```
triggerSource = source_trigger_manager.triggers[0]
```
![image](https://user-images.githubusercontent.com/40296674/150691454-34cd048e-fb0b-44e5-a852-39dd14bbfd7c.png)

The first trigger will activate the copied trigger. To do that, use `new_effect` function to add a new `activate trigger` effect to `triggerSource`:
```
triggerSource.new_effect.activate_trigger(trigger_id=triggerSource.trigger_id + 1)
```

After that, use copy_trigger to copy the structure of a trigger, including all of its property, conditions and effects, one by one.

```
triggerCopy = source_trigger_manager.copy_trigger(trigger_select=triggerSource.trigger_id)
triggerCopy.enabled = False
triggerCopy.get_condition(0).timer = 10
triggerCopy.get_effect(0).source_player = 2
triggerCopy.get_effect(1).message = "<RED> An imposter king has arrived!"
triggerCopy.get_effect(2).source_player = 2
triggerCopy.remove_effect(3)
```

The first trigger will activate the new copy trigger, so we'll put the new copied trigger's state to `False`.

You can edit each condition and effect by calling it's id using the function `get_condition` and `get_effect`.

The king spawned in has been changed to Player 2. Now we just need to remove the last `Activate Trigger` effect by using `remove_effect`.

And Voila!

![image](https://user-images.githubusercontent.com/40296674/150691897-0ac90488-331b-4c46-b796-b12e3cc659db.png)


There are a lot more examples, and this is just one of them. Check the main library to [learn more](https://github.com/KSneijders/AoE2ScenarioParser)

