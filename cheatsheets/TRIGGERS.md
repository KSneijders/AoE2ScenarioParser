# Triggers

You can retrieve access to the triggers using the object_manager. 

```py
trigger_manager = scenario.object_manager.trigger_manager
```

---

## Adding triggers
You can add triggers easily. You can change all parts of the trigger using attributes (type "trigger." and the autocomplete will show you a list of options.).  **Eventually**, there will be an API documentation. 

```py
trigger = trigger_manager.add_trigger("Trigger :)")
trigger.description = "This is a great description!"
```

To add conditions or effects, just call the method `add_condition` and `add_effect`. You can use the `condition` or `effect` dataset to give the function the right ID. If you're unsure about what attributes are available in every condition or effect, check the docs of the condition. Type (for example) `"conditions.chance"` and click it. Now show the docs (using `CTRL+Q` in PyCharm). It will show you: "Parameters for the chance condition are: amount_or_quantity". Now use the attribute `amount_or_quantity` to apply the right value.

The example shows: A trigger with 25% chance of showing a message. 

```py
condition = trigger.add_condition(Condition.CHANCE)  # From conditions dataset
condition.amount_or_quantity = 25

effect = trigger.add_effect(Effect.DISPLAY_INSTRUCTIONS)  # From effects dataset
effect.player_source = 1
effect.display_time = 11
effect.message = "This message was set using AoE2ScenarioParser!"
```

---
&nbsp;  

## Viewing triggers

**Tip:** As you know you can change the order of triggers in the in-game editor *(Not officially supported with this package (yet))*. When using the *view, edit and delete* functionality you can choose to select a trigger by `index` or by `display_index`. `display_index` is the index in which the triggers are shown in the in-game editor. The `index` is the index in which they were created. Both start from 0.

There's multiple ways to check out triggers and their contents. When editing or deleting a trigger you'll need an index. This can be the actual index or the display index.

You can use the following function to generate a simple overview of the triggers.

```py
trigger_manager.get_summary_as_string()

# This returns the following (As String):
Trigger Summary:
	Init Trigger    [Index: 0, Display: 0]	(conditions: 2,  effects: 1)
	Spawn Wave 1    [Index: 1, Display: 1]	(conditions: 2,  effects: 7)
	Spawn Wave 2    [Index: 2, Display: 2]	(conditions: 1,  effects: 7)
```

If you want to know all specifics about a trigger you can use the functions below. 

```py
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
```py
trigger_manager.get_content_as_string()
```

---
&nbsp;  

## Editing or removing triggers
When opening a file that already contains triggers you might want to edit or even remove said triggers. *Please note that it's not possible to remove specific conditions or effects (yet).*

You can edit a trigger like so:
```py
trigger = trigger_manager.get_trigger(trigger_id=0)
trigger = trigger_manager.get_trigger(display_index=0)

trigger.name = "New Trigger Name"
trigger.description = "Awesome New Description!"
```

For removing it basically works the same:
```py
# Remember to save to a different file. Especially when removing triggers.
trigger_manager.delete_trigger(trigger_id=0)
trigger_manager.delete_trigger(display_index=0)
```

---

End of the Triggers cheatsheet. [Return to README](./../README.md)
