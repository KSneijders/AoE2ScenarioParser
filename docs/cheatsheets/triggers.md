# Triggers

You can use the trigger manager to add, remove edit and view triggers
and variables.

## Adding

Here's an example of how to create (add) a trigger and add a condition
and effect to it:

```py
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.datasets.units import UnitInfo

# File & Folder setup
# Define paths to the scenario folder.
# You can find this folder by opening AoE2:DE and going to scenarios and clicking on 'open folder'
scenario_folder = "your/path/to/the/scenario/folder/"  # <-- Final slash is important
scenario_name = "name_of_your_scenario"

# Define Scenario file
scenario = AoE2DEScenario.from_file(f"{scenario_folder}{scenario_name}.aoe2scenario")

# Add Trigger
trigger_manager = scenario.trigger_manager
trigger = trigger_manager.add_trigger("Trigger Name Here")

# Add Timer Condition
timer_condition = trigger.new_condition.timer(timer=20)

# Add Create Object Effect
create_paladin_effect = trigger.new_effect.create_object(
    object_list_unit_id=UnitInfo.PALADIN.ID,
    source_player=PlayerId.ONE,
    location_x=5,
    location_y=4,
)

# Write to same folder with name + '_output'
scenario.write_to_file(f"{scenario_folder}{scenario_name}_output.aoe2scenario")
```

### Importing

Instead of directly adding triggers you can also import triggers from another scenario:

```py
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

# Define Scenario files
source_scenario = AoE2DEScenario.from_file(path_to_the_source_file)
target_scenario = AoE2DEScenario.from_file(path_to_the_target_file)

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

Selecting a trigger can be done using the `get_trigger` function. The
function accepts 1 argument, a `TriggerSelect` (Alias: `TS`) object.  

!!! Tip "For an index, just use an integer" 
    Instead of `TS.index(4)` you can just use `4`. 
    Integers are used in the same way as `TS.index(4)` for ease of use

You can import `TS` (or `TriggerSelect`) like so:

```py
from AoE2ScenarioParser.objects.support.trigger_select import TS
from AoE2ScenarioParser.objects.support.trigger_select import TriggerSelect
```

The constructor of `TriggerSelect` accepts 3 arguments, `trigger_index`,
`display_index` and `trigger`.

-   The `trigger_index` expects the trigger
    ID of a trigger. This is the a number related to the order of creation
    starting from 0.
-   The `display_index` expects the display ID of a
    trigger. This is the a number related to the display order in the
    in-game editor.
-   The `trigger` expects a trigger object. Read further
    below on how to create or select one.

```py
TriggerSelect(trigger_index=...)
TriggerSelect(display_index=...)
TriggerSelect(trigger=...)

# Use TS as alias & class methods:
TS.index(...)  # Short hand for: trigger_index
TS.display(...)  # Short hand for: display_index
TS.trigger(...)

# Examples:
trigger = trigger_manager.get_trigger(TS.index(7))
trigger = trigger_manager.get_trigger(7)  # <-- Same result as above, defaults to `TS.index(...)`
trigger = trigger_manager.get_trigger(TS.display(3))
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
scenario = AoE2DEScenario.from_file(read_file)

# Get Trigger
trigger_manager = scenario.trigger_manager
trigger = trigger_manager.get_trigger(0)
```

If you want to see the contents of the trigger you can do so by running
the `get_content_as_string` function. This will result in the following
(with the `create trigger` code):

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
                source_player: PlayerId.ONE
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
# Get the trigger_index or display_index using the content or summary methods above
trigger = trigger_manager.get_trigger(0)  # Or: TS.index(0)
trigger = trigger_manager.get_trigger(TS.display(0))

trigger.name = "New Trigger Name"
trigger.description = "Awesome New Description!"
```

### Copy

Pretty simple and straigtforward. It copies a trigger adding it at the
end of the trigger list. Selecting a trigger is done using the standard
trigger_index, display_index and trigger reference. You can use it as
follows:

```py
copied_trigger = trigger_manager.copy_trigger(3)
```

This will result in a full (deep)copy of your trigger. The only parts
that are edited are its `id` and the name (added `" (copy)"`).

### Copy per player

Just like the `copy_trigger` function, this trigger makes a (deep) copy
of the given function. But, while copying, it'll change the everything
player related. With this function comes great control. Below the usage
is shown:

```py
copied_triggers = trigger_manager.copy_trigger_per_player(
    from_player=PlayerId.ONE,
    trigger_select=3,
    create_copy_for_players=[
        PlayerId.TWO, PlayerId.THREE, PlayerId.FOUR  # Optional list
    ]
)
print(f"New trigger for Player Two: {copied_triggers[PlayerId.TWO]}")
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
    from_player=PlayerId.ONE,
    trigger_select=3,  # Or: TS.index(3)
    group_triggers_by=GroupBy.PLAYER,  # Other options: GroupBy.NONE and GroupBy.TRIGGER
)
```

## Removing

When removing a trigger you can select it the same way as when getting a
trigger using the get_trigger function. But on top of that
you can also use it's reference:

```py
trigger_manager.remove_trigger(3)  # Or: TS.index(3)
trigger_manager.remove_trigger(TS.display(0))
trigger_manager.remove_trigger(TS.trigger(trigger))
```

For removing effects and conditions it's very similiar but the
functions are accessed from the triggers themselves instead of the
trigger_manager. You can select the effect or condition you want to
remove using:

-   it's index (the order by time of creation)
-   display index (the order like the in-game editor)
-   reference (the reference to that effect/condition object)

```py
trigger = trigger_manager.get_trigger(0)
trigger.remove_effect(effect_index=0)
trigger.remove_effect(display_index=1)
trigger.remove_effect(effect=effect)

trigger.remove_condition(condition_index=0)
trigger.remove_condition(display_index=1)
trigger.remove_condition(condition=condition)
```
