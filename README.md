# AoE2ScenarioParser
This is a project for editing parts of an `aoe2scenario` file from **Age of Empires 2 
Definitive Edition** outside of the in-game editor. 


# Progress
Current up-to-date progress can be found on the [Trello](https://trello.com/b/7SNm3gXj/aoe2-de-parser) board. 

### Features:
- Reading any `aoe2scenario` file from AoE2:DE.
- Writing said file back to an `aoe2scenario` file.
- Add Triggers, Conditions and effects to any `aoe2scenario` file.

### Bugs:
- None

Please report any bugs you find to the [github issue board](https://github.com/KSneijders/AoE2ScenarioParser/issues).

# Installation
~~Run the following pip command for installation:~~ 

# Usage
To start, import the main `AoE2Scnerio` class from the module:

```python
from AoE2ScenarioParser.aoe2_scenario import AoE2Scenario
```
Also import the two datasets for ease of use:

```python
from AoE2ScenarioParser.datasets import effects
from AoE2ScenarioParser.datasets import conditions
```

Define the file you will be reading and the path you will be writing to.  
Note: *Creating folders isn't supported at this time. Please use an excisting folder.*  

```python
# It is recommended to not overwrite your file. This way you can keep a backup!
input_path = "File/Path/To/Your/Input/File"
output_path = "File/Path/To/Your/Output/File"
```

Now create the object with the filename as parameter. 

```python
scenario = AoE2Scenario(input_path)
```

You can retrieve access to the triggers using the object_manager. 

```python
trigger_object = scenario.object_manager.get_triggers()
```
    
Now the best part, adding triggers! You can add triggers easily. You can change all parts of the trigger using functions (type "trigger.set_" and the autocomplete will show you a list of options.).  Eventually there will be a API docs. 

```python
trigger = trigger_object.add_trigger("Trigger :)")
trigger.set_description("This is a great description!")
```

To add conditions or effects, just call the method `add_condition` and `add_effect`. You can use the dataset to figure give the function the right ID. If you're unsure about what parameters are available in every trigger, check the docs of the condition. Click on `conditions.chance` and show the docs (CTRL + Q in PyCharm). It will show you: "Parameters for the chance condition are: amount_or_quantity". Now use the function `set_amount_or_quantity` to apply the right value.

The example shows: A trigger with 25% chance of showing a message. 

```python
condition = trigger.add_condition(conditions.chance)
condition.set_amount_or_quantity(25)

effect = trigger.add_effect(effects.display_instructions)
effect.set_player_source(1)
effect.set_display_time(11)
effect.set_message("This message was set using AoE2ScenarioParser!")
```
    
When you are done, you can write all your progress to a file like so:

```python
scenario.write_to_file(output_path)
```

# License
## Code
GNU General Public License v3.0: Please see [the LICENSE file](https://github.com/KSneijders/AoE2ScenarioParser/blob/dev/LICENSE).