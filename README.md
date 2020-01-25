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
Run the following pip command for installation:

    pip install AoE2ScenarioParser

# Usage
## Getting Started
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

---
&nbsp;  
&nbsp;  

## Adding triggers
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


---
&nbsp;  
&nbsp;  

## Viewing triggers

**Tip:** As you know you can change the order of triggers in the in-game editor *(Not possible with this package (yet))*. When using the *view, edit and delete* functionality you can choose to select a trigger by `index` or by `display_index`. `display_index` is the index in which the triggers are shown in the in-game editor. The `index` is the index in which they were created. Both start from 0.

There's multiple ways to check out triggers and their contents. When editing or deleting a trigger you'll need an index. This can be the actual index or the display index.

You can use the following function to generate a simple overview of the triggers.

```python
trigger_object.get_trigger_overview_as_string()

# This returns the following (As String):
Trigger Overview:
	Init Trigger    [Index: 0, Display: 0]	(conditions: 2,  effects: 1)
	Spawn Wave 1    [Index: 1, Display: 1]	(conditions: 2,  effects: 7)
	Spawn Wave 2    [Index: 2, Display: 2]	(conditions: 1,  effects: 7)
```

If you want to know all specifics about a trigger you can use the functions below. 

```python
trigger_object.get_trigger_as_string(0)
# Or:
trigger_object.get_trigger_as_string_by_display_index(0)

# These functions return the following (As String):
'Init Trigger' [Index: 0, Display: 0]:
    enabled: True
    looping: False
    description: 'This is the initialisation trigger. '
    conditions:
        timer:
            timer: 5
            inverted: 0
        variable_value:
            amount_or_quantity: 1
            inverted: 0
            variable: 0
            comparison: 0
    effects:
        activate_trigger:
            trigger_id: 1

# You can also use the function below to generate the same as above but then for all the triggers.
trigger_object.get_content_as_string()
```

---
&nbsp;  
&nbsp;  

## Editing or removing triggers
When opening a file that already contains triggers you might want to edit or even remove said triggers. *Please note that it's not possible to remove specific conditions or effects (yet).*

You can edit a trigger like so:
```python
trigger = trigger_object.get_trigger(0)
# Or:
trigger = trigger_object.get_trigger_by_display_index(0)

# These functions are the same when adding new triggers.
trigger.set_name("New Trigger Name")
trigger.set_description("Awesome New Description!")
```

For removing it basically works the same:
```python
# Once again remember to not save to a different file. Especially when removing (important) triggers.
trigger_object.delete_trigger(0)
trigger_object.delete_trigger_by_display_index(0)
```

---
&nbsp;  
&nbsp;  

## Saving
When you are done, you can write all your progress to a file like so:

```python
scenario.write_to_file(output_path)
```
Please remember to use a different path than your input file. This way you have a backup file incase you encounter a bug or made a mistake.


---
&nbsp;  
&nbsp;  

# Authors
-  Kerwin Sneijders (Main Author)

# License
## Code
GNU General Public License v3.0: Please see [the LICENSE file](https://github.com/KSneijders/AoE2ScenarioParser/blob/dev/LICENSE).