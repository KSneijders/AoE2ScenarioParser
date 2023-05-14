# Triggers

You can use the trigger manager to add, remove edit and view triggers and variables.

## Adding

Here's an example of how to create (add) a trigger and add a condition and effect to it:

```py
from AoE2ScenarioParser.scenarios.aoe2_scenario import AoE2Scenario
from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.datasets.units import UnitInfo

# File & Folder setup
# Define paths to the scenario folder.
# You can find this folder by opening AoE2:DE and going to scenarios and clicking on 'open folder'
scenario_folder = "your/path/to/the/scenario/folder/"  # <-- Final slash is important
scenario_name = "name_of_your_scenario"

# Define Scenario file
scenario = AoE2Scenario.from_file(f"{scenario_folder}{scenario_name}.aoe2scenario")

# Add Trigger
trigger_manager = scenario.trigger_manager
trigger = trigger_manager.add_trigger("Trigger Name Here")

# Add Timer Condition
timer_condition = trigger.new_condition.timer(timer=20)

# Add Create Object Effect
create_paladin_effect = trigger.new_effect.create_object(
    object_list_unit_id=UnitInfo.PALADIN.ID,
    source_player=Player.ONE,
    location_x=5,
    location_y=4,
)

# Write to same folder with name + '_output'
scenario.write_to_file(f"{scenario_folder}{scenario_name}_output.aoe2scenario")
```

### Importing

Instead of directly adding triggers you can also import triggers from another scenario:

```py
from AoE2ScenarioParser.scenarios.aoe2_scenario import AoE2Scenario

# Define Scenario files
source_scenario = AoE2Scenario.from_file(path_to_the_source_file)
target_scenario = AoE2Scenario.from_file(path_to_the_target_file)

# Define Trigger Managers
source_trigger_manager = source_scenario.trigger_manager
target_trigger_manager = target_scenario.trigger_manager

# Import the triggers
# In this case all triggers from the source scenario are copied
# You can optionally set the index to which the imported triggers are set at
# Leaving this out will add the imported triggers to the end of the target scenario
# In the example below, the source triggers will be added BEFORE the target triggers due to the 0
target_trigger_manager.import_triggers(source_trigger_manager.triggers, 0)

target_scenario.write_to_file(path_to_output_file)
```

## Selecting

Selecting a trigger can be done using the `get_trigger` function in the TriggerManager `trigger_manager.get_trigger( ... )`. 
The function accepts 2 arguments. The first is a trigger identifier (named: `trigger`).
This can be an `int` representing the index of a trigger (the `trigger_id`).
The first argument can also be a Trigger object itself.

The second argument (named: `use_display_index`) is used to change the behaviour of the function.
When this is set to `True` (`False` by default) the `int` given in the first argument will be used to identify
the trigger using the **display** index instead of the normal index.

```py
# Examples:
trigger = trigger_manager.get_trigger(7)
trigger = trigger_manager.get_trigger(trigger_variable)
trigger = trigger_manager.get_trigger(4, use_display_index=True)
```

You can use the `get_summary_as_string` function to view these values without opening
the in-game editor. The code below includes the code above:

```py
print(trigger_manager.get_summary_as_string())

# Results in:
"""
Trigger Summary:
    Trigger Name Here    [Index: 0, Display: 0] (conditions: 1,  effects: 1)

Variables Summary:
    << No Variables >>
"""
```

As you can see, the trigger and display index can be seen in the
`[Index: x, Display: x]` part. These are the numbers you can use to
select triggers. Which would look like:

```py
# Define Scenario file
scenario = AoE2Scenario.from_file(read_file)

# Get Trigger
trigger_manager = scenario.trigger_manager
trigger = trigger_manager.get_trigger(0)
```

If you want to see the contents of the trigger you can do so by running the `get_content_as_string` function.  
This will result in the following (with the `create trigger` code):

```py
print(trigger_manager.get_content_as_string())

# Results in:
"""
Triggers:
    'Trigger Name Here' [Index: 0, Display: 0]:
        enabled: True
        looping: False
        conditions:
            timer [Index: 0, Display: 0]:
                timer: 20
                inverted: 0
        effects:
            create_object [Index: 0, Display: 0]:
                object_list_unit_id: UnitInfo.PALADIN.ID
                source_player: Player.ONE
                location_x: 5
                location_y: 4
                facet: 0

Variables:
    <<No Variables>>
"""
```

## Editing

When opening a file that already contains triggers you might want to
edit or even remove said triggers.

You can edit a trigger like so:

```py
trigger = trigger_manager.get_trigger(0)

trigger.name = "New Trigger Name"
trigger.description = "Awesome New Description!"
```

### Copy

Pretty simple and straightforward. It copies a trigger adding it at the
end of the trigger list. Selecting a trigger is done using the standard 
trigger identifiers

```py
copied_trigger = trigger_manager.copy_trigger(3)
```

This will result in a full (deep)copy of your trigger. The only parts
that are edited are its `id` and the name (added `" (copy)"`).

### Copy per player

Just like the `copy_trigger` function, this trigger makes a (deep) copy
of the given function. But, while copying, it'll change everything
player related. With this function comes great control. Below the usage
is shown:

```py
copied_triggers = trigger_manager.copy_trigger_per_player(
    from_player=Player.ONE,
    trigger=3,
    create_copy_for_players=[
        Player.TWO, Player.THREE, Player.FOUR  # Optional list
    ]
)
print(f"New trigger for Player Two: {copied_triggers[Player.TWO]}")
```

### Copy tree

This function copies the given trigger and all that are linked to this
one. The function searches all effects in the given trigger and selects
all triggers linked to it. It gets all triggers by taking the ids from
`(de)activate trigger` effects. This will result in the entire tree being
copied:

```py
trigger_manager.copy_trigger_tree(3)
```

### Copy tree per player

A combination of the `copy_trigger_per_player` and `copy_trigger_tree`
functions. This function copies the entire tree per player. Besides the
parameters that can be given to `copy_trigger_per_player` function, an
additional `group_triggers_by` parameter is included. This way you can
select in which order all the new triggers should be placed:

```py
trigger_manager.copy_trigger_tree_per_player(
    from_player=Player.ONE,
    trigger=3,
    group_triggers_by=GroupBy.PLAYER,  # Other options: GroupBy.BLANK and GroupBy.TRIGGER
)
```

## Removing

When removing a trigger you can select it the same way as when getting a
trigger using the get_trigger function. But on top of that
you can also use its reference:

```py
trigger_manager.remove_trigger(3)
trigger_manager.remove_trigger(trigger_object)
```

For removing effects and conditions it's very similar, but the
functions are accessed from the triggers themselves instead of the
trigger_manager. You can select the effect or condition you want to
remove using its index or reference:

```py
trigger = trigger_manager.get_trigger(0)

trigger.remove_effect(0)
trigger.remove_effect(effect)

trigger.remove_condition(0)
trigger.remove_condition(condition)
```
