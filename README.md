# AoE2ScenarioParser
This is a project for editing parts of an `aoe2scenario` file from **Age of Empires 2 
Definitive Edition** outside of the in-game editor. 


# Progress
Current up-to-date progress can be found on the [Trello](https://trello.com/b/7SNm3gXj/aoe2-de-parser) board. 

### Features:
- Reading `aoe2scenario` files from AoE2:DE (Check supported versions below).
- Writing said file back to an `aoe2scenario` file.
- Triggers
  - View (Specific or all) Triggers, Conditions and Effects.
  - Adding Triggers, Conditions and Effects.
  - Editing Triggers. (Only **adding** Conditions and Effects is currently supported)
  - Deleting Triggers.

## Bugs:
- None...? Surely not!?. 

Please report any bugs you find to the [github issue board](https://github.com/KSneijders/AoE2ScenarioParser/issues).

## Support:
This repository supports the `DE` scenario versions:
- 1.36
- 1.37 (Game update: [35584](https://www.ageofempires.com/news/aoe2de-update-35584/))

# Installation
Run the following pip command for installation:v

    pip install AoE2ScenarioParser

# Usage
## DISCLAIMER: NO SYNTAX OR STRUCTURE IS SET IN STONE AND COULD CHANGE AT ANY TIME
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
trigger_manager = scenario.object_manager.get_trigger_manager()
```

---
&nbsp;  

## Adding triggers
Now the best part, adding triggers! You can add triggers easily. You can change all parts of the trigger using functions (type "trigger.set_" and the autocomplete will show you a list of options.).  Eventually there will be a API docs. 

```python
trigger = trigger_manager.add_trigger("Trigger :)")
trigger.description = "This is a great description!"
```

To add conditions or effects, just call the method `add_condition` and `add_effect`. You can use the dataset to figure give the function the right ID. If you're unsure about what parameters are available in every trigger, check the docs of the condition. Click on `conditions.chance` and show the docs (CTRL + Q in PyCharm). It will show you: "Parameters for the chance condition are: amount_or_quantity". Now use the function `set_amount_or_quantity` to apply the right value.

The example shows: A trigger with 25% chance of showing a message. 

```python
condition = trigger.add_condition(conditions.chance)
condition.amount_or_quantity = 25

effect = trigger.add_effect(effects.display_instructions)
effect.player_source = 1
effect.display_time = 11
effect.message = "This message was set using AoE2ScenarioParser!"
```


---
&nbsp;  

## Viewing triggers

**Tip:** As you know you can change the order of triggers in the in-game editor *(Not possible with this package (yet))*. When using the *view, edit and delete* functionality you can choose to select a trigger by `index` or by `display_index`. `display_index` is the index in which the triggers are shown in the in-game editor. The `index` is the index in which they were created. Both start from 0.

There's multiple ways to check out triggers and their contents. When editing or deleting a trigger you'll need an index. This can be the actual index or the display index.

You can use the following function to generate a simple overview of the triggers.

```python
trigger_manager.get_summary_as_string()

# This returns the following (As String):
Trigger Summary:
	Init Trigger    [Index: 0, Display: 0]	(conditions: 2,  effects: 1)
	Spawn Wave 1    [Index: 1, Display: 1]	(conditions: 2,  effects: 7)
	Spawn Wave 2    [Index: 2, Display: 2]	(conditions: 1,  effects: 7)
```

If you want to know all specifics about a trigger you can use the functions below. 

```python
trigger_manager.get_trigger_as_string(trigger_id=0)
trigger_manager.get_trigger_as_string(display_index=0)
# You can also request the id from a trigger object:
trigger_manager.get_trigger_as_string(trigger_id=trigger.trigger_id)

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
```
You can also use this function to generate the above string but for all triggers at once.
```python
trigger_manager.get_content_as_string()
```

---
&nbsp;  

## Editing or removing triggers
When opening a file that already contains triggers you might want to edit or even remove said triggers. *Please note that it's not possible to remove specific conditions or effects (yet).*

You can edit a trigger like so:
```python
# Using it's ID
trigger = trigger_manager.get_trigger(trigger_id=0)
# Or display index (not both)
trigger = trigger_manager.get_trigger(display_index=0)

# These functions are the same when adding new triggers.
trigger.name = "New Trigger Name"
trigger.description = "Awesome New Description!"
```

For removing it basically works the same:
```python
# Once again remember to not save to a different file. Especially when removing (important) triggers.
trigger_manager.delete_trigger(0)
trigger_manager.delete_trigger_by_display_index(0)
```

---
&nbsp;  

## Datasets (Buildings, Units and Techs)
The project currently contains 4 datasets. These are currently pretty basic and only contain the in-editor options. The following datasets are included in the project:
- buildings
- units
- technologies (techs)
- terrains (Not very usefull atm)

*Please note*: There are also datasets for `effects` and `conditions` but those are already explained in this document.

You can use them like so:
```python
from AoE2ScenarioParser.datasets import techs, units, buildings

# Techs
techs.loom  # 22
techs.imperial_age  # 103
# Units
units.archer  # 4
units.man_at_arms  # 75
units.cannon_galleon  # 420
# Buildings
buildings.krepost  # 1251
buildings.wonder  # 276
```
You can also use strings to get the IDs
```python
techs.get_tech_id_by_string("loom")  # 22
units.get_unit_id_by_string("man_at_arms")  # 75
buildings.get_building_id_by_string("farm")  # 50
```
Security note:
---
These functions are implented for ease of use. Not security. They use `eval()` and should not be used in any server environment where others have access to the input of these functions. For more information please check out [this Stack Overflow answer](https://stackoverflow.com/a/661128/7230293).

Of course, you can combine that with `triggers` like so:
```python
trigger = triggers.add_trigger("Create Man@Arms")

effect = trigger.add_effect(effects.create_object)  # effects dataset
effect.object_list_unit_id = units.man_at_arms  # units dataset
effect.player_source = 1
effect.location_x = 0
effect.location_y = 0
```

---
&nbsp;  

## Saving
When you are done, you can write all your progress to a file like so:

```python
scenario.write_to_file(output_path)
```
Please remember to use a different path (filename) than your input file. This way you have a backup file incase you encounter a bug.


---
&nbsp;  

# Authors
-  Kerwin Sneijders (Main Author)

# License
## Code
GNU General Public License v3.0: Please see [the LICENSE file](https://github.com/KSneijders/AoE2ScenarioParser/blob/dev/LICENSE).
