# XS Script

For an introduction to the XS scripting language itself, you can check out the [UGC Guide](https://divy1211.github.io/AoE2DE_UGC_Guide/general/xs/beginner/).

## Support

As of writing this, **Age of Empires 2 Definitive Edition** does not support transferring XS scripts attached to a 
scenario through multiplayer lobbies. This results in an issue where you cannot use XS in multiplayer until everyone in 
the lobby places the XS file at the proper location by hand. Which is very cumbersome.

To get around this, you can add your XS script to a `Script Call` effect. When you add the XS to such an effect, it 
will, when loading the scenario, move all scripts from those calls to the `default0.xs` file. This does work in 
multiplayer because it happens on every machine separately.

So the XS support for the parser works with a dedicated trigger and a `Script Call` effect. In the in-game editor the 
amount of text in a `Script Call` effect is limited to a certain number of characters. This limitation can be bypassed
using the parser.

## Initialising XS Trigger

You can use the XS manager to add XS to your scenarios. All these XS calls do indeed transfer in multiplayer lobbies
as is explained above. You can use the XS manager like so:

```py
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

# File & Folder setup
scenario_folder = "your/path/to/the/scenario/folder/"
read_file = scenario_folder + "scenario_name.aoe2scenario"

# Define Scenario file
scenario = AoE2DEScenario.from_file(read_file)

xs_manager = scenario.xs_manager
```

Because the `XS Manager` uses a trigger with a `Script Call` in the background, it needs to place the trigger somewhere.
You can call the function below to create the trigger. You can also give it an index to insert it somewhere in the 
scenario. Not adding an index to the call just adds the trigger at the end of the list.

!!! warning
    Placing the trigger at the top of all triggers (`insert_index=0`) can take quite a lot of time if the map already 
    has a lot of triggers (For example over 1000 triggers).

```py
xs_manager.initialise_xs_trigger()
# Or place the XS trigger at the top of all triggers
xs_manager.initialise_xs_trigger(insert_index=0)
```

## Adding XS

!!! tip "You don't have to initialise the trigger"
    Whenever you call the `add_script()` function, it will automatically initialise the trigger if it hasn't been already.
    The use of the `initialise_xs_trigger()` function is to control where the trigger is placed.

You can add scripts to the trigger using the `add_script` function. This function accepts a path to an XS file and a 
direct XS script string.

```py
# Add a file to the script. 
# Work on your XS script in a file and this will add it to the scenario
xm.add_script(xs_file_path="path/to/xs/script.xs")

# Add XS directly
xs_script = """
int a = 1;
int b = a + 4;
"""
xm.add_script(xs_string=xs_script)
```
You can use both `xs_file_path=...` and `xs_string=...` in the same `add_script` call too.